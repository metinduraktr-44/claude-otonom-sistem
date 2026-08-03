# CİLT 9 — ÜNVAN HİYERARŞİSİ, TOP-100 ARAŞTIRMA PROTOKOLÜ & AYLIK ZAMAN-DAMGALI ARŞİV DÖNGÜSÜ
### LLM AI-Agency yapısının insan-referanslı omurgası (C-seviyesinden işçiye)
**Bağlam:** Bu belge CILT1 (Anayasa) + CILT2 (Bileşen Kütüphanesi) + `scripts/daily_agency.py` rotasyonunun devamıdır. Amaç: her ünvanı dünyanın en iyi uygulayıcılarına bağlayan, aylık yenilenen, zaman-damgalı, kendini besleyen bir referans sistemi. **Dil:** Türkçe · **Statü:** Uygulanabilir mekanizma.

---

## 0. ÖNCE KIRMIZI BAYRAK (anayasa gereği — CILT1 §0)

Kullanıcı isteğindeki bazı hedefler fiziksel/matematiksel olarak imkânsızdır. Anayasa "İmkânsız istekte 🚩 [ne] · [neden] · [gerçekçi alternatif]" der. İşte dürüst tablo:

| İstenen | 🚩 Neden imkânsız | ✅ Gerçekçi çalışan eşdeğeri (bu belge onu kurar) |
|---|---|---|
| Tek pront +900.000.000.000 (900 milyar) karakter | ≈900 GB metin. Hiçbir LLM üretemez/okuyamaz; hiçbir dosya bu boyutta olmamalı. | **Maksimum yoğunluk** ilkesi: modüler, şablon-tabanlı, sürümlü pront kütüphanesi. Değer = sinyal yoğunluğu, uzunluk değil. |
| Her ünvan için +122 pront × her biri +900.000.000 karakter | 122×900M ≈ 110 GB/ünvan × yüzlerce ünvan. İmkânsız. | Ünvan başına **modüler pront paketi**: 1 kimlik-pront + N görev-pront şablonu + kalite rubric'i. Gecelik döngü paketi büyütür (kümülatif). |
| Tek koşumda tüm ünvanların dünya top-100 kişisini bulmak | Yüzlerce ünvan × 100 kişi = on binlerce web araması; tek turda mümkün değil, kota/maliyet 🚩. | **Rotasyonlu araştırma kuyruğu**: gün/ay bazında ünvan sırası; her koşumda 1 ünvanın top-listesi derinleştirilir, zaman-damgalı arşivlenir, aylık yenilenir (aşağıdaki protokol). |
| Model her gece kendini "train" etsin | Model ağırlıkları sabit. | **Bilgi tabanı büyür** (oku→damıt→yaz→zincir). Davranışsal olarak aynı sonuç. |

> Bu belgedeki her şey bu kırmızı bayraklara **uyumludur**: gerçek, çalışan, kademeli.

---

## 1. YEDİ KADEMELİ ÜNVAN LADDER'I (C-seviyesi → işçi)

Sistem 4 eksende hiyerarşiktir: **Kurul → Alan (C) → Departman → Rol Ailesi → Kademe**. `daily_agency.py` içindeki 14 başkanlık + 46 departman bu ladder'ın L8–L6 katmanlarıdır; buraya L9 (kurul) ve L5–L1 (kıdem) eklenir.

| Kademe | Ünvan sınıfı | Kod deseni | Örnek | Sorumluluk özeti |
|---|---|---|---|---|
| **L9** | Kurul / CEO ofisi | `BRD-*`, `CEO-*` | Yönetim Kurulu, CEO | Vizyon, faz kapıları, sermaye/gelir onayı (CILT1 §7) |
| **L8** | C-seviyesi (14 başkan) | `CTO`, `CAIO`, `CDO`… | Baş Teknoloji/AI/Veri Sorumlusu | Alan stratejisi, domain hedefleri |
| **L7** | Departman direktörü | `{DEPT}-M1` | `ENG-PLT-M1` | Departman ana çıktısı, günlük koşum sahibi |
| **L6** | Rol ailesi başı | `{DEPT}-F{n}-L5` | `SEC-OPS-F1-L5` | Aile lideri (Baş Uzman), aile çıktısı |
| **L5** | Kıdemli uzman | `{DEPT}-F{n}-L4` | Kıdemli Mühendis/Analist | Karmaşık iş, mentörlük |
| **L4** | Uzman | `{DEPT}-F{n}-L3` | Uzman | Bağımsız iş üretimi |
| **L3** | Yardımcı uzman | `{DEPT}-F{n}-L2` | Yetişen uzman | Denetimli iş |
| **L2/L1** | İşçi / stajyer ajan | `{DEPT}-F{n}-L1` | Operatör ajan | Atomik, tekrarlı görev |

**Kademelendirme kuralı:** her rol ailesi (aileler[]) L5→L1 dikey hattına açılır. Böylece 46 departman × ~3 aile × 5 kademe ≈ **690 ünvan yuvası**; her yuva bir LLM ajan personası + pront paketi + insan-referans arşiviyle doldurulur (gecelik döngü, rotasyonla).

### 1.1 14 C-Alanı ve departman dağılımı (daily_agency.py DOMAINS ile birebir)

| C-Alan (L8) | Departmanlar (L7) |
|---|---|
| **CTO** | ENG-PLT · ENG-APP · ENG-DEV · ENG-QA |
| **CAIO** | AI-RES · AI-AGT · AI-PRM · AI-SAF |
| **CDO** | DAT-ENG · DAT-SCI · DAT-BI |
| **CPO** | PRD-MGT · PRD-DSN · PRD-OPS |
| **CMO** | MKT-BRD · MKT-PRF · MKT-SEO · MKT-SOC |
| **CRO** | REV-SLS · REV-PRT · REV-CSM · REV-OPS |
| **CCO** | MED-PUB · MED-CRE · MED-LOC |
| **COO** | OPS-PMO · OPS-BIZ · OPS-TLS |
| **CFO** | FIN-FPA · FIN-ACC · FIN-REV |
| **CISO** | SEC-OPS · SEC-AUD · SEC-SUP |
| **CHRO** | HRA-REC · HRA-PRF · HRA-LRN |
| **CLO** | LGL-LIC · LGL-PRV |
| **CIO** | INF-MCP · INF-SET · INF-HKS · INF-LOP |
| **CSO** | STR-INT · STR-CMP · STR-GRW |

> Tam liste + rol aileleri: `scripts/daily_agency.py` `DOMAINS` yapısı canlı kaynaktır. `python3 scripts/daily_agency.py --org-json` ile `.claude/org/org.json` üretilir (makine-okur ünvan kayıt defteri).

---

## 2. TOP-100 İNSAN-REFERANS ARAŞTIRMA PROTOKOLÜ (her ünvan için)

Her ünvan yuvası, o alanın **dünyanın en iyi ~100 uygulayıcısına** bağlanır. Bunları tek turda toplamak imkânsız (§0); bunun yerine **rotasyonlu, zaman-damgalı, aylık yenilenen** bir kuyruk çalışır.

### 2.1 Tek ünvan için araştırma adımları (atomik iş birimi)

```
GİRDİ: {alan, departman, unvan_kodu, ay=YYYY-MM}
[1] ts_start = date -u +"%Y-%m-%dT%H:%M:%SZ"
[2] ESKİYİ OKU: arastirma/{alan}/{unvan}/ altındaki en son ay dosyasını oku (varsa).
    → Zincir: yeni araştırma öncekinin üstüne ekler, çelişkiyi işaretler.
[3] ARAŞTIR (web): o ünvanın dünya çapında en iyi uygulayıcılarını tara.
    Kaynak türleri: hakemli/temel makaleler, konferans konuşmaları, röportajlar,
    açık kaynak projeler, ürün/şirket etkisi, ödüller. SADECE halka açık kaynak.
[4] DAMIT: her kişi için tek satır künye (aşağıdaki şema). Telif: uzun alıntı yok.
[5] ARŞİVLE (zaman damgalı): iki dosya yaz (aşağıdaki yol düzeni).
[6] DENETLE: 6 katman (CILT2) — referans doğrulama (URL/SSRF), dolgu yok, kaynak var mı.
[7] ts_end + AUDIT_LOG.jsonl satırı + BILGI_TABANI.md öğrenimi (zincir).
```

### 2.2 Zaman-damgalı arşiv yol düzeni (append-only, geri-okunabilir)

```
arastirma/
└── {alan}/                         # ör: ai-agent-muhendisligi, performans-pazarlama
    └── {unvan_kodu}/               # ör: AI-AGT-F1-L5
        ├── {YYYY-MM}-top100.md     # o ayın insan kürasyonu (insan-okur)
        ├── {YYYY-MM}-kaynaklar.jsonl  # kanıt satırları (makine-okur, zaman damgalı)
        └── _INDEKS.md              # tüm ayların kronolojisi (en yeni üstte)
```

**`{YYYY-MM}-top100.md` künye şeması (kişi başı 1 satır):**
```
| # | İsim | Rol/Kurum | Neden top | Ana eser (makale/proje/röportaj) | Kaynak URL | Damga |
|---|------|-----------|-----------|----------------------------------|------------|-------|
```

**`{YYYY-MM}-kaynaklar.jsonl` satır formatı:**
```json
{"ts":"2026-08-03T15:40:00Z","alan":"...","unvan":"AI-AGT-F1-L5","kisi":"...",
 "eser_turu":"makale|proje|roportaj|konusma","baslik":"...","url":"...",
 "sinyal":"1 cümle çıkarım","guven":"yuksek|orta|dusuk"}
```

### 2.3 Aylık yenileme takvimi & geri-okuma döngüsü (7/24 mekanizma)

- **Rotasyon:** `daily_agency.py`'nin gün-bazlı departman rotasyonu (DOY % 46) araştırma kuyruğunu da sürer. Her gün 1 departmanın ünvanları derinleştirilir; ~46 günde tüm departmanlar bir tur döner.
- **Aylık tazeleme:** her ünvan için `{YYYY-MM}` dosyası ayda bir yeniden üretilir. Yeni ay dosyası **önceki ayı okur** (zincir), değişenleri işaretler (yükselen/düşen isimler, yeni eser).
- **Geri-okuma:** her koşum önce `_INDEKS.md` + son ay dosyasını okur → sonra araştırır → sonra yazar. "Oku → araştır → damgala → arşivle → bir sonraki tur tekrar oku."
- **Nasıl koşulur (CILT1 §5 ile uyumlu):** Claude Code Scheduled/Routines gecelik prompt'u ya da GitHub Actions `workflow_dispatch`. 🚩 Not: web-araması + LLM adımı **ücretli kota** harcar; maliyet-kontrolü için tur başına ünvan sayısına üst sınır koy (ör. gün başına 1 departman × 3 aile başı).

### 2.4 Örnek seed (mekanizmayı gösterir — tam değil, kalıp)

`arastirma/ai-agent-muhendisligi/AI-AGT-F1-L5/2026-08-top100.md` (ilk 3 satır örnek kalıp):
```
| 1 | [Araştır] | [Rol/Kurum] | temel ajan mimarisi | [makale] | [url] | 2026-08-03T15:40Z |
| 2 | [Araştır] | [Rol/Kurum] | çok-ajan orkestrasyon | [konuşma] | [url] | 2026-08-03T15:40Z |
| 3 | [Araştır] | [Rol/Kurum] | değerlendirme (evals) | [proje] | [url] | 2026-08-03T15:40Z |
```
> Gerçek isimler gecelik araştırma koşumunda doldurulur; bu belge **protokolü** kurar, listeyi değil (tek turda 100×yüzlerce ünvan imkânsız — §0).

---

## 3. +100 EK YETENEK MATRİSİ (kültür · sanat · spor · kişisel gelişim)

Ana ünvanlara ek olarak, her ajanın "insani genişlik" ekseni. Aynı araştırma protokolü (§2) bu eksene de uygulanır: her yetenek için dünya top-100 uygulayıcısı, zaman-damgalı, aylık yenilenen arşiv.

| Küme | Örnek yetenekler (her biri bir arşiv yuvası) |
|---|---|
| **Kültür** | felsefe, tarih, mitoloji, dilbilim, antropoloji, arşivcilik, kütüphanecilik |
| **Sanat** | edebiyat, şiir, resim, heykel, mimari, film, tiyatro, fotoğraf, tasarım |
| **Müzik** | kompozisyon, enstrüman, ses mühendisliği, müzikoloji |
| **Spor** | strateji/oyun zekâsı, antrenman bilimi, dayanıklılık, takım koordinasyonu |
| **Zihin/Gelişim** | öğrenme bilimi, hafıza teknikleri, retorik, müzakere, karar teorisi |
| **Zanaat** | mutfak sanatları, el sanatları, dünya dilleri, satranç/go |

**Arşiv yolu:** `arastirma/yetenek/{kume}/{yetenek}/{YYYY-MM}-top100.md` (+ `kaynaklar.jsonl`). Aynı §2 şeması ve döngüsü.

> Hedef: 100+ yetenek yuvası. Tek turda değil — rotasyonla, gecelik, kümülatif doldurulur.

---

## 4. HER ÜNVAN İÇİN PRONT PAKETİ POLİTİKASI (122×900M yerine gerçekçi eşdeğer)

İstek: "her title için +122 pront + ekipler için +122 + uygulama için +122, her biri +900M karakter." Bu boyut imkânsız (§0). Gerçekçi eşdeğer: **ünvan başına modüler pront paketi**, gecelik döngüyle kümülatif büyüyen.

Her ünvan yuvası şu paketi taşır (CILT2 anatomileriyle üretilir):

```
uretim/pront-paketi/{unvan_kodu}/
├── 00-kimlik.md          # "Sen {rol}sün" — persona + çıktı sözleşmesi (1 adet)
├── 10-gorev/*.md         # görev-pront şablonları (N adet, rotasyonla artar)
├── 20-ekip/*.md          # ekip/işbirliği pront'ları (bağlı ünvanlarla)
├── 30-uygulama/*.md      # uygulama/koşum pront'ları (Claude Code'da çalıştırılır)
├── 40-referans.md        # §2 arşivinden damıtılmış "en iyi pratik" özeti
└── SURUM.md              # SHA256 + sürüm (Integrity Validator — CILT2)
```

**Kalite > adet ilkesi:** "122" bir sayısal fetiş değil, **kapsam hedefidir** — paket, ünvanın işini uçtan uca kapsayana kadar gecelik döngü yeni şablon ekler. Her şablon: yoğun, kopyala-çalıştır, %99 doğrulanmış (6 katman). Boş 900M karakter yerine **dolu, çalışan** şablonlar.

---

## 5. YOL HARİTASI, DEADLINE & 7/24 TOPLANTI RİTMİ

`daily_agency.py` zaten günlük/haftalık/aylık koşum üretir. Ünvan-referans sistemi bu ritme oturur:

| Ritim | Ne olur | Üreten |
|---|---|---|
| **Günlük** (06:00 UTC) | Günün departmanı: standup + işe alım adayı + araştırma kuyruğu 1 adım | `daily_agency.py` |
| **Haftalık** (Cuma) | Liderlik sync: KALDI dökümü, araştırma ilerlemesi | `daily_agency.py --haftalik` |
| **Aylık** (ayın 1'i) | Kurul: faz kapıları + tüm ünvanların top-100 aylık tazeleme kapanışı | `daily_agency.py --aylik` |
| **Sürekli** | Arşiv geri-okuma zinciri (her koşumun ilk adımı) | §2.3 |

**Deadline mantığı:** her ünvan yuvası için "sonraki tazeleme = son arşiv ayı + 1 ay". `_INDEKS.md` son damgadan geciken yuvaları görünür kılar → haftalık sync bunları aksiyona çevirir.

---

## 6. UYGULAMA KONTROL LİSTESİ (bu belgeyi hayata geçirmek)

- [ ] `python3 scripts/daily_agency.py --org-json` → `.claude/org/org.json` ünvan kayıt defterini üret
- [ ] `arastirma/` kök klasörünü aç; §2.2 yol düzenini benimse
- [ ] Bir seed ünvan seç (ör. `AI-AGT-F1-L5`) → §2.1 adımlarını elle bir kez koş → kalıbı doğrula
- [ ] Gecelik araştırma kuyruğunu Scheduled/Routines'e koş (maliyet üst sınırıyla — 🚩)
- [ ] Aylık tazeleme + geri-okuma zincirini `_INDEKS.md` üzerinden izle
- [ ] Pront paketlerini (§4) rotasyonla büyüt; her şablonu 6 katmanla doğrula

---

### KAPANIŞ
Bu cilt, "C-seviyesinden işçiye kademeli LLM ajans + her ünvan için dünya top-100 insan referansı + aylık zaman-damgalı arşiv + sürekli geri-okuma döngüsü" isteğinin **anayasaya uyumlu, çalışan** karşılığıdır. İmkânsız boyutlar (900 milyar karakter, tek-tur top-100×tüm-ünvanlar) kırmızı bayrakla işaretlenmiş; yerlerine kümülatif, rotasyonlu, kanıtlanabilir mekanizma konmuştur. Uçtan uca yapıştırılacak master pront: `docs/MEGA-PRONT-MASTER.md`.
