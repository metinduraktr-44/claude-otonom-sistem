---
name: kalite-serisi-loop
description: Tahmin prompt v-serisini iyileştir-değerlendir döngüsüne sokar; rubrik N ardışık GEÇTİ verene kadar yeni versiyon üretmeye devam eder.
category: evaluation
interval: 30m
stop-condition: Son versiyon rubrikten 3 ardışık değerlendirmede GEÇTİ alır (farklı test girdileriyle) VEYA 5 iterasyon sınırına ulaşılır.
components: [agent:prompt-engineering/v-serisi-iyilestirici, skill:evaluation/tahmin-kalite-olcumu, command:evaluation/v-serisi-rapor, hook:audit/timestamp-audit]
tags: [evaluation, prompt-engineering, quality-streak, loop]
---

# Kalite Serisi Loop

> **Loop Engineering** — tek yeşil değerlendirmeye güvenme. Kalitenin kalıcı olduğunu kanıtlamak
> için farklı test girdileriyle *ardışık GEÇTİ serisi* iste (quality-streak deseni).

## 🎯 Amaç
Tahmin prompt'unun güncel versiyonunu gerçekçi test girdileriyle değerlendir, KALDI aldığı her
eksende yeni versiyon üret ve rubrik 3 kez üst üste GEÇTİ verene kadar döngüyü sürdür —
tek seferlik şans başarısını değil, kararlı kaliteyi yakala.

## ⏱️ Zamanlama
Önerilen aralık: `30m`. Gecelik otonom koşuda: gece başına 1 seri (maliyet sınırı 🚩).

## ▶️ Çalıştır
```
/loop 30m "prompts/[seri] v-serisinin son versiyonunu 3 farklı gerçekçi tahmin senaryosuyla
tahmin-kalite-olcumu rubriğine vur. KALDI alırsa v-serisi-iyilestirici ile yeni versiyon üret
ve seriyi sıfırla. 3 ardışık GEÇTİ veya 5 iterasyona kadar devam et; her adımı damgala."
```

## 🔁 İterasyon adımları
1. **Algıla** — son vN'i ve BILGI_TABANI öğrenimlerini oku; yeni test girdisi seç (öncekiyle aynı olmasın).
2. **Değerlendir** — çıktıyı `tahmin-kalite-olcumu` rubriğine vur (4 eksen, GEÇTİ/KALDI).
3. **Planla** — KALDI ise en düşük eksen için düzeltme hedefi belirle; GEÇTİ ise seri sayacını artır.
4. **Uygula** — KALDI'da `v-serisi-iyilestirici` v(N+1) üretir; **seri sayacı sıfırlanır**.
5. **Gözle** — `timestamp-audit` her adımı damgalar; iterasyon öğrenimi BILGI_TABANI'na yazılır
   ve bir sonraki iterasyonun girdisi olur (zincir).

## 🛑 Durma koşulu
- **Başarı**: 3 ardışık GEÇTİ (her biri farklı test girdisiyle) → `/v-serisi-rapor` üret, dur.
- **Emniyet**: 5 iterasyonda başarı yoksa dur; en son teşhisleri raporla, kararı sahibe bırak (🚩 maliyet).

## 🧩 Referans bileşenler
- `agent:prompt-engineering/v-serisi-iyilestirici` — teşhis + yeni versiyon üretimi.
- `skill:evaluation/tahmin-kalite-olcumu` — 4 eksenli rubrik, GEÇTİ/KALDI kararı.
- `command:evaluation/v-serisi-rapor` — döngü sonu trend raporu.
- `hook:audit/timestamp-audit` — her adıma gerçek UTC damgası.

## 💡 Örnek
v3 iki kez GEÇTİ alır, üçüncü senaryoda (eksik veri durumu) kalibrasyon 2/5 → KALDI. Döngü v4'ü
"veri yoksa güven seviyesini düşür" kuralıyla üretir, seri sıfırdan başlar ve v4 3 ardışık
GEÇTİ ile döngüyü kapatır. Rapor: 9→15/20, kanıt metriği +6 puan.
