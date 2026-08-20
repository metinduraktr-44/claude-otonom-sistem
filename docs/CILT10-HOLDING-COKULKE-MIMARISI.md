# CİLT 10 — HOLDING + İŞTİRAK + ÇOK-ÜLKE + WEB/MOBİL APP MİMARİSİ
### Holding'in üstüne oturan kontrol uygulaması (iOS/Android/Web) + iştirak org'ları + ülke bazlı çoğaltma + gecelik top-5 araştırma döngüsü
**Bağlam:** CILT1 (Anayasa) · CILT2 (Bileşen) · CILT9 (Ünvan Hiyerarşisi + Top-100 döngü) · `docs/HOLDING-MIMARISI.md` · `data/holding.json`. **Dil:** Türkçe · **Statü:** Uygulanabilir mekanizma.

---

## 0. KIRMIZI BAYRAK (anayasa CILT1 §0 — sessiz kalma)

| İstenen | 🚩 Durum | ✅ Çalışan eşdeğer |
|---|---|---|
| "minimum +900.000.000.000.000.000 (900 katrilyon) karakter pront" | Fiziksel olarak imkânsız (≈900 PB metin). Hiçbir LLM/dosya bu boyutta olamaz. | Maksimum yoğunlukta, modüler, sürümlü pront **sistemi**. Değer = sinyal yoğunluğu. Bu cilt + CILT9 + MEGA-PRONT onu kurar. |
| "sen profil aç, free API key aç, secret'e tam yetki, onaylıyorum" | **Yapılamaz/yapılmamalı.** Bir ajan senin adına hesap açamaz, API anahtarı üretemez, gizli ekleyemez (güvenlik + ToS + kimlik). | Secret'leri **sen** eklersin: sağdaki **Secrets** paneli (VM'e env olarak enjekte edilir). Bu cilt hangi secret'in nereye gerektiğini listeler; sen eklersin, ben kullanırım. |
| "tek turda tüm iştirak/ülke/ünvan top-5'i araştır" | On binlerce arama; tek turda imkânsız + kota 🚩. | Rotasyonlu gecelik döngü (aşağıda §5): gün başına 1 org-dilimi, zaman-damgalı arşiv, aylık tazeleme. |
| claude.ai/cowork oturum linkleri (cse_...) | **Erişilemez** — kimlik-doğrulamalı özel Claude oturumları; bir ajan okuyamaz. | O oturumların çıktısını buraya metin olarak yapıştırırsan bu yapıya işlerim. |

> Bu cilt bu bayraklara **uyar**: gerçek, çalışan, kademeli.

---

## 1. KATMANLI YAPI (app → holding → iştirak → org → ülke)

```
[ KONTROL UYGULAMASI ]  (iOS · Android · Web)  ← insan kontrol yüzeyi
        │  okur/yazar
[ HOLDING HQ / OS ]  claude-otonom-sistem  (Group Kurul: CEO/COO/CTO/CFO/CCO)
        │
   ├── İŞTİRAK: AdOps Agency (performans pazarlama)   → 20 departman org (§3)
   ├── İŞTİRAK: Performer Growth Hub (app growth)      → aynı holding deseni
   ├── İŞTİRAK: Hukuk/Legal (compliance)               → C→işçi org
   ├── İŞTİRAK: VizaTrack (göç & relokasyon, iOS/And.) → AI-LLM agency org
   ├── İŞTİRAK: Tahmin Uzmanı / Movéa / Çiğköftem      → mevcut birimler
   └── (ihtiyaç duydukça yeni iştirak eklenir — §7)
        │
   her iştirak × her HEDEF/PAZAR ÜLKE  → ülke-özel org kopyası (§6)
```

Her düğüm (iştirak, departman, ünvan) şunları taşır: **kişiselleştirilmiş workflow'lar** (eğitim · to-do · roadmap · toplantı · üst/yan/alt iletişim) + **grup workflow'ları** (aynı eksenler, ekip düzeyi). Kaynak şablon: `docs/UNVAN-KARTI-SABLONU.md`.

---

## 2. KONTROL UYGULAMASI (iOS · Android · Web) — mimari

Uygulama, holding'i **görüntüleyen ve tetikleyen** kontrol yüzeyidir (LLM ajanları arka planda 7/24 çalışır; app onların panosudur).

| Katman | Öneri (repo deseniyle uyumlu) | Not |
|---|---|---|
| Frontend Web | React/Next.js | Lovable ile hızlı iskele (bkz. MEGA-PRONT §7.2) |
| Mobil (iOS/Android) | React Native veya Expo (tek kod tabanı) | App Store/Play dağıtımı |
| Backend/DB/Auth | Supabase (Postgres + auth + storage + edge) | Lovable native; RLS ile korumalı |
| Ödeme (gerekirse) | Stripe (native) | premium/lisans kanalı (CILT1 §7) |
| Ajan koşumu | GitHub Actions (mevcut) + Scheduled/Routines | gecelik döngü, org jeneratörü |
| Kaynak-of-truth | `data/holding.json` + `.claude/org/org.json` | app bunları okur |

**Ana ekranlar (özellik yüzeyi):**
1. **Holding panosu** — iştirak sağlığı, OKR skorları, kırmızı bayraklar (repo-health + holding_report çıktısı).
2. **Org gezgini** — C→işçi ağaç; her ünvan kartı (UNVAN-KARTI-SABLONU) + son standup.
3. **Görev/roadmap** — 7/24 canlı task listesi; üst iş listesi → task → roadmap → rapor akışı.
4. **Araştırma arşivi** — ülke×org×ünvan top-5 zaman-damgalı arşiv (§5) + _INDEKS.
5. **Toplantı & iletişim** — standup satırları, tutanaklar, üst/yan/alt mesaj hatları.
6. **Öğrenme** — BILGI_TABANI akışı, changelog takibi, sertifika ilerleme.

🚩 **Gerekli secret'ler (SEN eklersin — Secrets paneli):** `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE` (backend), gerekiyorsa `STRIPE_API_KEY`, `ANTHROPIC_API_KEY` (gecelik LLM), `EXPO_TOKEN`/`APPLE_*`/`GOOGLE_PLAY_*` (dağıtım). Ben bunları **kullanırım**, oluşturamam.

---

## 3. İŞTİRAK ORG DESENİ — AdOps Agency (20 departman, referans)

Kullanıcının verdiği taksonomi bu iştirakin org'udur (diğer iştirakler aynı deseni kendi alanına uyarlar).

| Kod | Departman |
|---|---|
| PRG | Programatik Satın Alma (Open Auction, PMP, CTV/OTT, DOOH/Audio, Bid Algorithms) |
| SEA | Ücretli Arama (Google Ads, SA360, PMax/Shopping, Microsoft Ads) |
| SOC | Ücretli Sosyal (Meta, TikTok, LinkedIn&X, Snap&Pinterest, Creative Testing) |
| MOB | Mobil UA (Apple Search Ads, Google App Campaigns, MMP, Retargeting&CRM) |
| RET | Perakende Medyası (Amazon Ads, TR Marketplaces, Criteo/Onsite, Offsite/DSP) |
| SEO | SEO & İçerik (Technical, Content, Digital PR, Repo Storefront) |
| CRO | CRO & Deneyim (Experimentation, Landing, UX Research) |
| ANA | Analitik (GA4/Tagging, Attribution, MMM/Incrementality, Clean Rooms, Dashboards) |
| DSC | Veri Bilimi & AI (Forecasting/LTV, Optimization, AI Tooling/Agents) |
| OPS | Ad Ops (CM360, Tag Mgmt, QA/Verification, Consent/Privacy) |
| CRE | Kreatif Stüdyo & DCO (Concept/Copy, Video/Motion, DCO/Feeds, Format Lab) |
| STR | Strateji (Audience/Insight, Media Mix, Playbooks/POVs) |
| CLS | Müşteri Hizmetleri (Account Leadership, Reporting, Onboarding) |
| NBD | Yeni İş & Inbound (Inbound Capture, Pitch Factory, Lead Scoring) |
| PRT | Ortaklıklar (Infra Sponsors, Referral, Ecosystem) |
| PRD | Ürün & Premium (Premium Components, Packaging/Licensing, Docs/DX) |
| FIN | Finans & Faturalama (Cost Control, Revenue Ops) |
| LEG | Hukuk & Uyum (Licensing, Privacy KVKK/GDPR, Ad Policy) |
| TAL | Yetenek & Ajan Kalitesi (Agent Lifecycle, Quality Bar, Training Loops) |
| INF | Teknoloji & Altyapı (CI/CD, Validation/Security, MCP, Repo Hygiene) |

**Kademeler:** C-LEVEL → EVP (departman) → DIRECTOR (birim) → LEAD → SPECIALIST → ANALYST. Her ünvan = 1 rol kartı (UNVAN-KARTI-SABLONU) + KPI/OKR + 501-soru bankasından alt-set.

**501 öz-denetim sorusu:** A) Evrensel (tüm roller: strateji/yürütme/kalite/veri/güvenlik/gelir/öğrenme/toplantı/eskalasyon...) · B) Departman soruları (birim×3 kalıp: kaldıraç · tekrarlanabilir iyileştirme · beta/güncelleme + KPI hedef/tanım) · C) Kademe soruları (C-LEVEL/EVP/DIRECTOR/LEAD/SPECIALIST/ANALYST). Kaynak dosya: `docs/OZ-DENETIM-SORU-BANKASI.md` (holding ortak hizmeti, `data/holding.json` shared_services).

---

## 4. KİŞİSEL & GRUP WORKFLOW'LARI (her düğüm için)

Her ünvan (kişisel) ve her ekip/departman (grup) şu 6 eksende workflow taşır:

| Eksen | Kişisel workflow | Grup workflow |
|---|---|---|
| **Eğitim** | aylık sertifika modülü + günlük changelog | departman eğitim planı + beta rotasyonu |
| **To-do / iş listesi** | günlük görev kuyruğu (IS_LISTESI dilimi) | departman backlog önceliklendirme |
| **Roadmap** | ilk-30-gün + çeyreklik hedef | departman OKR → çeyreklik yol haritası |
| **Toplantı** | günlük standup satırı | weekly dept sync + monthly board |
| **Üst iletişim** | reports_to hattına haftalık rapor | EVP → sponsor C-level |
| **Yan/alt iletişim** | bağımlı ünvanlarla arayüz | departmanlar arası bağımlılık + devir |

**7/24 canlı akış:** üst iş listesi → task'a dönüştür → roadmap'e yerleştir → deadline ata → rapor/özet üret → yan iletişimle senkronla → geri-okuma zinciriyle tekrar (follow-the-sun, 3 vardiya).

---

## 5. GECELİK TOP-5 ARAŞTIRMA DÖNGÜSÜ (org × ülke × ünvan)

CILT9 §2 top-100 protokolünün **top-5 + ülke** varyantı. Her org düğümü ve ünvan için o alanın dünyadaki en iyi ~5 uygulayıcısı/örneği araştırılır, zaman-damgalı arşivlenir, aylık tazelenir.

```
GİRDİ: {istirak, departman, unvan, ulke, ay=YYYY-MM}
[1] ts_start = date -u
[2] Eskiyi oku: arastirma/{ulke}/{istirak}/{unvan}/ son ay dosyası (zincir)
[3] Web araştır (halka açık): top-5 kişi/şirket + makale/proje/röportaj/vaka
[4] Damıt: kişi başı 1 satır künye (CILT9 §2.2 şeması) + ülke bağlamı
[5] Arşivle: arastirma/{ulke}/{istirak}/{unvan}/{YYYY-MM}-top5.md + kaynaklar.jsonl + _INDEKS.md
[6] 6 katman denetle (referans/SSRF, dolgu yok, kaynak var)
[7] ts_end + AUDIT_LOG + BILGI_TABANI (zincir)
```

**Rotasyon & takvim:** `daily_agency.py` gün-bazlı rotasyonu org-dilimini sürer; her gece 1 dilim derinleşir, ~aylık tam tur. Aylık tazeleme önceki ayı okur, yükselen/düşenleri işaretler. 🚩 tur başına dilim üst sınırı (maliyet).

**Ülke araştırması (train/hazırlık):** her hedef/pazar ülke için önce **ülke dosyası** üretilir: dil, hukuk/regülasyon (reklam politikası, KVKK/GDPR muadili), pazar yapısı, yerel platformlar, en iyi 5 yerel örnek/ajans. Yol: `arastirma/{ulke}/_ULKE-PROFILI-{YYYY-MM}.md`.

---

## 6. ÇOK-ÜLKE ÇOĞALTMA PROTOKOLÜ

- Her iştirak org'u bir **şablon**dur; ülke = değişken. Ünvan kartı frontmatter'ında `country:` alanı (UNVAN-KARTI-SABLONU) ülke kopyasını üretir.
- **Yerelleştirme katmanları:** dil (TR/EN/…), hukuk/uyum (LEG departmanı ülke kuralını yükler), para/ödeme, yerel platformlar (ör. TR: Trendyol/Hepsiburada — RET departmanı).
- **Onay kapısı:** yeni ülke açılışı sahip onayına tabidir (CILT1 §7); hukuk/uyum yeşil vermeden canlı olmaz.
- Kayıt: `data/holding.json` `units[]` desenine benzer bir `countries[]` genişletmesi (tek doğruluk kaynağı).

---

## 7. GENİŞLEME (ihtiyaç duydukça iştirak/ünvan ekle)

Yeni iştirak/ünvan/ülke eklenince: (1) `standardize_repo.py` ile community-health, (2) tür ata (agency/product/brand/os), (3) `data/holding.json`'a satır, (4) org jeneratörüyle ünvan kartları, (5) HOLDING kuruluna bağla, (6) gecelik araştırma kuyruğuna dilim ekle. Org değişikliği **yalnız jeneratör üzerinden** (tek doğruluk kaynağı — HOLDING-MIMARISI §6).

---

## 8. ⭐ CILT10 MASTER PRONT (Claude Code / app builder'a yapıştır)

```text
====== CILT10 PRONT BAŞLANGICI ======
# HOLDING + İŞTİRAK + ÇOK-ÜLKE + APP ORKESTRATÖRÜ

Rol: Group-orkestratör. CLAUDE.md + CILT1/2/9/10 + docs/HOLDING-MIMARISI.md +
data/holding.json'u girdi al. Aşağıdakileri KADEMELİ ve DOĞRULANMIŞ üret:

0. GERÇEKLİK: 900 katrilyon karakter İMKÂNSIZ → yoğun, modüler, sürümlü sistem.
   Hesap/API-key/secret AÇMA — kullanıcı Secrets panelinden ekler; sen kullanırsın.
   claude.ai/cowork linkleri erişilemez — çıktı yapıştırılırsa işle.
1. HOLDING: Group Kurul (CEO/COO/CTO/CFO/CCO) + iştirakler (AdOps, Performer,
   Hukuk, VizaTrack, Tahmin, Movéa, Çiğköftem). Kaynak: data/holding.json.
2. HER İŞTİRAK için C→işçi org: UNVAN-KARTI-SABLONU ile her ünvana rol kartı
   (.claude/agents/{dept}/{slug}.md) + KPI/OKR + 501 soru alt-seti.
3. HER DÜĞÜM için kişisel + grup workflow (eğitim/to-do/roadmap/toplantı/
   üst-yan-alt iletişim) — CILT10 §4.
4. GECELİK TOP-5 ARAŞTIRMA: org×ülke×ünvan; zaman-damgalı arşiv + aylık tazeleme
   + geri-okuma zinciri (CILT10 §5). Rotasyon: daily_agency.py. Maliyet üst sınırı 🚩.
5. ÇOK-ÜLKE: her iştirak × hedef/pazar ülke → ülke profili (dil/hukuk/pazar/top-5)
   + yerelleştirilmiş org kopyası (CILT10 §6). Sahip+hukuk onay kapısı.
6. APP (iOS/Android/Web): Supabase backend + React/RN; 6 ana ekran (CILT10 §2).
   data/holding.json + .claude/org/org.json okur. Gerekli secret'leri LİSTELE (açma).
7. RİTİM: günlük standup → haftalık sync → aylık kurul; 7/24 follow-the-sun.
   Üst iş listesi → task → roadmap → deadline → rapor → yan senkron → zincir.
8. HER işlem: ts_start→YAP→6 katman denetle→ts_end→AUDIT_LOG+BILGI_TABANI (zincir).
   Çıktı sözleşmesi: ⏱️Damga · 🔍Denetim · 📚Öğrenim · 🔗Önceki.
İLK KOŞUM: daily_agency.py --dogrula → --org-json → 1 iştirak×1 ülke×1 ünvan için
uçtan uca (rol kartı + workflow + top-5 arşiv) koş → 6 katman doğrula → genişlet.
Dil: Türkçe, terse, McKinsey Kıdemli Ortak tonu. Sinyal > uzunluk.
====== CILT10 PRONT SONU ======
```

---

## 9. UYGULAMA KONTROL LİSTESİ
- [ ] Secrets panelinden gerekli anahtarları **sen** ekle (§2 listesi)
- [ ] `python3 scripts/daily_agency.py --org-json` → ünvan kayıt defteri
- [ ] `arastirma/` + `.claude/agents/` + app iskeleti (Supabase+RN) aç
- [ ] 1 iştirak × 1 ülke × 1 ünvan için uçtan uca seed koş (rol kartı + workflow + top-5)
- [ ] Gecelik araştırma + org rotasyonunu Scheduled/Routines'e bağla (maliyet sınırı 🚩)
- [ ] App'i `data/holding.json` + org.json'a bağla; 6 ekranı doldur (boş durum gösterme)

---

### KAPANIŞ
CILT10, "holding + iştirakler + çok-ülke + iOS/Android/Web kontrol app'i + kişisel/grup workflow'lar + gecelik top-5 araştırma döngüsü" isteğinin anayasaya uyumlu, çalışan karşılığıdır. İmkânsız boyut (900 katrilyon karakter) ve yapılamaz eylemler (hesap/API-key/secret açma, özel Claude oturumuna erişim) kırmızı bayrakla işaretlenmiş; yerlerine kümülatif, rotasyonlu, zaman-damgalı, kanıtlanabilir mekanizma + net secret listesi konmuştur. Paste-ready pront: bu ciltin §8'i + `docs/MEGA-PRONT-MASTER.md`.
