---
name: haftalik-icerik-loop
description: Movéa için haftalık içerik üretim döngüsü — takvimi açar, kalemleri üretir, denetimden geçirir, damgalar ve içerik/hafta metriğini raporlar. Haftalık ritim kurulacaksa veya "haftalık içerik döngüsü", "içerik otomasyonu" dendiğinde kullan.
category: operations
interval: 7d
stop-condition: Haftalık takvimdeki tüm kalemler "GEÇTİ" durumunda VE metrik satırı AUDIT_LOG.jsonl'a damgalanmış.
components: [agent:brand-content/marka-icerik-ajani, command:content/icerik-takvimi, command:content/linkedin-yayinci, hook:audit/timestamp-audit]
tags: [movea, brand-content, weekly, loop, tr]
---
# Haftalık İçerik Döngüsü (Movéa)
> Amaç: her hafta, marka sesinden sapmadan takvimi dolduran yayınlanabilir içerik seti +
> kanıt metriği **içerik/hafta**. GELIR_MOTORU pilot sözleşmesinin operasyon karşılığı.

## Zamanlama
`interval: 7d` — önerilen başlangıç: Pazartesi 06:00 TRT (hafta açılışı).

## Çalıştır
```
/loop 7d "TON_REHBERI ve BILGI_TABANI'nı oku. /icerik-takvimi ile haftayı aç.
marka-icerik-ajani ile tüm boş hücreleri doldur (post + görsel brief + CTA).
LinkedIn kalemlerini /linkedin-yayinci ile formatla. Her kalemi 6 katman denetimden
geçir; KALDI olanı düzelt (kalem başına maks 3 tur). Takvim durumlarını güncelle,
metrik satırını yaz, öğrenimi BILGI_TABANI'na ekle."
```

## İterasyon adımları
1. **OKU** — `TON_REHBERI.md` + `BILGI_TABANI.md` + geçen haftanın `AUDIT_LOG.jsonl` satırları.
2. **TAKVİM** — `/icerik-takvimi` → `icerik/TAKVIM-[hafta].md` (hedef içerik/hafta sabitlenir).
3. **ÜRET** — `marka-icerik-ajani` boş hücreleri doldurur; LinkedIn kalemleri `/linkedin-yayinci`den geçer.
4. **DENETLE** — 6 katman; sonuç kalem bazında `GEÇTİ/KALDI`; KALDI → düzelt → tekrar denetle.
5. **DAMGA** — `timestamp-audit` hook'u her yazımı `AUDIT_LOG.jsonl`'a işler; döngü sonunda metrik satırı.
6. **ZİNCİR** — 1 satır öğrenim (`hangi format/hook çalıştı`) → `BILGI_TABANI.md` → gelecek haftanın girdisi.

## Durma koşulu
Takvimdeki tüm kalemler `GEÇTİ` + metrik satırı damgalı. Kalem 3 turda geçemezse:
`KALDI` olarak işaretle, teslim etme, gelecek haftanın 1. iş kalemi yap (sözleşme: KALDI teslim edilmez).

## 🚩 Maliyet sınırı
Döngü başına maks 1 tam tur + kalem başına 3 düzeltme. Aylık kota eşiği aşılırsa
döngü iki haftada bire iner — karar sahibi: Metin.

## Örnek
Pazartesi 06:00: takvim 5 kalem açar → ajan 5 seti üretir → 1 kalem ses uyumsuz (KALDI) →
düzeltme turu → 5/5 GEÇTİ → metrik: `içerik/hafta = 5` → öğrenim: "soru-hook IG'de kaydetmeyi artırdı".
