# HOLDING MİMARİSİ — metinduraktr-44 Portföyü
> Üretim: 2026-07-17 · Kapsam: 7 repo tek çatı (holding) altında iş birimi olarak · Yönetim: claude-otonom-sistem = Holding HQ / işletim sistemi
> İlke: her iş birimi kendi alanında bağımsız yürür; holding ortak standart + gözetim + sermaye/değer akışı sağlar. Sinyal > uzunluk.

## 0. NEDEN HOLDING
7 repo dağınık değil; iki tür varlık taşıyor: (a) **AI ajans dikeyleri** (hizmet + gelir motoru), (b) **ürün/marka varlıkları**. Bir holding çatısı: ortak güvenlik/kalite standardı, çapraz-öğrenme (bilgi tabanı), tek gözetim ritmi ve gelir modeli tutarlılığı sağlar.

## 1. HOLDING KURULU (tüm birimlerin üstünde)
| Rol | Sorumluluk | Karşılık |
|---|---|---|
| Sahip / Chairman | Metin Durak — nihai onay: sermaye, faz kapıları, birim aç/kapa | — |
| Group CEO | Portföy stratejisi, birimler arası tahsis | adops `ceo-orchestrator` deseni holding'e terfi |
| Group COO | Operasyon ritmi (gözetim, standup, kurul) | CILT6 operasyon ritmi |
| Group CTO | Ortak teknik standart (CI, doğrulama, MCP, güvenlik) | claude-otonom-sistem/scripts + CILT8 |
| Group CFO | API bütçesi + birim gelir konsolidasyonu | GELIR_MOTORU.md |
| Group CCO | 5 güvenlik kuralı + lisans/uyum tüm repolarda | CILT1 + CILT8 |

## 2. İŞ BİRİMLERİ (7 repo)
| Birim | Repo | Tür | Alan | Durum |
|---|---|---|---|---|
| **Holding HQ / OS** | claude-otonom-sistem | işletim sistemi | Ortak standart, gözetim, jeneratörler | Aktif (umbrella) |
| **AdOps Agency** | adops-agents | AI ajans (hizmet+gelir) | Performans pazarlama & programatik | Aktif — 600 ajan, 5 gelir kanalı |
| **Tahmin Uzmanı** | a-agency-tahmin-uzman- | AI ajans | Spor/finans/danışmanlık forecast | Aktif |
| **Performer** | performer-growth-hub | ajans + web sitesi | Uygulama büyüme / app growth | Aktif (marka sitesi) |
| **Movéa (M-AIOS)** | or-na.com | ürün/marka OS | Premium medikal scrubs DTC | Aktif |
| **VizaTrack** | VizaTrack | ürün (iOS/Android/Web) | Göç & relokasyon platformu | Aktif |
| **Çiğköftem** | cigkoftem-web-app | ürün | Gıda markası web app | Aktif |

Segmentasyon: **Ajans dikeyleri** (AdOps, Tahmin, Performer) gelir motoru; **ürün/markalar** (Movéa, VizaTrack, Çiğköftem) portföy varlığı; **HQ** hepsini yönetir.

## 3. ORTAK HİZMETLER (holding → tüm birimler)
- **Güvenlik & Kalite:** 5 kural + 6-katman doğrulama (CILT1/CILT8) · SECURITY/COC/şablonlar her repoda.
- **Bilgi Zinciri:** her birim kendi BILGI_TABANI + AUDIT_LOG; holding çapraz-öğrenimi HQ'da toplar.
- **Standardizasyon Motoru:** scripts/standardize_repo.py (yeni birim = 1 komutla standarda gelir).
- **Rol-Model Kütüphanesi:** disiplin başına dünya top isimleri (adops-agents/data/rol_modelleri.json + docs/ROL-MODELLERI.md) — ajans birimleri ortak kullanır.
- **Soru Bankası:** 501 öz-denetim sorusu (adops-agents/docs/OZ-DENETIM-SORU-BANKASI.md) — her ajan birimine uygulanabilir.
- **Gelir Modeli:** 5 kanal deseni (sponsorluk/placement/referral/premium/inbound) ajans birimlerine ortak.

## 4. YÖNETİŞİM RİTMİ (holding düzeyi)
- **Günlük:** her birim kendi standup'ını üretir; HQ günlük gözetim görevi (Cowork) durumları toplar.
- **Haftalık:** Group liderlik sync — birim EVP/CEO'ları; portföy önceliği.
- **Aylık:** Holding kurulu — birim OKR skorları, faz kapıları, sermaye tahsisi.
- **repo-health.yml:** her gün tüm repoların community-health matrisini üretir (sapma görünür).

## 5. DEĞER / SERMAYE AKIŞI
- Ajans dikeyleri (AdOps/Tahmin/Performer) → gelir → HQ (API bütçesi + reinvest).
- Ürün/markalar (Movéa/VizaTrack/Çiğköftem) → kendi gelir modelleri; HQ ortak altyapı + pazarlama desteği verir (AdOps birimi iç müşteri olarak markalara hizmet edebilir — çapraz-sinerji).
- 🚩 Sermaye/gelir taahhütleri sahip onayına tabidir (CILT1).

## 6. GENİŞLEME
Yeni repo/birim eklenince: (1) standardize_repo.py ile community-health, (2) tür ata (ajans/ürün/OS), (3) bu tabloya satır, (4) uygunsa org jeneratörü (ajanssa 600-kart deseni), (5) HOLDING kuruluna bağla. Org değişikliği yalnız jeneratör üzerinden (tek doğruluk kaynağı).
