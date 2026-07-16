---
description: "Haftalık etkinlik/kıyas-kurum tarama teslimi: öne çıkan 5 sinyal + kıyas tablosu + 3 öneri. Kullan: her Cuma teslim öncesi veya 'haftalık raporu çıkar' dendiğinde."
---
# /haftalik-tarama-raporu

Girdi: `etkinlik-tarama` skill çıktısı veya ham sinyal listesi ($ARGUMENTS).
Eksikse önce taramayı çalıştır, sonra raporu üret. Dolgu yok; her satır kaynaklı.

## Çıktı formatı (aynen)

**HAFTALIK TARAMA — [tarih aralığı] · İBB Kültür AŞ**

**1) Öne çıkan 5 sinyal** (etki sırasıyla)
`[tür] kurum — sinyal — kaynak+tarih — fırsat/tehdit — önerilen tepki (1 satır)`

**2) Kıyas tablosu**
| Kurum | Öne çıkan program | Fiyat aralığı | Format hamlesi | Kültür AŞ'ye not |
|---|---|---|---|---|

**3) Üç öneri** (90 günde uygulanabilir; sahip + ilk adım + beklenen etki)

Altbilgi: ⏱️[ts_start→ts_end] · 🔍[GEÇTİ/KALDI] · 📚[bu haftanın öğrenimi, 1 satır]
