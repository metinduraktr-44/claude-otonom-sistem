---
name: haftalik-tarama-loop
description: Her hafta kültür-etkinlik sahnesini tarar, kıyas tablosu kurar ve İBB Kültür AŞ haftalık tarama raporunu damgalı teslim eder.
category: operations
interval: 7d
stop-condition: Haftalık rapor 5 kaynaklı sinyal + dolu kıyas tablosu + 3 öneri ile üretildi, DENETÇİ GEÇTİ verdi ve AUDIT_LOG.jsonl'a damgalandı.
components: [agent:culture-events/etkinlik-tarayici, agent:culture-events/kitle-trend-analisti, skill:research/etkinlik-tarama, command:reporting/haftalik-tarama-raporu, hook:audit/timestamp-audit]
tags: [kultur, etkinlik, tarama, haftalik-rapor, loop]
---
# Haftalık Tarama Döngüsü

> Operasyon döngüsü — GELIR_MOTORU pilotunun kanıt metriğini üretir: **haftalık tarama teslimi**.

## 🎯 Amaç
Her hafta kıyas kurumların program/bilet/format hamlelerini toplayıp
karar girdisine çevirmek ve Cuma teslimini istisnasız çıkarmak.

## ⏱️ Zamanlama
Önerilen aralık: `7d` (Perşembe gecesi çalıştır → Cuma teslim).

## ▶️ Çalıştır
```
/loop 7d "etkinlik-tarama skill'i ile haftalık taramayı yap: kurum siteleri, biletleme platformları, kültür-sanat basını. Sinyalleri çıkar, kıyas tablosunu doldur, /haftalik-tarama-raporu formatında raporu üret. DENETİM KUYRUĞUNDAN geçir, AUDIT_LOG.jsonl'a damgala, öğrenimi BILGI_TABANI.md'ye ekle."
```

## 🔁 İterasyon adımları
1. **Algıla** — `etkinlik-tarama` skill'i ile kaynak listesini gez (son 7 gün + gelecek 90 gün).
2. **Damıt** — `etkinlik-tarayici` sinyalleri fırsat/tehdide çevirir; format/kitle sinyalini `kitle-trend-analisti` derinleştirir.
3. **Üret** — `/haftalik-tarama-raporu` formatında teslimi yaz.
4. **Denetle** — CLAUDE.md DENETİM KUYRUĞU; KALDI ise düzelt, en fazla 3 iterasyon (maliyet sınırı 🚩).
5. **Damgala & öğren** — `timestamp-audit` AUDIT_LOG.jsonl'a yazar; öğrenim BILGI_TABANI.md'ye → gelecek haftanın girdisi (zincir).

## 🛑 Durma koşulu
Rapor tam (5 sinyal + tablo + 3 öneri), DENETÇİ GEÇTİ, damga atıldı — veya 3 iterasyon doldu (KALDI raporu ertesi güne düzeltme notuyla bırakılır).

## 🧩 Referans bileşenler
- `agent:culture-events/etkinlik-tarayici` — sinyal çıkarma, fırsat/tehdit
- `agent:culture-events/kitle-trend-analisti` — trend derinleştirme
- `skill:research/etkinlik-tarama` — kaynak listesi + yordam
- `command:reporting/haftalik-tarama-raporu` — teslim formatı
- `hook:audit/timestamp-audit` — damga

## 💡 Örnek
Perşembe gecesi döngü 14 duyurudan 5 sinyal damıtır: 2 takvim çakışması (tehdit),
1 boş çocuk-aile kuşağı (fırsat); tablo + 3 öneri Cuma 09:00'da teslim, damgalı.
