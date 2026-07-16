---
allowed-tools: Read, Write
argument-hint: "[hafta: GG.AA] [platformlar: ig,linkedin,x] [odak/kampanya]"
description: Haftalık içerik takvimi üretir — gün × platform × tema tablosu; içerik/hafta hedefini sabitler. "İçerik takvimi", "haftalık plan", "bu hafta ne paylaşalım" dendiğinde kullan. Örnek; /icerik-takvimi 21.07 ig,linkedin lansman
---
# /icerik-takvimi
Girdi: `$ARGUMENTS` → hafta başlangıcı, platform listesi, odak (kampanya/tema). Eksikse:
hafta = önümüzdeki Pazartesi, platformlar = ig,linkedin, odak = ton rehberindeki pillar dağılımı.

## Süreç
1. `TON_REHBERI.md` + `BILGI_TABANI.md` oku (pillar dağılımı ve geçen haftanın öğrenimi).
2. Pillar dağılımı (rehberde yoksa varsayılan): eğitici %30 · marka/perde-arkası %25 ·
   ürün %20 · topluluk %15 · promosyon %10.
3. Tabloyu üret ve `icerik/TAKVIM-[hafta].md` dosyasına yaz.

## Çıktı formatı (zorunlu)
| Gün | Platform | Tema/Pillar | Format | CTA hedefi | Durum |
|---|---|---|---|---|---|
| Pzt | IG | ... | carousel | kaydet | boş |
Durum değerleri: `boş → üretildi → GEÇTİ`. Takvim `marka-icerik-ajani`nin iş listesidir.

Tablonun altına sabit satır:
`HEDEF: [N] içerik/hafta · ODAK: [kampanya] · DAMGA: [date -u]`

## Kurallar
- Aynı gün aynı platforma 1'den fazla kalem koyma (ritim > hacim).
- Promosyon pillar'ı %10'u aşarsa 🚩 uyar (marka sesi erozyonu).
- Özel gün/bayram haftasıysa 1 kalemi ona ayır ve işaretle.
