# HOLDING × İŞTİRAK ORG
> Üretim: 2026-08-28T13:42:17Z · Kaynak: data/holding_istirak_org.json

**İştirak:** 8 · **Rol:** 633 · **Prompt hedef:** 77226 (122/rol)
**900M/900B karakter/prompt RED — 122×4–12KiB sözleşme**

## Kurul
| Rol | Görev |
|---|---|
| Chairman / Sahip | Nihai onay: sermaye, faz kapıları, birim aç/kapa |
| Group CEO | Portföy stratejisi, birimler arası tahsis |
| Group COO | Operasyon ritmi (gözetim, standup, kurul) |
| Group CTO | Ortak teknik standart (CI, doğrulama, MCP, güvenlik) |
| Group CFO | API bütçesi + birim gelir konsolidasyonu |
| Group CCO | 5 güvenlik kuralı + lisans/uyum tüm repolarda |

## İştirakler

### Holding HQ / OS (`hq`)
- Repo: `claude-otonom-sistem` · Segment: os · Web/app: False
- Domain: Ortak standart, gözetim, jeneratörler, MCP/skill motoru
- Roller: 71 · Prompt hedef: 8662
- C-roles: CEO, COO, CTO, CFO, CCO, CAIO
- Departmanlar:
  - **INF** Teknoloji & Altyapı: CI/CD & Actions, Validation & Security, MCP & Integrations, Repo Hygiene
  - **TAL** Yetenek & Ajan Kalitesi: Agent Lifecycle, Quality Bar, Training Loops
  - **PRD** Ürün & Premium Paket: Premium Components, Packaging & Licensing, Docs & DX
  - **FIN** Finans & Faturalama: Cost Control, Revenue Ops
  - **LEG** Hukuk & Uyum: Licensing, Privacy (KVKK/GDPR), Ad Policy
- Top-5 seed:
  - Dario Amodei — AI güvenlik / org design — https://www.anthropic.com
  - Sam Altman — ürün+platform ölçek — https://openai.com
  - Demis Hassabis — araştırma→ürün — https://deepmind.google
  - Jensen Huang — platform ekonomisi — https://www.nvidia.com
  - Satya Nadella — holding portföy yönetimi — https://www.microsoft.com
- Workflows: bireysel + grupsal + 7×24 follow-the-sun

### AdOps Agency (`adops`)
- Repo: `adops-agents` · Segment: agency · Web/app: False
- Domain: Performans pazarlama & programatik
- Roller: 219 · Prompt hedef: 26718
- C-roles: CEO, COO, CMO, CDO, CFO, CCO
- Departmanlar:
  - **PRG** Programatik Satın Alma: Open Auction & Curation, PMP & Deals, CTV / OTT, DOOH & Audio, Bid Algorithms
  - **SEA** Ücretli Arama: Google Ads Core, SA360 & Automation, PMax & Shopping, Microsoft Ads
  - **SOC** Ücretli Sosyal: Meta, TikTok, LinkedIn & X, Snap & Pinterest, Creative Testing
  - **MOB** Mobil UA & Uygulama: Apple Search Ads, Google App Campaigns, MMP (Adjust/AppsFlyer), Retargeting & CRM
  - **RET** Perakende Medyası: Amazon Ads, TR Marketplaces, Criteo & Onsite, Offsite & DSP
  - **SEO** SEO & İçerik Motoru: Technical SEO, Content Production, Digital PR & Links, Repo Storefront
  - **CRO** CRO & Deneyim: Experimentation, Landing Systems, UX Research
  - **ANA** Analitik & Ölçümleme: GA4 & Tagging, Attribution, MMM & Incrementality, Clean Rooms & Privacy, Dashboards
  - **CRE** Kreatif Stüdyo & DCO: Concept & Copy, Video & Motion, DCO & Feeds, Ad Format Lab
  - **STR** Strateji & Planlama: Audience & Insight, Media Mix, Playbooks & POVs
  - **CLS** Müşteri Hizmetleri: Account Leadership, Reporting Cadence, Onboarding
  - **NBD** Yeni İş & Inbound: Inbound Capture, Pitch Factory, Lead Scoring
  - **PRT** Ortaklıklar & Sponsorluklar: Infra Sponsors, Referral Programs, Ecosystem Relations
- Top-5 seed:
  - Avinash Kaushik — dijital analitik — https://www.kaushik.net
  - Neil Patel — growth/SEO — https://neilpatel.com
  - Mari Smith — sosyal reklam — https://www.marismith.com
  - Rand Fishkin — SEO/audience — https://sparktoro.com
  - Brian Solis — dijital dönüşüm — https://briansolis.com
- Workflows: bireysel + grupsal + 7×24 follow-the-sun

### Performer Growth Hub (`performer`)
- Repo: `performer-growth-hub` · Segment: agency · Web/app: True
- Domain: Uygulama büyüme / app growth (UA, retention, monetization)
- Roller: 78 · Prompt hedef: 9516
- C-roles: CEO, CPO, CMO, CDO, CTO
- Departmanlar:
  - **UA** User Acquisition: Paid UA, ASA/GAC, Influencer UA, Creative UA Lab
  - **RETN** Retention & CRM: Lifecycle, Push/Email, In-app Messaging, Win-back
  - **MON** Monetization: IAP, Ads Mediation, Pricing Experiments
  - **PROD** Product Growth: Onboarding Funnel, Feature Adoption, A/B Lab
  - **DATA** Growth Analytics: MMP, Cohort LTV, Experiment Design
- Top-5 seed:
  - Andrew Chen — growth loops — https://andrewchen.com
  - Brian Balfour — growth frameworks — https://brianbalfour.com
  - Elena Verna — PLG/growth — https://www.elenaverna.com
  - Casey Winters — marketplace growth — https://caseyaccidental.com
  - Reforge (team) — growth programları — https://www.reforge.com
- Workflows: bireysel + grupsal + 7×24 follow-the-sun

### VizaTrack (`vizatrack`)
- Repo: `VizaTrack` · Segment: product · Web/app: True
- Domain: Göç & relokasyon — iOS/Android/Web
- Roller: 84 · Prompt hedef: 10248
- C-roles: CEO, CTO, CPO, CLO, CMO, COO
- Departmanlar:
  - **MOBAPP** Mobil Ürün: iOS, Android, Cross-platform UX
  - **WEB** Web Platform: SSR/App Router, Case Portal, Docs
  - **CASE** Vize Operasyon: Başvuru Akışı, Doküman QA, Ajans Ortaklığı
  - **COMP** Uyumluluk: Ülke Mevzuatı, KVKK/GDPR, Audit Trail
  - **CS** Müşteri Başarı: Onboarding, Support SLA, NPS
  - **GROW** Büyüme: SEO Content, Paid Acquisition, Partner Channel
- Top-5 seed:
  - Nir Eyal — habit/ürün — https://www.nirandfar.com
  - Lenny Rachitsky — ürün büyüme — https://www.lennyrachitsky.com
  - Marty Cagan — ürün liderliği — https://www.svpg.com
  - Julie Zhuo — ürün tasarım — https://medium.com/@joulee
  - Shreyas Doshi — PM craft — https://twitter.com/shreyas
- Workflows: bireysel + grupsal + 7×24 follow-the-sun

### Holding Hukuk & Uyum (`hukuk`)
- Repo: `claude-otonom-sistem` · Segment: shared-service · Web/app: False
- Domain: KVKK/GDPR, lisans, reklam politikası, sözleşme, ülke onayı
- Roller: 55 · Prompt hedef: 6710
- C-roles: CLO, CCO, DPO
- Departmanlar:
  - **PRIV** Gizlilik: KVKK, GDPR, DPIA
  - **LIC** Lisanslama: OSS License, Vendor Contracts, IP
  - **ADP** Reklam Politikası: Platform Policy, Claim Review, Crisis
  - **REG** Regülasyon: Ülke Onayı, Cross-border Transfer, Retention
- Top-5 seed:
  - Daniel Solove — gizlilik hukuku — https://teachprivacy.com
  - Woodrow Hartzog — privacy by design — https://www.woodrowhartzog.com
  - Helen Nissenbaum — contextual integrity — https://nissenbaum.tech.cornell.edu
  - EDPB (kurum) — GDPR otorite — https://edpb.europa.eu
  - KVKK (kurum) — TR gizlilik — https://www.kvkk.gov.tr
- Workflows: bireysel + grupsal + 7×24 follow-the-sun

### Tahmin Uzmanı (`tahmin`)
- Repo: `a-agency-tahmin-uzman-` · Segment: agency · Web/app: False
- Domain: Spor/finans/danışmanlık forecast
- Roller: 42 · Prompt hedef: 5124
- C-roles: CEO, CSO, CDO
- Departmanlar:
  - **FCST** Forecasting: Sports Models, Finance Models, Scenario Lab
  - **RES** Araştırma: Signal Desk, Source QA, Archive Loop
  - **DEL** Teslimat: Client Briefs, Risk Flags, Retros
- Top-5 seed:
  - Nate Silver — probabilistik forecast — https://www.natesilver.net
  - Philip Tetlock — superforecasting — https://www.goodjudgment.com
  - Annie Duke — karar bilimi — https://www.annieduke.com
  - Nassim Taleb — risk/anti-fragile — https://www.fooledbyrandomness.com
  - Gary Klein — naturalistic decision — https://www.gary-klein.com
- Workflows: bireysel + grupsal + 7×24 follow-the-sun

### Movéa (M-AIOS) (`movea`)
- Repo: `or-na.com` · Segment: brand · Web/app: True
- Domain: Premium medikal scrubs DTC
- Roller: 42 · Prompt hedef: 5124
- C-roles: CEO, CMO, COO
- Departmanlar:
  - **BRD** Marka: Positioning, Creative System, Community
  - **ECOM** E-ticaret: PDP, Checkout, CRM
  - **OPS** Operasyon: Inventory, Fulfillment, CX
- Top-5 seed:
  - Seth Godin — marka/permission — https://seths.blog
  - April Dunford — positioning — https://www.aprildunford.com
  - Emily Kramer — B2B/DTC marketing — https://www.mkt1.co
  - Rachel Karten — sosyal marka — https://www.linkedin.com/in/rachelkarten
  - DTC Newsletter (seed) — DTC operasyon — https://www.dtcnewsletter.co
- Workflows: bireysel + grupsal + 7×24 follow-the-sun

### Çiğköftem (`cigkoftem`)
- Repo: `cigkoftem-web-app` · Segment: brand · Web/app: True
- Domain: Gıda markası web app
- Roller: 42 · Prompt hedef: 5124
- C-roles: CEO, CMO, COO
- Departmanlar:
  - **MENU** Menü & İçerik: Recipe CMS, Local SEO, Campaign
  - **ORD** Sipariş: Web Order, Franchise Ops, CX
  - **MKT** Yerel Pazarlama: Maps/SEO, Social Local, Promo
- Top-5 seed:
  - Danny Meyer — hospitality — https://www.dhmnyc.com
  - Will Guidara — CX excellence — https://www.willguidara.com
  - Chipotle (case) — QSR dijital — https://www.chipotle.com
  - Yemeksepeti/ecosystem — TR foodtech — https://www.yemeksepeti.com
  - Getir (case) — hızlı teslimat — https://getir.com
- Workflows: bireysel + grupsal + 7×24 follow-the-sun

## Entegrasyon
- Skill ajans: `data/skill_title_haritasi.json`
- MCP: `data/mcp_hiyerarsi.json`
- Ülke: `data/ulke_pazar_iskeleti.json`
- Rol kartları (pilot): `uretim/rol-kartlari/`
