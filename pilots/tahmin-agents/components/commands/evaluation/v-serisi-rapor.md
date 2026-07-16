---
description: "Tahmin prompt v-serisinin (v1→vN) versiyonlar arası kalite trendini raporlar: eksen bazında rubrik skorları, GEÇTİ/KALDI geçmişi, kullanım sayısı ve bir sonraki iyileştirme önerisi. Kullan: haftalık konsolidasyon (Cuma), yeni versiyon teslimi sonrası veya 'v-serisi ne durumda' sorusunda. Örnek: /v-serisi-rapor prompts/mac-tahmin"
---

# /v-serisi-rapor

Versiyonlar arası kalite trendi raporu. Parametre: `$ARGUMENTS` = v-serisi dosya öneki
(örn. `prompts/mac-tahmin`). Parametresiz çağrıda depodaki tüm v-serilerini listele ve sor.

## Adımlar
1. **Topla** — Glob ile `$ARGUMENTS*v[0-9]*.md` dosyalarını bul; her versiyonun frontmatter'ından
   `version` ve `changelog` oku. AUDIT_LOG.jsonl'dan `islem:"v_serisi_iyilestirme"` satırlarını
   ve rubrik skorlarını (varsa `islem:"kalite_olcumu"`) çek.
2. **Ölç** — skoru olmayan versiyon varsa `tahmin-kalite-olcumu` skill'iyle puanla (eksik veri
   varsa 🚩 işaretle, uydurma).
3. **Trendle** — versiyon sırasına göre toplam puan ve eksen puanlarını tablola; artış/düşüş okla.
4. **Öner** — en zayıf ekseni işaretle; bir sonraki iterasyon için `v-serisi-iyilestirici`ye
   tek cümlelik görev tanımı yaz.

## Çıktı formatı
```
V-SERİSİ RAPORU — [seri adı] · [tarih UTC]

| Versiyon | Kalibrasyon | Gerekçe | Veri | Tutarlılık | Toplam | Karar | Kullanım |
|---|---|---|---|---|---|---|---|
| v1 | 2 | 3 | 1 | 3 | 9/20 | KALDI | 4 |
| v2 | 3 | 3 | 3 | 4 | 13/20 | KALDI | 11 |
| v3 | 4 | 4 | 3 | 4 | 15/20 | GEÇTİ | 27 |

TREND: toplam 9→13→15 (↑) · en zayıf eksen: Veri dayanağı (3)
KANIT METRİĞİ: kalite artışı +6 puan / 3 versiyon · kullanım 42 çağrı
SONRAKİ GÖREV: v4 — veri dayanağı eksenine kaynak-zorunluluğu kuralı ekle.
```

## Kurallar
- Kullanım sayısı AUDIT_LOG satır sayımından gelir; log yoksa "veri yok" yaz, tahmin etme.
- Rapor sonunda damga altbilgisi zorunlu: ⏱️ · 🔍 · 📚 · 🔗.
