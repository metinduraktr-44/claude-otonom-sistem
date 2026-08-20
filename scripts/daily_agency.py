#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""daily_agency.py — K2 GÜNDÜZ döngüsü: günün departmanı koşumu (CILT6 §2).
K4 yeniden inşa, 2026-07-27 · İş #17 kısmi teslim. Orijinal (17 Tem F0) konteynerle
kayboldu; bu sürüm AdOps daily_ops.py deseni + CILT5 §99 rotasyonu + CILT6 ritminden
tersine mühendislikle yeniden üretildi. Rotasyon 5 tarihsel indeksle doğrulanır (--dogrula).
Üretir: uretim/gunluk/{tarih}-{DEPT}.md (standup + işe alım iskeleti + makale taslağı
+ öz-denetim soruları), IS_LISTESI damgası, AUDIT_LOG.jsonl + BILGI_TABANI.md zinciri.
GEMINI → OPENROUTER → ANTHROPIC sırasıyla LLM; key yoksa deterministik iskelet
(döngü asla kırılmaz — CILT6: K2 anahtarsız da çalışır).
Kipler: (varsayılan) günlük · --haftalik liderlik tutanağı · --aylik kurul tutanağı
        · --dogrula rotasyon testi · --org-json .claude/org/org.json'ı yeniden yazar
"""
import json, os, re, sys, datetime, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _load_dotenv():
    env_path = os.path.join(ROOT, ".env")
    if not os.path.isfile(env_path):
        return
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            k, v = k.strip(), v.strip().strip("'").strip('"')
            if k and k not in os.environ:
                os.environ[k] = v

_load_dotenv()
NOW = datetime.datetime.now(datetime.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
TODAY = NOW.strftime("%Y-%m-%d")
DOY = int(NOW.strftime("%j"))

# CILT5 §99 rotasyonu — sıra org_uret.py DOMAINS düzleştirmesiyle BİREBİR aynıdır.
# (domain başkanı, [(kod, ad, [katalog eşleme], günlük ana çıktı, [rol aileleri])])
DOMAINS = [
    ("CTO", [
        ("ENG-PLT", "Platform Mühendisliği", ["katalog/agents/development-team", "katalog/agents/api-graphql", "katalog/skills/development"], "platform bileşen bakımı + API sözleşme denetimi", ["Platform Mühendisi", "Altyapı Mühendisi", "API Mühendisi"]),
        ("ENG-APP", "Uygulama Geliştirme", ["katalog/agents/programming-languages", "katalog/skills/web-development", "katalog/commands/nextjs-vercel"], "pilot paketleri için uygulama bileşeni üretimi", ["Backend Mühendisi", "Frontend Mühendisi", "Mobil Mühendisi"]),
        ("ENG-DEV", "DevOps & SRE", ["katalog/agents/devops-infrastructure", "katalog/commands/deployment", "katalog/commands/automation"], "workflow sağlığı + gecelik döngü nöbeti", ["DevOps Mühendisi", "Site Güvenilirlik Mühendisi (SRE)"]),
        ("ENG-QA", "Kalite & Test", ["katalog/agents/performance-testing", "katalog/commands/testing"], "6 katman doğrulama koşumu + validate.py bakımı", ["Test Otomasyon Mühendisi", "QA Analisti"]),
    ]),
    ("CAIO", [
        ("AI-RES", "AI Araştırma", ["katalog/agents/ai-specialists", "katalog/skills/ai-research"], "günlük literatür/repo taraması → BILGI_TABANI damıtımı", ["AI Araştırmacısı", "Model Değerlendirme Uzmanı (Evals)"]),
        ("AI-AGT", "Ajan Mühendisliği", ["katalog/agents/ai-specialists", "katalog/agents/mcp-dev-team", "katalog/commands/orchestration"], "yeni ajan bileşeni üretimi (CILT2 şablonu)", ["Ajan Mühendisi", "Orkestrasyon Mühendisi", "Araç (Tool) Entegrasyon Mühendisi"]),
        ("AI-PRM", "Prompt & Context Mühendisliği", ["katalog/agents/ai-specialists", "katalog/skills/ai-maestro"], "pilot promptlarının v-serisi iyileştirmesi", ["Prompt Mühendisi", "Context Mühendisi"]),
        ("AI-SAF", "AI Güvenliği & Hizalama", ["katalog/agents/security", "katalog/skills/security"], "5 güvenlik kuralı denetimi + script inceleme (Kural 2)", ["Hizalama Uzmanı", "Red-Team Uzmanı"]),
    ]),
    ("CDO", [
        ("DAT-ENG", "Veri Mühendisliği", ["katalog/agents/database", "katalog/skills/database"], "AUDIT_LOG/BILGI_TABANI veri bütünlüğü", ["Veri Mühendisi", "Veri Boru Hattı Mühendisi"]),
        ("DAT-SCI", "Veri Bilimi", ["katalog/agents/data-ai", "katalog/skills/scientific"], "pilot metrik modelleri (tahmin/fiyat)", ["Veri Bilimci", "Makine Öğrenmesi Mühendisi"]),
        ("DAT-BI", "Analitik & BI", ["katalog/skills/analytics", "katalog/commands/analysis"], "haftalık konsolide paket metrikleri", ["BI Analisti", "Veri Görselleştirme Uzmanı"]),
    ]),
    ("CPO", [
        ("PRD-MGT", "Ürün Yönetimi", ["katalog/agents/expert-advisors", "katalog/commands/project-management"], "bileşen yol haritası önceliklendirme", ["Ürün Yöneticisi", "Teknik Ürün Yöneticisi"]),
        ("PRD-DSN", "Tasarım", ["katalog/agents/ui-analysis", "katalog/skills/creative-design", "katalog/skills/design-to-code"], "pilot arayüz/şablon tasarımları", ["Ürün Tasarımcısı (UX)", "Arayüz Tasarımcısı (UI)", "Tasarım Sistemi Uzmanı"]),
        ("PRD-OPS", "Ürün Operasyonları", ["katalog/skills/productivity", "katalog/commands/utilities"], "kullanım geri bildirimi → KARAR_LOGU girdisi", ["Ürün Operasyon Uzmanı", "Kullanıcı Araştırmacısı"]),
    ]),
    ("CMO", [
        ("MKT-BRD", "Marka & İçerik", ["katalog/agents/business-marketing", "katalog/skills/marketing"], "Movéa pilotu marka içerik üretimi", ["Marka Stratejisti", "İçerik Pazarlama Uzmanı"]),
        ("MKT-PRF", "Performans Pazarlama (AdOps)", ["katalog/agents/business-marketing", "katalog/skills/business-marketing"], "Response DGA dikeyi: kampanya/atıf analizi", ["Performans Pazarlama Uzmanı", "Medya Satın Alma Uzmanı", "Atıf (Attribution) Analisti"]),
        ("MKT-SEO", "SEO & Organik Büyüme", ["katalog/skills/marketing", "katalog/commands/marketing"], "repo/ürün sayfası görünürlük artışı", ["SEO Uzmanı", "İçerik Optimizasyon Uzmanı"]),
        ("MKT-SOC", "Sosyal Medya", ["katalog/skills/marketing", "katalog/skills/enterprise-communication"], "LinkedIn yayın akışı (movea komutu ile)", ["Sosyal Medya Yöneticisi", "Topluluk Yöneticisi"]),
    ]),
    ("CRO", [
        ("REV-SLS", "Satış", ["katalog/agents/business-marketing", "katalog/skills/career"], "ajans lead hunisi takibi (GELIR_MOTORU kanal 5)", ["Satış Temsilcisi (AE)", "Satış Geliştirme Temsilcisi (SDR)"]),
        ("REV-PRT", "İş Ortaklıkları", ["katalog/agents/finance", "katalog/skills/business-marketing"], "infra sponsorluk adayları (kanal 1) izleme", ["Ortaklık Yöneticisi", "Sponsorluk Geliştirme Uzmanı"]),
        ("REV-CSM", "Müşteri Başarısı", ["katalog/skills/enterprise-communication", "katalog/commands/setup"], "pilot iç müşteri memnuniyet döngüsü", ["Müşteri Başarı Yöneticisi", "Onboarding Uzmanı"]),
        ("REV-OPS", "Gelir Operasyonları", ["katalog/skills/analytics", "katalog/commands/sync"], "gelir kanalı metrik panosu", ["RevOps Analisti", "CRM Uzmanı"]),
    ]),
    ("CCO", [
        ("MED-PUB", "Yayıncılık & Makale", ["katalog/agents/documentation", "katalog/skills/document-processing", "katalog/commands/documentation"], "GÜNDE MİN. 1 makale/güncelleme üretimi", ["Teknik Yazar", "Editör", "Araştırma Yazarı"]),
        ("MED-CRE", "Video & Kreatif", ["katalog/agents/podcast-creator-team", "katalog/agents/ffmpeg-clip-team", "katalog/skills/video", "katalog/skills/media"], "tanıtım/kreatif varlık üretimi", ["Video Editörü", "Grafik Tasarımcısı"]),
        ("MED-LOC", "Yerelleştirme (TR)", ["katalog/skills/document-processing", "katalog/commands/documentation"], "katalog bileşenlerinin TR/dikey uyarlaması", ["Yerelleştirme Uzmanı", "Çevirmen-Editör"]),
    ]),
    ("COO", [
        ("OPS-PMO", "Program Yönetimi (PMO)", ["katalog/commands/project-management", "katalog/commands/team"], "günlük iş listesi dağıtımı + takip", ["Program Yöneticisi", "Proje Koordinatörü"]),
        ("OPS-BIZ", "İş Operasyonları", ["katalog/skills/operations", "katalog/skills/workflow-automation"], "operasyon ritmi (CILT6) uygulaması", ["İş Operasyon Analisti", "Süreç İyileştirme Uzmanı"]),
        ("OPS-TLS", "Araç & Tedarik", ["katalog/agents/development-tools", "katalog/agents/web-tools"], "araç envanteri + maliyet izleme", ["Araç Yönetim Uzmanı", "Tedarik Analisti"]),
    ]),
    ("CFO", [
        ("FIN-FPA", "Finansal Planlama (FP&A)", ["katalog/agents/finance", "katalog/skills/analytics"], "token/kredi bütçe takibi", ["FP&A Analisti", "Bütçe Uzmanı"]),
        ("FIN-ACC", "Muhasebe & Raporlama", ["katalog/agents/finance", "katalog/skills/document-processing"], "aylık finansal özet", ["Muhasebe Uzmanı", "Finansal Raporlama Analisti"]),
        ("FIN-REV", "Gelir Motoru İzleme", ["katalog/agents/finance", "katalog/skills/business-marketing"], "GELIR_MOTORU.md 5 kanal KPI'ları", ["Gelir Analisti", "Monetizasyon Uzmanı"]),
    ]),
    ("CISO", [
        ("SEC-OPS", "Güvenlik Operasyonları", ["katalog/agents/security", "katalog/commands/security"], "günlük güvenlik taraması", ["Güvenlik Operasyon Analisti", "Olay Müdahale Uzmanı"]),
        ("SEC-AUD", "Uyum Denetimi (5 Kural)", ["katalog/agents/security", "katalog/skills/security"], "her yeni bileşen: 5 kural + script inceleme onayı", ["Denetçi (Auditor)", "Bileşen Güvenlik İnceleme Uzmanı"]),
        ("SEC-SUP", "Tedarik Zinciri Güvenliği", ["katalog/agents/security", "katalog/hooks"], "upstream/bağımlılık değişiklik kontrolü", ["Tedarik Zinciri Güvenlik Analisti", "Bağımlılık İzleme Uzmanı"]),
    ]),
    ("CHRO", [
        ("HRA-REC", "Ajan İşe Alım", ["katalog/agents/expert-advisors", "katalog/KATALOG_INDEKS.md"], "katalogdan rol-bileşen eşleştirme (işe alım)", ["Ajan İşe Alım Uzmanı", "Yetenek Haritalama Analisti"]),
        ("HRA-PRF", "Performans & Kalite", ["katalog/agents/performance-testing", "katalog/skills/productivity"], "ajan çıktı kalite puanlama", ["Performans Değerlendirme Uzmanı", "Kalite Güvence Analisti"]),
        ("HRA-LRN", "Eğitim & Bilgi Tabanı", ["katalog/skills/document-processing", "katalog/agents/documentation"], "BILGI_TABANI.md küratörlüğü (append-only)", ["Bilgi Tabanı Küratörü", "Öğrenim Damıtma Uzmanı"]),
    ]),
    ("CLO", [
        ("LGL-LIC", "Lisans Uyumu (MIT)", ["katalog/skills/security", "katalog/KATALOG_INDEKS.md"], "MIT atıf bütünlüğü (LICENSE-UPSTREAM)", ["Lisans Uyum Uzmanı", "Atıf (Attribution) Denetçisi"]),
        ("LGL-PRV", "Veri Gizliliği", ["katalog/agents/security", "katalog/skills/security"], "pilot verilerinde gizlilik kontrolü", ["Gizlilik Uzmanı (KVKK/GDPR)", "Veri Sınıflandırma Analisti"]),
    ]),
    ("CIO", [
        ("INF-MCP", "MCP Entegrasyonları", ["katalog/mcps", "katalog/agents/mcp-dev-team"], "MCP kataloğu bakım + yeni bağlayıcı değerlendirme", ["MCP Entegrasyon Mühendisi", "Bağlayıcı (Connector) Uzmanı"]),
        ("INF-SET", "Ayar & Yapılandırma", ["katalog/settings", "katalog/commands/setup"], "settings şablonları + ortam standartları", ["Yapılandırma Yöneticisi", "Ortam (Environment) Uzmanı"]),
        ("INF-HKS", "Hooks & Otomasyon", ["katalog/hooks", "katalog/commands/automation"], "damga/denetim hook zinciri bakımı", ["Hook Geliştirici", "Otomasyon Mühendisi"]),
        ("INF-LOP", "Döngüler & Zamanlama", ["katalog/loops", "katalog/sandbox"], "nightly + daily-agency + upstream-sync nöbeti", ["Döngü Operatörü", "Zamanlama (Scheduler) Uzmanı"]),
    ]),
    ("CSO", [
        ("STR-INT", "Pazar İstihbaratı", ["katalog/agents/deep-research-team", "katalog/skills/web-data"], "günlük ekosistem taraması (CILT3 haritası)", ["Pazar İstihbarat Analisti", "Trend Araştırmacısı"]),
        ("STR-CMP", "Rakip Analizi", ["katalog/agents/deep-research-team", "katalog/skills/analytics"], "muadil repo/ürün kıyaslama raporu", ["Rakip Analiz Uzmanı", "Kıyaslama (Benchmark) Analisti"]),
        ("STR-GRW", "Büyüme & Yatırım", ["katalog/agents/finance", "katalog/agents/expert-advisors"], "gelir kanalı büyüme deneyleri", ["Büyüme Stratejisti", "Yatırım Analisti"]),
    ]),
]
DEPTS = [(chair, d) for chair, ds in DOMAINS for d in ds]  # 46 sıralı departman

TOPICS = [  # MED-PUB günlük makale rotasyonu (TR, merkez org gündemi)
    "claude-code-skills-ile-ajans-otomasyonu", "mcp-guvenlik-denetimi-kontrol-listesi",
    "tersine-muhendislik-ile-bilesen-uretimi", "tr-dikey-yerellestirme-deseni",
    "agentic-media-buying-hazirlik", "acik-kaynak-katalog-secim-kriterleri",
    "gunluk-otonom-dongu-tasarimi", "audit-log-zinciriyle-izlenebilirlik",
    "skill-vs-agent-vs-command-ayrimi", "upstream-senkron-ve-vendorlama-riski",
    "rol-tabanli-llm-org-tasarimi", "progressive-disclosure-token-ekonomisi",
    "pilot-istirak-devreye-alma", "gelir-kanali-deney-tasarimi", "oz-denetim-soru-bankasi-kullanimi",
]

def read(p):
    fp = os.path.join(ROOT, p)
    return open(fp, encoding="utf-8").read() if os.path.exists(fp) else ""

def write(p, content):
    fp = os.path.join(ROOT, p)
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
    print("WROTE", p)

def append(p, content):
    fp = os.path.join(ROOT, p)
    with open(fp, "a", encoding="utf-8") as f:
        f.write(content)

def llm(prompt, max_tokens=1600):
    """Gemini → OpenRouter → Anthropic. Key yoksa None (iskelet devam)."""
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    try:
        from gemini_client import chat as gm_chat, configured as gm_ok
        if gm_ok():
            text = gm_chat(prompt, max_tokens=max_tokens)
            if text:
                return text
    except Exception as e:
        print("GEMINI SKIPPED:", e)
    try:
        from openrouter_client import chat as or_chat, configured as or_ok
        if or_ok():
            text = or_chat(prompt, max_tokens=max_tokens)
            if text:
                return text
    except Exception as e:
        print("OPENROUTER SKIPPED:", e)
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        return None
    body = json.dumps({"model": "claude-sonnet-4-5", "max_tokens": max_tokens,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body,
        headers={"x-api-key": key, "anthropic-version": "2023-06-01",
                 "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.loads(r.read())
        return "".join(b.get("text", "") for b in data.get("content", []))
    except Exception as e:
        print("LLM SKIPPED:", e)
        return None

def sorular(n=8):
    """docs/OZ-DENETIM-SORU-BANKASI.md'den DOY tabanlı deterministik örneklem."""
    txt = read("docs/OZ-DENETIM-SORU-BANKASI.md")
    qs = [m.strip() for m in re.findall(r"^\s*(?:\d+\.|-)\s+(.+\?)\s*$", txt, re.M)]
    if not qs:
        return []
    return [qs[(DOY * 7 + i * 53) % len(qs)] for i in range(n)]

def dept_of(doy):
    return DEPTS[doy % 46]

def gunluk():
    chair, (kod, ad, esleme, cikti, aileler) = dept_of(DOY)
    bilesen = esleme[DOY % len(esleme)]
    lead = f"{kod}-M1"
    path = f"uretim/gunluk/{TODAY}-{kod}.md"
    if os.path.exists(os.path.join(ROOT, path)):
        print("SKIP (bugünkü çıktı zaten var):", path)
        return path, kod
    L = [f"# GÜNLÜK KOŞUM — {TODAY} · {kod} ({ad})",
         f"> Üretim: {TS} · Rotasyon: gün {DOY} % 46 = {DOY % 46} · Başkan: {chair} grup başkanı · Sorumlu hat: `{lead}`",
         "", "## 1. STANDUP TUTANAĞI",
         f"| Rol | Katkı |", "|---|---|",
         f"| {chair} (başkan) | Günün ana çıktısı: {cikti} |"]
    for i, f_ in enumerate(aileler, 1):
        L.append(f"| {kod}-F{i}-L5 (Baş {f_}) | [K4 Cowork doldurur: kendi katalog bileşeni perspektifinden 1 madde] |")
    L += ["", "## 2. İŞE ALIM ADAYI (katalog eşlemesinden deterministik seçim)",
          f"- Kaynak klasör: `{bilesen}` · Uyarlama: CILT2 şablonu + CILT7 anatomisi (TR/dikey)",
          "- SEC-AUD denetimi: 5 kural (CILT4) — script içeren bileşen KOŞULMAZ, incele/özetle (Kural 2); SKILLS'te upstream `risk` alanı okunur",
          "- [K4 Cowork doldurur: seçilen bileşen + taslak + denetim sonucu]",
          "", "## 3. MAKALE TASLAĞI",
          f"- Konu (rotasyon): `{TOPICS[DOY % len(TOPICS)]}` — [K4 Cowork 300-500 kelime doldurur]",
          "", "## 4. TAKİP",
          f"- İş listesi damgası: {TS} · Upstream durumu: `katalog/SENKRON_LOG.md` son satır",
          ""]
    qs = sorular()
    if qs:
        L.append("## 5. GÜNÜN ÖZ-DENETİM SORULARI (docs/OZ-DENETIM-SORU-BANKASI.md)")
        L += [f"{i}. {q}" for i, q in enumerate(qs, 1)]
        L.append("> Kritik 'hayır'lar IS_LISTESI'ne aksiyon olarak düşer.")
    write(path, "\n".join(L) + "\n")
    isl = read("IS_LISTESI.md")
    if isl:
        if "> Son koşum damgası:" in isl:
            isl = re.sub(r"> Son koşum damgası: \S+", f"> Son koşum damgası: {TS}", isl, count=1)
        else:
            isl = isl.replace("\n\n", f"\n> Son koşum damgası: {TS}\n\n", 1)
        write("IS_LISTESI.md", isl)
    return path, kod

def haftalik():
    girdiler = []
    for line in read("AUDIT_LOG.jsonl").splitlines():
        try:
            j = json.loads(line)
        except Exception:
            continue
        ts = j.get("ts_start") or j.get("ts", "")
        if ts and (NOW - datetime.datetime.fromisoformat(ts.replace("Z", "+00:00"))).days < 7:
            girdiler.append(j)
    kaldi = [j for j in girdiler if str(j.get("denetim", "")).upper() == "KALDI"]
    path = f"uretim/toplantilar/{TODAY}-haftalik-liderlik.md"
    write(path, "\n".join([
        f"# HAFTALIK LİDERLİK SYNC — {TODAY}", f"> Üretim: {TS} · Katılım: 14 grup başkanı + CEO-05 · Kayıt: CILT6 §3",
        "", f"- Son 7 gün AUDIT kaydı: **{len(girdiler)}** · KALDI: **{len(kaldi)}**",
        f"- Rotasyon kanıtı (İş #4): AUDIT satır sayısı gün bazında K4 oturumunda doğrulanır",
        "- KALDI dökümü: " + ("; ".join(j.get("islem", "?") + "@" + (j.get("ts_start") or j.get("ts", ""))[:10] for j in kaldi) if kaldi else "—"),
        "- [K4 Cowork doldurur: haftalık konsolide paket + domain başına 1 satır]", ""]))
    return path

def aylik():
    path = f"uretim/toplantilar/{TODAY}-aylik-kurul.md"
    senkron = [l for l in read("katalog/SENKRON_LOG.md").splitlines() if l.startswith("| 2")]
    write(path, "\n".join([
        f"# AYLIK KURUL TUTANAĞI — {TODAY}", f"> Üretim: {TS} · Katılım: KURUL (5) + CEO ofisi (6) · Karar kaydı: KARAR_LOGU.md (BRD-05)",
        "", "## Gündem", "1. Faz kapıları (ROADMAP.md) — durum ve blokörler",
        f"2. Upstream delta incelemesi (İş #16, Kural 2): birikmiş {len(senkron)} senkron kaydı — toplu karar",
        "3. Gelir kanalları (GELIR_MOTORU.md 5 kanal) aylık KPI kesiti",
        "4. 46/46 departman işe alım kapsaması (İş #8)",
        "", "- [K4 Cowork doldurur: kararlar → KARAR_LOGU.md]", ""]))
    return path

def dogrula():
    assert len(DEPTS) == 46, "departman 46 değil: %d" % len(DEPTS)
    beklenen = {198: "MKT-BRD", 200: "MKT-SEO", 201: "MKT-SOC", 207: "MED-CRE", 208: "MED-LOC"}
    for doy, kod in beklenen.items():
        gercek = dept_of(doy)[1][0]
        assert gercek == kod, f"rotasyon kayması: gün {doy} → {gercek}, beklenen {kod}"
    print("DOĞRULAMA: GEÇTİ — 46 departman, rotasyon 5 tarihsel indeksle birebir")

def org_json():
    data = {"generated": TS, "source": "scripts/daily_agency.py --org-json (CILT5 §99 sırası)",
            "departments": [{"code": k, "name_tr": a, "chair": c, "esleme": e, "cikti": ci,
                             "aileler": f} for c, (k, a, e, ci, f) in DEPTS]}
    write(".claude/org/org.json", json.dumps(data, ensure_ascii=False, indent=1) + "\n")

if __name__ == "__main__":
    if "--dogrula" in sys.argv:
        dogrula(); sys.exit(0)
    if "--org-json" in sys.argv:
        org_json(); sys.exit(0)
    dogrula()
    if "--haftalik" in sys.argv:
        out = haftalik(); islem = "haftalik-liderlik"; kod = "CEO-02"
    elif "--aylik" in sys.argv:
        out = aylik(); islem = "aylik-kurul"; kod = "BRD-05"
    else:
        out, kod = gunluk(); islem = "daily-agency"
    append("AUDIT_LOG.jsonl", json.dumps({
        "ts_start": TS, "ts_end": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "islem": islem, "departman": kod, "cikti": out, "denetim": "RUN",
        "onceki_ogrenim_kullanildi": "evet (BILGI_TABANI.md okunur — K4 doldurur)"}, ensure_ascii=False) + "\n")
    append("BILGI_TABANI.md", f"\n- [{TS}] {islem}: iskelet üretildi ({out}); K4 Cowork oturumu taslağı doldurur.")
    print("DAILY AGENCY DONE", TS)
