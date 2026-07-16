# BİLGİ TABANI (birikimli öğrenme — her koşuda büyür)
Sistemin "öğrenmesi" burada birikir. Her haftalık döngü yeni başlık ekler;
bir sonraki koşu bunu girdi alır (zincir).

## 2026-07-16 — Seed (repo_scaffold)
- Repo kuruldu. Dikey: VESTRA e-ticaret; odak: rakip fiyat/stok/kampanya istihbaratı.
- Kanıt metriği: haftalık izleme raporunun otomatik teslimi (GELIR_MOTORU pilotu, K-001).
- Mimari karar: veri toplama (fiyat-izleme) ile aksiyon önerisi (rakip-fiyat-izleyici)
  ayrıldı — skill veri üretir, agent karar üretir; rapor komutu ikisini birleştirir.
- Loop durma koşulu üçlü: rapor teslim + aksiyon logu + öğrenim kaydı (hepsi damgalı).
- Sınır: yalnız kamuya açık sayfalar; robots.txt + KVKK; ücretli tarama (Bright Data)
  yalnız WebFetch yetmezse (🚩 kota).
- Açık iş: `data/sources.md` gerçek rakip listesiyle doldurulacak — ilk baz çekim
  olmadan değişim raporu üretilemez.
