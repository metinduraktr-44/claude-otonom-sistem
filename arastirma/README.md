# arastirma/ — Zaman-damgalı insan-referans arşivi (CILT9 §2 / CILT10 §5)

Bu klasör, her org düğümü/ünvan için o alanın dünyadaki en iyi uygulayıcılarının (top-5/top-100) zaman-damgalı, aylık yenilenen, geri-okunabilir arşividir.

## Yol düzeni
```
arastirma/
├── {ulke}/                              # global | tr | de | ...
│   └── _ULKE-PROFILI-{YYYY-MM}.md       # dil/hukuk/pazar/yerel top-5 (train)
│   └── {istirak}/                       # adops | performer | vizatrack | ...
│       └── {UNVAN}/                     # ör: MKT-PRF-LEAD
│           ├── {YYYY-MM}-top5.md        # insan kürasyonu (insan-okur)
│           ├── {YYYY-MM}-kaynaklar.jsonl# kanıt satırları (makine-okur, damgalı)
│           └── _INDEKS.md               # tüm ayların kronolojisi (en yeni üstte)
```

## Döngü (her koşum)
`ts_start` → son ay dosyasını **oku** (zincir) → web'de araştır (halka açık) → kişi başı 1 satır künye **damıt** → **arşivle** (top-N + kaynaklar.jsonl) → 6 katman **denetle** → `ts_end` + `AUDIT_LOG.jsonl` + `BILGI_TABANI.md`.

## Rotasyon & maliyet
`scripts/daily_agency.py` gün-bazlı rotasyonu (DOY % 46) araştırma dilimini sürer. 🚩 Web+LLM adımları ücretli kota harcar → tur başına ünvan/dilim üst sınırı zorunlu. Tek turda tüm ünvan×ülke top-100 **imkânsız** (CILT9 §0); bu arşiv kümülatif dolar.

## Seed durumu (bu commit)
- `tr/_ULKE-PROFILI-2026-08.md` — gerçek, kaynaklı Türkiye pazarı+regülasyon profili.
- `global/adops/MKT-PRF-LEAD/2026-08-top5.md` — gerçek, kaynaklı paid-social/performans top-5 seed.
Gerisi gecelik döngüyle (rotasyon) doldurulur.
