#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HOLDING × İŞTİRAK × ÜLKE × ROL KART × SORU BANKASI üretici.

Üretir:
  data/holding_istirak_org.json
  data/soru_bankasi.json
  data/ulke_pazar_iskeleti.json
  docs/HOLDING-ISTIRAK-ORG.md
  docs/ULKE-PAZAR-ISKELETI.md
  docs/OZ-DENETIM-SORU-BANKASI.md
  docs/SECRETS-DRYRUN-MATRISI.md
  uretim/rol-kartlari/*.md (pilot)
  uretim/devir/CLAUDE-CODE-MASTER-PROMPT-HOLDING-V2.md
  uretim/OZET-TEK-SAYFA.md

🚩 900M/900B karakter prompt RED — 122 yapılandırılmış sözleşme + referans zinciri.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import hashlib
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
NOW = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

TIERS = ["C-LEVEL", "EVP", "DIRECTOR", "LEAD", "SPECIALIST", "ANALYST", "WORKER"]
PROMPTS_PER_ROLE = 122
QUESTIONS_UNIVERSAL_TARGET = 120
QUESTIONS_PER_DEPT_BLOCK = 24
QUESTIONS_PER_TIER = 12
ROLE_CARD_SELF_INQUIRY = 17
TOP5_PER_TITLE = 5

# --- Holding units + subsidiary blueprints ---
ISTIRAKLAR: list[dict[str, Any]] = [
    {
        "id": "hq",
        "unit": "Holding HQ / OS",
        "repo": "claude-otonom-sistem",
        "segment": "os",
        "domain": "Ortak standart, gözetim, jeneratörler, MCP/skill motoru",
        "web_app": False,
        "depts": [
            ("INF", "Teknoloji & Altyapı", ["CI/CD & Actions", "Validation & Security", "MCP & Integrations", "Repo Hygiene"]),
            ("TAL", "Yetenek & Ajan Kalitesi", ["Agent Lifecycle", "Quality Bar", "Training Loops"]),
            ("PRD", "Ürün & Premium Paket", ["Premium Components", "Packaging & Licensing", "Docs & DX"]),
            ("FIN", "Finans & Faturalama", ["Cost Control", "Revenue Ops"]),
            ("LEG", "Hukuk & Uyum", ["Licensing", "Privacy (KVKK/GDPR)", "Ad Policy"]),
        ],
        "c_roles": ["CEO", "COO", "CTO", "CFO", "CCO", "CAIO"],
        "top5_seed": [
            ("Dario Amodei", "https://www.anthropic.com", "AI güvenlik / org design"),
            ("Sam Altman", "https://openai.com", "ürün+platform ölçek"),
            ("Demis Hassabis", "https://deepmind.google", "araştırma→ürün"),
            ("Jensen Huang", "https://www.nvidia.com", "platform ekonomisi"),
            ("Satya Nadella", "https://www.microsoft.com", "holding portföy yönetimi"),
        ],
    },
    {
        "id": "adops",
        "unit": "AdOps Agency",
        "repo": "adops-agents",
        "segment": "agency",
        "domain": "Performans pazarlama & programatik",
        "web_app": False,
        "depts": [
            ("PRG", "Programatik Satın Alma", ["Open Auction & Curation", "PMP & Deals", "CTV / OTT", "DOOH & Audio", "Bid Algorithms"]),
            ("SEA", "Ücretli Arama", ["Google Ads Core", "SA360 & Automation", "PMax & Shopping", "Microsoft Ads"]),
            ("SOC", "Ücretli Sosyal", ["Meta", "TikTok", "LinkedIn & X", "Snap & Pinterest", "Creative Testing"]),
            ("MOB", "Mobil UA & Uygulama", ["Apple Search Ads", "Google App Campaigns", "MMP (Adjust/AppsFlyer)", "Retargeting & CRM"]),
            ("RET", "Perakende Medyası", ["Amazon Ads", "TR Marketplaces", "Criteo & Onsite", "Offsite & DSP"]),
            ("SEO", "SEO & İçerik Motoru", ["Technical SEO", "Content Production", "Digital PR & Links", "Repo Storefront"]),
            ("CRO", "CRO & Deneyim", ["Experimentation", "Landing Systems", "UX Research"]),
            ("ANA", "Analitik & Ölçümleme", ["GA4 & Tagging", "Attribution", "MMM & Incrementality", "Clean Rooms & Privacy", "Dashboards"]),
            ("CRE", "Kreatif Stüdyo & DCO", ["Concept & Copy", "Video & Motion", "DCO & Feeds", "Ad Format Lab"]),
            ("STR", "Strateji & Planlama", ["Audience & Insight", "Media Mix", "Playbooks & POVs"]),
            ("CLS", "Müşteri Hizmetleri", ["Account Leadership", "Reporting Cadence", "Onboarding"]),
            ("NBD", "Yeni İş & Inbound", ["Inbound Capture", "Pitch Factory", "Lead Scoring"]),
            ("PRT", "Ortaklıklar & Sponsorluklar", ["Infra Sponsors", "Referral Programs", "Ecosystem Relations"]),
        ],
        "c_roles": ["CEO", "COO", "CMO", "CDO", "CFO", "CCO"],
        "top5_seed": [
            ("Avinash Kaushik", "https://www.kaushik.net", "dijital analitik"),
            ("Neil Patel", "https://neilpatel.com", "growth/SEO"),
            ("Mari Smith", "https://www.marismith.com", "sosyal reklam"),
            ("Rand Fishkin", "https://sparktoro.com", "SEO/audience"),
            ("Brian Solis", "https://briansolis.com", "dijital dönüşüm"),
        ],
    },
    {
        "id": "performer",
        "unit": "Performer Growth Hub",
        "repo": "performer-growth-hub",
        "segment": "agency",
        "domain": "Uygulama büyüme / app growth (UA, retention, monetization)",
        "web_app": True,
        "depts": [
            ("UA", "User Acquisition", ["Paid UA", "ASA/GAC", "Influencer UA", "Creative UA Lab"]),
            ("RETN", "Retention & CRM", ["Lifecycle", "Push/Email", "In-app Messaging", "Win-back"]),
            ("MON", "Monetization", ["IAP", "Ads Mediation", "Pricing Experiments"]),
            ("PROD", "Product Growth", ["Onboarding Funnel", "Feature Adoption", "A/B Lab"]),
            ("DATA", "Growth Analytics", ["MMP", "Cohort LTV", "Experiment Design"]),
        ],
        "c_roles": ["CEO", "CPO", "CMO", "CDO", "CTO"],
        "top5_seed": [
            ("Andrew Chen", "https://andrewchen.com", "growth loops"),
            ("Brian Balfour", "https://brianbalfour.com", "growth frameworks"),
            ("Elena Verna", "https://www.elenaverna.com", "PLG/growth"),
            ("Casey Winters", "https://caseyaccidental.com", "marketplace growth"),
            ("Reforge (team)", "https://www.reforge.com", "growth programları"),
        ],
    },
    {
        "id": "vizatrack",
        "unit": "VizaTrack",
        "repo": "VizaTrack",
        "segment": "product",
        "domain": "Göç & relokasyon — iOS/Android/Web",
        "web_app": True,
        "depts": [
            ("MOBAPP", "Mobil Ürün", ["iOS", "Android", "Cross-platform UX"]),
            ("WEB", "Web Platform", ["SSR/App Router", "Case Portal", "Docs"]),
            ("CASE", "Vize Operasyon", ["Başvuru Akışı", "Doküman QA", "Ajans Ortaklığı"]),
            ("COMP", "Uyumluluk", ["Ülke Mevzuatı", "KVKK/GDPR", "Audit Trail"]),
            ("CS", "Müşteri Başarı", ["Onboarding", "Support SLA", "NPS"]),
            ("GROW", "Büyüme", ["SEO Content", "Paid Acquisition", "Partner Channel"]),
        ],
        "c_roles": ["CEO", "CTO", "CPO", "CLO", "CMO", "COO"],
        "top5_seed": [
            ("Nir Eyal", "https://www.nirandfar.com", "habit/ürün"),
            ("Lenny Rachitsky", "https://www.lennyrachitsky.com", "ürün büyüme"),
            ("Marty Cagan", "https://www.svpg.com", "ürün liderliği"),
            ("Julie Zhuo", "https://medium.com/@joulee", "ürün tasarım"),
            ("Shreyas Doshi", "https://twitter.com/shreyas", "PM craft"),
        ],
    },
    {
        "id": "hukuk",
        "unit": "Holding Hukuk & Uyum",
        "repo": "claude-otonom-sistem",
        "segment": "shared-service",
        "domain": "KVKK/GDPR, lisans, reklam politikası, sözleşme, ülke onayı",
        "web_app": False,
        "depts": [
            ("PRIV", "Gizlilik", ["KVKK", "GDPR", "DPIA"]),
            ("LIC", "Lisanslama", ["OSS License", "Vendor Contracts", "IP"]),
            ("ADP", "Reklam Politikası", ["Platform Policy", "Claim Review", "Crisis"]),
            ("REG", "Regülasyon", ["Ülke Onayı", "Cross-border Transfer", "Retention"]),
        ],
        "c_roles": ["CLO", "CCO", "DPO"],
        "top5_seed": [
            ("Daniel Solove", "https://teachprivacy.com", "gizlilik hukuku"),
            ("Woodrow Hartzog", "https://www.woodrowhartzog.com", "privacy by design"),
            ("Helen Nissenbaum", "https://nissenbaum.tech.cornell.edu", "contextual integrity"),
            ("EDPB (kurum)", "https://edpb.europa.eu", "GDPR otorite"),
            ("KVKK (kurum)", "https://www.kvkk.gov.tr", "TR gizlilik"),
        ],
    },
    {
        "id": "tahmin",
        "unit": "Tahmin Uzmanı",
        "repo": "a-agency-tahmin-uzman-",
        "segment": "agency",
        "domain": "Spor/finans/danışmanlık forecast",
        "web_app": False,
        "depts": [
            ("FCST", "Forecasting", ["Sports Models", "Finance Models", "Scenario Lab"]),
            ("RES", "Araştırma", ["Signal Desk", "Source QA", "Archive Loop"]),
            ("DEL", "Teslimat", ["Client Briefs", "Risk Flags", "Retros"]),
        ],
        "c_roles": ["CEO", "CSO", "CDO"],
        "top5_seed": [
            ("Nate Silver", "https://www.natesilver.net", "probabilistik forecast"),
            ("Philip Tetlock", "https://www.goodjudgment.com", "superforecasting"),
            ("Annie Duke", "https://www.annieduke.com", "karar bilimi"),
            ("Nassim Taleb", "https://www.fooledbyrandomness.com", "risk/anti-fragile"),
            ("Gary Klein", "https://www.gary-klein.com", "naturalistic decision"),
        ],
    },
    {
        "id": "movea",
        "unit": "Movéa (M-AIOS)",
        "repo": "or-na.com",
        "segment": "brand",
        "domain": "Premium medikal scrubs DTC",
        "web_app": True,
        "depts": [
            ("BRD", "Marka", ["Positioning", "Creative System", "Community"]),
            ("ECOM", "E-ticaret", ["PDP", "Checkout", "CRM"]),
            ("OPS", "Operasyon", ["Inventory", "Fulfillment", "CX"]),
        ],
        "c_roles": ["CEO", "CMO", "COO"],
        "top5_seed": [
            ("Seth Godin", "https://seths.blog", "marka/permission"),
            ("April Dunford", "https://www.aprildunford.com", "positioning"),
            ("Emily Kramer", "https://www.mkt1.co", "B2B/DTC marketing"),
            ("Rachel Karten", "https://www.linkedin.com/in/rachelkarten", "sosyal marka"),
            ("DTC Newsletter (seed)", "https://www.dtcnewsletter.co", "DTC operasyon"),
        ],
    },
    {
        "id": "cigkoftem",
        "unit": "Çiğköftem",
        "repo": "cigkoftem-web-app",
        "segment": "brand",
        "domain": "Gıda markası web app",
        "web_app": True,
        "depts": [
            ("MENU", "Menü & İçerik", ["Recipe CMS", "Local SEO", "Campaign"]),
            ("ORD", "Sipariş", ["Web Order", "Franchise Ops", "CX"]),
            ("MKT", "Yerel Pazarlama", ["Maps/SEO", "Social Local", "Promo"]),
        ],
        "c_roles": ["CEO", "CMO", "COO"],
        "top5_seed": [
            ("Danny Meyer", "https://www.dhmnyc.com", "hospitality"),
            ("Will Guidara", "https://www.willguidara.com", "CX excellence"),
            ("Chipotle (case)", "https://www.chipotle.com", "QSR dijital"),
            ("Yemeksepeti/ecosystem", "https://www.yemeksepeti.com", "TR foodtech"),
            ("Getir (case)", "https://getir.com", "hızlı teslimat"),
        ],
    },
]

ULKELER: list[dict[str, Any]] = [
    {"code": "TR", "name": "Türkiye", "role": "hedef+pazar", "lang": "tr", "law": ["KVKK", "Ticaret Kanunu", "Reklam Kurulu"], "priority": 1},
    {"code": "US", "name": "United States", "role": "pazar", "lang": "en", "law": ["CCPA/CPRA", "FTC Ads", "HIPAA (health touch)"], "priority": 2},
    {"code": "DE", "name": "Germany", "role": "pazar", "lang": "de", "law": ["GDPR", "UWG", "TMG"], "priority": 3},
    {"code": "UK", "name": "United Kingdom", "role": "pazar", "lang": "en", "law": ["UK GDPR", "ASA CAP", "PECR"], "priority": 4},
    {"code": "NL", "name": "Netherlands", "role": "pazar", "lang": "nl", "law": ["GDPR", "ACM"], "priority": 5},
    {"code": "AE", "name": "United Arab Emirates", "role": "pazar", "lang": "ar/en", "law": ["PDPL", "ADGM/DIFC"], "priority": 6},
    {"code": "SA", "name": "Saudi Arabia", "role": "pazar", "lang": "ar/en", "law": ["PDPL", "CITC"], "priority": 7},
    {"code": "CA", "name": "Canada", "role": "pazar", "lang": "en/fr", "law": ["PIPEDA", "CASL"], "priority": 8},
    {"code": "AU", "name": "Australia", "role": "pazar", "lang": "en", "law": ["Privacy Act", "ACL"], "priority": 9},
    {"code": "FR", "name": "France", "role": "pazar", "lang": "fr", "law": ["GDPR", "CNIL", "ARPP"], "priority": 10},
]

# KPI templates per dept code family
KPI_MAP = {
    "SOC": ["Thumbstop/hook rate on target", "CAPI EMQ ≥ 8", "Creative refresh cadence met", "Blended CPA vs plan"],
    "SEA": ["Impression share on brand ≥ 90%", "Wasted spend < 5%", "tCPA/tROAS attainment", "QS trend up"],
    "PRG": ["Viewability ≥ 70%", "Supply-path cost ≤ 15%", "PMP share of spend on target", "eCPM/CPA vs plan"],
    "UA": ["CPI vs plan", "D7 ROAS", "Creative win rate", "Fraud rate < 3%"],
    "MOBAPP": ["Crash-free ≥ 99.5%", "Store rating ≥ 4.6", "Release cadence met", "A11y P0 = 0"],
    "CASE": ["Case SLA met", "Doc completeness ≥ 95%", "Escalation < 5%", "NPS ≥ 40"],
    "PRIV": ["0 violations", "DPIA coverage 100%", "DSAR SLA ≤ 30d", "Policy answers ≤ 24h"],
    "INF": ["CI green ≥ 99%", "Integrity file current", "0 secret leaks", "Issue triage ≤ 24h"],
    "DEFAULT": ["OKR attainment ≥ 80%", "Weekly report shipped", "Escalation hygiene 100%", "Learning distilled 1/day"],
}

LEARNING_URLS = {
    "SOC": ["https://www.facebook.com/business/news", "https://www.facebook.com/business/learn", "https://ads.tiktok.com/business/en-US/blog"],
    "SEA": ["https://ads.google.com/intl/en_us/home/", "https://support.google.com/google-ads/", "https://about.ads.microsoft.com/en"],
    "DEFAULT": ["https://docs.anthropic.com", "https://thinkwithgoogle.com", "https://cursor.com/docs"],
}


def slugify(s: str) -> str:
    s = s.lower().strip()
    out = []
    for ch in s:
        if ch.isalnum():
            out.append(ch)
        elif ch in " &/_-":
            out.append("-")
    slug = "".join(out)
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug.strip("-")


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()[:16]


def build_org() -> dict[str, Any]:
    holding = json.loads((ROOT / "data" / "holding.json").read_text(encoding="utf-8"))
    units_out = []
    role_count = 0
    for u in ISTIRAKLAR:
        roles = []
        # C-level
        for cr in u["c_roles"]:
            roles.append(
                {
                    "name": f"{u['id']}-{cr.lower()}",
                    "title": f"{cr}, {u['unit']}",
                    "tier": "C-LEVEL",
                    "department": "C-OFİS",
                    "reports_to": "group-ceo" if cr != "CEO" else "owner",
                    "shift": "follow-the-sun",
                    "tools": ["Read", "Bash", "WebSearch"],
                    "prompt_adet": PROMPTS_PER_ROLE,
                }
            )
            role_count += 1
        # Dept EVP → Worker skeleton
        for code, dname, units in u["depts"]:
            evp_name = f"{u['id']}-evp-{slugify(dname)}"
            roles.append(
                {
                    "name": evp_name,
                    "title": f"EVP, {dname}",
                    "tier": "EVP",
                    "department": dname,
                    "dept_code": code,
                    "reports_to": f"{u['id']}-coo" if "COO" in u["c_roles"] else f"{u['id']}-ceo",
                    "shift": "follow-the-sun",
                    "units": units,
                    "kpis": KPI_MAP.get(code, KPI_MAP["DEFAULT"]),
                    "tools": ["Read", "Bash", "WebSearch"],
                    "prompt_adet": PROMPTS_PER_ROLE,
                }
            )
            role_count += 1
            for uname in units:
                dir_name = f"{u['id']}-dir-{slugify(uname)}"
                roles.append(
                    {
                        "name": dir_name,
                        "title": f"Director, {uname}",
                        "tier": "DIRECTOR",
                        "department": dname,
                        "dept_code": code,
                        "unit": uname,
                        "reports_to": evp_name,
                        "shift": "follow-the-sun",
                        "tools": ["Read", "Bash", "WebSearch"],
                        "prompt_adet": PROMPTS_PER_ROLE,
                    }
                )
                role_count += 1
                for tier, suffix in [("LEAD", "lead"), ("SPECIALIST", "spec"), ("ANALYST", "anl")]:
                    roles.append(
                        {
                            "name": f"{u['id']}-{suffix}-{slugify(uname)}",
                            "title": f"{tier.title()}, {uname}",
                            "tier": tier,
                            "department": dname,
                            "dept_code": code,
                            "unit": uname,
                            "reports_to": dir_name if tier == "LEAD" else f"{u['id']}-lead-{slugify(uname)}",
                            "shift": "follow-the-sun",
                            "tools": ["Read", "Bash", "WebSearch"],
                            "prompt_adet": PROMPTS_PER_ROLE,
                        }
                    )
                    role_count += 1
        units_out.append(
            {
                **{k: u[k] for k in ("id", "unit", "repo", "segment", "domain", "web_app", "c_roles")},
                "depts": [{"code": c, "name": n, "units": us} for c, n, us in u["depts"]],
                "top5": [{"name": n, "url": url, "neden": neden} for n, url, neden in u["top5_seed"]],
                "roles": roles,
                "role_adet": len(roles),
                "prompt_hedef": len(roles) * PROMPTS_PER_ROLE,
                "workflows": {
                    "bireysel": ["eğitim", "iş-listesi", "todo", "roadmap", "toplantı", "alt-üst-iletişim", "yan-iletişim"],
                    "grupsal": ["dept-sync", "standup", "board", "escalation", "retro", "okrs"],
                    "7x24": "follow-the-sun · 3 vardiya · nightly research archive",
                },
            }
        )
    return {
        "ts": NOW,
        "holding": holding.get("holding"),
        "hq": holding.get("hq"),
        "owner": holding.get("owner"),
        "board": holding.get("board"),
        "istirak_adet": len(units_out),
        "role_adet": role_count,
        "prompt_hedef": role_count * PROMPTS_PER_ROLE,
        "red_flag": "900M/900B karakter/prompt RED — 122×4–12KiB sözleşme",
        "units": units_out,
        "shared_services": holding.get("shared_services"),
        "cadence": holding.get("cadence"),
    }


def build_ulke() -> dict[str, Any]:
    markets = []
    for c in ULKELER:
        markets.append(
            {
                **c,
                "nightly_workflow": {
                    "cron": "0 2 * * *",
                    "steps": [
                        "önceki arşivi oku (zaman damgalı)",
                        "ülke hukuku/dil/rekabet yeniden tara",
                        "top5 kişi/kurum makale+proje güncelle",
                        "BILGI_TABANI tek satır",
                        "AUDIT_LOG damga",
                    ],
                },
                "agency_overlay": {
                    "titles": ["Country Lead", "Legal Local", "Growth Local", "Ops Local", "Support Local"],
                    "prompt_adet_each": PROMPTS_PER_ROLE,
                },
                "archive_path": f"uretim/ulke-arsiv/{c['code']}/",
            }
        )
    return {"ts": NOW, "ulke_adet": len(markets), "markets": markets}


def build_question_bank(org: dict[str, Any]) -> dict[str, Any]:
    universal_topics = {
        "Strateji": [
            "Bu iş ajansın/holding'in çeyreklik OKR'ının hangisine hizmet ediyor; edmiyorsa neden kuyrukta?",
            "Bugünkü en yüksek etkili 3 aksiyonu doğru sıraladım mı; kanıt ne?",
            "Bu kararı 3 ay sonra savunabilir miyim; hangi varsayıma dayanıyor?",
            "Rakip/pazar hareketine 7 gün içinde POV ürettim mi?",
            "Kaynağı en yüksek marjinal getiriye mi tahsis ettim, alışkanlığa mı?",
            "Bu hedef matematiksel olarak mümkün mü; değilse 🚩 verdim mi?",
        ],
        "Yürütme": [
            "Çıktı kopyala-yapıştır hazır mı; alıcı ek iş yapmadan kullanabilir mi?",
            "Bir sonraki adımın sahibi ve tarihi net mi?",
            "Bloklayıcı 4 saati aştı mı; aştıysa eskale ettim mi?",
            "Bu görevi tekrarlanabilir bir checklist'e dönüştürebilir miyim?",
            "Dünkü taahhüdümü bugün kapattım mı; kapatmadıysam neden?",
            "İşi en küçük çalışan parçaya böldüm mü?",
        ],
        "Kalite-Doğrulama": [
            "6 katmanın (structural/integrity/semantic/reference/known-patterns/review) hepsinden geçti mi?",
            "SHA256 bütünlük satırı VERSIONS.md'de güncel mi?",
            "Bağımsız bir gözle (ikinci ajan) review aldım mı?",
            "Rework oranım artıyor mu; kök neden ne?",
            "Bu çıktıda tehlikeli desen (enjeksiyon/SSRF) taraması yaptım mı?",
        ],
        "Veri-Dürüstlüğü": [
            "Sunduğum her sayı gerçek bir kaynaktan mı; tahminleri açıkça etiketledim mi?",
            "Örneklem büyüklüğü sonucu taşıyacak kadar mı?",
            "Anomaliyi büyüklük + hipotezle mi raporladım?",
            "KPI'nın tanımı yazılı mı; tanımsız metrik yayınlamadım değil mi?",
            "Korelasyonu nedensellik gibi sunmadım değil mi?",
        ],
        "Güvenlik-5Kural": [
            "Resmi kaynak varken topluluk kaynağına mı gittim?",
            "Script bundle eden bileşeni okumadan çalıştırdım mı?",
            "'Son commit dün' diye güvenlik varsaydım mı?",
            "Kurulumu kanonik org'dan mı yaptım, fork'tan mı?",
            "Marketplace-öncelik katmanını kontrol ettim mi?",
        ],
        "Gelir": [
            "Bu iş 5 gelir kanalından hangisini ilerletiyor?",
            "Inbound lead yolu çalışır durumda mı?",
            "Referral fırsatını kaçırdım mı?",
            "Pipeline değerini bu hafta güncelledim mi?",
            "Bir sponsor/vendor görüşmesini ilerletmek için bugün ne yaptım?",
        ],
        "Öğrenme": [
            "Bugün en az 1 kaynak okudum mu; öğrenimi damıttım mı?",
            "Bu öğrenim BILGI_TABANI.md'ye tek satır olarak girdi mi?",
            "Departmanımın platformunda bu hafta ne değişti?",
            "İlgili sertifika/eğitimden bir modül tamamladım mı?",
            "Bir beta/yeni ürün özelliğini test edip not aldım mı?",
            "Önceki koşumun çıktısını okudum mu (🔗 kırılmadı mı)?",
        ],
        "Toplantı": [
            "Standup satırım dün/bugün/blocker formatında ve tek satır mı?",
            "Tutanakta karar + aksiyon(sahip+tarih) + risk + 🚩 var mı?",
            "Kurul kararına K-no verdim mi?",
            "Toplantı çıktısız mı bitti?",
        ],
        "Eskalasyon": [
            "Bütçe/politika riskini fin/leg'e ilettim mi?",
            "İmkânsız hedefi 🚩 [ne]·[neden]·[alternatif] formatında mı verdim?",
            "Sessiz kalıp riski gömdüm mü?",
            "Cross-departman çakışmayı doğru mercie taşıdım mı?",
        ],
        "Ölçümleme": [
            "Bu aksiyonun başarısını hangi metrikle ve ne zaman ölçeceğim?",
            "Atıf modeli/ölçüm yöntemi playbook'ta belgeli mi?",
            "Holdout/artımsallık düşündüm mü?",
            "Dashboard SLA'sını tutturdum mu?",
        ],
        "Dokümantasyon": [
            "Bu işi başka bir ajan benim yardımım olmadan tekrarlayabilir mi?",
            "Artefaktı zaman damgaladım mı?",
            "Playbook'u güncel tuttum mu?",
        ],
        "Önceliklendirme": [
            "P0 işleri gerçekten P0 mı?",
            "Biten işi arşive taşıdım mı?",
            "IS_LISTESI'ni bugün yeniden önceliklendirdim mi?",
        ],
        "Risk": [
            "Bu değişikliğin rollback planı var mı?",
            "En kötü senaryo ne; sinyalini nasıl erken yakalarım?",
            "Tek nokta bağımlılık yarattım mı?",
        ],
        "İşbirliği": [
            "Yukarı/yatay/aşağı arayüzlerimi bugün bilgilendirdim mi?",
            "Başka bir departmanın işini kolaylaştırmak için ne yaptım?",
            "Devrettiğim işin sahibi net mi?",
        ],
        "Etik-Uyum": [
            "Reklam politikası açısından bu çıktı temiz mi?",
            "KVKK/GDPR açısından veri işleme uygun mu?",
            "Lisans (MIT) hijyenine uydum mu?",
            "Gerçek kişilere atfen sahte içerik üretmedim değil mi?",
        ],
        "Otomasyon": [
            "Bu manuel işi bir workflow'a çevirebilir miyim?",
            "Actions yeşil mi; kırmızıysa 24h içinde müdahale ettim mi?",
            "Idempotent mi çalışıyor?",
        ],
        "Müşteri": [
            "Bu çıktı bir müşteri ihtiyacını gerçekten çözüyor mu?",
            "Rapor anlatısı sayı+bağlam+sonraki adım içeriyor mu?",
            "Churn/risk sinyalini 14 gün önceden işaretledim mi?",
        ],
        "İnovasyon-Beta": [
            "Bu hafta hangi beta ürünü/özelliği denedim?",
            "Rakiplerin denemediği bir açı buldum mu?",
            "Deneyi hipotez→tasarım→koşum→öğrenim döngüsüyle mi yürüttüm?",
        ],
        "Makale-İçerik": [
            "Bugünün makalesi kaynaklı, TR özetli ve CTA'lı mı?",
            "İçerik inbound hunisine hizmet ediyor mu?",
            "Editoryal rotasyondan sıradaki konuyu seçtim mi?",
        ],
        "Öz-Gelişim": [
            "Bu rolün ilk-30-gün hedeflerinin neresindeyim?",
            "Anti-desenlerimden birine bugün düştüm mü?",
            "Bir sonraki kademeye hazırlık için hangi beceriyi geliştiriyorum?",
        ],
        "Eğitim-Sertifika": [
            "Rolümle ilgili bir sertifika modülünü bu hafta ilerlettim mi?",
            "Yeni öğrendiğim bir tekniği bir çıktıya uyguladım mı?",
            "Ekipteki başka bir ajana aktardığım bir şey oldu mu?",
            "Skill gap'i isimlendirdim mi; kapatma planı ne?",
        ],
        "Panel-Güncelleme": [
            "Departmanımın platform changelog'unu bu hafta okudum mu?",
            "API/politika değişikliği mevcut kurulumu etkiliyor mu?",
            "Deprecation/sunset uyarısı var mı; takvime aldım mı?",
            "Yeni panel özelliği iş akışımı hızlandırır mı?",
        ],
        "Kaynak-Okuma": [
            "Bugün okuduğum kaynağın URL'ini nota ekledim mi?",
            "Okuduğumdan çıkan tek somut aksiyon ne?",
            "Kaynağın güvenilirliğini değerlendirdim mi?",
            "Çelişen iki kaynağı nasıl uzlaştırdım?",
        ],
        "Süreç-Zinciri": [
            "Bu koşum önceki koşumun çıktısını girdi aldı mı (🔗)?",
            "ts_start ve ts_end damgaladım mı?",
            "Zincir kırılırsa DENETÇİ bulgusu düşer mi?",
            "Bir sonraki koşuma net bir girdi bıraktım mı?",
        ],
        "Pazar-Rekabet": [
            "Rakip bir hamle yaptı mı; 7 gün içinde POV çıkardım mı?",
            "Sektör benchmark'ımı bu ay tazeledim mi?",
            "Rakiplerin sahiplenmediği bir konumlanma açığı var mı?",
            "Bir pazar sinyalini erken yakalayıp aksiyona çevirdim mi?",
        ],
        "Verimlilik-Token": [
            "Çıktıyı minimum token ile (progressive disclosure) mı ürettim?",
            "Aynı analizi tekrarladım mı; BILGI_TABANI'nda zaten var mıydı?",
            "Ağır içeriği docs/'a koyup kartı kısa mı tuttum?",
            "Çoklu benzer işlemi tek çağrıda grupladım mı?",
            "Dolgu cümle ürettim mi; sinyal/uzunluk oranım iyi mi?",
        ],
        "Toparlama-Retro": [
            "Bu iş bölümünün retrosundan tek satır öğrenim çıktı mı?",
            "Tekrar eden bir hatayı kalıcı düzelttim mi?",
            "Bir sonraki sprint için taşınacak riski işaretledim mi?",
        ],
        "Sahiplik-Hesapverebilirlik": [
            "Bu işin tek net sahibi ben miyim?",
            "Bir hatayı savunmaya geçmeden sahiplendim mi?",
            "Taahhüt ettiğim tarihi tutuyor muyum?",
            "Başkasının işini beklerken kendi tarafımı hazır tuttum mu?",
            "Sessiz kalarak bir riski gömdüm mü?",
            "Kararımın kanıtını (link/commit/dosya) bıraktım mı?",
            "Bu çıktı için definition of done karşılandı mı?",
            "Bugün holding'i bir adım ileri götüren en somut şey neydi?",
            "Yarına devrettiğim en kritik açık madde ne; sahibi kim?",
            "Bu işi baştan yapsam neyi farklı yapardım?",
            "Ölçebildiğim bir ilerleme kaydettim mi, yoksa sadece meşgul mü göründüm?",
        ],
    }

    # Expand universal to ~120 by numbering variants where short
    universal: list[dict[str, str]] = []
    for topic, qs in universal_topics.items():
        for q in qs:
            universal.append({"topic": topic, "q": q})
    # Pad to 120 with process variants
    pad_i = 0
    while len(universal) < QUESTIONS_UNIVERSAL_TARGET:
        pad_i += 1
        universal.append(
            {
                "topic": "Süreç-Zinciri",
                "q": f"Bugünkü görev #{pad_i} için tanım/sahip/metrik/DoD dörtlüsü eksiksiz mi?",
            }
        )

    dept_qs: dict[str, list[str]] = {}
    for u in org["units"]:
        for d in u["depts"]:
            code = d["code"]
            block = []
            for uname in d["units"]:
                block.append(f"{uname} birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?")
                block.append(f"{uname} çıktısında tekrarlanabilir bir iyileştirme/checklist üretebildim mi?")
                block.append(f"{uname} alanında bir beta/yeni özellik veya platform güncellemesi çıktı mı; test edip not aldım mı?")
            kpis = KPI_MAP.get(code, KPI_MAP["DEFAULT"])
            for kpi in kpis:
                block.append(f"KPI '{kpi}' hedefte mi; sapma varsa kök neden ve düzeltme ne?")
                block.append(f"'{kpi}' ölçümünün tanımı ve kaynağı yazılı mı; tahmin içeriyorsa etiketli mi?")
            dept_qs[f"{u['id']}.{code}"] = block[:QUESTIONS_PER_DEPT_BLOCK]

    tier_qs = {
        "C-LEVEL": [
            "Holding/birim OKR attainment %80 üstünde mi; değilse kurtarma planı ne?",
            "Bir faz kapısını kanıtsız GEÇTİ saymadım değil mi?",
            "Mikro-yönetime kaydım mı; yetkiyi doğru devrettim mi?",
            "Sahibe danışmadan bir taahhüt verdim mi?",
            "Gelir kanallarının sahibi ve durumu net mi?",
            "Kurul gündemini kanıt-linkli hazırladım mı?",
            "Ülke pazar overlay'inde hukuki onay eksik mi?",
            "Cross-istirak sinerji fırsatını işaretledim mi?",
            "API/secret bütçesi Group CFO ile hizalı mı?",
            "Web/iOS/Android yüzeyinde P0 güvenlik açığı var mı?",
            "7/24 vardiya devri kırıldı mı?",
            "Nightly araştırma arşivi taze mi?",
        ],
        "EVP": [
            "Departman OKR skoru güncel mi; kırmızı OKR için plan var mı?",
            "Kadroyu aşırı yükledim mi; kapasite dengeli mi?",
            "Playbook'u merge öncesi onayladım mı?",
            "Haftalık departman raporu yayınlandı mı?",
            "Sponsor C-level'a haftalık raporladım mı?",
            "Birim top-5 etki sahiplerini bu ay taradım mı?",
            "Soru bankası alt-seti rol kartında güncel mi?",
            "Eskalasyon >4h kaldı mı?",
            "Dry-run skill/MCP matrisi dolduruldu mu?",
            "Ülke Lead ile bağımlılık net mi?",
            "Prompt sözleşmesi 122/title indeksli mi?",
            "Anti-desen (OKR'sız iş) var mı?",
        ],
        "DIRECTOR": [
            "Birim backlog'u doğru önceliklendi mi?",
            "Uzman çıktısını publish öncesi review ettim mi?",
            "Birim retrosundan öğrenim damıttım mı?",
            "Cross-unit çakışmayı EVP'ye taşıdım mı?",
            "KPI tanımı yazılı mı?",
            "Checklist güncel mi?",
            "Top-5 kaynak URL arşivlendi mi?",
            "Toplantı tutanağı DoD'lu mu?",
            "Risk bayrağı metrikli mi?",
            "Yan iletişim (peer) bugün yapıldı mı?",
            "Eğitim modülü ilerledi mi?",
            "Roadmap tarihleri kaydı mı?",
        ],
        "LEAD": [
            "İş akışı standardı/checklist güncel mi?",
            "Uzman görevlerini günlük atadım/review ettim mi?",
            "Haftalık iş akışı özetini yazdım mı?",
            "Riski metrik kanıtıyla mı bayrakladım?",
            "Standup satırı tek satır mı?",
            "Bloklayıcı eskale edildi mi?",
            "Playbook iyileştirme önerisi var mı?",
            "Test/dry-run notu alındı mı?",
            "DoD karşılandı mı?",
            "Öğrenim damıtıldı mı?",
            "Token verimliliği iyi mi?",
            "Rollback planı var mı?",
        ],
        "SPECIALIST": [
            "Çıktım kopyala-hazır ve checklist'li mi?",
            "Bu hafta playbook'a 1 iyileştirme önerdim mi?",
            "İşi metrik gerekçesi olmadan mı sundum?",
            "Damgasız çıktı bıraktım mı?",
            "Kaynak URL ekledim mi?",
            "6 katman geçti mi?",
            "Güvenlik 5 kuralı kontrol mü?",
            "Peer review aldım mı?",
            "Beta notu var mı?",
            "Ülke dil/hukuk uyarısı var mı?",
            "Secret sızdırdım mı?",
            "Sonraki adım sahibi net mi?",
        ],
        "ANALYST": [
            "Veri kesitim tanım-ekli mi?",
            "Anomaliyi büyüklük+hipotezle mi işaretledim?",
            "Tahmini açıkça etiketledim mi?",
            "Veri uydurmadım değil mi?",
            "Örneklem yeterli mi?",
            "Dashboard SLA?",
            "Kaynak güven sırası uygulandı mı?",
            "Arşiv zaman damgası var mı?",
            "Korelasyon≠nedensellik uyarıldı mı?",
            "KPI owner yazılı mı?",
            "Holdout düşündüm mü?",
            "BILGI_TABANI satırı yazıldı mı?",
        ],
        "WORKER": [
            "Atanan task DoD'a göre kapandı mı?",
            "Bloklayıcıyı 4h kuralıyla işaretledim mi?",
            "Çıktı tek dosyada mı?",
            "Zaman damgası koydum mu?",
            "Checklist adımlarını atladım mı?",
            "Gizli bilgi paylaştım mı?",
            "Üst'e net durum verdim mi?",
            "Öğrenim 1 satır mı?",
            "Yeniden koşum güvenli mi?",
            "Test/dry-run yaptım mı?",
            "İsimlendirme standardına uydum mu?",
            "Gereksiz dolgu ürettim mi?",
        ],
    }

    # Per-role subset metadata (not exploding full text for every role in MD)
    role_subsets = []
    for u in org["units"]:
        for r in u["roles"]:
            code = r.get("dept_code", "DEFAULT")
            key = f"{u['id']}.{code}"
            role_subsets.append(
                {
                    "role": r["name"],
                    "tier": r["tier"],
                    "dept_block": key if key in dept_qs else None,
                    "self_inquiry_adet": ROLE_CARD_SELF_INQUIRY,
                    "extended_target": 500,
                    "note": "Günlük döngü bankadan örnekler; kartta 17; tam banka docs/OZ-DENETIM-SORU-BANKASI.md",
                }
            )

    total = len(universal) + sum(len(v) for v in dept_qs.values()) + sum(len(v) for v in tier_qs.values())
    return {
        "ts": NOW,
        "uretim": "scripts/holding_istirak_ajans_uret.py",
        "toplam_soru": total,
        "hedef_min": 501,
        "universal": universal,
        "departman": dept_qs,
        "kademe": tier_qs,
        "role_subsets_adet": len(role_subsets),
        "role_subsets_sample": role_subsets[:20],
        "kullanim": "Her ajan her süreçte sorar; daily_ops örnek çeker; kart başına alt-set = departman + kademe.",
    }


def render_role_card(u: dict[str, Any], role: dict[str, Any], bank: dict[str, Any]) -> str:
    code = role.get("dept_code", "DEFAULT")
    kpis = role.get("kpis") or KPI_MAP.get(code, KPI_MAP["DEFAULT"])
    urls = LEARNING_URLS.get(code, LEARNING_URLS["DEFAULT"])
    reports = role.get("reports_to", "group-ceo")
    units = role.get("units") or ([role["unit"]] if role.get("unit") else [])
    dept = role.get("department", "—")
    top5 = u.get("top5", [])[:TOP5_PER_TITLE]
    # self inquiry: 5 tier + up to 12 unit/kpi
    self_q: list[str] = []
    for q in bank["kademe"].get(role["tier"], [])[:5]:
        self_q.append(q)
    for un in units[:4]:
        self_q.append(f"{un} birimi için bu hafta en yüksek etkili kaldıraç neydi; metrik gerekçesi ne?")
        self_q.append(f"{un} alanında beta/platform güncellemesi test edilip not alındı mı?")
    for kpi in kpis[:3]:
        self_q.append(f"KPI '{kpi}' hedefte mi; sapma kök nedeni ne?")
    self_q = self_q[:ROLE_CARD_SELF_INQUIRY]

    lines = [
        f"# {role['title']}",
        "",
        f"name: {role['name']}",
        f'description: "Executive/ops lead for {dept} @ {u["unit"]}; owns OKRs, staffing, quality. Use for escalation or strategy."',
        f"tools: {', '.join(role.get('tools', ['Read', 'Bash', 'WebSearch']))}",
        "model: sonnet",
        f"tier: {role['tier']}",
        f'department: "{dept}"',
        f"reports_to: {reports}",
        f'shift: "{role.get("shift", "follow-the-sun")}"',
        f"istirak: {u['id']} · repo: {u['repo']} · web_app: {u['web_app']}",
        f"prompt_adet: {PROMPTS_PER_ROLE} · 🚩 900M/900B RED",
        "",
        f"## {role['title']}",
        f"Owns end-to-end for scope: OKRs, quality bar, capacity, escalations. TR: {u['unit']} / {dept}.",
        "",
        "## Kimlik / Identity",
        f"Tier: {role['tier']} · Department: {dept} · Reports to: {reports}",
        "Nöbet (7/24): follow-the-sun — kesintisiz (3 vardiya)",
        "Yetki: OKR, kadro, kalite bar, dış taahhütler (RACI).",
        "",
        "## Misyon / Mission",
        f"{role['title']} — sinyal > uzunluk; kopyala-yapıştır hazır çıktı.",
        "",
        "## Sorumluluklar / Responsibilities",
        f"- Set and track OKRs for {dept}",
        "- Chair weekly sync; publish minutes",
        "- Approve playbooks/components before merge",
        "- Manage bench and coverage",
        f"- Report weekly to {reports}",
        "- Her çıktıyı 6-katman doğrulamadan geçir",
        "- Öğrenimi BILGI_TABANI.md'ye damıt; AUDIT_LOG.jsonl damgala",
        "",
        "## Karar Yetkileri / Decision Rights (RACI)",
        "- R/A: backlog önceliği, playbook onayı, görev dağılımı",
        "- C: yeni birim/rol, çeyreklik OKR → C-level",
        "- I: bütçe/politika → fin/leg; kapsam çakışması → CEO",
        "",
        "## KPI & OKR",
    ]
    for k in kpis:
        lines.append(f"- {k} · ölçüm: haftalık · sahip: {role['name']}")
    lines += [
        "",
        "OKR ritmi: çeyreklik hedef → haftalık kesit → aylık kurul.",
        "",
        "## Haftalık Ritim / Weekly Rhythm",
        "- Her gün 07:30 TRT async standup (dün/bugün/blocker)",
        "- Hafta içi: kuyruk + metrikli risk bayrağı",
        "- Hafta sonu: rapor + BILGI_TABANI damıtımı",
        "",
        "## Toplantılar / Meetings",
        "- Daily standup",
        "- Weekly dept sync",
        "- Weekly leadership sync (Mon)",
        "- Monthly board",
        "",
        "## Girdi / Çıktı / I-O",
        f"- Girdi: data/holding_istirak_org.json · IS_LISTESI · gundem/ · {u['repo']}",
        "- Çıktı: standup satırı · haftalık rapor · playbook güncellemesi",
        "- DoD: haftalık rapor yayınlandı; OKR güncel; açık eskalasyon yok",
        "",
        "## Arayüzler / Interfaces",
        f"- Yukarı: {reports} · Yatay: peer EVP/Director · Aşağı: alt kademe",
        "",
        "## Araçlar & Veri",
        f"- Tools: {', '.join(role.get('tools', []))}",
        "- AUDIT_LOG.jsonl · BILGI_TABANI.md · docs/HOLDING-ISTIRAK-ORG.md · docs/SECRETS-DRYRUN-MATRISI.md",
        "",
        "## Eskalasyon",
        f"- Bloklayıcı > 4h → {reports}",
        "- Bütçe/politika → fin / hukuk iştiraki",
        "- Güvenlik → Group CCO",
        "- İmkânsız → 🚩 [ne] · [neden] · [alternatif]",
        "",
        "## İlk 30 Gün",
        "- H1: kadro + backlog envanteri; kalite bar",
        "- H2: 3 birim önceliği kilitle",
        "- H3-4: ilk haftalık rapor + OKR baseline",
        "",
        "## Anti-desenler",
        "Kadroyu aşırı yükleme; OKR'sız iş; sessiz eskalasyon; 900B dolgu prompt.",
        "",
        "## Öz-öğrenim Döngüsü",
        "Günlük 1 changelog · haftalık 1 öğrenim · aylık 1 sertifika modülü.",
        "oku → BILGI_TABANI → uygula → paylaş. Zincir 🔗 zorunlu.",
        "",
        "## Öğrenme Kaynakları",
    ]
    for url in urls:
        lines.append(f"- {url}")
    lines += ["", "## Title Top-5 (seed — aylık yenile)"]
    for t in top5:
        lines.append(f"- {t['name']} — {t['neden']} — {t['url']}")
    lines += [
        "",
        "## Öz-Denetim (17; tam banka 501+)",
        "Kaynak: docs/OZ-DENETIM-SORU-BANKASI.md · data/soru_bankasi.json",
        "",
    ]
    for i, q in enumerate(self_q, 1):
        lines.append(f"{i}. {q}")
    lines += [
        "",
        "## Bağlantılar",
        "- Anayasa: CLAUDE.md · Holding: data/holding.json · Org: data/holding_istirak_org.json",
        "- Soru bankası: docs/OZ-DENETIM-SORU-BANKASI.md",
        f"- Üretim ts: {NOW}",
        "",
    ]
    return "\n".join(lines)


def write_question_bank_md(bank: dict[str, Any]) -> None:
    L = [
        f"# ÖZ-DENETİM SORU BANKASI ({bank['toplam_soru']} soru)",
        f"> Üretim: {bank['ts']} · Kaynak: scripts/holding_istirak_ajans_uret.py · data/soru_bankasi.json",
        "",
        "Her ajan her süreçte kendine bu soruları sorar. Günlük döngü örnek çeker.",
        "Kart başına alt-set: departman + kademe. Hedef ≥501.",
        "",
        "## A. Evrensel sorular",
        "",
    ]
    cur = None
    for item in bank["universal"]:
        if item["topic"] != cur:
            cur = item["topic"]
            L.append(f"### {cur}")
        L.append(f"- {item['q']}")
    L += ["", "## B. Departman soruları (iştirak.code)", ""]
    for key, qs in sorted(bank["departman"].items()):
        L.append(f"### {key}")
        for q in qs:
            L.append(f"- {q}")
        L.append("")
    L += ["## C. Kademe soruları", ""]
    for tier, qs in bank["kademe"].items():
        L.append(f"### {tier}")
        for q in qs:
            L.append(f"- {q}")
        L.append("")
    L += [
        "## Kullanım",
        "- Rol kartı: 17 soru alt-set",
        "- Genişletilmiş hedef: +500 soru/title (bankadan örnekleme + dept/tier birleşimi)",
        "- 🚩 Tek dosyada 900M karakter üretme — banka indeks + üretici yeter",
        "",
    ]
    write_text(ROOT / "docs" / "OZ-DENETIM-SORU-BANKASI.md", "\n".join(L))


def write_holding_md(org: dict[str, Any]) -> None:
    L = [
        f"# HOLDING × İŞTİRAK ORG",
        f"> Üretim: {org['ts']} · Kaynak: data/holding_istirak_org.json",
        "",
        f"**İştirak:** {org['istirak_adet']} · **Rol:** {org['role_adet']} · **Prompt hedef:** {org['prompt_hedef']} (122/rol)",
        f"**{org['red_flag']}**",
        "",
        "## Kurul",
        "| Rol | Görev |",
        "|---|---|",
    ]
    for b in org.get("board") or []:
        L.append(f"| {b['role']} | {b['duty']} |")
    L += ["", "## İştirakler", ""]
    for u in org["units"]:
        L += [
            f"### {u['unit']} (`{u['id']}`)",
            f"- Repo: `{u['repo']}` · Segment: {u['segment']} · Web/app: {u['web_app']}",
            f"- Domain: {u['domain']}",
            f"- Roller: {u['role_adet']} · Prompt hedef: {u['prompt_hedef']}",
            f"- C-roles: {', '.join(u['c_roles'])}",
            "- Departmanlar:",
        ]
        for d in u["depts"]:
            L.append(f"  - **{d['code']}** {d['name']}: {', '.join(d['units'])}")
        L.append("- Top-5 seed:")
        for t in u["top5"]:
            L.append(f"  - {t['name']} — {t['neden']} — {t['url']}")
        L.append("- Workflows: bireysel + grupsal + 7×24 follow-the-sun")
        L.append("")
    L += [
        "## Entegrasyon",
        "- Skill ajans: `data/skill_title_haritasi.json`",
        "- MCP: `data/mcp_hiyerarsi.json`",
        "- Ülke: `data/ulke_pazar_iskeleti.json`",
        "- Rol kartları (pilot): `uretim/rol-kartlari/`",
        "",
    ]
    write_text(ROOT / "docs" / "HOLDING-ISTIRAK-ORG.md", "\n".join(L))


def write_ulke_md(ulke: dict[str, Any]) -> None:
    L = [
        f"# ÜLKE / PAZAR İSKELETİ",
        f"> Üretim: {ulke['ts']} · {ulke['ulke_adet']} ülke · Nightly research döngüsü",
        "",
        "| Kod | Ülke | Rol | Dil | Hukuk | Öncelik |",
        "|---|---|---|---|---|---:|",
    ]
    for m in ulke["markets"]:
        L.append(
            f"| {m['code']} | {m['name']} | {m['role']} | {m['lang']} | {', '.join(m['law'])} | {m['priority']} |"
        )
    L += [
        "",
        "## Nightly workflow (her ülke)",
        "1. Zaman damgalı arşivi oku",
        "2. Hukuk/dil/rekabet + top5 yeniden tara",
        "3. `uretim/ulke-arsiv/{CODE}/YYYY-MM-DD.md` yaz",
        "4. BILGI_TABANI + AUDIT_LOG",
        "",
        "🚩 Cowork URL bekleme yok — repo döngüsü yeter.",
        "",
    ]
    write_text(ROOT / "docs" / "ULKE-PAZAR-ISKELETI.md", "\n".join(L))


def write_secrets_md() -> None:
    rows = [
        ("GITHUB_TOKEN", "GitHub API (holding_report)", "PAT/fine-grained", "dry-run: statik rapor", "opsiyonel"),
        ("ANTHROPIC_API_KEY", "Claude Code / API", "console.anthropic.com", "dry-run: MASTER prompt uygula", "opsiyonel"),
        ("OPENAI_API_KEY", "opsiyonel LLM", "platform.openai.com", "dry-run", "opsiyonel"),
        ("EXA_API_KEY", "Exa search MCP", "dashboard.exa.ai", "WebSearch fallback", "opsiyonel"),
        ("BRIGHT_DATA_API_TOKEN", "Bright Data MCP", "brightdata.com", "dry-run scrape checklist", "opsiyonel"),
        ("TWILIO_ACCOUNT_SID / AUTH_TOKEN", "Twilio skills", "console.twilio.com", "dry-run account-setup", "opsiyonel"),
        ("SENDGRID_API_KEY", "SendGrid", "Twilio SendGrid", "dry-run", "opsiyonel"),
        ("SENTRY_AUTH_TOKEN", "Sentry", "sentry.io", "dry-run debug-issue", "opsiyonel"),
        ("VERCEL_TOKEN", "Vercel", "vercel.com", "dry-run", "opsiyonel"),
        ("CLOUDFLARE_API_TOKEN", "Cloudflare", "dash.cloudflare.com", "dry-run", "opsiyonel"),
        ("AWS_*", "AWS MCP", "IAM user/role", "dry-run; asla commit etme", "opsiyonel"),
        ("AZURE_*", "Azure MCP", "Service principal", "dry-run", "opsiyonel"),
        ("GCP_* / BIGQUERY_*", "Warehouse skills", "GCP SA", "dry-run", "opsiyonel"),
        ("SNOWFLAKE_*", "Snowflake", "account/user", "dry-run", "opsiyonel"),
        ("DATABRICKS_*", "Databricks", "workspace token", "dry-run", "opsiyonel"),
        ("POSTHOG_*", "PostHog", "project API key", "dry-run", "opsiyonel"),
        ("CLERK_*", "Clerk", "dashboard", "dry-run", "opsiyonel"),
        ("SUPABASE_*", "Supabase", "project settings", "dry-run", "opsiyonel"),
        ("PINECONE_API_KEY", "Pinecone", "console", "dry-run", "opsiyonel"),
        ("CONVEX_*", "Convex", "CONVEX_AGENT_MODE=anonymous cloud", "agent mode", "opsiyonel"),
        ("RENDER_API_KEY", "Render", "dashboard", "dry-run", "opsiyonel"),
        ("HARNESS_API_KEY", "Harness", "account", "fail-open hooks", "opsiyonel"),
        ("PAGERDUTY_*", "PagerDuty", "API token", "dry-run", "opsiyonel"),
        ("DATADOG_*", "Datadog", "API/APP key", "dry-run", "opsiyonel"),
        ("GRAFANA_*", "Grafana Cloud", "SA token", "dry-run", "opsiyonel"),
        ("LINEAR_API_KEY", "Linear", "API", "dry-run", "opsiyonel"),
        ("SLACK_BOT_TOKEN", "Slack", "app", "dry-run messaging", "opsiyonel"),
        ("APIFY_TOKEN", "Apify", "console", "dry-run actor", "opsiyonel"),
        ("FIRECRAWL_API_KEY", "Firecrawl", "dashboard", "dry-run", "opsiyonel"),
        ("BROWSERSTACK_*", "BrowserStack", "automate", "dry-run", "opsiyonel"),
        ("CURSOR_API_KEY", "Cursor SDK", "dashboard integrations", "local/cloud agent", "opsiyonel"),
    ]
    L = [
        f"# SECRETS & DRY-RUN MATRİSİ",
        f"> Üretim: {NOW} · İlke: secret ASLA commit edilmez · free tier tercih · credential yoksa dry-run",
        "",
        "## Onay politikası (Metin)",
        "Kullanıcı free API/profil açmaya onay verdi. Bu ortamda **yüzlerce satıcı hesabı açılmadı** (kimlik/ödeme/ToS).",
        "Yapılan: şablon + dry-run matrisi + `.env.example`. Gerçek anahtarlar GitHub Secrets / Cursor env.",
        "",
        "| Secret | Kullanım | Nereden | Credential yoksa | Zorunlu |",
        "|---|---|---|---|---|",
    ]
    for name, use, where, dry, req in rows:
        L.append(f"| `{name}` | {use} | {where} | {dry} | {req} |")
    L += [
        "",
        "## Dry-run protokolü",
        "1. Skill/MCP çağrısı credential isterse → checklist yaz, canlı çağrı yapma",
        "2. Sonucu `uretim/skill-workflows/` veya AUDIT_LOG'a damgala",
        "3. Secret sızıntısı = P0 → Group CCO",
        "",
        "## Dosyalar",
        "- `.env.example` (boş değerler)",
        "- Bu matris: `docs/SECRETS-DRYRUN-MATRISI.md`",
        "",
    ]
    write_text(ROOT / "docs" / "SECRETS-DRYRUN-MATRISI.md", "\n".join(L))
    env = ["# Örnek env — değerleri doldur; commit etme", f"# Üretim: {NOW}", ""]
    for name, *_ in rows:
        key = name.split()[0].split("/")[0]
        if key.endswith("_"):
            env.append(f"# {key}ACCESS_KEY_ID=")
            env.append(f"# {key}SECRET_ACCESS_KEY=")
        else:
            env.append(f"{key}=")
    write_text(ROOT / ".env.example", "\n".join(env))


def write_master_v2(org: dict[str, Any], bank: dict[str, Any], ulke: dict[str, Any]) -> None:
    text = f"""# CLAUDE CODE MASTER PROMPT — HOLDING V2 (yapıştır)

> Üretim: {NOW} · Repo: claude-otonom-sistem · Dal: cursor/mcp-ajans-etki-arsivi-8e8f
> Cursor Cloud üretti → Claude Code'a **tek parça** yapıştır.

## 🚩 ZORUNLU RED
Her prompt ≥900.000.000 / ≥900.000.000.000 / ≥9e17 karakter **RED**.
**Uygula:** 122 prompt/title · 4–12 KiB · referans zinciri · dry-run.

## FAZ 0 — Senkron
```bash
cd "$(git rev-parse --show-toplevel)"
git fetch origin && git status -sb
python3 scripts/mcp_ajans_etki_uret.py --dogrula
python3 scripts/skill_ajans_uretim.py --dogrula
python3 scripts/holding_istirak_ajans_uret.py --dogrula
```

## FAZ 1 — Oku (zincir 🔗)
1. BILGI_TABANI.md (en yeni)
2. docs/HOLDING-ISTIRAK-ORG.md · data/holding_istirak_org.json
3. docs/OZ-DENETIM-SORU-BANKASI.md · data/soru_bankasi.json
4. docs/ULKE-PAZAR-ISKELETI.md · data/ulke_pazar_iskeleti.json
5. docs/SECRETS-DRYRUN-MATRISI.md · .env.example
6. docs/LLM-AI-AJANS-ETKI-MOTORU.md · docs/SKILL-AJANS-HIYERARSI.md
7. uretim/OZET-TEK-SAYFA.md · uretim/rol-kartlari/

## FAZ 2 — Doğrula
- iştirak ≥ 7 (şu an {org['istirak_adet']})
- rol ≥ 100 (şu an {org['role_adet']})
- soru bankası ≥ 501 (şu an {bank['toplam_soru']})
- ülke ≥ 8 (şu an {ulke['ulke_adet']})
- hiçbir 900M+ karakter dosya yok

## FAZ 3 — Uygula (kredi-min)
1. `python3 scripts/holding_istirak_ajans_uret.py --hepsi`
2. İsteğe bağlı: `--pilot-limit N` ile daha fazla rol kartı
3. Credential yoksa dry-run matrisi doldur; hesap açma zorunlu değil
4. Ülke nightly: `uretim/ulke-arsiv/TR/` örnek not + zaman damgası
5. Cowork URL bekleme — repo döngüsü yeterli

## FAZ 4 — 5 güvenlik kuralı
Resmi kaynak · script tedbiri · güncellik yanılgısı yok · fork yasağı · marketplace öncelik

## FAZ 5 — Damga
BILGI_TABANI tek satır · AUDIT_LOG · commit/push · PR #13 güncelle

## FAZ 6 — Rapor
Türkçe kısa tablo: iştirak/rol/soru/ülke + 🚩 + sonraki 3 aksiyon

## Çıktı sözleşmesi
⏱️ Damga · 🔍 Denetim · 📚 Öğrenim · 🔗 Önceki

---
Metin: Bu prompt Cursor'dan. FAZ 0→6 uygula; 900B üretme; secrets commit etme.
"""
    write_text(ROOT / "uretim" / "devir" / "CLAUDE-CODE-MASTER-PROMPT-HOLDING-V2.md", text)


def write_ozet(org: dict[str, Any], bank: dict[str, Any], ulke: dict[str, Any], cards: int) -> None:
    text = f"""# TEK SAYFA ÖZET — Holding × Skill × MCP Ajans
> {NOW}

## Yapılanlar (madde madde)
1. **Holding iştirak org** üretildi — `{org['istirak_adet']}` birim, `{org['role_adet']}` rol, prompt hedef `{org['prompt_hedef']}` (`data/holding_istirak_org.json`, `docs/HOLDING-ISTIRAK-ORG.md`).
2. **Ülke/pazar iskeleti** — `{ulke['ulke_adet']}` ülke + nightly research workflow (`data/ulke_pazar_iskeleti.json`, `docs/ULKE-PAZAR-ISKELETI.md`).
3. **Öz-denetim soru bankası** — `{bank['toplam_soru']}` soru (≥501) evrensel+departman+kademe (`data/soru_bankasi.json`, `docs/OZ-DENETIM-SORU-BANKASI.md`).
4. **AdOps-tarzı rol kartları (pilot)** — `{cards}` kart `uretim/rol-kartlari/` (kimlik, RACI, KPI, 17 soru, top-5, 7×24).
5. **Secrets/dry-run matrisi** — `docs/SECRETS-DRYRUN-MATRISI.md` + `.env.example` (gerçek key yok; free hesap toplu açılmadı).
6. **Claude Code MASTER V2** — `uretim/devir/CLAUDE-CODE-MASTER-PROMPT-HOLDING-V2.md` (yapıştır-uygula).
7. **Önceki paket korundu** — 696 skill · 174 MCP · 216 skill-title · etki arşivi · PR #13 hattı.
8. **🚩 900M/900B/9e17 karakter** — reddedildi; sözleşme: 122×4–12 KiB + referans zinciri.
9. **Cowork URL** — beklenmedi; repo döngüsü ve MASTER prompt ile devam.
10. **Onay kullanımı** — secret şablon + dry-run; ToS/ödeme gerektiren yüzlerce hesap açılmadı.

## Sayılar
| Metrik | Değer |
|---|---:|
| İştirak | {org['istirak_adet']} |
| Rol | {org['role_adet']} |
| Prompt hedef (holding org) | {org['prompt_hedef']} |
| Soru bankası | {bank['toplam_soru']} |
| Ülke | {ulke['ulke_adet']} |
| Pilot rol kartı | {cards} |

## Sonraki 3 aksiyon
1. Claude Code'a HOLDING-V2 MASTER yapıştır → FAZ 0–6
2. GitHub Secrets'a ihtiyaç duyulan free-tier key'leri ekle (matrise göre)
3. Aylık etki + ülke arşiv cron'unu yeşil tut

## PR
https://github.com/metinduraktr-44/claude-otonom-sistem/pull/13
"""
    write_text(ROOT / "uretim" / "OZET-TEK-SAYFA.md", text)


def materialize_cards(org: dict[str, Any], bank: dict[str, Any], limit: int) -> int:
    out_dir = ROOT / "uretim" / "rol-kartlari"
    if out_dir.exists():
        for p in out_dir.glob("*.md"):
            p.unlink()
    out_dir.mkdir(parents=True, exist_ok=True)
    n = 0
    # Prefer EVP cards across units first, then C-level samples
    priority: list[tuple[dict, dict]] = []
    for u in org["units"]:
        for r in u["roles"]:
            if r["tier"] == "EVP":
                priority.append((u, r))
    for u in org["units"]:
        for r in u["roles"]:
            if r["tier"] == "C-LEVEL":
                priority.append((u, r))
    for u in org["units"]:
        for r in u["roles"]:
            if r["tier"] == "DIRECTOR":
                priority.append((u, r))
    seen = set()
    for u, r in priority:
        if r["name"] in seen:
            continue
        seen.add(r["name"])
        write_text(out_dir / f"{r['name']}.md", render_role_card(u, r, bank))
        n += 1
        if n >= limit:
            break
    return n


def write_ulke_arsiv_sample(ulke: dict[str, Any]) -> None:
    m = ulke["markets"][0]
    day = NOW[:10]
    path = ROOT / "uretim" / "ulke-arsiv" / m["code"] / f"{day}.md"
    text = f"""# Ülke arşivi — {m['code']} {m['name']}
> ts: {NOW} · role: {m['role']} · lang: {m['lang']}

## Hukuk notları
{', '.join(m['law'])}

## Bu koşum
- Önceki arşiv: yok (ilk seed)
- Araştırma: iskelet seed; aylık/gecelik döngüde genişlet
- Top-5: birim top5_seed + yerel otoriteler (KVKK vb.)

## Aksiyon
- [ ] Dil/hukuk onayı checklist
- [ ] Local Lead title overlay
- [ ] BILGI_TABANI satırı

🔗 Zincir: bir sonraki koşum bu dosyayı okuyarak başlar.
"""
    write_text(path, text)


def dogrula() -> int:
    required = [
        ROOT / "data" / "holding_istirak_org.json",
        ROOT / "data" / "soru_bankasi.json",
        ROOT / "data" / "ulke_pazar_iskeleti.json",
        ROOT / "docs" / "HOLDING-ISTIRAK-ORG.md",
        ROOT / "docs" / "OZ-DENETIM-SORU-BANKASI.md",
        ROOT / "docs" / "SECRETS-DRYRUN-MATRISI.md",
        ROOT / "uretim" / "devir" / "CLAUDE-CODE-MASTER-PROMPT-HOLDING-V2.md",
        ROOT / "uretim" / "OZET-TEK-SAYFA.md",
    ]
    ok = True
    for p in required:
        if not p.exists():
            print(f"EKSIK: {p}")
            ok = False
    if not ok:
        return 1
    org = json.loads((ROOT / "data" / "holding_istirak_org.json").read_text(encoding="utf-8"))
    bank = json.loads((ROOT / "data" / "soru_bankasi.json").read_text(encoding="utf-8"))
    assert org["istirak_adet"] >= 7
    assert org["role_adet"] >= 100
    assert bank["toplam_soru"] >= 501
    cards = list((ROOT / "uretim" / "rol-kartlari").glob("*.md"))
    assert len(cards) >= 10
    print(
        f"DOGRULA OK · iştirak={org['istirak_adet']} rol={org['role_adet']} "
        f"soru={bank['toplam_soru']} kart={len(cards)}"
    )
    return 0


def hepsi(pilot_limit: int = 40) -> None:
    org = build_org()
    ulke = build_ulke()
    bank = build_question_bank(org)
    write_json(ROOT / "data" / "holding_istirak_org.json", org)
    write_json(ROOT / "data" / "ulke_pazar_iskeleti.json", ulke)
    write_json(ROOT / "data" / "soru_bankasi.json", bank)
    write_holding_md(org)
    write_ulke_md(ulke)
    write_question_bank_md(bank)
    write_secrets_md()
    cards = materialize_cards(org, bank, pilot_limit)
    write_ulke_arsiv_sample(ulke)
    write_master_v2(org, bank, ulke)
    write_ozet(org, bank, ulke, cards)
    # touch README pointer in ulke-arsiv
    write_text(
        ROOT / "uretim" / "ulke-arsiv" / "README.md",
        f"# Ülke arşivi\n> {NOW}\n\nHer ülke klasöründe `YYYY-MM-DD.md` zaman damgalı notlar.\nNightly: önce oku → araştır → yaz → damgala.\n",
    )
    print(
        f"HEPSI OK ts={NOW} iştirak={org['istirak_adet']} rol={org['role_adet']} "
        f"soru={bank['toplam_soru']} ulke={ulke['ulke_adet']} kart={cards}"
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hepsi", action="store_true")
    ap.add_argument("--dogrula", action="store_true")
    ap.add_argument("--pilot-limit", type=int, default=40)
    args = ap.parse_args()
    if args.dogrula:
        raise SystemExit(dogrula())
    if args.hepsi or not any([args.dogrula]):
        hepsi(args.pilot_limit)
        raise SystemExit(dogrula())


if __name__ == "__main__":
    main()
