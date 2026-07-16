---
name: haftalik-izleme-loop
description: Her hafta rakip fiyat/stok/kampanya verisini toplar, analiz eder, haftalık raporu teslim eder ve aksiyonları loglar. VESTRA pilotunun kanıt metriği bu döngüdür.
category: operations
interval: 7d
stop-condition: Haftalık rapor raporlar/ altına teslim edildi VE aksiyonlar AUDIT_LOG.jsonl'a damgayla loglandı VE öğrenim BILGI_TABANI.md'ye eklendi.
components: [agent:ecommerce/rakip-fiyat-izleyici, skill:web-data/fiyat-izleme, skill:ecommerce/kampanya-analizi, command:reporting/haftalik-fiyat-raporu, hook:audit/timestamp-audit]
tags: [ecommerce, fiyat-izleme, rakip-analizi, haftalik-rapor, loop]
---
# Haftalık İzleme Döngüsü

> VESTRA'nın haftalık rakip istihbarat ritmi: izle → damıt → raporla → logla.
> GELIR_MOTORU kanıt metriği: bu raporun her hafta otomatik teslimi.

## 🎯 Amaç
Her 7 günde bir rakip fiyat/stok/kampanya değişimlerini tek raporda toplamak
ve her aksiyonu damgalı olarak loglamak. Rapor teslim edilmeden döngü kapanmaz.

## ⏱️ Zamanlama
Önerilen aralık: `7d` (Cuma sabahı — haftalık paket konsolidasyonuna denk).

## ▶️ Çalıştır
```
/loop 7d "sources.md'deki rakip ürünleri tara, son 7 günün değişimlerini çıkar,
/haftalik-fiyat-raporu ile raporu üret, aksiyonları AUDIT_LOG.jsonl'a damgayla
yaz, öğrenimi BILGI_TABANI.md'ye ekle. Kaynaksız sayı kullanma; robots.txt ve
KVKK sınırına uy."
```

## 🔁 İterasyon adımları
1. **Algıla** — `fiyat-izleme` skill'i kaynakları çeker, snapshot yazar.
2. **Akıl yürüt** — değişimleri eşiğe vur; kampanya sinyallerini `kampanya-analizi`ne devret.
3. **Planla** — `rakip-fiyat-izleyici` aksiyon önerilerini üretir (en fazla 5).
4. **Uygula** — `/haftalik-fiyat-raporu` raporu `raporlar/` altına teslim eder.
5. **Gözle** — DENETİM KUYRUĞU (CLAUDE.md) koşar; KALDI ise düzelt, 3'e dön.
   Maksimum 3 iterasyon (maliyet kontrolü 🚩); sonra eksikleri 🚩 ile raporla.

## 🛑 Durma koşulu
Rapor teslim + aksiyonlar loglandı + öğrenim eklendi. Üçü de damgalı olmalı.

## 🧩 Bileşenler
`rakip-fiyat-izleyici` (analiz+aksiyon) · `fiyat-izleme` (veri) ·
`kampanya-analizi` (kampanya) · `/haftalik-fiyat-raporu` (teslim) ·
`timestamp-audit` (damga).

## 💡 Örnek
Cuma koşusu 24 SKU'da 6 değişim bulur, 3 aksiyon önerir, raporu
`raporlar/2026-29-fiyat-raporu.md` olarak teslim eder, 4 satır loglar.
