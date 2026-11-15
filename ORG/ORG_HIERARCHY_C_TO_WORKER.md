# ORG Hierarchy — C-Level → Worker (LATOS)

> Kaynak: `data/holding_istirak_org.json` · **633 title** · ts: 2026-11-15T10:05:00Z · Europe/Istanbul 2026-11-15T13:05:00+03:00
> Additive to `ORG/ORG_CHART.md`. Hiçbir title atlanmaz — tam liste ROSTER + bu hiyerarşi.

## Kademe sözleşmesi
`C-LEVEL` → `EVP` → `DIRECTOR` → `LEAD` → `SPECIALIST` → `ANALYST` (worker/IC)

## Kurul
- **Chairman / Sahip** (`owner`): Nihai onay: sermaye, faz kapıları, birim aç/kapa
- **Group CEO** (`group-ceo`): Portföy stratejisi, birimler arası tahsis
- **Group COO** (`group-coo`): Operasyon ritmi (gözetim, standup, kurul)
- **Group CTO** (`group-cto`): Ortak teknik standart (CI, doğrulama, MCP, güvenlik)
- **Group CFO** (`group-cfo`): API bütçesi + birim gelir konsolidasyonu
- **Group CCO** (`group-cco`): 5 güvenlik kuralı + lisans/uyum tüm repolarda

## Birimler × kademe (özet sayılar + örnekler)

### Holding HQ / OS (`hq`)
- **C-LEVEL:** 6
- **EVP:** 5
- **DIRECTOR:** 15
- **LEAD:** 15
- **SPECIALIST:** 15
- **ANALYST:** 15
#### C-LEVEL
- `hq-ceo` — CEO, Holding HQ / OS → reports_to: `owner`
- `hq-coo` — COO, Holding HQ / OS → reports_to: `group-ceo`
- `hq-cto` — CTO, Holding HQ / OS → reports_to: `group-ceo`
- `hq-cfo` — CFO, Holding HQ / OS → reports_to: `group-ceo`
- `hq-cco` — CCO, Holding HQ / OS → reports_to: `group-ceo`
- `hq-caio` — CAIO, Holding HQ / OS → reports_to: `group-ceo`
#### EVP
- `hq-evp-teknoloji-altyapı` — EVP, Teknoloji & Altyapı → reports_to: `hq-coo`
- `hq-evp-yetenek-ajan-kalitesi` — EVP, Yetenek & Ajan Kalitesi → reports_to: `hq-coo`
- `hq-evp-ürün-premium-paket` — EVP, Ürün & Premium Paket → reports_to: `hq-coo`
- `hq-evp-finans-faturalama` — EVP, Finans & Faturalama → reports_to: `hq-coo`
- `hq-evp-hukuk-uyum` — EVP, Hukuk & Uyum → reports_to: `hq-coo`
#### DIRECTOR
- `hq-dir-ci-cd-actions` — Director, CI/CD & Actions → reports_to: `hq-evp-teknoloji-altyapı`
- `hq-dir-validation-security` — Director, Validation & Security → reports_to: `hq-evp-teknoloji-altyapı`
- `hq-dir-mcp-integrations` — Director, MCP & Integrations → reports_to: `hq-evp-teknoloji-altyapı`
- `hq-dir-repo-hygiene` — Director, Repo Hygiene → reports_to: `hq-evp-teknoloji-altyapı`
- `hq-dir-agent-lifecycle` — Director, Agent Lifecycle → reports_to: `hq-evp-yetenek-ajan-kalitesi`
- `hq-dir-quality-bar` — Director, Quality Bar → reports_to: `hq-evp-yetenek-ajan-kalitesi`
- `hq-dir-training-loops` — Director, Training Loops → reports_to: `hq-evp-yetenek-ajan-kalitesi`
- `hq-dir-premium-components` — Director, Premium Components → reports_to: `hq-evp-ürün-premium-paket`
- `hq-dir-packaging-licensing` — Director, Packaging & Licensing → reports_to: `hq-evp-ürün-premium-paket`
- `hq-dir-docs-dx` — Director, Docs & DX → reports_to: `hq-evp-ürün-premium-paket`
- `hq-dir-cost-control` — Director, Cost Control → reports_to: `hq-evp-finans-faturalama`
- `hq-dir-revenue-ops` — Director, Revenue Ops → reports_to: `hq-evp-finans-faturalama`
- `hq-dir-licensing` — Director, Licensing → reports_to: `hq-evp-hukuk-uyum`
- `hq-dir-privacy-kvkk-gdpr` — Director, Privacy (KVKK/GDPR) → reports_to: `hq-evp-hukuk-uyum`
- `hq-dir-ad-policy` — Director, Ad Policy → reports_to: `hq-evp-hukuk-uyum`
#### LEAD
- `hq-lead-ci-cd-actions` — Lead, CI/CD & Actions → reports_to: `hq-dir-ci-cd-actions`
- `hq-lead-validation-security` — Lead, Validation & Security → reports_to: `hq-dir-validation-security`
- `hq-lead-mcp-integrations` — Lead, MCP & Integrations → reports_to: `hq-dir-mcp-integrations`
- `hq-lead-repo-hygiene` — Lead, Repo Hygiene → reports_to: `hq-dir-repo-hygiene`
- `hq-lead-agent-lifecycle` — Lead, Agent Lifecycle → reports_to: `hq-dir-agent-lifecycle`
- `hq-lead-quality-bar` — Lead, Quality Bar → reports_to: `hq-dir-quality-bar`
- `hq-lead-training-loops` — Lead, Training Loops → reports_to: `hq-dir-training-loops`
- `hq-lead-premium-components` — Lead, Premium Components → reports_to: `hq-dir-premium-components`
- `hq-lead-packaging-licensing` — Lead, Packaging & Licensing → reports_to: `hq-dir-packaging-licensing`
- `hq-lead-docs-dx` — Lead, Docs & DX → reports_to: `hq-dir-docs-dx`
- `hq-lead-cost-control` — Lead, Cost Control → reports_to: `hq-dir-cost-control`
- `hq-lead-revenue-ops` — Lead, Revenue Ops → reports_to: `hq-dir-revenue-ops`
- `hq-lead-licensing` — Lead, Licensing → reports_to: `hq-dir-licensing`
- `hq-lead-privacy-kvkk-gdpr` — Lead, Privacy (KVKK/GDPR) → reports_to: `hq-dir-privacy-kvkk-gdpr`
- `hq-lead-ad-policy` — Lead, Ad Policy → reports_to: `hq-dir-ad-policy`
#### SPECIALIST
- `hq-spec-ci-cd-actions` — Specialist, CI/CD & Actions → reports_to: `hq-lead-ci-cd-actions`
- `hq-spec-validation-security` — Specialist, Validation & Security → reports_to: `hq-lead-validation-security`
- `hq-spec-mcp-integrations` — Specialist, MCP & Integrations → reports_to: `hq-lead-mcp-integrations`
- `hq-spec-repo-hygiene` — Specialist, Repo Hygiene → reports_to: `hq-lead-repo-hygiene`
- `hq-spec-agent-lifecycle` — Specialist, Agent Lifecycle → reports_to: `hq-lead-agent-lifecycle`
- `hq-spec-quality-bar` — Specialist, Quality Bar → reports_to: `hq-lead-quality-bar`
- `hq-spec-training-loops` — Specialist, Training Loops → reports_to: `hq-lead-training-loops`
- `hq-spec-premium-components` — Specialist, Premium Components → reports_to: `hq-lead-premium-components`
- `hq-spec-packaging-licensing` — Specialist, Packaging & Licensing → reports_to: `hq-lead-packaging-licensing`
- `hq-spec-docs-dx` — Specialist, Docs & DX → reports_to: `hq-lead-docs-dx`
- `hq-spec-cost-control` — Specialist, Cost Control → reports_to: `hq-lead-cost-control`
- `hq-spec-revenue-ops` — Specialist, Revenue Ops → reports_to: `hq-lead-revenue-ops`
- `hq-spec-licensing` — Specialist, Licensing → reports_to: `hq-lead-licensing`
- `hq-spec-privacy-kvkk-gdpr` — Specialist, Privacy (KVKK/GDPR) → reports_to: `hq-lead-privacy-kvkk-gdpr`
- `hq-spec-ad-policy` — Specialist, Ad Policy → reports_to: `hq-lead-ad-policy`
#### ANALYST
- `hq-anl-ci-cd-actions` — Analyst, CI/CD & Actions → reports_to: `hq-lead-ci-cd-actions`
- `hq-anl-validation-security` — Analyst, Validation & Security → reports_to: `hq-lead-validation-security`
- `hq-anl-mcp-integrations` — Analyst, MCP & Integrations → reports_to: `hq-lead-mcp-integrations`
- `hq-anl-repo-hygiene` — Analyst, Repo Hygiene → reports_to: `hq-lead-repo-hygiene`
- `hq-anl-agent-lifecycle` — Analyst, Agent Lifecycle → reports_to: `hq-lead-agent-lifecycle`
- `hq-anl-quality-bar` — Analyst, Quality Bar → reports_to: `hq-lead-quality-bar`
- `hq-anl-training-loops` — Analyst, Training Loops → reports_to: `hq-lead-training-loops`
- `hq-anl-premium-components` — Analyst, Premium Components → reports_to: `hq-lead-premium-components`
- `hq-anl-packaging-licensing` — Analyst, Packaging & Licensing → reports_to: `hq-lead-packaging-licensing`
- `hq-anl-docs-dx` — Analyst, Docs & DX → reports_to: `hq-lead-docs-dx`
- `hq-anl-cost-control` — Analyst, Cost Control → reports_to: `hq-lead-cost-control`
- `hq-anl-revenue-ops` — Analyst, Revenue Ops → reports_to: `hq-lead-revenue-ops`
- `hq-anl-licensing` — Analyst, Licensing → reports_to: `hq-lead-licensing`
- `hq-anl-privacy-kvkk-gdpr` — Analyst, Privacy (KVKK/GDPR) → reports_to: `hq-lead-privacy-kvkk-gdpr`
- `hq-anl-ad-policy` — Analyst, Ad Policy → reports_to: `hq-lead-ad-policy`

### AdOps Agency (`adops`)
- **C-LEVEL:** 6
- **EVP:** 13
- **DIRECTOR:** 50
- **LEAD:** 50
- **SPECIALIST:** 50
- **ANALYST:** 50
#### C-LEVEL
- `adops-ceo` — CEO, AdOps Agency → reports_to: `owner`
- `adops-coo` — COO, AdOps Agency → reports_to: `group-ceo`
- `adops-cmo` — CMO, AdOps Agency → reports_to: `group-ceo`
- `adops-cdo` — CDO, AdOps Agency → reports_to: `group-ceo`
- `adops-cfo` — CFO, AdOps Agency → reports_to: `group-ceo`
- `adops-cco` — CCO, AdOps Agency → reports_to: `group-ceo`
#### EVP
- `adops-evp-programatik-satın-alma` — EVP, Programatik Satın Alma → reports_to: `adops-coo`
- `adops-evp-ücretli-arama` — EVP, Ücretli Arama → reports_to: `adops-coo`
- `adops-evp-ücretli-sosyal` — EVP, Ücretli Sosyal → reports_to: `adops-coo`
- `adops-evp-mobil-ua-uygulama` — EVP, Mobil UA & Uygulama → reports_to: `adops-coo`
- `adops-evp-perakende-medyası` — EVP, Perakende Medyası → reports_to: `adops-coo`
- `adops-evp-seo-içerik-motoru` — EVP, SEO & İçerik Motoru → reports_to: `adops-coo`
- `adops-evp-cro-deneyim` — EVP, CRO & Deneyim → reports_to: `adops-coo`
- `adops-evp-analitik-ölçümleme` — EVP, Analitik & Ölçümleme → reports_to: `adops-coo`
- `adops-evp-kreatif-stüdyo-dco` — EVP, Kreatif Stüdyo & DCO → reports_to: `adops-coo`
- `adops-evp-strateji-planlama` — EVP, Strateji & Planlama → reports_to: `adops-coo`
- `adops-evp-müşteri-hizmetleri` — EVP, Müşteri Hizmetleri → reports_to: `adops-coo`
- `adops-evp-yeni-iş-inbound` — EVP, Yeni İş & Inbound → reports_to: `adops-coo`
- `adops-evp-ortaklıklar-sponsorluklar` — EVP, Ortaklıklar & Sponsorluklar → reports_to: `adops-coo`
#### DIRECTOR
- `adops-dir-open-auction-curation` — Director, Open Auction & Curation → reports_to: `adops-evp-programatik-satın-alma`
- `adops-dir-pmp-deals` — Director, PMP & Deals → reports_to: `adops-evp-programatik-satın-alma`
- `adops-dir-ctv-ott` — Director, CTV / OTT → reports_to: `adops-evp-programatik-satın-alma`
- `adops-dir-dooh-audio` — Director, DOOH & Audio → reports_to: `adops-evp-programatik-satın-alma`
- `adops-dir-bid-algorithms` — Director, Bid Algorithms → reports_to: `adops-evp-programatik-satın-alma`
- `adops-dir-google-ads-core` — Director, Google Ads Core → reports_to: `adops-evp-ücretli-arama`
- `adops-dir-sa360-automation` — Director, SA360 & Automation → reports_to: `adops-evp-ücretli-arama`
- `adops-dir-pmax-shopping` — Director, PMax & Shopping → reports_to: `adops-evp-ücretli-arama`
- `adops-dir-microsoft-ads` — Director, Microsoft Ads → reports_to: `adops-evp-ücretli-arama`
- `adops-dir-meta` — Director, Meta → reports_to: `adops-evp-ücretli-sosyal`
- `adops-dir-tiktok` — Director, TikTok → reports_to: `adops-evp-ücretli-sosyal`
- `adops-dir-linkedin-x` — Director, LinkedIn & X → reports_to: `adops-evp-ücretli-sosyal`
- `adops-dir-snap-pinterest` — Director, Snap & Pinterest → reports_to: `adops-evp-ücretli-sosyal`
- `adops-dir-creative-testing` — Director, Creative Testing → reports_to: `adops-evp-ücretli-sosyal`
- `adops-dir-apple-search-ads` — Director, Apple Search Ads → reports_to: `adops-evp-mobil-ua-uygulama`
- `adops-dir-google-app-campaigns` — Director, Google App Campaigns → reports_to: `adops-evp-mobil-ua-uygulama`
- `adops-dir-mmp-adjust-appsflyer` — Director, MMP (Adjust/AppsFlyer) → reports_to: `adops-evp-mobil-ua-uygulama`
- `adops-dir-retargeting-crm` — Director, Retargeting & CRM → reports_to: `adops-evp-mobil-ua-uygulama`
- `adops-dir-amazon-ads` — Director, Amazon Ads → reports_to: `adops-evp-perakende-medyası`
- `adops-dir-tr-marketplaces` — Director, TR Marketplaces → reports_to: `adops-evp-perakende-medyası`
- `adops-dir-criteo-onsite` — Director, Criteo & Onsite → reports_to: `adops-evp-perakende-medyası`
- `adops-dir-offsite-dsp` — Director, Offsite & DSP → reports_to: `adops-evp-perakende-medyası`
- `adops-dir-technical-seo` — Director, Technical SEO → reports_to: `adops-evp-seo-içerik-motoru`
- `adops-dir-content-production` — Director, Content Production → reports_to: `adops-evp-seo-içerik-motoru`
- `adops-dir-digital-pr-links` — Director, Digital PR & Links → reports_to: `adops-evp-seo-içerik-motoru`
- `adops-dir-repo-storefront` — Director, Repo Storefront → reports_to: `adops-evp-seo-içerik-motoru`
- `adops-dir-experimentation` — Director, Experimentation → reports_to: `adops-evp-cro-deneyim`
- `adops-dir-landing-systems` — Director, Landing Systems → reports_to: `adops-evp-cro-deneyim`
- `adops-dir-ux-research` — Director, UX Research → reports_to: `adops-evp-cro-deneyim`
- `adops-dir-ga4-tagging` — Director, GA4 & Tagging → reports_to: `adops-evp-analitik-ölçümleme`
- `adops-dir-attribution` — Director, Attribution → reports_to: `adops-evp-analitik-ölçümleme`
- `adops-dir-mmm-incrementality` — Director, MMM & Incrementality → reports_to: `adops-evp-analitik-ölçümleme`
- `adops-dir-clean-rooms-privacy` — Director, Clean Rooms & Privacy → reports_to: `adops-evp-analitik-ölçümleme`
- `adops-dir-dashboards` — Director, Dashboards → reports_to: `adops-evp-analitik-ölçümleme`
- `adops-dir-concept-copy` — Director, Concept & Copy → reports_to: `adops-evp-kreatif-stüdyo-dco`
- `adops-dir-video-motion` — Director, Video & Motion → reports_to: `adops-evp-kreatif-stüdyo-dco`
- `adops-dir-dco-feeds` — Director, DCO & Feeds → reports_to: `adops-evp-kreatif-stüdyo-dco`
- `adops-dir-ad-format-lab` — Director, Ad Format Lab → reports_to: `adops-evp-kreatif-stüdyo-dco`
- `adops-dir-audience-insight` — Director, Audience & Insight → reports_to: `adops-evp-strateji-planlama`
- `adops-dir-media-mix` — Director, Media Mix → reports_to: `adops-evp-strateji-planlama`
- `adops-dir-playbooks-povs` — Director, Playbooks & POVs → reports_to: `adops-evp-strateji-planlama`
- `adops-dir-account-leadership` — Director, Account Leadership → reports_to: `adops-evp-müşteri-hizmetleri`
- `adops-dir-reporting-cadence` — Director, Reporting Cadence → reports_to: `adops-evp-müşteri-hizmetleri`
- `adops-dir-onboarding` — Director, Onboarding → reports_to: `adops-evp-müşteri-hizmetleri`
- `adops-dir-inbound-capture` — Director, Inbound Capture → reports_to: `adops-evp-yeni-iş-inbound`
- `adops-dir-pitch-factory` — Director, Pitch Factory → reports_to: `adops-evp-yeni-iş-inbound`
- `adops-dir-lead-scoring` — Director, Lead Scoring → reports_to: `adops-evp-yeni-iş-inbound`
- `adops-dir-infra-sponsors` — Director, Infra Sponsors → reports_to: `adops-evp-ortaklıklar-sponsorluklar`
- `adops-dir-referral-programs` — Director, Referral Programs → reports_to: `adops-evp-ortaklıklar-sponsorluklar`
- `adops-dir-ecosystem-relations` — Director, Ecosystem Relations → reports_to: `adops-evp-ortaklıklar-sponsorluklar`
#### LEAD
- `adops-lead-open-auction-curation` — Lead, Open Auction & Curation → reports_to: `adops-dir-open-auction-curation`
- `adops-lead-pmp-deals` — Lead, PMP & Deals → reports_to: `adops-dir-pmp-deals`
- `adops-lead-ctv-ott` — Lead, CTV / OTT → reports_to: `adops-dir-ctv-ott`
- `adops-lead-dooh-audio` — Lead, DOOH & Audio → reports_to: `adops-dir-dooh-audio`
- `adops-lead-bid-algorithms` — Lead, Bid Algorithms → reports_to: `adops-dir-bid-algorithms`
- `adops-lead-google-ads-core` — Lead, Google Ads Core → reports_to: `adops-dir-google-ads-core`
- `adops-lead-sa360-automation` — Lead, SA360 & Automation → reports_to: `adops-dir-sa360-automation`
- `adops-lead-pmax-shopping` — Lead, PMax & Shopping → reports_to: `adops-dir-pmax-shopping`
- `adops-lead-microsoft-ads` — Lead, Microsoft Ads → reports_to: `adops-dir-microsoft-ads`
- `adops-lead-meta` — Lead, Meta → reports_to: `adops-dir-meta`
- `adops-lead-tiktok` — Lead, TikTok → reports_to: `adops-dir-tiktok`
- `adops-lead-linkedin-x` — Lead, LinkedIn & X → reports_to: `adops-dir-linkedin-x`
- `adops-lead-snap-pinterest` — Lead, Snap & Pinterest → reports_to: `adops-dir-snap-pinterest`
- `adops-lead-creative-testing` — Lead, Creative Testing → reports_to: `adops-dir-creative-testing`
- `adops-lead-apple-search-ads` — Lead, Apple Search Ads → reports_to: `adops-dir-apple-search-ads`
- `adops-lead-google-app-campaigns` — Lead, Google App Campaigns → reports_to: `adops-dir-google-app-campaigns`
- `adops-lead-mmp-adjust-appsflyer` — Lead, MMP (Adjust/AppsFlyer) → reports_to: `adops-dir-mmp-adjust-appsflyer`
- `adops-lead-retargeting-crm` — Lead, Retargeting & CRM → reports_to: `adops-dir-retargeting-crm`
- `adops-lead-amazon-ads` — Lead, Amazon Ads → reports_to: `adops-dir-amazon-ads`
- `adops-lead-tr-marketplaces` — Lead, TR Marketplaces → reports_to: `adops-dir-tr-marketplaces`
- `adops-lead-criteo-onsite` — Lead, Criteo & Onsite → reports_to: `adops-dir-criteo-onsite`
- `adops-lead-offsite-dsp` — Lead, Offsite & DSP → reports_to: `adops-dir-offsite-dsp`
- `adops-lead-technical-seo` — Lead, Technical SEO → reports_to: `adops-dir-technical-seo`
- `adops-lead-content-production` — Lead, Content Production → reports_to: `adops-dir-content-production`
- `adops-lead-digital-pr-links` — Lead, Digital PR & Links → reports_to: `adops-dir-digital-pr-links`
- `adops-lead-repo-storefront` — Lead, Repo Storefront → reports_to: `adops-dir-repo-storefront`
- `adops-lead-experimentation` — Lead, Experimentation → reports_to: `adops-dir-experimentation`
- `adops-lead-landing-systems` — Lead, Landing Systems → reports_to: `adops-dir-landing-systems`
- `adops-lead-ux-research` — Lead, UX Research → reports_to: `adops-dir-ux-research`
- `adops-lead-ga4-tagging` — Lead, GA4 & Tagging → reports_to: `adops-dir-ga4-tagging`
- `adops-lead-attribution` — Lead, Attribution → reports_to: `adops-dir-attribution`
- `adops-lead-mmm-incrementality` — Lead, MMM & Incrementality → reports_to: `adops-dir-mmm-incrementality`
- `adops-lead-clean-rooms-privacy` — Lead, Clean Rooms & Privacy → reports_to: `adops-dir-clean-rooms-privacy`
- `adops-lead-dashboards` — Lead, Dashboards → reports_to: `adops-dir-dashboards`
- `adops-lead-concept-copy` — Lead, Concept & Copy → reports_to: `adops-dir-concept-copy`
- `adops-lead-video-motion` — Lead, Video & Motion → reports_to: `adops-dir-video-motion`
- `adops-lead-dco-feeds` — Lead, DCO & Feeds → reports_to: `adops-dir-dco-feeds`
- `adops-lead-ad-format-lab` — Lead, Ad Format Lab → reports_to: `adops-dir-ad-format-lab`
- `adops-lead-audience-insight` — Lead, Audience & Insight → reports_to: `adops-dir-audience-insight`
- `adops-lead-media-mix` — Lead, Media Mix → reports_to: `adops-dir-media-mix`
- `adops-lead-playbooks-povs` — Lead, Playbooks & POVs → reports_to: `adops-dir-playbooks-povs`
- `adops-lead-account-leadership` — Lead, Account Leadership → reports_to: `adops-dir-account-leadership`
- `adops-lead-reporting-cadence` — Lead, Reporting Cadence → reports_to: `adops-dir-reporting-cadence`
- `adops-lead-onboarding` — Lead, Onboarding → reports_to: `adops-dir-onboarding`
- `adops-lead-inbound-capture` — Lead, Inbound Capture → reports_to: `adops-dir-inbound-capture`
- `adops-lead-pitch-factory` — Lead, Pitch Factory → reports_to: `adops-dir-pitch-factory`
- `adops-lead-lead-scoring` — Lead, Lead Scoring → reports_to: `adops-dir-lead-scoring`
- `adops-lead-infra-sponsors` — Lead, Infra Sponsors → reports_to: `adops-dir-infra-sponsors`
- `adops-lead-referral-programs` — Lead, Referral Programs → reports_to: `adops-dir-referral-programs`
- `adops-lead-ecosystem-relations` — Lead, Ecosystem Relations → reports_to: `adops-dir-ecosystem-relations`
#### SPECIALIST
- `adops-spec-open-auction-curation` — Specialist, Open Auction & Curation → reports_to: `adops-lead-open-auction-curation`
- `adops-spec-pmp-deals` — Specialist, PMP & Deals → reports_to: `adops-lead-pmp-deals`
- `adops-spec-ctv-ott` — Specialist, CTV / OTT → reports_to: `adops-lead-ctv-ott`
- `adops-spec-dooh-audio` — Specialist, DOOH & Audio → reports_to: `adops-lead-dooh-audio`
- `adops-spec-bid-algorithms` — Specialist, Bid Algorithms → reports_to: `adops-lead-bid-algorithms`
- `adops-spec-google-ads-core` — Specialist, Google Ads Core → reports_to: `adops-lead-google-ads-core`
- `adops-spec-sa360-automation` — Specialist, SA360 & Automation → reports_to: `adops-lead-sa360-automation`
- `adops-spec-pmax-shopping` — Specialist, PMax & Shopping → reports_to: `adops-lead-pmax-shopping`
- `adops-spec-microsoft-ads` — Specialist, Microsoft Ads → reports_to: `adops-lead-microsoft-ads`
- `adops-spec-meta` — Specialist, Meta → reports_to: `adops-lead-meta`
- `adops-spec-tiktok` — Specialist, TikTok → reports_to: `adops-lead-tiktok`
- `adops-spec-linkedin-x` — Specialist, LinkedIn & X → reports_to: `adops-lead-linkedin-x`
- `adops-spec-snap-pinterest` — Specialist, Snap & Pinterest → reports_to: `adops-lead-snap-pinterest`
- `adops-spec-creative-testing` — Specialist, Creative Testing → reports_to: `adops-lead-creative-testing`
- `adops-spec-apple-search-ads` — Specialist, Apple Search Ads → reports_to: `adops-lead-apple-search-ads`
- `adops-spec-google-app-campaigns` — Specialist, Google App Campaigns → reports_to: `adops-lead-google-app-campaigns`
- `adops-spec-mmp-adjust-appsflyer` — Specialist, MMP (Adjust/AppsFlyer) → reports_to: `adops-lead-mmp-adjust-appsflyer`
- `adops-spec-retargeting-crm` — Specialist, Retargeting & CRM → reports_to: `adops-lead-retargeting-crm`
- `adops-spec-amazon-ads` — Specialist, Amazon Ads → reports_to: `adops-lead-amazon-ads`
- `adops-spec-tr-marketplaces` — Specialist, TR Marketplaces → reports_to: `adops-lead-tr-marketplaces`
- `adops-spec-criteo-onsite` — Specialist, Criteo & Onsite → reports_to: `adops-lead-criteo-onsite`
- `adops-spec-offsite-dsp` — Specialist, Offsite & DSP → reports_to: `adops-lead-offsite-dsp`
- `adops-spec-technical-seo` — Specialist, Technical SEO → reports_to: `adops-lead-technical-seo`
- `adops-spec-content-production` — Specialist, Content Production → reports_to: `adops-lead-content-production`
- `adops-spec-digital-pr-links` — Specialist, Digital PR & Links → reports_to: `adops-lead-digital-pr-links`
- `adops-spec-repo-storefront` — Specialist, Repo Storefront → reports_to: `adops-lead-repo-storefront`
- `adops-spec-experimentation` — Specialist, Experimentation → reports_to: `adops-lead-experimentation`
- `adops-spec-landing-systems` — Specialist, Landing Systems → reports_to: `adops-lead-landing-systems`
- `adops-spec-ux-research` — Specialist, UX Research → reports_to: `adops-lead-ux-research`
- `adops-spec-ga4-tagging` — Specialist, GA4 & Tagging → reports_to: `adops-lead-ga4-tagging`
- `adops-spec-attribution` — Specialist, Attribution → reports_to: `adops-lead-attribution`
- `adops-spec-mmm-incrementality` — Specialist, MMM & Incrementality → reports_to: `adops-lead-mmm-incrementality`
- `adops-spec-clean-rooms-privacy` — Specialist, Clean Rooms & Privacy → reports_to: `adops-lead-clean-rooms-privacy`
- `adops-spec-dashboards` — Specialist, Dashboards → reports_to: `adops-lead-dashboards`
- `adops-spec-concept-copy` — Specialist, Concept & Copy → reports_to: `adops-lead-concept-copy`
- `adops-spec-video-motion` — Specialist, Video & Motion → reports_to: `adops-lead-video-motion`
- `adops-spec-dco-feeds` — Specialist, DCO & Feeds → reports_to: `adops-lead-dco-feeds`
- `adops-spec-ad-format-lab` — Specialist, Ad Format Lab → reports_to: `adops-lead-ad-format-lab`
- `adops-spec-audience-insight` — Specialist, Audience & Insight → reports_to: `adops-lead-audience-insight`
- `adops-spec-media-mix` — Specialist, Media Mix → reports_to: `adops-lead-media-mix`
- `adops-spec-playbooks-povs` — Specialist, Playbooks & POVs → reports_to: `adops-lead-playbooks-povs`
- `adops-spec-account-leadership` — Specialist, Account Leadership → reports_to: `adops-lead-account-leadership`
- `adops-spec-reporting-cadence` — Specialist, Reporting Cadence → reports_to: `adops-lead-reporting-cadence`
- `adops-spec-onboarding` — Specialist, Onboarding → reports_to: `adops-lead-onboarding`
- `adops-spec-inbound-capture` — Specialist, Inbound Capture → reports_to: `adops-lead-inbound-capture`
- `adops-spec-pitch-factory` — Specialist, Pitch Factory → reports_to: `adops-lead-pitch-factory`
- `adops-spec-lead-scoring` — Specialist, Lead Scoring → reports_to: `adops-lead-lead-scoring`
- `adops-spec-infra-sponsors` — Specialist, Infra Sponsors → reports_to: `adops-lead-infra-sponsors`
- `adops-spec-referral-programs` — Specialist, Referral Programs → reports_to: `adops-lead-referral-programs`
- `adops-spec-ecosystem-relations` — Specialist, Ecosystem Relations → reports_to: `adops-lead-ecosystem-relations`
#### ANALYST
- `adops-anl-open-auction-curation` — Analyst, Open Auction & Curation → reports_to: `adops-lead-open-auction-curation`
- `adops-anl-pmp-deals` — Analyst, PMP & Deals → reports_to: `adops-lead-pmp-deals`
- `adops-anl-ctv-ott` — Analyst, CTV / OTT → reports_to: `adops-lead-ctv-ott`
- `adops-anl-dooh-audio` — Analyst, DOOH & Audio → reports_to: `adops-lead-dooh-audio`
- `adops-anl-bid-algorithms` — Analyst, Bid Algorithms → reports_to: `adops-lead-bid-algorithms`
- `adops-anl-google-ads-core` — Analyst, Google Ads Core → reports_to: `adops-lead-google-ads-core`
- `adops-anl-sa360-automation` — Analyst, SA360 & Automation → reports_to: `adops-lead-sa360-automation`
- `adops-anl-pmax-shopping` — Analyst, PMax & Shopping → reports_to: `adops-lead-pmax-shopping`
- `adops-anl-microsoft-ads` — Analyst, Microsoft Ads → reports_to: `adops-lead-microsoft-ads`
- `adops-anl-meta` — Analyst, Meta → reports_to: `adops-lead-meta`
- `adops-anl-tiktok` — Analyst, TikTok → reports_to: `adops-lead-tiktok`
- `adops-anl-linkedin-x` — Analyst, LinkedIn & X → reports_to: `adops-lead-linkedin-x`
- `adops-anl-snap-pinterest` — Analyst, Snap & Pinterest → reports_to: `adops-lead-snap-pinterest`
- `adops-anl-creative-testing` — Analyst, Creative Testing → reports_to: `adops-lead-creative-testing`
- `adops-anl-apple-search-ads` — Analyst, Apple Search Ads → reports_to: `adops-lead-apple-search-ads`
- `adops-anl-google-app-campaigns` — Analyst, Google App Campaigns → reports_to: `adops-lead-google-app-campaigns`
- `adops-anl-mmp-adjust-appsflyer` — Analyst, MMP (Adjust/AppsFlyer) → reports_to: `adops-lead-mmp-adjust-appsflyer`
- `adops-anl-retargeting-crm` — Analyst, Retargeting & CRM → reports_to: `adops-lead-retargeting-crm`
- `adops-anl-amazon-ads` — Analyst, Amazon Ads → reports_to: `adops-lead-amazon-ads`
- `adops-anl-tr-marketplaces` — Analyst, TR Marketplaces → reports_to: `adops-lead-tr-marketplaces`
- `adops-anl-criteo-onsite` — Analyst, Criteo & Onsite → reports_to: `adops-lead-criteo-onsite`
- `adops-anl-offsite-dsp` — Analyst, Offsite & DSP → reports_to: `adops-lead-offsite-dsp`
- `adops-anl-technical-seo` — Analyst, Technical SEO → reports_to: `adops-lead-technical-seo`
- `adops-anl-content-production` — Analyst, Content Production → reports_to: `adops-lead-content-production`
- `adops-anl-digital-pr-links` — Analyst, Digital PR & Links → reports_to: `adops-lead-digital-pr-links`
- `adops-anl-repo-storefront` — Analyst, Repo Storefront → reports_to: `adops-lead-repo-storefront`
- `adops-anl-experimentation` — Analyst, Experimentation → reports_to: `adops-lead-experimentation`
- `adops-anl-landing-systems` — Analyst, Landing Systems → reports_to: `adops-lead-landing-systems`
- `adops-anl-ux-research` — Analyst, UX Research → reports_to: `adops-lead-ux-research`
- `adops-anl-ga4-tagging` — Analyst, GA4 & Tagging → reports_to: `adops-lead-ga4-tagging`
- `adops-anl-attribution` — Analyst, Attribution → reports_to: `adops-lead-attribution`
- `adops-anl-mmm-incrementality` — Analyst, MMM & Incrementality → reports_to: `adops-lead-mmm-incrementality`
- `adops-anl-clean-rooms-privacy` — Analyst, Clean Rooms & Privacy → reports_to: `adops-lead-clean-rooms-privacy`
- `adops-anl-dashboards` — Analyst, Dashboards → reports_to: `adops-lead-dashboards`
- `adops-anl-concept-copy` — Analyst, Concept & Copy → reports_to: `adops-lead-concept-copy`
- `adops-anl-video-motion` — Analyst, Video & Motion → reports_to: `adops-lead-video-motion`
- `adops-anl-dco-feeds` — Analyst, DCO & Feeds → reports_to: `adops-lead-dco-feeds`
- `adops-anl-ad-format-lab` — Analyst, Ad Format Lab → reports_to: `adops-lead-ad-format-lab`
- `adops-anl-audience-insight` — Analyst, Audience & Insight → reports_to: `adops-lead-audience-insight`
- `adops-anl-media-mix` — Analyst, Media Mix → reports_to: `adops-lead-media-mix`
- `adops-anl-playbooks-povs` — Analyst, Playbooks & POVs → reports_to: `adops-lead-playbooks-povs`
- `adops-anl-account-leadership` — Analyst, Account Leadership → reports_to: `adops-lead-account-leadership`
- `adops-anl-reporting-cadence` — Analyst, Reporting Cadence → reports_to: `adops-lead-reporting-cadence`
- `adops-anl-onboarding` — Analyst, Onboarding → reports_to: `adops-lead-onboarding`
- `adops-anl-inbound-capture` — Analyst, Inbound Capture → reports_to: `adops-lead-inbound-capture`
- `adops-anl-pitch-factory` — Analyst, Pitch Factory → reports_to: `adops-lead-pitch-factory`
- `adops-anl-lead-scoring` — Analyst, Lead Scoring → reports_to: `adops-lead-lead-scoring`
- `adops-anl-infra-sponsors` — Analyst, Infra Sponsors → reports_to: `adops-lead-infra-sponsors`
- `adops-anl-referral-programs` — Analyst, Referral Programs → reports_to: `adops-lead-referral-programs`
- `adops-anl-ecosystem-relations` — Analyst, Ecosystem Relations → reports_to: `adops-lead-ecosystem-relations`

### Performer Growth Hub (`performer`)
- **C-LEVEL:** 5
- **EVP:** 5
- **DIRECTOR:** 17
- **LEAD:** 17
- **SPECIALIST:** 17
- **ANALYST:** 17
#### C-LEVEL
- `performer-ceo` — CEO, Performer Growth Hub → reports_to: `owner`
- `performer-cpo` — CPO, Performer Growth Hub → reports_to: `group-ceo`
- `performer-cmo` — CMO, Performer Growth Hub → reports_to: `group-ceo`
- `performer-cdo` — CDO, Performer Growth Hub → reports_to: `group-ceo`
- `performer-cto` — CTO, Performer Growth Hub → reports_to: `group-ceo`
#### EVP
- `performer-evp-user-acquisition` — EVP, User Acquisition → reports_to: `performer-ceo`
- `performer-evp-retention-crm` — EVP, Retention & CRM → reports_to: `performer-ceo`
- `performer-evp-monetization` — EVP, Monetization → reports_to: `performer-ceo`
- `performer-evp-product-growth` — EVP, Product Growth → reports_to: `performer-ceo`
- `performer-evp-growth-analytics` — EVP, Growth Analytics → reports_to: `performer-ceo`
#### DIRECTOR
- `performer-dir-paid-ua` — Director, Paid UA → reports_to: `performer-evp-user-acquisition`
- `performer-dir-asa-gac` — Director, ASA/GAC → reports_to: `performer-evp-user-acquisition`
- `performer-dir-influencer-ua` — Director, Influencer UA → reports_to: `performer-evp-user-acquisition`
- `performer-dir-creative-ua-lab` — Director, Creative UA Lab → reports_to: `performer-evp-user-acquisition`
- `performer-dir-lifecycle` — Director, Lifecycle → reports_to: `performer-evp-retention-crm`
- `performer-dir-push-email` — Director, Push/Email → reports_to: `performer-evp-retention-crm`
- `performer-dir-in-app-messaging` — Director, In-app Messaging → reports_to: `performer-evp-retention-crm`
- `performer-dir-win-back` — Director, Win-back → reports_to: `performer-evp-retention-crm`
- `performer-dir-iap` — Director, IAP → reports_to: `performer-evp-monetization`
- `performer-dir-ads-mediation` — Director, Ads Mediation → reports_to: `performer-evp-monetization`
- `performer-dir-pricing-experiments` — Director, Pricing Experiments → reports_to: `performer-evp-monetization`
- `performer-dir-onboarding-funnel` — Director, Onboarding Funnel → reports_to: `performer-evp-product-growth`
- `performer-dir-feature-adoption` — Director, Feature Adoption → reports_to: `performer-evp-product-growth`
- `performer-dir-a-b-lab` — Director, A/B Lab → reports_to: `performer-evp-product-growth`
- `performer-dir-mmp` — Director, MMP → reports_to: `performer-evp-growth-analytics`
- `performer-dir-cohort-ltv` — Director, Cohort LTV → reports_to: `performer-evp-growth-analytics`
- `performer-dir-experiment-design` — Director, Experiment Design → reports_to: `performer-evp-growth-analytics`
#### LEAD
- `performer-lead-paid-ua` — Lead, Paid UA → reports_to: `performer-dir-paid-ua`
- `performer-lead-asa-gac` — Lead, ASA/GAC → reports_to: `performer-dir-asa-gac`
- `performer-lead-influencer-ua` — Lead, Influencer UA → reports_to: `performer-dir-influencer-ua`
- `performer-lead-creative-ua-lab` — Lead, Creative UA Lab → reports_to: `performer-dir-creative-ua-lab`
- `performer-lead-lifecycle` — Lead, Lifecycle → reports_to: `performer-dir-lifecycle`
- `performer-lead-push-email` — Lead, Push/Email → reports_to: `performer-dir-push-email`
- `performer-lead-in-app-messaging` — Lead, In-app Messaging → reports_to: `performer-dir-in-app-messaging`
- `performer-lead-win-back` — Lead, Win-back → reports_to: `performer-dir-win-back`
- `performer-lead-iap` — Lead, IAP → reports_to: `performer-dir-iap`
- `performer-lead-ads-mediation` — Lead, Ads Mediation → reports_to: `performer-dir-ads-mediation`
- `performer-lead-pricing-experiments` — Lead, Pricing Experiments → reports_to: `performer-dir-pricing-experiments`
- `performer-lead-onboarding-funnel` — Lead, Onboarding Funnel → reports_to: `performer-dir-onboarding-funnel`
- `performer-lead-feature-adoption` — Lead, Feature Adoption → reports_to: `performer-dir-feature-adoption`
- `performer-lead-a-b-lab` — Lead, A/B Lab → reports_to: `performer-dir-a-b-lab`
- `performer-lead-mmp` — Lead, MMP → reports_to: `performer-dir-mmp`
- `performer-lead-cohort-ltv` — Lead, Cohort LTV → reports_to: `performer-dir-cohort-ltv`
- `performer-lead-experiment-design` — Lead, Experiment Design → reports_to: `performer-dir-experiment-design`
#### SPECIALIST
- `performer-spec-paid-ua` — Specialist, Paid UA → reports_to: `performer-lead-paid-ua`
- `performer-spec-asa-gac` — Specialist, ASA/GAC → reports_to: `performer-lead-asa-gac`
- `performer-spec-influencer-ua` — Specialist, Influencer UA → reports_to: `performer-lead-influencer-ua`
- `performer-spec-creative-ua-lab` — Specialist, Creative UA Lab → reports_to: `performer-lead-creative-ua-lab`
- `performer-spec-lifecycle` — Specialist, Lifecycle → reports_to: `performer-lead-lifecycle`
- `performer-spec-push-email` — Specialist, Push/Email → reports_to: `performer-lead-push-email`
- `performer-spec-in-app-messaging` — Specialist, In-app Messaging → reports_to: `performer-lead-in-app-messaging`
- `performer-spec-win-back` — Specialist, Win-back → reports_to: `performer-lead-win-back`
- `performer-spec-iap` — Specialist, IAP → reports_to: `performer-lead-iap`
- `performer-spec-ads-mediation` — Specialist, Ads Mediation → reports_to: `performer-lead-ads-mediation`
- `performer-spec-pricing-experiments` — Specialist, Pricing Experiments → reports_to: `performer-lead-pricing-experiments`
- `performer-spec-onboarding-funnel` — Specialist, Onboarding Funnel → reports_to: `performer-lead-onboarding-funnel`
- `performer-spec-feature-adoption` — Specialist, Feature Adoption → reports_to: `performer-lead-feature-adoption`
- `performer-spec-a-b-lab` — Specialist, A/B Lab → reports_to: `performer-lead-a-b-lab`
- `performer-spec-mmp` — Specialist, MMP → reports_to: `performer-lead-mmp`
- `performer-spec-cohort-ltv` — Specialist, Cohort LTV → reports_to: `performer-lead-cohort-ltv`
- `performer-spec-experiment-design` — Specialist, Experiment Design → reports_to: `performer-lead-experiment-design`
#### ANALYST
- `performer-anl-paid-ua` — Analyst, Paid UA → reports_to: `performer-lead-paid-ua`
- `performer-anl-asa-gac` — Analyst, ASA/GAC → reports_to: `performer-lead-asa-gac`
- `performer-anl-influencer-ua` — Analyst, Influencer UA → reports_to: `performer-lead-influencer-ua`
- `performer-anl-creative-ua-lab` — Analyst, Creative UA Lab → reports_to: `performer-lead-creative-ua-lab`
- `performer-anl-lifecycle` — Analyst, Lifecycle → reports_to: `performer-lead-lifecycle`
- `performer-anl-push-email` — Analyst, Push/Email → reports_to: `performer-lead-push-email`
- `performer-anl-in-app-messaging` — Analyst, In-app Messaging → reports_to: `performer-lead-in-app-messaging`
- `performer-anl-win-back` — Analyst, Win-back → reports_to: `performer-lead-win-back`
- `performer-anl-iap` — Analyst, IAP → reports_to: `performer-lead-iap`
- `performer-anl-ads-mediation` — Analyst, Ads Mediation → reports_to: `performer-lead-ads-mediation`
- `performer-anl-pricing-experiments` — Analyst, Pricing Experiments → reports_to: `performer-lead-pricing-experiments`
- `performer-anl-onboarding-funnel` — Analyst, Onboarding Funnel → reports_to: `performer-lead-onboarding-funnel`
- `performer-anl-feature-adoption` — Analyst, Feature Adoption → reports_to: `performer-lead-feature-adoption`
- `performer-anl-a-b-lab` — Analyst, A/B Lab → reports_to: `performer-lead-a-b-lab`
- `performer-anl-mmp` — Analyst, MMP → reports_to: `performer-lead-mmp`
- `performer-anl-cohort-ltv` — Analyst, Cohort LTV → reports_to: `performer-lead-cohort-ltv`
- `performer-anl-experiment-design` — Analyst, Experiment Design → reports_to: `performer-lead-experiment-design`

### VizaTrack (`vizatrack`)
- **C-LEVEL:** 6
- **EVP:** 6
- **DIRECTOR:** 18
- **LEAD:** 18
- **SPECIALIST:** 18
- **ANALYST:** 18
#### C-LEVEL
- `vizatrack-ceo` — CEO, VizaTrack → reports_to: `owner`
- `vizatrack-cto` — CTO, VizaTrack → reports_to: `group-ceo`
- `vizatrack-cpo` — CPO, VizaTrack → reports_to: `group-ceo`
- `vizatrack-clo` — CLO, VizaTrack → reports_to: `group-ceo`
- `vizatrack-cmo` — CMO, VizaTrack → reports_to: `group-ceo`
- `vizatrack-coo` — COO, VizaTrack → reports_to: `group-ceo`
#### EVP
- `vizatrack-evp-mobil-ürün` — EVP, Mobil Ürün → reports_to: `vizatrack-coo`
- `vizatrack-evp-web-platform` — EVP, Web Platform → reports_to: `vizatrack-coo`
- `vizatrack-evp-vize-operasyon` — EVP, Vize Operasyon → reports_to: `vizatrack-coo`
- `vizatrack-evp-uyumluluk` — EVP, Uyumluluk → reports_to: `vizatrack-coo`
- `vizatrack-evp-müşteri-başarı` — EVP, Müşteri Başarı → reports_to: `vizatrack-coo`
- `vizatrack-evp-büyüme` — EVP, Büyüme → reports_to: `vizatrack-coo`
#### DIRECTOR
- `vizatrack-dir-ios` — Director, iOS → reports_to: `vizatrack-evp-mobil-ürün`
- `vizatrack-dir-android` — Director, Android → reports_to: `vizatrack-evp-mobil-ürün`
- `vizatrack-dir-cross-platform-ux` — Director, Cross-platform UX → reports_to: `vizatrack-evp-mobil-ürün`
- `vizatrack-dir-ssr-app-router` — Director, SSR/App Router → reports_to: `vizatrack-evp-web-platform`
- `vizatrack-dir-case-portal` — Director, Case Portal → reports_to: `vizatrack-evp-web-platform`
- `vizatrack-dir-docs` — Director, Docs → reports_to: `vizatrack-evp-web-platform`
- `vizatrack-dir-başvuru-akışı` — Director, Başvuru Akışı → reports_to: `vizatrack-evp-vize-operasyon`
- `vizatrack-dir-doküman-qa` — Director, Doküman QA → reports_to: `vizatrack-evp-vize-operasyon`
- `vizatrack-dir-ajans-ortaklığı` — Director, Ajans Ortaklığı → reports_to: `vizatrack-evp-vize-operasyon`
- `vizatrack-dir-ülke-mevzuatı` — Director, Ülke Mevzuatı → reports_to: `vizatrack-evp-uyumluluk`
- `vizatrack-dir-kvkk-gdpr` — Director, KVKK/GDPR → reports_to: `vizatrack-evp-uyumluluk`
- `vizatrack-dir-audit-trail` — Director, Audit Trail → reports_to: `vizatrack-evp-uyumluluk`
- `vizatrack-dir-onboarding` — Director, Onboarding → reports_to: `vizatrack-evp-müşteri-başarı`
- `vizatrack-dir-support-sla` — Director, Support SLA → reports_to: `vizatrack-evp-müşteri-başarı`
- `vizatrack-dir-nps` — Director, NPS → reports_to: `vizatrack-evp-müşteri-başarı`
- `vizatrack-dir-seo-content` — Director, SEO Content → reports_to: `vizatrack-evp-büyüme`
- `vizatrack-dir-paid-acquisition` — Director, Paid Acquisition → reports_to: `vizatrack-evp-büyüme`
- `vizatrack-dir-partner-channel` — Director, Partner Channel → reports_to: `vizatrack-evp-büyüme`
#### LEAD
- `vizatrack-lead-ios` — Lead, iOS → reports_to: `vizatrack-dir-ios`
- `vizatrack-lead-android` — Lead, Android → reports_to: `vizatrack-dir-android`
- `vizatrack-lead-cross-platform-ux` — Lead, Cross-platform UX → reports_to: `vizatrack-dir-cross-platform-ux`
- `vizatrack-lead-ssr-app-router` — Lead, SSR/App Router → reports_to: `vizatrack-dir-ssr-app-router`
- `vizatrack-lead-case-portal` — Lead, Case Portal → reports_to: `vizatrack-dir-case-portal`
- `vizatrack-lead-docs` — Lead, Docs → reports_to: `vizatrack-dir-docs`
- `vizatrack-lead-başvuru-akışı` — Lead, Başvuru Akışı → reports_to: `vizatrack-dir-başvuru-akışı`
- `vizatrack-lead-doküman-qa` — Lead, Doküman QA → reports_to: `vizatrack-dir-doküman-qa`
- `vizatrack-lead-ajans-ortaklığı` — Lead, Ajans Ortaklığı → reports_to: `vizatrack-dir-ajans-ortaklığı`
- `vizatrack-lead-ülke-mevzuatı` — Lead, Ülke Mevzuatı → reports_to: `vizatrack-dir-ülke-mevzuatı`
- `vizatrack-lead-kvkk-gdpr` — Lead, KVKK/GDPR → reports_to: `vizatrack-dir-kvkk-gdpr`
- `vizatrack-lead-audit-trail` — Lead, Audit Trail → reports_to: `vizatrack-dir-audit-trail`
- `vizatrack-lead-onboarding` — Lead, Onboarding → reports_to: `vizatrack-dir-onboarding`
- `vizatrack-lead-support-sla` — Lead, Support SLA → reports_to: `vizatrack-dir-support-sla`
- `vizatrack-lead-nps` — Lead, NPS → reports_to: `vizatrack-dir-nps`
- `vizatrack-lead-seo-content` — Lead, SEO Content → reports_to: `vizatrack-dir-seo-content`
- `vizatrack-lead-paid-acquisition` — Lead, Paid Acquisition → reports_to: `vizatrack-dir-paid-acquisition`
- `vizatrack-lead-partner-channel` — Lead, Partner Channel → reports_to: `vizatrack-dir-partner-channel`
#### SPECIALIST
- `vizatrack-spec-ios` — Specialist, iOS → reports_to: `vizatrack-lead-ios`
- `vizatrack-spec-android` — Specialist, Android → reports_to: `vizatrack-lead-android`
- `vizatrack-spec-cross-platform-ux` — Specialist, Cross-platform UX → reports_to: `vizatrack-lead-cross-platform-ux`
- `vizatrack-spec-ssr-app-router` — Specialist, SSR/App Router → reports_to: `vizatrack-lead-ssr-app-router`
- `vizatrack-spec-case-portal` — Specialist, Case Portal → reports_to: `vizatrack-lead-case-portal`
- `vizatrack-spec-docs` — Specialist, Docs → reports_to: `vizatrack-lead-docs`
- `vizatrack-spec-başvuru-akışı` — Specialist, Başvuru Akışı → reports_to: `vizatrack-lead-başvuru-akışı`
- `vizatrack-spec-doküman-qa` — Specialist, Doküman QA → reports_to: `vizatrack-lead-doküman-qa`
- `vizatrack-spec-ajans-ortaklığı` — Specialist, Ajans Ortaklığı → reports_to: `vizatrack-lead-ajans-ortaklığı`
- `vizatrack-spec-ülke-mevzuatı` — Specialist, Ülke Mevzuatı → reports_to: `vizatrack-lead-ülke-mevzuatı`
- `vizatrack-spec-kvkk-gdpr` — Specialist, KVKK/GDPR → reports_to: `vizatrack-lead-kvkk-gdpr`
- `vizatrack-spec-audit-trail` — Specialist, Audit Trail → reports_to: `vizatrack-lead-audit-trail`
- `vizatrack-spec-onboarding` — Specialist, Onboarding → reports_to: `vizatrack-lead-onboarding`
- `vizatrack-spec-support-sla` — Specialist, Support SLA → reports_to: `vizatrack-lead-support-sla`
- `vizatrack-spec-nps` — Specialist, NPS → reports_to: `vizatrack-lead-nps`
- `vizatrack-spec-seo-content` — Specialist, SEO Content → reports_to: `vizatrack-lead-seo-content`
- `vizatrack-spec-paid-acquisition` — Specialist, Paid Acquisition → reports_to: `vizatrack-lead-paid-acquisition`
- `vizatrack-spec-partner-channel` — Specialist, Partner Channel → reports_to: `vizatrack-lead-partner-channel`
#### ANALYST
- `vizatrack-anl-ios` — Analyst, iOS → reports_to: `vizatrack-lead-ios`
- `vizatrack-anl-android` — Analyst, Android → reports_to: `vizatrack-lead-android`
- `vizatrack-anl-cross-platform-ux` — Analyst, Cross-platform UX → reports_to: `vizatrack-lead-cross-platform-ux`
- `vizatrack-anl-ssr-app-router` — Analyst, SSR/App Router → reports_to: `vizatrack-lead-ssr-app-router`
- `vizatrack-anl-case-portal` — Analyst, Case Portal → reports_to: `vizatrack-lead-case-portal`
- `vizatrack-anl-docs` — Analyst, Docs → reports_to: `vizatrack-lead-docs`
- `vizatrack-anl-başvuru-akışı` — Analyst, Başvuru Akışı → reports_to: `vizatrack-lead-başvuru-akışı`
- `vizatrack-anl-doküman-qa` — Analyst, Doküman QA → reports_to: `vizatrack-lead-doküman-qa`
- `vizatrack-anl-ajans-ortaklığı` — Analyst, Ajans Ortaklığı → reports_to: `vizatrack-lead-ajans-ortaklığı`
- `vizatrack-anl-ülke-mevzuatı` — Analyst, Ülke Mevzuatı → reports_to: `vizatrack-lead-ülke-mevzuatı`
- `vizatrack-anl-kvkk-gdpr` — Analyst, KVKK/GDPR → reports_to: `vizatrack-lead-kvkk-gdpr`
- `vizatrack-anl-audit-trail` — Analyst, Audit Trail → reports_to: `vizatrack-lead-audit-trail`
- `vizatrack-anl-onboarding` — Analyst, Onboarding → reports_to: `vizatrack-lead-onboarding`
- `vizatrack-anl-support-sla` — Analyst, Support SLA → reports_to: `vizatrack-lead-support-sla`
- `vizatrack-anl-nps` — Analyst, NPS → reports_to: `vizatrack-lead-nps`
- `vizatrack-anl-seo-content` — Analyst, SEO Content → reports_to: `vizatrack-lead-seo-content`
- `vizatrack-anl-paid-acquisition` — Analyst, Paid Acquisition → reports_to: `vizatrack-lead-paid-acquisition`
- `vizatrack-anl-partner-channel` — Analyst, Partner Channel → reports_to: `vizatrack-lead-partner-channel`

### Holding Hukuk & Uyum (`hukuk`)
- **C-LEVEL:** 3
- **EVP:** 4
- **DIRECTOR:** 12
- **LEAD:** 12
- **SPECIALIST:** 12
- **ANALYST:** 12
#### C-LEVEL
- `hukuk-clo` — CLO, Holding Hukuk & Uyum → reports_to: `group-ceo`
- `hukuk-cco` — CCO, Holding Hukuk & Uyum → reports_to: `group-ceo`
- `hukuk-dpo` — DPO, Holding Hukuk & Uyum → reports_to: `group-ceo`
#### EVP
- `hukuk-evp-gizlilik` — EVP, Gizlilik → reports_to: `hukuk-ceo`
- `hukuk-evp-lisanslama` — EVP, Lisanslama → reports_to: `hukuk-ceo`
- `hukuk-evp-reklam-politikası` — EVP, Reklam Politikası → reports_to: `hukuk-ceo`
- `hukuk-evp-regülasyon` — EVP, Regülasyon → reports_to: `hukuk-ceo`
#### DIRECTOR
- `hukuk-dir-kvkk` — Director, KVKK → reports_to: `hukuk-evp-gizlilik`
- `hukuk-dir-gdpr` — Director, GDPR → reports_to: `hukuk-evp-gizlilik`
- `hukuk-dir-dpia` — Director, DPIA → reports_to: `hukuk-evp-gizlilik`
- `hukuk-dir-oss-license` — Director, OSS License → reports_to: `hukuk-evp-lisanslama`
- `hukuk-dir-vendor-contracts` — Director, Vendor Contracts → reports_to: `hukuk-evp-lisanslama`
- `hukuk-dir-ip` — Director, IP → reports_to: `hukuk-evp-lisanslama`
- `hukuk-dir-platform-policy` — Director, Platform Policy → reports_to: `hukuk-evp-reklam-politikası`
- `hukuk-dir-claim-review` — Director, Claim Review → reports_to: `hukuk-evp-reklam-politikası`
- `hukuk-dir-crisis` — Director, Crisis → reports_to: `hukuk-evp-reklam-politikası`
- `hukuk-dir-ülke-onayı` — Director, Ülke Onayı → reports_to: `hukuk-evp-regülasyon`
- `hukuk-dir-cross-border-transfer` — Director, Cross-border Transfer → reports_to: `hukuk-evp-regülasyon`
- `hukuk-dir-retention` — Director, Retention → reports_to: `hukuk-evp-regülasyon`
#### LEAD
- `hukuk-lead-kvkk` — Lead, KVKK → reports_to: `hukuk-dir-kvkk`
- `hukuk-lead-gdpr` — Lead, GDPR → reports_to: `hukuk-dir-gdpr`
- `hukuk-lead-dpia` — Lead, DPIA → reports_to: `hukuk-dir-dpia`
- `hukuk-lead-oss-license` — Lead, OSS License → reports_to: `hukuk-dir-oss-license`
- `hukuk-lead-vendor-contracts` — Lead, Vendor Contracts → reports_to: `hukuk-dir-vendor-contracts`
- `hukuk-lead-ip` — Lead, IP → reports_to: `hukuk-dir-ip`
- `hukuk-lead-platform-policy` — Lead, Platform Policy → reports_to: `hukuk-dir-platform-policy`
- `hukuk-lead-claim-review` — Lead, Claim Review → reports_to: `hukuk-dir-claim-review`
- `hukuk-lead-crisis` — Lead, Crisis → reports_to: `hukuk-dir-crisis`
- `hukuk-lead-ülke-onayı` — Lead, Ülke Onayı → reports_to: `hukuk-dir-ülke-onayı`
- `hukuk-lead-cross-border-transfer` — Lead, Cross-border Transfer → reports_to: `hukuk-dir-cross-border-transfer`
- `hukuk-lead-retention` — Lead, Retention → reports_to: `hukuk-dir-retention`
#### SPECIALIST
- `hukuk-spec-kvkk` — Specialist, KVKK → reports_to: `hukuk-lead-kvkk`
- `hukuk-spec-gdpr` — Specialist, GDPR → reports_to: `hukuk-lead-gdpr`
- `hukuk-spec-dpia` — Specialist, DPIA → reports_to: `hukuk-lead-dpia`
- `hukuk-spec-oss-license` — Specialist, OSS License → reports_to: `hukuk-lead-oss-license`
- `hukuk-spec-vendor-contracts` — Specialist, Vendor Contracts → reports_to: `hukuk-lead-vendor-contracts`
- `hukuk-spec-ip` — Specialist, IP → reports_to: `hukuk-lead-ip`
- `hukuk-spec-platform-policy` — Specialist, Platform Policy → reports_to: `hukuk-lead-platform-policy`
- `hukuk-spec-claim-review` — Specialist, Claim Review → reports_to: `hukuk-lead-claim-review`
- `hukuk-spec-crisis` — Specialist, Crisis → reports_to: `hukuk-lead-crisis`
- `hukuk-spec-ülke-onayı` — Specialist, Ülke Onayı → reports_to: `hukuk-lead-ülke-onayı`
- `hukuk-spec-cross-border-transfer` — Specialist, Cross-border Transfer → reports_to: `hukuk-lead-cross-border-transfer`
- `hukuk-spec-retention` — Specialist, Retention → reports_to: `hukuk-lead-retention`
#### ANALYST
- `hukuk-anl-kvkk` — Analyst, KVKK → reports_to: `hukuk-lead-kvkk`
- `hukuk-anl-gdpr` — Analyst, GDPR → reports_to: `hukuk-lead-gdpr`
- `hukuk-anl-dpia` — Analyst, DPIA → reports_to: `hukuk-lead-dpia`
- `hukuk-anl-oss-license` — Analyst, OSS License → reports_to: `hukuk-lead-oss-license`
- `hukuk-anl-vendor-contracts` — Analyst, Vendor Contracts → reports_to: `hukuk-lead-vendor-contracts`
- `hukuk-anl-ip` — Analyst, IP → reports_to: `hukuk-lead-ip`
- `hukuk-anl-platform-policy` — Analyst, Platform Policy → reports_to: `hukuk-lead-platform-policy`
- `hukuk-anl-claim-review` — Analyst, Claim Review → reports_to: `hukuk-lead-claim-review`
- `hukuk-anl-crisis` — Analyst, Crisis → reports_to: `hukuk-lead-crisis`
- `hukuk-anl-ülke-onayı` — Analyst, Ülke Onayı → reports_to: `hukuk-lead-ülke-onayı`
- `hukuk-anl-cross-border-transfer` — Analyst, Cross-border Transfer → reports_to: `hukuk-lead-cross-border-transfer`
- `hukuk-anl-retention` — Analyst, Retention → reports_to: `hukuk-lead-retention`

### Tahmin Uzmanı (`tahmin`)
- **C-LEVEL:** 3
- **EVP:** 3
- **DIRECTOR:** 9
- **LEAD:** 9
- **SPECIALIST:** 9
- **ANALYST:** 9
#### C-LEVEL
- `tahmin-ceo` — CEO, Tahmin Uzmanı → reports_to: `owner`
- `tahmin-cso` — CSO, Tahmin Uzmanı → reports_to: `group-ceo`
- `tahmin-cdo` — CDO, Tahmin Uzmanı → reports_to: `group-ceo`
#### EVP
- `tahmin-evp-forecasting` — EVP, Forecasting → reports_to: `tahmin-ceo`
- `tahmin-evp-araştırma` — EVP, Araştırma → reports_to: `tahmin-ceo`
- `tahmin-evp-teslimat` — EVP, Teslimat → reports_to: `tahmin-ceo`
#### DIRECTOR
- `tahmin-dir-sports-models` — Director, Sports Models → reports_to: `tahmin-evp-forecasting`
- `tahmin-dir-finance-models` — Director, Finance Models → reports_to: `tahmin-evp-forecasting`
- `tahmin-dir-scenario-lab` — Director, Scenario Lab → reports_to: `tahmin-evp-forecasting`
- `tahmin-dir-signal-desk` — Director, Signal Desk → reports_to: `tahmin-evp-araştırma`
- `tahmin-dir-source-qa` — Director, Source QA → reports_to: `tahmin-evp-araştırma`
- `tahmin-dir-archive-loop` — Director, Archive Loop → reports_to: `tahmin-evp-araştırma`
- `tahmin-dir-client-briefs` — Director, Client Briefs → reports_to: `tahmin-evp-teslimat`
- `tahmin-dir-risk-flags` — Director, Risk Flags → reports_to: `tahmin-evp-teslimat`
- `tahmin-dir-retros` — Director, Retros → reports_to: `tahmin-evp-teslimat`
#### LEAD
- `tahmin-lead-sports-models` — Lead, Sports Models → reports_to: `tahmin-dir-sports-models`
- `tahmin-lead-finance-models` — Lead, Finance Models → reports_to: `tahmin-dir-finance-models`
- `tahmin-lead-scenario-lab` — Lead, Scenario Lab → reports_to: `tahmin-dir-scenario-lab`
- `tahmin-lead-signal-desk` — Lead, Signal Desk → reports_to: `tahmin-dir-signal-desk`
- `tahmin-lead-source-qa` — Lead, Source QA → reports_to: `tahmin-dir-source-qa`
- `tahmin-lead-archive-loop` — Lead, Archive Loop → reports_to: `tahmin-dir-archive-loop`
- `tahmin-lead-client-briefs` — Lead, Client Briefs → reports_to: `tahmin-dir-client-briefs`
- `tahmin-lead-risk-flags` — Lead, Risk Flags → reports_to: `tahmin-dir-risk-flags`
- `tahmin-lead-retros` — Lead, Retros → reports_to: `tahmin-dir-retros`
#### SPECIALIST
- `tahmin-spec-sports-models` — Specialist, Sports Models → reports_to: `tahmin-lead-sports-models`
- `tahmin-spec-finance-models` — Specialist, Finance Models → reports_to: `tahmin-lead-finance-models`
- `tahmin-spec-scenario-lab` — Specialist, Scenario Lab → reports_to: `tahmin-lead-scenario-lab`
- `tahmin-spec-signal-desk` — Specialist, Signal Desk → reports_to: `tahmin-lead-signal-desk`
- `tahmin-spec-source-qa` — Specialist, Source QA → reports_to: `tahmin-lead-source-qa`
- `tahmin-spec-archive-loop` — Specialist, Archive Loop → reports_to: `tahmin-lead-archive-loop`
- `tahmin-spec-client-briefs` — Specialist, Client Briefs → reports_to: `tahmin-lead-client-briefs`
- `tahmin-spec-risk-flags` — Specialist, Risk Flags → reports_to: `tahmin-lead-risk-flags`
- `tahmin-spec-retros` — Specialist, Retros → reports_to: `tahmin-lead-retros`
#### ANALYST
- `tahmin-anl-sports-models` — Analyst, Sports Models → reports_to: `tahmin-lead-sports-models`
- `tahmin-anl-finance-models` — Analyst, Finance Models → reports_to: `tahmin-lead-finance-models`
- `tahmin-anl-scenario-lab` — Analyst, Scenario Lab → reports_to: `tahmin-lead-scenario-lab`
- `tahmin-anl-signal-desk` — Analyst, Signal Desk → reports_to: `tahmin-lead-signal-desk`
- `tahmin-anl-source-qa` — Analyst, Source QA → reports_to: `tahmin-lead-source-qa`
- `tahmin-anl-archive-loop` — Analyst, Archive Loop → reports_to: `tahmin-lead-archive-loop`
- `tahmin-anl-client-briefs` — Analyst, Client Briefs → reports_to: `tahmin-lead-client-briefs`
- `tahmin-anl-risk-flags` — Analyst, Risk Flags → reports_to: `tahmin-lead-risk-flags`
- `tahmin-anl-retros` — Analyst, Retros → reports_to: `tahmin-lead-retros`

### Movéa (M-AIOS) (`movea`)
- **C-LEVEL:** 3
- **EVP:** 3
- **DIRECTOR:** 9
- **LEAD:** 9
- **SPECIALIST:** 9
- **ANALYST:** 9
#### C-LEVEL
- `movea-ceo` — CEO, Movéa (M-AIOS) → reports_to: `owner`
- `movea-cmo` — CMO, Movéa (M-AIOS) → reports_to: `group-ceo`
- `movea-coo` — COO, Movéa (M-AIOS) → reports_to: `group-ceo`
#### EVP
- `movea-evp-marka` — EVP, Marka → reports_to: `movea-coo`
- `movea-evp-e-ticaret` — EVP, E-ticaret → reports_to: `movea-coo`
- `movea-evp-operasyon` — EVP, Operasyon → reports_to: `movea-coo`
#### DIRECTOR
- `movea-dir-positioning` — Director, Positioning → reports_to: `movea-evp-marka`
- `movea-dir-creative-system` — Director, Creative System → reports_to: `movea-evp-marka`
- `movea-dir-community` — Director, Community → reports_to: `movea-evp-marka`
- `movea-dir-pdp` — Director, PDP → reports_to: `movea-evp-e-ticaret`
- `movea-dir-checkout` — Director, Checkout → reports_to: `movea-evp-e-ticaret`
- `movea-dir-crm` — Director, CRM → reports_to: `movea-evp-e-ticaret`
- `movea-dir-inventory` — Director, Inventory → reports_to: `movea-evp-operasyon`
- `movea-dir-fulfillment` — Director, Fulfillment → reports_to: `movea-evp-operasyon`
- `movea-dir-cx` — Director, CX → reports_to: `movea-evp-operasyon`
#### LEAD
- `movea-lead-positioning` — Lead, Positioning → reports_to: `movea-dir-positioning`
- `movea-lead-creative-system` — Lead, Creative System → reports_to: `movea-dir-creative-system`
- `movea-lead-community` — Lead, Community → reports_to: `movea-dir-community`
- `movea-lead-pdp` — Lead, PDP → reports_to: `movea-dir-pdp`
- `movea-lead-checkout` — Lead, Checkout → reports_to: `movea-dir-checkout`
- `movea-lead-crm` — Lead, CRM → reports_to: `movea-dir-crm`
- `movea-lead-inventory` — Lead, Inventory → reports_to: `movea-dir-inventory`
- `movea-lead-fulfillment` — Lead, Fulfillment → reports_to: `movea-dir-fulfillment`
- `movea-lead-cx` — Lead, CX → reports_to: `movea-dir-cx`
#### SPECIALIST
- `movea-spec-positioning` — Specialist, Positioning → reports_to: `movea-lead-positioning`
- `movea-spec-creative-system` — Specialist, Creative System → reports_to: `movea-lead-creative-system`
- `movea-spec-community` — Specialist, Community → reports_to: `movea-lead-community`
- `movea-spec-pdp` — Specialist, PDP → reports_to: `movea-lead-pdp`
- `movea-spec-checkout` — Specialist, Checkout → reports_to: `movea-lead-checkout`
- `movea-spec-crm` — Specialist, CRM → reports_to: `movea-lead-crm`
- `movea-spec-inventory` — Specialist, Inventory → reports_to: `movea-lead-inventory`
- `movea-spec-fulfillment` — Specialist, Fulfillment → reports_to: `movea-lead-fulfillment`
- `movea-spec-cx` — Specialist, CX → reports_to: `movea-lead-cx`
#### ANALYST
- `movea-anl-positioning` — Analyst, Positioning → reports_to: `movea-lead-positioning`
- `movea-anl-creative-system` — Analyst, Creative System → reports_to: `movea-lead-creative-system`
- `movea-anl-community` — Analyst, Community → reports_to: `movea-lead-community`
- `movea-anl-pdp` — Analyst, PDP → reports_to: `movea-lead-pdp`
- `movea-anl-checkout` — Analyst, Checkout → reports_to: `movea-lead-checkout`
- `movea-anl-crm` — Analyst, CRM → reports_to: `movea-lead-crm`
- `movea-anl-inventory` — Analyst, Inventory → reports_to: `movea-lead-inventory`
- `movea-anl-fulfillment` — Analyst, Fulfillment → reports_to: `movea-lead-fulfillment`
- `movea-anl-cx` — Analyst, CX → reports_to: `movea-lead-cx`

### Çiğköftem (`cigkoftem`)
- **C-LEVEL:** 3
- **EVP:** 3
- **DIRECTOR:** 9
- **LEAD:** 9
- **SPECIALIST:** 9
- **ANALYST:** 9
#### C-LEVEL
- `cigkoftem-ceo` — CEO, Çiğköftem → reports_to: `owner`
- `cigkoftem-cmo` — CMO, Çiğköftem → reports_to: `group-ceo`
- `cigkoftem-coo` — COO, Çiğköftem → reports_to: `group-ceo`
#### EVP
- `cigkoftem-evp-menü-içerik` — EVP, Menü & İçerik → reports_to: `cigkoftem-coo`
- `cigkoftem-evp-sipariş` — EVP, Sipariş → reports_to: `cigkoftem-coo`
- `cigkoftem-evp-yerel-pazarlama` — EVP, Yerel Pazarlama → reports_to: `cigkoftem-coo`
#### DIRECTOR
- `cigkoftem-dir-recipe-cms` — Director, Recipe CMS → reports_to: `cigkoftem-evp-menü-içerik`
- `cigkoftem-dir-local-seo` — Director, Local SEO → reports_to: `cigkoftem-evp-menü-içerik`
- `cigkoftem-dir-campaign` — Director, Campaign → reports_to: `cigkoftem-evp-menü-içerik`
- `cigkoftem-dir-web-order` — Director, Web Order → reports_to: `cigkoftem-evp-sipariş`
- `cigkoftem-dir-franchise-ops` — Director, Franchise Ops → reports_to: `cigkoftem-evp-sipariş`
- `cigkoftem-dir-cx` — Director, CX → reports_to: `cigkoftem-evp-sipariş`
- `cigkoftem-dir-maps-seo` — Director, Maps/SEO → reports_to: `cigkoftem-evp-yerel-pazarlama`
- `cigkoftem-dir-social-local` — Director, Social Local → reports_to: `cigkoftem-evp-yerel-pazarlama`
- `cigkoftem-dir-promo` — Director, Promo → reports_to: `cigkoftem-evp-yerel-pazarlama`
#### LEAD
- `cigkoftem-lead-recipe-cms` — Lead, Recipe CMS → reports_to: `cigkoftem-dir-recipe-cms`
- `cigkoftem-lead-local-seo` — Lead, Local SEO → reports_to: `cigkoftem-dir-local-seo`
- `cigkoftem-lead-campaign` — Lead, Campaign → reports_to: `cigkoftem-dir-campaign`
- `cigkoftem-lead-web-order` — Lead, Web Order → reports_to: `cigkoftem-dir-web-order`
- `cigkoftem-lead-franchise-ops` — Lead, Franchise Ops → reports_to: `cigkoftem-dir-franchise-ops`
- `cigkoftem-lead-cx` — Lead, CX → reports_to: `cigkoftem-dir-cx`
- `cigkoftem-lead-maps-seo` — Lead, Maps/SEO → reports_to: `cigkoftem-dir-maps-seo`
- `cigkoftem-lead-social-local` — Lead, Social Local → reports_to: `cigkoftem-dir-social-local`
- `cigkoftem-lead-promo` — Lead, Promo → reports_to: `cigkoftem-dir-promo`
#### SPECIALIST
- `cigkoftem-spec-recipe-cms` — Specialist, Recipe CMS → reports_to: `cigkoftem-lead-recipe-cms`
- `cigkoftem-spec-local-seo` — Specialist, Local SEO → reports_to: `cigkoftem-lead-local-seo`
- `cigkoftem-spec-campaign` — Specialist, Campaign → reports_to: `cigkoftem-lead-campaign`
- `cigkoftem-spec-web-order` — Specialist, Web Order → reports_to: `cigkoftem-lead-web-order`
- `cigkoftem-spec-franchise-ops` — Specialist, Franchise Ops → reports_to: `cigkoftem-lead-franchise-ops`
- `cigkoftem-spec-cx` — Specialist, CX → reports_to: `cigkoftem-lead-cx`
- `cigkoftem-spec-maps-seo` — Specialist, Maps/SEO → reports_to: `cigkoftem-lead-maps-seo`
- `cigkoftem-spec-social-local` — Specialist, Social Local → reports_to: `cigkoftem-lead-social-local`
- `cigkoftem-spec-promo` — Specialist, Promo → reports_to: `cigkoftem-lead-promo`
#### ANALYST
- `cigkoftem-anl-recipe-cms` — Analyst, Recipe CMS → reports_to: `cigkoftem-lead-recipe-cms`
- `cigkoftem-anl-local-seo` — Analyst, Local SEO → reports_to: `cigkoftem-lead-local-seo`
- `cigkoftem-anl-campaign` — Analyst, Campaign → reports_to: `cigkoftem-lead-campaign`
- `cigkoftem-anl-web-order` — Analyst, Web Order → reports_to: `cigkoftem-lead-web-order`
- `cigkoftem-anl-franchise-ops` — Analyst, Franchise Ops → reports_to: `cigkoftem-lead-franchise-ops`
- `cigkoftem-anl-cx` — Analyst, CX → reports_to: `cigkoftem-lead-cx`
- `cigkoftem-anl-maps-seo` — Analyst, Maps/SEO → reports_to: `cigkoftem-lead-maps-seo`
- `cigkoftem-anl-social-local` — Analyst, Social Local → reports_to: `cigkoftem-lead-social-local`
- `cigkoftem-anl-promo` — Analyst, Promo → reports_to: `cigkoftem-lead-promo`

## Doğrulama
- Bu dosyada listelenen roller: **633** (beklenen 633)
- JOB_CARDS mevcut: **43** · kalan skeleton backlog fazlı
- Security `ORG/ROLES/` ayrı track — üzerine yazılmaz

## RACI notu
Her title için tek **A** (Accountable) iş kartında — Faz 4 derinliği. Skeleton kartlarda placeholder.
