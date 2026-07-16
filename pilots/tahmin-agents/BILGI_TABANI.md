# BİLGİ TABANI (birikimli öğrenme — her koşuda büyür)
Sistemin "öğrenmesi" burada birikir. Her iterasyon yeni satır ekler; bir sonraki koşu bunu girdi alır (zincir).

## 2026-07-16 — Seed (repo kuruluşu)
- Repo kuruldu. Dikey odak: tahmin/analitik; ana pilot: prompt v-serisi iyileştirme (`v-serisi-iyilestirici`).
- Kanıt metriği: v-serisi kalite artışı (rubrik toplam puanı, 20 üzerinden) + kullanım sayısı (AUDIT_LOG sayımı).
- Rubrik 4 eksen: kalibrasyon · gerekçe kalitesi · veri dayanağı · tutarlılık. GEÇTİ eşiği: ≥14/20 ve hiçbir eksen <3.
- Döngü deseni: quality-streak uyarlaması — 3 ardışık GEÇTİ (farklı test girdileriyle) veya 5 iterasyon emniyet sınırı.
- Denetim: 6 katman (structural/integrity-SHA256/semantic/reference/patterns/review) + gerçek `date -u` damgası.
- İlk öğrenim: kalite iddiası rubrik eksenine bağlanmadan kabul edilmez; "daha iyi" tek başına geçersiz.
