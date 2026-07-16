# GELİR MOTORU — HEDEF İŞ: CLAUDE OTONOM SİSTEM'İN KENDİSİ
> Karar: K-001 (2026-07-14) · Sahip: İŞ/GELİR STRATEJİSTİ · Sistem ürünün kendisidir.
> (v2'den v3 yapısına taşındı, 2026-07-16. FAZ 4 gecelik üretimi bu dosyaya bağlıdır; genel çerçeve: docs/CILT1 §7.)

## TEZ
Depo (davila7/claude-code-templates) bunun kanıtı: bileşen kütüphanesi + CLI + katalog = dağıtılabilir ürün.
Aynı model Türkçe pazar + Metin'in dikeyleri (medya/programmatic, e-ticaret, kültür-etkinlik, tahmin/analitik) için kopyalanır.

## ÜRÜN KATMANLARI
| Katman | Ürün | Gelir yolu | Durum |
|---|---|---|---|
| 1. Bileşen kütüphanesi | Türkçe/dikey agent+skill+hook paketleri (pazarlama, e-ticaret, medya planlama) | Paket satışı / lisans | Gecelik üretim başlasın |
| 2. Global agent servisleri | `--create-agent` + SDK ile müşteriye kurulan "AI ajanı" | Kurulum bedeli + aylık bakım | Katman 1'den 3 bileşen GEÇTİ sonrası |
| 3. Kurulum + danışmanlık | Bu sistemin (ANAYASA+kurul+gecelik döngü) müşteriye kurulması | Proje bedeli | Katman 2 ile birlikte |

## PİLOT İÇ MÜŞTERİLER (dogfooding — dış satıştan önce kanıt)
| Pilot | İlk bileşen adayı | Kanıt metriği |
|---|---|---|
| Tahmin Uzmanı | prompt v-serisi iyileştirme ajanı | v-serisi kalite artışı, kullanım sayısı |
| VESTRA | rakip fiyat izleme skill'i | haftalık izleme raporu otomasyonu |
| Response DGA | pitch-deck üretici ajan | pitch başına hazırlık süresi ↓ |
| İBB Kültür AŞ | etkinlik/rakip tarama skill'i | haftalık tarama teslimi |
| Movéa | marka içerik ajanı | içerik/hafta sayısı |

## GECELİK ÜRETİM SÖZLEŞMESİ (FAZ 4'ün gelir bağlantısı)
- GECELİK ÇIKTI: 1 bileşen (agent/skill/hook taslağı) VEYA 1 pilot deliverable — her gece, istisnasız.
- KALİTE EŞİĞİ: DENETÇİ rubric GEÇMELİ; KALDI olan teslim edilmez, ertesi gece düzeltilir.
- TESLİM: Proje dokümanı (claude-otonom-sistem/uretim/[tarih]-[ad].md) + haftalık konsolide paket (Cuma).
- ÖLÇÜM: (a) GEÇTİ bileşen sayısı/hafta ≥5 · (b) pilot kullanımda bileşen sayısı · (c) pilot→dış satış dönüşümü · (d) ilk dış gelir (₺) — hedef: 90 gün içinde ilk ödeme.

## HAFTALIK RİTİM → GELİR EŞLEMESİ
Pzt: skill üret (Katman 1) · Sal: agent genişlet (Katman 1-2) · Çar: MCP/sandbox dene (Ar-Ge) ·
Per: pilot deliverable (dogfooding kanıtı) · Cum: denetim + haftalık paket konsolidasyonu · Hafta sonu: makale + bilgi tabanı temizliği

## 🚩 SINIR
Gecelik ağır otomasyon kota/ücret harcar. Aylık bütçe eşiği aşılırsa: gecelik döngü haftada 3'e iner (Pzt/Çar/Cum). Karar sahibi: Metin.
