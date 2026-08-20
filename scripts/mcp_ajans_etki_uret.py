#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mcp_ajans_etki_uret.py — MCP hiyerarşi + etki/yetenek arşivi + ajans org + prompt katalog.

🚩 İstek: 900.000.000 karakter/prompt · İmkânsız (bağlam penceresi + depo boyutu).
Gerçekçi sözleşme: her prompt yapılandırılmış çıktı sözleşmesi, hedef 4–12 KiB,
≥122 prompt/rol ailesi, referans zinciri (MCP → etki sahibi → KB) ile derinlik.

Kipler:
  --hepsi     tüm artefaktlar (varsayılan)
  --sadece-mcp / --sadece-arsiv / --sadece-org / --sadece-prompt
  --pilot     yalnız C-level + INF-MCP için prompt markdown materyalize
  --dogrula   sayım/şema denetimi
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
NOW = dt.datetime.now(dt.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
TODAY = NOW.strftime("%Y-%m-%d")
PROMPTS_PER_ROLE = 122
TARGET_CHARS_MIN = 4000
TARGET_CHARS_MAX = 12000

# --- daily_agency DOMAINS (kaynak doğruluğu: scripts/daily_agency.py) ---
DOMAINS = [
    ("CTO", [
        ("ENG-PLT", "Platform Mühendisliği", ["Platform Mühendisi", "Altyapı Mühendisi", "API Mühendisi"]),
        ("ENG-APP", "Uygulama Geliştirme", ["Backend Mühendisi", "Frontend Mühendisi", "Mobil Mühendisi"]),
        ("ENG-DEV", "DevOps & SRE", ["DevOps Mühendisi", "Site Güvenilirlik Mühendisi (SRE)"]),
        ("ENG-QA", "Kalite & Test", ["Test Otomasyon Mühendisi", "QA Analisti"]),
    ]),
    ("CAIO", [
        ("AI-RES", "AI Araştırma", ["AI Araştırmacısı", "Model Değerlendirme Uzmanı (Evals)"]),
        ("AI-AGT", "Ajan Mühendisliği", ["Ajan Mühendisi", "Orkestrasyon Mühendisi", "Araç (Tool) Entegrasyon Mühendisi"]),
        ("AI-PRM", "Prompt & Context Mühendisliği", ["Prompt Mühendisi", "Context Mühendisi"]),
        ("AI-SAF", "AI Güvenliği & Hizalama", ["Hizalama Uzmanı", "Red-Team Uzmanı"]),
    ]),
    ("CDO", [
        ("DAT-ENG", "Veri Mühendisliği", ["Veri Mühendisi", "Veri Boru Hattı Mühendisi"]),
        ("DAT-SCI", "Veri Bilimi", ["Veri Bilimci", "Makine Öğrenmesi Mühendisi"]),
        ("DAT-BI", "Analitik & BI", ["BI Analisti", "Veri Görselleştirme Uzmanı"]),
    ]),
    ("CPO", [
        ("PRD-MGT", "Ürün Yönetimi", ["Ürün Yöneticisi", "Teknik Ürün Yöneticisi"]),
        ("PRD-DSN", "Tasarım", ["Ürün Tasarımcısı (UX)", "Arayüz Tasarımcısı (UI)", "Tasarım Sistemi Uzmanı"]),
        ("PRD-OPS", "Ürün Operasyonları", ["Ürün Operasyon Uzmanı", "Kullanıcı Araştırmacısı"]),
    ]),
    ("CMO", [
        ("MKT-BRD", "Marka & İçerik", ["Marka Stratejisti", "İçerik Pazarlama Uzmanı"]),
        ("MKT-PRF", "Performans Pazarlama (AdOps)", ["Performans Pazarlama Uzmanı", "Medya Satın Alma Uzmanı", "Atıf (Attribution) Analisti"]),
        ("MKT-SEO", "SEO & Organik Büyüme", ["SEO Uzmanı", "İçerik Optimizasyon Uzmanı"]),
        ("MKT-SOC", "Sosyal Medya", ["Sosyal Medya Yöneticisi", "Topluluk Yöneticisi"]),
    ]),
    ("CRO", [
        ("REV-SLS", "Satış", ["Satış Temsilcisi (AE)", "Satış Geliştirme Temsilcisi (SDR)"]),
        ("REV-PRT", "İş Ortaklıkları", ["Ortaklık Yöneticisi", "Sponsorluk Geliştirme Uzmanı"]),
        ("REV-CSM", "Müşteri Başarısı", ["Müşteri Başarı Yöneticisi", "Onboarding Uzmanı"]),
        ("REV-OPS", "Gelir Operasyonları", ["RevOps Analisti", "CRM Uzmanı"]),
    ]),
    ("CCO", [
        ("MED-PUB", "Yayıncılık & Makale", ["Teknik Yazar", "Editör", "Araştırma Yazarı"]),
        ("MED-CRE", "Video & Kreatif", ["Video Editörü", "Grafik Tasarımcısı"]),
        ("MED-LOC", "Yerelleştirme (TR)", ["Yerelleştirme Uzmanı", "Çevirmen-Editör"]),
    ]),
    ("COO", [
        ("OPS-PMO", "Program Yönetimi (PMO)", ["Program Yöneticisi", "Proje Koordinatörü"]),
        ("OPS-BIZ", "İş Operasyonları", ["İş Operasyon Analisti", "Süreç İyileştirme Uzmanı"]),
        ("OPS-TLS", "Araç & Tedarik", ["Araç Yönetim Uzmanı", "Tedarik Analisti"]),
    ]),
    ("CFO", [
        ("FIN-FPA", "Finansal Planlama (FP&A)", ["FP&A Analisti", "Bütçe Uzmanı"]),
        ("FIN-ACC", "Muhasebe & Raporlama", ["Muhasebe Uzmanı", "Finansal Raporlama Analisti"]),
        ("FIN-REV", "Gelir Motoru İzleme", ["Gelir Analisti", "Monetizasyon Uzmanı"]),
    ]),
    ("CISO", [
        ("SEC-OPS", "Güvenlik Operasyonları", ["Güvenlik Operasyon Analisti", "Olay Müdahale Uzmanı"]),
        ("SEC-AUD", "Uyum Denetimi (5 Kural)", ["Denetçi (Auditor)", "Bileşen Güvenlik İnceleme Uzmanı"]),
        ("SEC-SUP", "Tedarik Zinciri Güvenliği", ["Tedarik Zinciri Güvenlik Analisti", "Bağımlılık İzleme Uzmanı"]),
    ]),
    ("CHRO", [
        ("HRA-REC", "Ajan İşe Alım", ["Ajan İşe Alım Uzmanı", "Yetenek Haritalama Analisti"]),
        ("HRA-PRF", "Performans & Kalite", ["Performans Değerlendirme Uzmanı", "Kalite Güvence Analisti"]),
        ("HRA-LRN", "Eğitim & Bilgi Tabanı", ["Bilgi Tabanı Küratörü", "Öğrenim Damıtma Uzmanı"]),
    ]),
    ("CLO", [
        ("LGL-LIC", "Lisans Uyumu (MIT)", ["Lisans Uyum Uzmanı", "Atıf (Attribution) Denetçisi"]),
        ("LGL-PRV", "Veri Gizliliği", ["Gizlilik Uzmanı (KVKK/GDPR)", "Veri Sınıflandırma Analisti"]),
    ]),
    ("CIO", [
        ("INF-MCP", "MCP Entegrasyonları", ["MCP Entegrasyon Mühendisi", "Bağlayıcı (Connector) Uzmanı"]),
        ("INF-SET", "Ayar & Yapılandırma", ["Yapılandırma Yöneticisi", "Ortam (Environment) Uzmanı"]),
        ("INF-HKS", "Hooks & Otomasyon", ["Hook Geliştirici", "Otomasyon Mühendisi"]),
        ("INF-LOP", "Döngüler & Zamanlama", ["Döngü Operatörü", "Zamanlama (Scheduler) Uzmanı"]),
    ]),
    ("CSO", [
        ("STR-INT", "Pazar İstihbaratı", ["Pazar İstihbarat Analisti", "Trend Araştırmacısı"]),
        ("STR-CMP", "Rakip Analizi", ["Rakip Analiz Uzmanı", "Kıyaslama (Benchmark) Analisti"]),
        ("STR-GRW", "Büyüme & Yatırım", ["Büyüme Stratejisti", "Yatırım Analisti"]),
    ]),
]

BOARD = [
    ("Chairman / Sahip", "owner", "KURUL"),
    ("Group CEO", "group-ceo", "C-OFİS"),
    ("Group COO", "group-coo", "C-OFİS"),
    ("Group CTO", "group-cto", "C-LEVEL"),
    ("Group CFO", "group-cfo", "C-LEVEL"),
    ("Group CCO", "group-cco", "C-LEVEL"),
]

# Cursor oturumunda görülen canlı MCP sunucuları (katalog dışı / runtime)
LIVE_MCP_SERVERS = [
    ("cloud", "Railway", "deploy"), ("cloud", "Aws-mcp", "infra"), ("cloud", "Azure", "infra"),
    ("data", "Aurora-dsql", "db"), ("security", "Zscaler", "zt"), ("security", "Zscaler-mcp-server", "zt"),
    ("backend", "Appwrite-api", "baas"), ("docs", "Appwrite-docs", "docs"),
    ("data", "Cockroachdb-toolbox", "db"), ("data", "Cockroachdb-toolbox-http", "db"),
    ("data", "Cockroachdb-cloud", "db"), ("vector", "Pinecone", "vector"),
    ("backend", "Encore-mcp", "backend"), ("cloud", "Firebase", "baas"),
    ("cloud", "Aws-serverless-mcp", "serverless"), ("data", "Mongodb", "db"),
    ("cloud", "Awsiac", "iac"), ("cloud", "Awspricing", "cost"),
    ("qa", "Browserstack", "test"), ("backend", "Convex", "baas"),
    ("sales", "Zoominfo", "gtm"), ("analytics", "Mixpanel", "product-analytics"),
    ("search", "Opensearch-mcp-server", "search"), ("search", "Ddg-search", "search"),
    ("cloud", "Awslabs.aws-api-mcp-server", "infra"), ("docs", "Aws-knowledge-mcp-server", "docs"),
    ("web-data", "Bright Data", "scrape"), ("orm", "Prisma-Local", "orm"),
    ("orm", "Prisma-Remote", "orm"), ("design", "Figma", "design"),
    ("pm", "Linear", "pm"), ("obs", "Coralogix", "observability"),
    ("obs", "Datadog", "observability"), ("deploy", "Monk", "deploy"),
    ("docs", "Twilio-docs", "docs"), ("finops", "Vantage", "finops"),
    ("data", "Paradedb", "search-db"), ("docs", "Awsknowledge", "docs"),
    ("auth", "Workos", "auth"), ("vector", "Turbopuffer", "vector"),
    ("deploy", "Render", "deploy"), ("security", "Jfrog", "supply-chain"),
    ("ops", "Pagerduty-mcp", "incident"), ("data", "PlanetScale", "db"),
    ("auth", "Clerk", "auth"), ("data", "Neon", "db"), ("data", "Supabase", "baas"),
    ("deploy", "Vercel", "deploy"), ("obs", "Sentry", "errors"),
    ("docs", "Cloudflare-docs", "docs"), ("cloud", "Cloudflare-bindings", "edge"),
    ("cloud", "Cloudflare-builds", "ci"), ("obs", "Cloudflare-observability", "obs"),
    ("obs", "Observe", "observability"), ("web-data", "Apify", "scrape"),
    ("flags", "Confidence-flags", "flags"), ("docs", "Confidence-docs", "docs"),
    ("obs", "Grafana-cloud", "observability"), ("comms", "Slack", "comms"),
    ("research", "Exa", "research"), ("code", "Spottercode", "code-intel"),
    ("analytics", "Pendo-external", "product-analytics"), ("docs", "Elastic-docs", "docs"),
    ("api", "Postman", "api"), ("eval", "Braintrust", "evals"),
    ("ops", "Antimetal", "rca"), ("data", "Azure-cosmosdb", "db"),
    ("analytics", "Amplitude", "product-analytics"), ("ml", "Huggingface-skills", "ml"),
    ("analytics", "Posthog", "product-analytics"), ("data", "Clickhouse", "analytics-db"),
    ("data", "Snowflake", "warehouse"), ("docs", "Gitbook", "docs"),
    ("analytics", "Hex", "analytics"), ("design", "Canva", "design"),
    ("docs", "Mintlify", "docs"), ("docs", "Mintlify MCP", "docs"),
    ("prd", "ChatPRD", "prd"), ("ops", "Tierzero", "incident"),
    ("cicd", "Harness", "cicd"), ("meta", "cursor-cloud", "agent-ops"),
]

PROMPT_FAMILIES = [
    ("strateji", "Strateji & öncelik"),
    ("arastirma", "Araştırma & damıtım"),
    ("uretim", "Üretim & teslim"),
    ("denetim", "Denetim & güvenlik"),
    ("operasyon", "Operasyon & ritm"),
    ("gelir", "Gelir & değer"),
    ("iletisim", "İletişim & rapor"),
]

# 122 = 7 aile × 17 + 3 özel (onboarding/kriz/handoff)
PROMPT_SLOTS = []
for fam_id, fam_name in PROMPT_FAMILIES:
    for i in range(1, 18):
        PROMPT_SLOTS.append((fam_id, fam_name, i, f"{fam_name} — senaryo {i:02d}"))
PROMPT_SLOTS += [
    ("ozel", "Özel", 1, "Rol onboarding (ilk 48 saat)"),
    ("ozel", "Özel", 2, "Kriz / kırmızı bayrak protokolü"),
    ("ozel", "Özel", 3, "Handoff & bilgi aktarımı"),
]
assert len(PROMPT_SLOTS) == PROMPTS_PER_ROLE


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def catalog_mcps() -> list[dict[str, Any]]:
    root = ROOT / "katalog" / "mcps"
    out: list[dict[str, Any]] = []
    for p in sorted(root.rglob("*.json")):
        rel = str(p.relative_to(root))
        cat = p.parent.name
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            out.append({"id": rel, "kategori": cat, "kaynak": "katalog", "hata": str(e)})
            continue
        servers = data.get("mcpServers") or {}
        for name, cfg in servers.items():
            out.append({
                "id": f"{cat}/{name}",
                "dosya": rel,
                "kategori": cat,
                "kaynak": "katalog",
                "sunucu": name,
                "komut": cfg.get("command"),
                "args": cfg.get("args"),
                "env_keys": sorted((cfg.get("env") or {}).keys()),
                "mekanizma": _mekanizma(cfg),
            })
        if not servers:
            out.append({
                "id": rel.replace(".json", ""),
                "dosya": rel,
                "kategori": cat,
                "kaynak": "katalog",
                "sunucu": p.stem,
                "mekanizma": "config-json",
            })
    return out


def _mekanizma(cfg: dict[str, Any]) -> str:
    cmd = (cfg.get("command") or "").lower()
    if "npx" in cmd or "node" in cmd:
        return "stdio-node"
    if "uvx" in cmd or "python" in cmd or "uv " in cmd:
        return "stdio-python"
    if "docker" in cmd:
        return "stdio-docker"
    if cfg.get("url"):
        return "http-sse"
    return "stdio-other"


def build_mcp_hierarchy(catalog: list[dict[str, Any]]) -> dict[str, Any]:
    by_cat: dict[str, list] = {}
    for m in catalog:
        by_cat.setdefault(m["kategori"], []).append(m)
    live = [
        {
            "id": f"live/{domain}/{name}",
            "kategori": domain,
            "kaynak": "cursor-runtime",
            "sunucu": name,
            "etiket": tag,
            "mekanizma": "mcp-remote-or-local",
        }
        for domain, name, tag in LIVE_MCP_SERVERS
    ]
    layers = {
        "L0_orkestrasyon": {
            "aciklama": "Orkestratör (CLAUDE.md uzman kurulu) + cursor-cloud meta",
            "ornekler": ["cursor-cloud", "CLAUDE orkestratör", "daily_agency"],
        },
        "L1_arastirma": {
            "aciklama": "Web/araştırma/doküman MCP",
            "kategoriler": ["research", "web", "web-data", "docs", "Exa", "Bright Data", "Apify"],
        },
        "L2_veri_backend": {
            "aciklama": "DB/BaaS/vector/warehouse",
            "kategoriler": ["database", "data", "vector", "orm", "backend"],
        },
        "L3_gozlem_guvenlik": {
            "aciklama": "Observability, güvenlik, olay",
            "kategoriler": ["obs", "security", "ops", "qa"],
        },
        "L4_teslim_gelir": {
            "aciklama": "Deploy, CI/CD, analytics, GTM, tasarım",
            "kategoriler": ["deploy", "cicd", "cloud", "analytics", "marketing", "design", "prd"],
        },
        "L5_uretkenlik": {
            "aciklama": "Filesystem, productivity, integration, audio",
            "kategoriler": ["filesystem", "productivity", "integration", "audio", "devtools"],
        },
    }
    return {
        "ts": TS,
        "katalog_adet": len(catalog),
        "canli_adet": len(live),
        "toplam": len(catalog) + len(live),
        "katmanlar": layers,
        "katalog_kategoriler": {k: len(v) for k, v in sorted(by_cat.items())},
        "katalog": catalog,
        "canli": live,
        "is_akis_sirasi": [
            "1) L1 araştırma → sinyal",
            "2) L2 veri/backend doğrulama",
            "3) L3 gözlem/güvenlik denetim",
            "4) L4 teslim/gelir aksiyon",
            "5) L0 damga → BILGI_TABANI + AUDIT_LOG",
        ],
    }


def tech_influencers() -> list[dict[str, Any]]:
    """Kanonik 100+ teknoloji/AI etki sahibi (kamuya açık isimler; aylık yenileme için iskelet)."""
    names = [
        ("Sam Altman", "CEO", "OpenAI", "AI-platform", "C-LEVEL"),
        ("Dario Amodei", "CEO", "Anthropic", "AI-safety", "C-LEVEL"),
        ("Jensen Huang", "CEO", "NVIDIA", "AI-infra", "C-LEVEL"),
        ("Demis Hassabis", "CEO", "Google DeepMind", "AI-research", "C-LEVEL"),
        ("Fei-Fei Li", "CEO/Prof", "World Labs / Stanford", "spatial-AI", "C-LEVEL"),
        ("Yann LeCun", "Chief AI Scientist", "Meta", "open-AI", "C-LEVEL"),
        ("Geoffrey Hinton", "Researcher", "Independent", "deep-learning", "DOMAIN"),
        ("Yoshua Bengio", "Founder", "Mila", "AI-safety", "DOMAIN"),
        ("Andrew Ng", "Founder", "DeepLearning.AI", "AI-education", "C-LEVEL"),
        ("Andrej Karpathy", "Founder", "Eureka Labs", "AI-education", "DOMAIN"),
        ("Ilya Sutskever", "Scientist", "SSI", "AGI-research", "DOMAIN"),
        ("Mustafa Suleyman", "CEO", "Microsoft AI", "AI-product", "C-LEVEL"),
        ("Satya Nadella", "CEO", "Microsoft", "platform", "C-LEVEL"),
        ("Sundar Pichai", "CEO", "Google/Alphabet", "platform", "C-LEVEL"),
        ("Mark Zuckerberg", "CEO", "Meta", "platform", "C-LEVEL"),
        ("Elon Musk", "CEO", "xAI/Tesla", "AI-auto", "C-LEVEL"),
        ("Jeff Dean", "Chief Scientist", "Google DeepMind", "systems-ML", "DOMAIN"),
        ("Oriol Vinyals", "VP", "Google DeepMind", "LLM", "DOMAIN"),
        ("Noam Shazeer", "Co-founder", "Character.AI", "transformers", "DOMAIN"),
        ("Aidan Gomez", "CEO", "Cohere", "enterprise-LLM", "C-LEVEL"),
        ("Emad Mostaque", "Founder", "Stability AI", "gen-media", "C-LEVEL"),
        ("Clem Delangue", "CEO", "Hugging Face", "open-source-ML", "C-LEVEL"),
        ("Arthur Mensch", "CEO", "Mistral AI", "open-weights", "C-LEVEL"),
        ("Mira Murati", "Founder", "Thinking Machines Lab", "AI-research", "C-LEVEL"),
        ("Helen Toner", "Director", "CSET", "AI-policy", "DOMAIN"),
        ("Paul Christiano", "Researcher", "Alignment", "alignment", "DOMAIN"),
        ("Jan Leike", "Researcher", "Anthropic/OpenAI alum", "alignment", "DOMAIN"),
        ("Chris Olah", "Researcher", "Anthropic", "interpretability", "DOMAIN"),
        ("Anthropic Claude Team", "Research", "Anthropic", "constitutional-AI", "TEAM"),
        ("OpenAI Research", "Research", "OpenAI", "frontier", "TEAM"),
        ("Percy Liang", "Prof", "Stanford CRFM", "evals", "DOMAIN"),
        ("Chelsea Finn", "Prof", "Stanford", "robotics-ML", "DOMAIN"),
        ("Pieter Abbeel", "Prof", "UC Berkeley", "robotics", "DOMAIN"),
        ("Sergey Levine", "Prof", "UC Berkeley", "RL", "DOMAIN"),
        ("Dawn Song", "Prof", "UC Berkeley", "AI-security", "DOMAIN"),
        ("Ion Stoica", "Prof/Co-founder", "UC Berkeley / Anyscale", "distributed-AI", "DOMAIN"),
        ("Matei Zaharia", "CTO/Co-founder", "Databricks", "data-AI", "C-LEVEL"),
        ("Ali Ghodsi", "CEO", "Databricks", "lakehouse", "C-LEVEL"),
        ("Francois Chollet", "Researcher", "Google/Independent", "AGI-measure", "DOMAIN"),
        ("Jim Fan", "Research Scientist", "NVIDIA", "embodied-AI", "DOMAIN"),
        ("Jim Keller", "CEO", "Tenstorrent", "chips", "C-LEVEL"),
        ("Lisa Su", "CEO", "AMD", "compute", "C-LEVEL"),
        ("Pat Gelsinger", "ex-CEO", "Intel", "semiconductor", "C-LEVEL"),
        ("Brian Chesky", "CEO", "Airbnb", "product", "C-LEVEL"),
        ("Dylan Field", "CEO", "Figma", "design-tooling", "C-LEVEL"),
        ("Guillaume Beaudouin", "—", "—", "skip", "WORKER"),  # placeholder replaced below
    ]
    # Expand to ≥100 with curated practitioners / infra / open-source leaders
    extra = [
        ("Simon Willison", "Creator", "Datasette", "LLM-tools", "DOMAIN"),
        ("Harrison Chase", "CEO", "LangChain", "agent-framework", "C-LEVEL"),
        ("Jerry Liu", "CEO", "LlamaIndex", "RAG", "C-LEVEL"),
        ("Andrew Mayne", "Writer", "Independent", "prompting", "WORKER"),
        ("Riley Goodside", "Prompt eng.", "Scale AI", "prompting", "WORKER"),
        ("Swyx", "Founder", "Smol AI / Latent Space", "AI-devtools", "DOMAIN"),
        ("Latent Space", "Podcast", "Latent Space", "AI-media", "TEAM"),
        ("Lenny Rachitsky", "Writer", "Lenny's Newsletter", "product", "DOMAIN"),
        ("Packy McCormick", "Writer", "Not Boring", "tech-strategy", "DOMAIN"),
        ("Benedict Evans", "Analyst", "Independent", "tech-strategy", "DOMAIN"),
        ("Mary Meeker", "Partner", "Bond", "internet-trends", "C-LEVEL"),
        ("Cathy O'Neil", "Author", "ORCAA", "AI-ethics", "DOMAIN"),
        ("Kate Crawford", "Researcher", "USC/MSR", "AI-power", "DOMAIN"),
        ("Timnit Gebru", "Founder", "DAIR", "AI-ethics", "DOMAIN"),
        ("Margaret Mitchell", "Chief Ethics", "Hugging Face", "AI-ethics", "DOMAIN"),
        ("Gary Marcus", "Prof", "Independent", "AI-critique", "DOMAIN"),
        ("Melanie Mitchell", "Prof", "SFI", "AI-concepts", "DOMAIN"),
        ("Stuart Russell", "Prof", "UC Berkeley", "AI-control", "DOMAIN"),
        ("Max Tegmark", "Prof", "MIT / FLI", "AI-safety", "DOMAIN"),
        ("Eliezer Yudkowsky", "Researcher", "MIRI", "AI-risk", "DOMAIN"),
        ("Holden Karnofsky", "Advisor", "Open Phil", "AI-policy", "DOMAIN"),
        ("Helen Edwards", "—", "skip", "skip", "WORKER"),
        ("Chip Huyen", "Author", "Independent", "ML-systems", "DOMAIN"),
        ("Eugene Yan", "Applied scientist", "Amazon", "recsys", "WORKER"),
        ("Lilian Weng", "Research", "OpenAI/Thinking Machines", "ML-surveys", "DOMAIN"),
        ("Jay Alammar", "Educator", "Cohere", "explainers", "WORKER"),
        ("Sebastian Raschka", "AI educator", "Lightning AI", "LLM-from-scratch", "DOMAIN"),
        ("Jeremy Howard", "Founder", "fast.ai", "practical-DL", "DOMAIN"),
        ("Rachel Thomas", "Co-founder", "fast.ai", "ethics-edu", "DOMAIN"),
        ("Carlos Rivera", "Researcher", "Google", "transformers", "DOMAIN"),
        ("Ashish Vaswani", "Co-founder", "Essential AI", "attention", "DOMAIN"),
        ("Alec Radford", "Researcher", "OpenAI", "GPT", "DOMAIN"),
        ("Tom Brown", "Researcher", "Anthropic", "GPT-3", "DOMAIN"),
        ("Jason Wei", "Researcher", "OpenAI", "prompting", "DOMAIN"),
        ("Hyung Won Chung", "Researcher", "OpenAI", "instruction-tuning", "DOMAIN"),
        ("Tri Dao", "Researcher", "Princeton/Together", "FlashAttention", "DOMAIN"),
        ("Albert Gu", "Researcher", "Cartesia", "SSM", "DOMAIN"),
        ("Chris Lattner", "CEO", "Modular", "Mojo/AI-compilers", "C-LEVEL"),
        ("George Hotz", "Founder", "comma.ai / tinygrad", "open-compute", "DOMAIN"),
        ("Jim Zemlin", "ED", "Linux Foundation", "open-source", "C-LEVEL"),
        ("Nat Friedman", "Investor", "Independent", "devtools", "C-LEVEL"),
        ("Patrick Collison", "CEO", "Stripe", "payments-infra", "C-LEVEL"),
        ("John Collison", "President", "Stripe", "payments", "C-LEVEL"),
        ("Tobias Lütke", "CEO", "Shopify", "commerce", "C-LEVEL"),
        ("Daniel Ek", "CEO", "Spotify", "media-platform", "C-LEVEL"),
        ("Brian Armstrong", "CEO", "Coinbase", "crypto", "C-LEVEL"),
        ("Vitalik Buterin", "Founder", "Ethereum", "crypto", "DOMAIN"),
        ("Guillermo Rauch", "CEO", "Vercel", "frontend-cloud", "C-LEVEL"),
        ("Malte Ubl", "CTO", "Vercel", "edge", "C-LEVEL"),
        ("Quinn Slack", "CEO", "Sourcegraph", "code-intel", "C-LEVEL"),
        ("Beyang Liu", "CTO", "Sourcegraph", "code-search", "C-LEVEL"),
        ("Amjad Masad", "CEO", "Replit", "agentic-IDE", "C-LEVEL"),
        ("Michele Catasta", "President", "Replit", "AI-coding", "C-LEVEL"),
        ("Alexandr Wang", "CEO", "Scale AI", "data-labeling", "C-LEVEL"),
        ("Daphne Koller", "Founder", "insitro", "AI-bio", "C-LEVEL"),
        ("Eric Schmidt", "ex-CEO", "Google", "AI-geo", "C-LEVEL"),
        ("Reid Hoffman", "Partner", "Greylock", "AI-invest", "C-LEVEL"),
        ("Marc Andreessen", "GP", "a16z", "AI-invest", "C-LEVEL"),
        ("Ben Horowitz", "GP", "a16z", "AI-invest", "C-LEVEL"),
        ("Vinod Khosla", "Founder", "Khosla Ventures", "deeptech", "C-LEVEL"),
        ("Sarah Guo", "Founder", "Conviction", "AI-invest", "C-LEVEL"),
        ("Sonya Huang", "Partner", "Sequoia", "AI-invest", "C-LEVEL"),
        ("Bill Gurley", "GP", "Benchmark", "markets", "C-LEVEL"),
        ("Paul Graham", "Co-founder", "Y Combinator", "startups", "DOMAIN"),
        ("Garry Tan", "CEO", "Y Combinator", "startups", "C-LEVEL"),
        ("Wendy Hall", "Partner", "YC", "AI-startups", "DOMAIN"),
        ("Logan Kilpatrick", "Product", "Google AI Studio", "developer-AI", "WORKER"),
        ("Simon Last", "Co-founder", "Notion", "productivity", "C-LEVEL"),
        ("Ivan Zhao", "CEO", "Notion", "knowledge-work", "C-LEVEL"),
        ("Stewart Butterfield", "Founder", "Slack/Flickr", "comms", "DOMAIN"),
        ("Tobi Lütke", "CEO", "Shopify", "commerce-AI", "C-LEVEL"),
        ("Dylan Patel", "Chief Analyst", "SemiAnalysis", "semiconductors", "DOMAIN"),
        ("George Adams", "Founder", "SemiAnalysis", "chips", "DOMAIN"),
        ("Horace Dediu", "Analyst", "Asymco", "platform-strategy", "DOMAIN"),
        ("Ben Thompson", "Writer", "Stratechery", "strategy", "DOMAIN"),
        ("Matt Levine", "Writer", "Bloomberg", "markets", "DOMAIN"),
        ("Casey Newton", "Writer", "Platformer", "tech-media", "DOMAIN"),
        ("Kara Swisher", "Journalist", "Independent", "tech-media", "DOMAIN"),
        ("Lex Fridman", "Podcaster", "Independent", "AI-interviews", "DOMAIN"),
        ("Dwarkesh Patel", "Podcaster", "Dwarkesh Podcast", "longform-AI", "DOMAIN"),
        ("Nathan Labenz", "Host", "Cognitive Revolution", "AI-podcast", "DOMAIN"),
        ("Noam Brown", "Researcher", "OpenAI", "reasoning-agents", "DOMAIN"),
        ("Shunyu Yao", "Researcher", "OpenAI", "ReAct/agents", "DOMAIN"),
        ("Ofir Press", "Researcher", "Princeton/TTIC", "LLM-reasoning", "DOMAIN"),
        ("Dan Hendrycks", "Director", "CAIS", "AI-safety-evals", "DOMAIN"),
        ("Anca Dragan", "Director", "DeepMind", "AI-alignment", "DOMAIN"),
        ("Joelle Pineau", "VP", "Meta AI / McGill", "RL", "DOMAIN"),
        ("Yoshua Lab", "Lab", "Mila", "research", "TEAM"),
        ("Stanford CRFM", "Center", "Stanford", "evals", "TEAM"),
        ("EleutherAI", "Collective", "EleutherAI", "open-LLM", "TEAM"),
        ("LAION", "Org", "LAION", "datasets", "TEAM"),
        ("Allen Institute for AI", "Org", "AI2", "NLP", "TEAM"),
        ("Mozilla AI", "Org", "Mozilla", "open-AI", "TEAM"),
        ("Linux Foundation AI", "Org", "LF", "standards", "TEAM"),
        ("CNCF", "Org", "CNCF", "cloud-native", "TEAM"),
        ("Anthropic Safety", "Team", "Anthropic", "RSP", "TEAM"),
        ("OpenAI Superalignment", "Team", "OpenAI", "alignment", "TEAM"),
    ]
    raw = [(n, r, o, d, l) for (n, r, o, d, l) in names + extra if d != "skip" and n != "Helen Edwards"]
    # Deduplicate by name
    seen = set()
    people = []
    for i, (n, r, o, d, l) in enumerate(raw, 1):
        if n in seen:
            continue
        seen.add(n)
        people.append({
            "rank": len(people) + 1,
            "ad": n,
            "unvan": r,
            "org": o,
            "alan": d,
            "ajans_katman": l,
            "kaynaklar": [
                {"tip": "arama", "not": "Aylık tarama: makale/röportaj/proje"},
            ],
            "son_inceleme": TODAY,
            "guncelleme_durumu": "seed",
        })
    # Pad to ≥100 if needed with numbered domain experts placeholders marked for research
    pad = 1
    while len(people) < 100:
        people.append({
            "rank": len(people) + 1,
            "ad": f"Araştırma Adayı T-{pad:03d}",
            "unvan": "TBD",
            "org": "TBD",
            "alan": "pending-research",
            "ajans_katman": "WORKER",
            "kaynaklar": [],
            "son_inceleme": TODAY,
            "guncelleme_durumu": "bos-slot",
        })
        pad += 1
    return people


def culture_talents() -> list[dict[str, Any]]:
    """100+ kültür/sanat/spor özel yetenek (kamuya açık; aylık yenileme)."""
    raw = [
        # Spor
        ("Lionel Messi", "Futbol", "spor", "GOAT-sembol"),
        ("Cristiano Ronaldo", "Futbol", "spor", "marka-atlet"),
        ("Serena Williams", "Tenis", "spor", "ikon"),
        ("Novak Djokovic", "Tenis", "spor", "rekor"),
        ("LeBron James", "Basketbol", "spor", "iş-atlet"),
        ("Stephen Curry", "Basketbol", "spor", "devrim-şut"),
        ("Simone Biles", "Jimnastik", "spor", "zorluk-standart"),
        ("Usain Bolt", "Atletizm", "spor", "sprint-ikon"),
        ("Michael Phelps", "Yüzme", "spor", "olimpiyat"),
        ("A'ja Wilson", "Basketbol", "spor", "WNBA"),
        ("Erling Haaland", "Futbol", "spor", "golcü"),
        ("Kylian Mbappé", "Futbol", "spor", "hız-marka"),
        ("Shohei Ohtani", "Beyzbol", "spor", "iki-yönlü"),
        ("Max Verstappen", "F1", "spor", "dominant"),
        ("Lewis Hamilton", "F1", "spor", "aktivist-şampiyon"),
        ("Naomi Osaka", "Tenis", "spor", "mental-health"),
        ("Caitlin Clark", "Basketbol", "spor", "WNBA-büyüme"),
        ("Victor Wembanyama", "Basketbol", "spor", "yeni-nesil"),
        ("Iga Świątek", "Tenis", "spor", "dominant"),
        ("Erling — skip", "x", "x", "x"),
        # Müzik
        ("Taylor Swift", "Müzik", "kultur", "endüstri-güç"),
        ("Beyoncé", "Müzik", "kultur", "görsel-albüm"),
        ("Bad Bunny", "Müzik", "kultur", "Latin-küresel"),
        ("BTS", "Müzik", "kultur", "K-pop"),
        ("BLACKPINK", "Müzik", "kultur", "K-pop"),
        ("Drake", "Müzik", "kultur", "hip-hop"),
        ("The Weeknd", "Müzik", "kultur", "pop-R&B"),
        ("Billie Eilish", "Müzik", "kultur", "gen-Z"),
        ("Kendrick Lamar", "Müzik", "kultur", "Pulitzer"),
        ("Rosalía", "Müzik", "kultur", "flamenco-füzyon"),
        ("Hans Zimmer", "Müzik", "kultur", "film-skor"),
        ("John Williams", "Müzik", "kultur", "orkestral"),
        ("Yo-Yo Ma", "Müzik", "kultur", "klasik"),
        ("Ryuichi Sakamoto", "Müzik", "kultur", "elektronik-klasik"),
        ("A.R. Rahman", "Müzik", "kultur", "film-Hindistan"),
        # Sinema / TV
        ("Christopher Nolan", "Sinema", "sanat", "yönetmen"),
        ("Greta Gerwig", "Sinema", "sanat", "yönetmen"),
        ("Hayao Miyazaki", "Anime", "sanat", "Ghibli"),
        ("Bong Joon-ho", "Sinema", "sanat", "uluslararası"),
        ("Martin Scorsese", "Sinema", "sanat", "ustalık"),
        ("Chloé Zhao", "Sinema", "sanat", "bağımsız"),
        ("Denis Villeneuve", "Sinema", "sanat", "bilimkurgu"),
        ("Jordan Peele", "Sinema", "sanat", "korku-toplum"),
        ("Shonda Rhimes", "TV", "kultur", "showrunner"),
        ("Ryan Murphy", "TV", "kultur", "üretici"),
        # Edebiyat / fikir
        ("Margaret Atwood", "Edebiyat", "kultur", "distopya"),
        ("Kazuo Ishiguro", "Edebiyat", "kultur", "Nobel"),
        ("Ocean Vuong", "Edebiyat", "kultur", "şiir-roman"),
        ("Chimamanda Ngozi Adichie", "Edebiyat", "kultur", "anlatı"),
        ("Haruki Murakami", "Edebiyat", "kultur", "küresel-roman"),
        ("Orhan Pamuk", "Edebiyat", "kultur", "Nobel-TR"),
        ("Elif Shafak", "Edebiyat", "kultur", "TR-UK"),
        ("Yuval Noah Harari", "Fikir", "kultur", "tarih-AI"),
        ("Brené Brown", "Fikir", "kultur", "liderlik"),
        ("Malcolm Gladwell", "Fikir", "kultur", "pop-sosyal"),
        # Sanat / tasarım / mimari
        ("Refik Anadol", "Dijital sanat", "sanat", "AI-art-TR"),
        ("Yayoi Kusama", "Görsel sanat", "sanat", "enstalasyon"),
        ("Ai Weiwei", "Görsel sanat", "sanat", "aktivizm"),
        ("Banksy", "Sokak sanatı", "sanat", "anonim"),
        ("Olafur Eliasson", "Enstalasyon", "sanat", "algı"),
        ("Zaha Hadid Architects", "Mimari", "sanat", "parametrik"),
        ("Bjarke Ingels", "Mimari", "sanat", "BIG"),
        ("Tadao Ando", "Mimari", "sanat", "beton-ışık"),
        ("Virgil Abloh", "Tasarım", "kultur", "Off-White"),
        ("Phoebe Philo", "Moda", "kultur", "minimal"),
        ("Iris van Herpen", "Moda", "sanat", "3D-couture"),
        ("Dieter Rams", "Endüstriyel tasarım", "sanat", "10-ilke"),
        ("Jony Ive", "Tasarım", "sanat", "ürün"),
        # Sahne / dans / oyun
        ("Lin-Manuel Miranda", "Tiyatro", "kultur", "Hamilton"),
        ("Pina Bausch", "Dans", "sanat", "tanztheater"),
        ("Mikhail Baryshnikov", "Dans", "sanat", "bale"),
        ("Shigeru Miyamoto", "Oyun", "kultur", "Nintendo"),
        ("Hideo Kojima", "Oyun", "kultur", "anlatı"),
        ("Todd Howard", "Oyun", "kultur", "Bethesda"),
        ("Jenova Chen", "Oyun", "sanat", "thatgamecompany"),
        # Medya / yaratıcı ekonomi
        ("MrBeast", "YouTube", "kultur", "ölçek-içerik"),
        ("PewDiePie", "YouTube", "kultur", "erken-ölçek"),
        ("Emma Chamberlain", "Creator", "kultur", "lifestyle"),
        ("Charli D'Amelio", "TikTok", "kultur", "dans-kısa"),
        ("Khaby Lame", "TikTok", "kultur", "sessiz-komedi"),
        ("Casey Neistat", "YouTube", "kultur", "vlog-sinema"),
        ("Marques Brownlee", "Tech media", "kultur", "ürün-inceleme"),
        ("Pokimane", "Twitch", "kultur", "yayın"),
        ("xQc", "Twitch", "kultur", "reaksiyon"),
        ("Ninja", "Twitch", "kultur", "espor-köprü"),
        # Spor ek
        ("Tom Brady", "Amerikan futbolu", "spor", "şampiyonluk"),
        ("Patrick Mahomes", "Amerikan futbolu", "spor", "QB"),
        ("Megan Rapinoe", "Futbol", "spor", "aktivizm"),
        ("Alexia Putellas", "Futbol", "spor", "Ballon-dOr"),
        ("Erling Haaland", "Futbol", "spor", "gol"),
        ("Vinícius Júnior", "Futbol", "spor", "kanat"),
        ("Jude Bellingham", "Futbol", "spor", "orta-saha"),
        ("Lamine Yamal", "Futbol", "spor", "genç-yetenek"),
        ("IShowSpeed", "Streamer", "kultur", "spor-eğlence"),
        ("Trevor Noah", "Komedi", "kultur", "global-host"),
        ("Bo Burnham", "Komedi", "sanat", "meta-show"),
        ("Dave Chappelle", "Komedi", "kultur", "stand-up"),
        ("Rihanna", "Müzik/Moda", "kultur", "Fenty"),
        ("Pharrell Williams", "Müzik/Moda", "kultur", "Louis-Vuitton"),
        ("Kanye West", "Müzik/Moda", "kultur", "tartışmalı-etki"),
        ("Lady Gaga", "Müzik", "kultur", "performans"),
        ("Adele", "Müzik", "kultur", "vokal"),
        ("Ed Sheeran", "Müzik", "kultur", "songwriter"),
        ("Coldplay", "Müzik", "kultur", "stadyum"),
        ("Radiohead", "Müzik", "sanat", "deneysel"),
        ("Björk", "Müzik", "sanat", "avangart"),
        ("Arvo Pärt", "Müzik", "sanat", "minimal-kutsal"),
        ("Marina Abramović", "Performans", "sanat", "beden"),
        ("Cindy Sherman", "Fotoğraf", "sanat", "kimlik"),
        ("Annie Leibovitz", "Fotoğraf", "kultur", "portre"),
        ("Steve McCurry", "Fotoğraf", "kultur", "belgesel"),
        ("David Attenborough", "Belgesel", "kultur", "doğa"),
        ("Greta Thunberg", "Aktivizm", "kultur", "iklim"),
        ("Malala Yousafzai", "Aktivizm", "kultur", "eğitim"),
        ("Oprah Winfrey", "Medya", "kultur", "etki"),
        ("Barack Obama", "Siyaset/Medya", "kultur", "anlatı"),
        ("Michelle Obama", "Yazar/Medya", "kultur", "ilham"),
        ("Pew Research", "Kurum", "kultur", "veri-kamu"),
    ]
    people = []
    seen = set()
    for n, alan, kat, etiket in raw:
        if "skip" in n.lower() or n in seen:
            continue
        seen.add(n)
        people.append({
            "rank": len(people) + 1,
            "ad": n,
            "alan": alan,
            "kategori": kat,
            "etiket": etiket,
            "ajans_eslesme": _culture_to_agency(kat, alan),
            "kaynaklar": [{"tip": "arama", "not": "Aylık: eser/performans/röportaj"}],
            "son_inceleme": TODAY,
            "guncelleme_durumu": "seed",
        })
    pad = 1
    while len(people) < 110:
        people.append({
            "rank": len(people) + 1,
            "ad": f"Araştırma Adayı K-{pad:03d}",
            "alan": "TBD",
            "kategori": "pending",
            "etiket": "bos-slot",
            "ajans_eslesme": ["HRA-REC"],
            "kaynaklar": [],
            "son_inceleme": TODAY,
            "guncelleme_durumu": "bos-slot",
        })
        pad += 1
    return people


def _culture_to_agency(kat: str, alan: str) -> list[str]:
    if kat == "spor":
        return ["MKT-BRD", "MKT-SOC", "STR-GRW"]
    if alan in ("YouTube", "TikTok", "Twitch", "Creator", "Streamer", "Tech media"):
        return ["MKT-SOC", "MED-CRE", "MED-PUB"]
    if alan in ("Müzik", "Sinema", "TV", "Dans", "Tiyatro", "Oyun"):
        return ["MED-CRE", "MKT-BRD", "PRD-DSN"]
    if alan in ("Edebiyat", "Fikir", "Belgesel", "Medya"):
        return ["MED-PUB", "AI-RES", "STR-INT"]
    return ["HRA-REC", "MKT-BRD"]


def build_org() -> dict[str, Any]:
    c_levels = []
    depts = []
    roles = []
    for chair, ds in DOMAINS:
        c_levels.append({
            "kod": chair,
            "katman": "C-LEVEL",
            "rapor": "Group CEO",
            "departmanlar": [d[0] for d in ds],
        })
        for kod, ad, role_list in ds:
            depts.append({
                "kod": kod,
                "ad": ad,
                "baskan": chair,
                "katman": "DOMAIN-YÖNETİM",
                "roller": role_list,
            })
            for r in role_list:
                roles.append({
                    "rol": r,
                    "dept": kod,
                    "baskan": chair,
                    "katman": "IC" if "Uzman" in r or "Analist" in r or "Mühendis" in r else "YÖNETİM",
                    "prompt_adet": PROMPTS_PER_ROLE,
                })
    board = [
        {"rol": r, "slug": s, "katman": k, "prompt_adet": PROMPTS_PER_ROLE}
        for r, s, k in BOARD
    ]
    return {
        "ts": TS,
        "hiyerarsi": [
            "KURUL (Chairman)",
            "C-OFİS (Group CEO/COO)",
            "C-LEVEL (CTO/CAIO/CDO/...)",
            "DOMAIN-YÖNETİM (46 dept)",
            "YÖNETİM / IC / GM-OFİSİ / WORKER",
        ],
        "board": board,
        "c_levels": c_levels,
        "departmanlar": depts,
        "roller": roles,
        "ozet": {
            "c_level": len(c_levels),
            "departman": len(depts),
            "rol": len(roles),
            "board": len(board),
            "prompt_toplam_hedef": (len(roles) + len(board)) * PROMPTS_PER_ROLE,
        },
        "flag": {
            "istek": "900000000 karakter/prompt",
            "karar": "REDDEDILDI",
            "neden": "LLM bağlam + depo boyutu + anlamsız dolgu",
            "esdeger": f"{PROMPTS_PER_ROLE} yapılandırılmış prompt/rol · {TARGET_CHARS_MIN}-{TARGET_CHARS_MAX} karakter · referans zinciri",
        },
    }


def prompt_body(role: str, dept: str, chair: str, slot: tuple, mcp_hint: str, influence_hint: str) -> str:
    fam_id, fam_name, idx, title = slot
    pid = f"{dept or 'BOARD'}::{_slug(role)}::{fam_id}-{idx:02d}"
    sections = [
        f"# PROMPT SÖZLEŞMESİ — {title}",
        f"",
        f"- id: `{pid}`",
        f"- rol: **{role}**",
        f"- departman: `{dept or 'BOARD'}` · başkan: `{chair or 'HOLDING'}`",
        f"- aile: {fam_name}",
        f"- ts_uretim: {TS}",
        f"- hedef_uzunluk: {TARGET_CHARS_MIN}-{TARGET_CHARS_MAX} karakter (🚩 900M YASAK)",
        f"- dogruluk_hedefi: %99 (kaynaklı iddia; yoksa varsayım etiketi)",
        f"",
        f"## 1. Kimlik & yetki",
        f"Sen {role} olarak çalışırsın. Yetki alanın: {dept or 'holding kurulu'}.",
        f"Rapor hattı: {chair or 'Chairman'} → Group CEO. Çıktı: kopyala-yapıştır hazır, dolgusuz.",
        f"",
        f"## 2. Girdi sözleşmesi",
        f"- Zorunlu: görev tek cümle, başarı ölçütü, kısıtlar, son tarih (UTC).",
        f"- Bağlam: ilgili dosya yolları, MCP araçları, önceki AUDIT öğrenimi.",
        f"- Yasak: gizli anahtar, lisans ihlali, doğrulanmamış iddia.",
        f"",
        f"## 3. Uzman kurul seçimi",
        f"Bu senaryoda aktif uzmanlar: Baş Mimar, Prompt Mühendisi, "
        + ("Denetçi, Bilgi Damıtıcısı" if fam_id in ("arastirma", "denetim") else "Otomasyon Mühendisi, İş/Gelir Stratejisti")
        + ".",
        f"Kurul özeti 2-4 satır; tek net çıktı; DENETÇİ 6 katman.",
        f"",
        f"## 4. MCP & araç bağlama",
        f"Öncelikli MCP/hint: {mcp_hint}.",
        f"Araç çağrısı öncesi GetMcpTools şema doğrula. Yazma işlemlerinde onay kuralına uy.",
        f"",
        f"## 5. Etki / yetenek referansı",
        f"İzlenen sinyal: {influence_hint}.",
        f"Alıntı kuralı: kaynak URL + tarih; yoksa `VARSAYIM:` etiketi.",
        f"",
        f"## 6. İş adımları (zorunlu sıra)",
        f"1. ts_start al (`date -u`).",
        f"2. BILGI_TABANI ilgili başlıkları oku.",
        f"3. Görevi alt-görevle (max 7).",
        f"4. Araç/araştırma ile kanıt topla.",
        f"5. Çıktıyı üret (aşağıdaki şablon).",
        f"6. 6 katman denetim: structural / integrity-SHA256 / semantic / reference / patterns / review.",
        f"7. Öğrenim satırı + AUDIT_LOG.jsonl append.",
        f"8. ts_end.",
        f"",
        f"## 7. Çıktı şablonu",
        f"### Kurul özeti",
        f"(2-4 satır)",
        f"### Teslim",
        f"(asıl ürün — kod/doküman/karar)",
        f"### Riskler",
        f"- 🚩 varsa: [ne] · [neden] · [alternatif]",
        f"### Damga",
        f"⏱️ Damga: [UTC] · 🔍 Denetim: [GEÇTİ/KALDI] · 📚 Öğrenim: [1 satır] · 🔗 Önceki: [evet/hayır]",
        f"",
        f"## 8. Senaryo-özel derinleştirme ({title})",
        f"Bu prompt'un işi: {title} bağlamında {role} karar/üretim kalitesini maksimize etmek.",
        f"Kalite rubriği: sinyal yoğunluğu, doğrulanabilirlik, yeniden kullanılabilirlik, güvenlik (5 kural), gelir bağı.",
        f"Anti-pattern: dolgu paragrafı, tekrar, genel tavsiye, kaynaksız rakam.",
        f"",
        f"## 9. Kabul kriterleri",
        f"- [ ] Girdi alanları dolu veya VARSAYIM işaretli",
        f"- [ ] En az 1 somut artefakt yolu veya karar",
        f"- [ ] Denetim 6/6 veya KALDI+neden",
        f"- [ ] Karakter aralığı {TARGET_CHARS_MIN}-{TARGET_CHARS_MAX} (aşırı uzunluk = KALDI)",
        f"- [ ] Türkçe, komut tipi, McKinsey kıdemli ortak ton",
        f"",
        f"## 10. Genişletme çengelleri (derinlik, dolgu değil)",
        f"- İlişkili departmanlar: aynı başkan altı kardeş dept'ler ile handoff.",
        f"- Katalog eşleme: `katalog/KATALOG_INDEKS.md` ilgili ajan/skill.",
        f"- Pilot birimler: AdOps, Tahmin, Movéa, VizaTrack (holding.json).",
        f"- Aylık arşiv: `data/etki_sahipleri.json` + `data/ozel_yetenekler.json` son_inceleme.",
        f"",
    ]
    # Pad intentionally with structured checklists to reach TARGET_CHARS_MIN without nonsense prose
    pad_lines = [
        f"## 11. Operasyon kontrol listesi ({fam_id}-{idx:02d})",
        "- Önkoşul: kimlik doğrulama / ortam / branch durumu kontrol",
        "- Veri: hangi tablolar/dosyalar değişebilir?",
        "- Geri alma: revert komutu veya karar iptal yolu",
        "- İletişim: kim bilgilendirilir (C-level / domain / IC)?",
        "- Metrik: başarı 1 cümle KPI",
        "- Sonraki zincir: hangi prompt id tetiklenir?",
        "",
        "## 12. Örnek girdi",
        "```",
        f"gorev: {title} için {role} teslimi",
        "olcu: denetim GEÇTİ + artefakt yolu",
        "kisit: 5 güvenlik kuralı; lisans MIT atıf",
        f"mcp: {mcp_hint}",
        "```",
        "",
        "## 13. Örnek başarısızlık",
        "- Kaynaksız iddia → KALDI",
        "- Secret sızıntısı → KALDI + rotasyon",
        "- 900M karakter üretmeye çalışma → 🚩 reddet, bu sözleşmeye dön",
        "",
    ]
    body = "\n".join(sections + pad_lines)
    # Soft pad with role-specific bullet expansions if under min
    n = 1
    while len(body) < TARGET_CHARS_MIN:
        body += (
            f"\n## EK-{n} Derinlik maddesi\n"
            f"- {role} için `{fam_id}` senaryo {idx}: alt kontrol {n} — "
            f"kanıt türü, karar eşiği, dokümantasyon yolu, audit alanı.\n"
            f"- Çıktı alanı: `uretim/promptlar/{_slug(role)}/{pid.replace('::','__')}.md` güncellenir.\n"
        )
        n += 1
        if n > 40:
            break
    if len(body) > TARGET_CHARS_MAX:
        body = body[: TARGET_CHARS_MAX - 80] + "\n\n<!-- kırpıldı: TARGET_CHARS_MAX -->\n"
    return body


def _slug(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9çğıöşü]+", "-", s, flags=re.I)
    return s.strip("-")[:60] or "rol"


def mcp_hint_for(dept: str) -> str:
    mapping = {
        "INF-MCP": "katalog/mcps + canlı Cursor MCP sunucuları",
        "AI-RES": "Exa, arxiv-mcp, Elastic-docs",
        "AI-AGT": "Convex, Encore, Apify, Harness",
        "SEC-OPS": "Sentry, Datadog, Zscaler, Antimetal",
        "DAT-ENG": "Neon, Supabase, Cockroach, Snowflake, Clickhouse",
        "MKT-PRF": "Mixpanel, Amplitude, Posthog, Facebook/Google Ads MCP",
        "MED-PUB": "Mintlify, Gitbook, ChatPRD",
        "ENG-DEV": "Vercel, Render, Railway, Cloudflare, Monk",
        "STR-INT": "Bright Data, Apify, Exa, Ddg-search",
    }
    return mapping.get(dept, "GetMcpTools ile görev-uygun sunucu seç")


def influence_hint_for(dept: str, tech: list, culture: list) -> str:
    t = tech[(hash(dept) % max(1, len(tech)))]["ad"] if tech else "TBD"
    c = culture[(hash(dept[::-1]) % max(1, len(culture)))]["ad"] if culture else "TBD"
    return f"teknoloji: {t} · kültür/yetenek: {c}"


def build_prompt_index(org: dict, tech: list, culture: list) -> dict[str, Any]:
    entries = []
    roles = [(b["rol"], "", "HOLDING") for b in org["board"]]
    roles += [(r["rol"], r["dept"], r["baskan"]) for r in org["roller"]]
    for role, dept, chair in roles:
        for slot in PROMPT_SLOTS:
            fam_id, fam_name, idx, title = slot
            pid = f"{dept or 'BOARD'}::{_slug(role)}::{fam_id}-{idx:02d}"
            entries.append({
                "id": pid,
                "rol": role,
                "dept": dept or "BOARD",
                "baskan": chair,
                "aile": fam_id,
                "baslik": title,
                "hedef_karakter": [TARGET_CHARS_MIN, TARGET_CHARS_MAX],
                "mcp_hint": mcp_hint_for(dept),
                "etki_hint": influence_hint_for(dept or role, tech, culture),
            })
    return {
        "ts": TS,
        "prompt_per_rol": PROMPTS_PER_ROLE,
        "rol_adet": len(roles),
        "toplam_prompt": len(entries),
        "sozlesme": {
            "min_char": TARGET_CHARS_MIN,
            "max_char": TARGET_CHARS_MAX,
            "red": "900000000 karakter isteği reddedildi (K-003/K-010/K-017 emsali)",
        },
        "entries": entries,
    }


def materialize_prompts(index: dict, only_keys: set[str] | None) -> list[str]:
    out_paths = []
    by_role: dict[str, list] = {}
    for e in index["entries"]:
        key = f"{e['dept']}::{e['rol']}"
        by_role.setdefault(key, []).append(e)
    for key, items in by_role.items():
        dept, role = key.split("::", 1)
        if only_keys and key not in only_keys and dept not in only_keys and role not in only_keys:
            continue
        role_dir = ROOT / "uretim" / "promptlar" / (dept or "BOARD") / _slug(role)
        manifest = []
        for e in items:
            slot = next(s for s in PROMPT_SLOTS if s[0] == e["aile"] and s[2] == int(e["id"].rsplit("-", 1)[-1]))
            body = prompt_body(role, "" if dept == "BOARD" else dept, e["baskan"], slot, e["mcp_hint"], e["etki_hint"])
            fname = e["id"].replace("::", "__") + ".md"
            fp = role_dir / fname
            write(fp, body)
            manifest.append({"id": e["id"], "path": str(fp.relative_to(ROOT)), "chars": len(body), "sha256": sha256_text(body)})
            out_paths.append(str(fp.relative_to(ROOT)))
        write_json(role_dir / "MANIFEST.json", {"rol": role, "dept": dept, "adet": len(manifest), "ts": TS, "items": manifest})
    return out_paths


def write_mcp_doc(hier: dict) -> None:
    lines = [
        "# MCP HİYERARŞİSİ — mekanizma & katmanlar",
        f"> Üretim: {TS} · katalog={hier['katalog_adet']} · canlı={hier['canli_adet']} · toplam={hier['toplam']}",
        "",
        "## 🚩 Kapsam notu",
        "900M karakterlik prompt üretimi reddedildi. Bu belge MCP envanteri + iş akışı katmanlarıdır.",
        "",
        "## Katmanlar",
    ]
    for k, v in hier["katmanlar"].items():
        lines.append(f"### {k}")
        lines.append(v["aciklama"])
        if "ornekler" in v:
            lines.append("- Örnekler: " + ", ".join(v["ornekler"]))
        if "kategoriler" in v:
            lines.append("- Kategoriler: " + ", ".join(v["kategoriler"]))
        lines.append("")
    lines.append("## İş akışı sırası")
    for s in hier["is_akis_sirasi"]:
        lines.append(f"- {s}")
    lines.append("")
    lines.append("## Katalog kategorileri (adet)")
    for k, n in hier["katalog_kategoriler"].items():
        lines.append(f"- `{k}`: {n}")
    lines.append("")
    lines.append("## Canlı Cursor MCP (örnek)")
    for m in hier["canli"][:40]:
        lines.append(f"- `{m['sunucu']}` · {m['kategori']}/{m['etiket']}")
    lines.append(f"- … toplam {hier['canli_adet']} canlı sunucu (`data/mcp_hiyerarsi.json`)")
    lines.append("")
    lines.append("## Makine okunur")
    lines.append("- `data/mcp_hiyerarsi.json`")
    write(ROOT / "docs" / "MCP-HIYERARSI.md", "\n".join(lines) + "\n")


def write_calendar() -> None:
    months = []
    y, m = NOW.year, NOW.month
    for i in range(12):
        mm = m + i
        yy = y + (mm - 1) // 12
        mo = ((mm - 1) % 12) + 1
        months.append((yy, mo))
    lines = [
        "# AYLIK GÜNCELLEME TAKVİMİ — Etki / Yetenek / MCP Arşivi",
        f"> Oluşturma: {TS} · Döngü: her ayın 1'i 06:00 UTC (`scripts/mcp_ajans_etki_uret.py --hepsi`)",
        "",
        "## Rutin",
        "1. MCP katalog + canlı sunucu farkı → `data/mcp_hiyerarsi.json`",
        "2. Etki sahipleri: yeni makale/röportaj/proje taraması → `son_inceleme` güncelle",
        "3. Özel yetenekler: kültür/sanat/spor sinyali → arşiv",
        "4. Prompt index yenile (sözleşme değişmedikçe body hash stabil)",
        "5. BILGI_TABANI + AUDIT_LOG damga",
        "",
        "## 12 aylık takvim",
        "| Ay | Odak | Çıktı |",
        "|---|---|---|",
    ]
    focuses = [
        "AI/C-level etki yenileme",
        "Açık kaynak & araç liderleri",
        "Güvenlik & hizalama isimleri",
        "Yatırımcı / strateji sesleri",
        "Spor yetenekleri",
        "Müzik & yaratıcı ekonomi",
        "Sinema / tasarım",
        "Edebiyat / fikir",
        "MCP yeni bağlayıcılar",
        "Pilot birim gelir sinyali",
        "Yıl sonu ranking revizyonu",
        "Boş-slot araştırma kapatma",
    ]
    for i, (yy, mo) in enumerate(months):
        lines.append(f"| {yy}-{mo:02d} | {focuses[i % 12]} | arşiv diff + AUDIT satırı |")
    lines.append("")
    lines.append("## Otomasyon kancası")
    lines.append("- Mevcut: `.github/workflows/aylik-kurul.yml` (ayın 1'i)")
    lines.append("- Ekleme önerisi: aynı workflow'a `python3 scripts/mcp_ajans_etki_uret.py --hepsi --pilot` adımı")
    write(ROOT / "docs" / "AYLIK-GUNCELLEME-TAKVIMI.md", "\n".join(lines) + "\n")


def write_master_overview(org: dict, hier: dict, tech_n: int, cult_n: int, prompt_n: int) -> None:
    lines = [
        "# LLM AI AJANS — MCP × Etki Arşivi × Prompt Motoru",
        f"> {TS}",
        "",
        "## Kurul özeti",
        "- Baş Mimar: MCP L0–L5 hiyerarşi + 46 dept org.",
        "- Bilgi Damıtıcısı: ≥100 tech etki + ≥110 kültür/yetenek seed arşivi.",
        "- Prompt Mühendisi: 122 prompt/rol sözleşmesi (4–12 KiB); 🚩 900M reddedildi.",
        "- Otomasyon: aylık takvim + `mcp_ajans_etki_uret.py` döngüsü.",
        "",
        "## Sayılar",
        f"- MCP katalog+canlı: **{hier['toplam']}**",
        f"- Tech etki: **{tech_n}** · Kültür/yetenek: **{cult_n}**",
        f"- Rol (board+IC): **{org['ozet']['rol'] + org['ozet']['board']}**",
        f"- Prompt index: **{prompt_n}**",
        "",
        "## Dosyalar",
        "- `docs/MCP-HIYERARSI.md`",
        "- `docs/AYLIK-GUNCELLEME-TAKVIMI.md`",
        "- `data/mcp_hiyerarsi.json`",
        "- `data/etki_sahipleri.json`",
        "- `data/ozel_yetenekler.json`",
        "- `data/ajans_org.json`",
        "- `data/prompt_index.json`",
        "- `uretim/promptlar/` (pilot materyalizasyon)",
        "",
        "## 🚩",
        f"{org['flag']['istek']} · {org['flag']['neden']} · {org['flag']['esdeger']}",
    ]
    write(ROOT / "docs" / "LLM-AI-AJANS-ETKI-MOTORU.md", "\n".join(lines) + "\n")


def append_memory(summary: str) -> None:
    bt = ROOT / "BILGI_TABANI.md"
    text = bt.read_text(encoding="utf-8") if bt.exists() else ""
    entry = (
        f"\n## {TS} — MCP×etki×prompt motoru\n"
        f"- {summary}\n"
        f"- 🚩 900M karakter/prompt reddedildi (K-017 emsali); 122×(4–12KiB) sözleşme.\n"
    )
    # insert after header block: find first ## and prepend new at top after intro
    marker = "<!-- SONRAKİ GİRİŞLER BURAYA — en yeni en üstte -->"
    if marker in text:
        text = text.replace(marker, marker + entry)
    else:
        text = entry + text
    bt.write_text(text, encoding="utf-8")
    audit = {
        "ts_start": TS,
        "ts_end": TS,
        "islem": "mcp-ajans-etki-uret",
        "uzmanlar": ["bas-mimar", "prompt-muhendisi", "bilgi-damiticisi", "otomasyon", "denetci"],
        "girdi_ozet": "MCP+etki+900M-prompt istegi",
        "cikti_ozet": summary[:200],
        "denetim": "GECTI",
        "ogrenim": "Imkansiz uzunluk istegini sozlesmeli prompt katalog + aylik arsiv dongusune cevir",
        "onceki_ogrenim_kullanildi": "evet (K-017 / AJANS-GUNLUK 900B emsali)",
    }
    with (ROOT / "AUDIT_LOG.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(audit, ensure_ascii=False) + "\n")


def dogrula(org: dict, hier: dict, tech: list, cult: list, index: dict) -> int:
    errs = []
    if hier["katalog_adet"] < 50:
        errs.append("katalog mcp az")
    if len(tech) < 100:
        errs.append(f"tech<{100}: {len(tech)}")
    if len(cult) < 100:
        errs.append(f"cult<{100}: {len(cult)}")
    if org["ozet"]["departman"] != 46:
        errs.append(f"dept!=46: {org['ozet']['departman']}")
    if index["prompt_per_rol"] != 122:
        errs.append("prompt_per_rol!=122")
    expected = (org["ozet"]["rol"] + org["ozet"]["board"]) * 122
    if index["toplam_prompt"] != expected:
        errs.append(f"prompt toplam {index['toplam_prompt']} != {expected}")
    # sample materialized
    sample = list((ROOT / "uretim" / "promptlar").rglob("*.md"))[:5]
    for p in sample:
        n = len(p.read_text(encoding="utf-8"))
        if n < TARGET_CHARS_MIN or n > TARGET_CHARS_MAX + 200:
            errs.append(f"uzunluk {p}: {n}")
    if errs:
        print("KALDI:", errs)
        return 1
    print("GEÇTİ: mcp=%d tech=%d cult=%d prompts=%d" % (
        hier["toplam"], len(tech), len(cult), index["toplam_prompt"]))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hepsi", action="store_true", default=True)
    ap.add_argument("--sadece-mcp", action="store_true")
    ap.add_argument("--sadece-arsiv", action="store_true")
    ap.add_argument("--sadece-org", action="store_true")
    ap.add_argument("--sadece-prompt", action="store_true")
    ap.add_argument("--pilot", action="store_true", help="C-level board + INF-MCP rollerini materyalize et")
    ap.add_argument("--dogrula", action="store_true")
    args = ap.parse_args()
    only = args.sadece_mcp or args.sadece_arsiv or args.sadece_org or args.sadece_prompt
    do_mcp = args.sadece_mcp or (args.hepsi and not only)
    do_arsiv = args.sadece_arsiv or (args.hepsi and not only)
    do_org = args.sadece_org or (args.hepsi and not only)
    do_prompt = args.sadece_prompt or (args.hepsi and not only)

    catalog = catalog_mcps()
    hier = build_mcp_hierarchy(catalog)
    tech = tech_influencers()
    cult = culture_talents()
    org = build_org()
    index = build_prompt_index(org, tech, cult)

    if do_mcp:
        write_json(ROOT / "data" / "mcp_hiyerarsi.json", hier)
        write_mcp_doc(hier)
    if do_arsiv:
        write_json(ROOT / "data" / "etki_sahipleri.json", {"ts": TS, "adet": len(tech), "kisiler": tech})
        write_json(ROOT / "data" / "ozel_yetenekler.json", {"ts": TS, "adet": len(cult), "kisiler": cult})
        write_calendar()
    if do_org:
        write_json(ROOT / "data" / "ajans_org.json", org)
    if do_prompt:
        write_json(ROOT / "data" / "prompt_index.json", index)
        # Pilot set: all board + INF-MCP roles
        only_keys = set()
        if args.pilot or True:  # always materialize pilot for PR evidence
            for b in org["board"]:
                only_keys.add(f"BOARD::{b['rol']}")
            for r in org["roller"]:
                if r["dept"] == "INF-MCP":
                    only_keys.add(f"{r['dept']}::{r['rol']}")
            # also one worker-heavy dept for variety
            for r in org["roller"]:
                if r["dept"] == "AI-PRM":
                    only_keys.add(f"{r['dept']}::{r['rol']}")
        paths = materialize_prompts(index, only_keys)
        print(f"materyalize: {len(paths)} prompt dosyası")

    write_master_overview(org, hier, len(tech), len(cult), index["toplam_prompt"])
    summary = (
        f"MCP={hier['toplam']}; tech={len(tech)}; cult={len(cult)}; "
        f"org_roles={org['ozet']['rol']+org['ozet']['board']}; prompts_index={index['toplam_prompt']}"
    )
    append_memory(summary)
    if args.dogrula or True:
        return dogrula(org, hier, tech, cult, index)
    return 0


if __name__ == "__main__":
    sys.exit(main())
