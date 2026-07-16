---
description: Haftalık rakip fiyat/stok/kampanya değişim tablosu ve önceliklendirilmiş aksiyon listesi üretir. Use when hafta kapanışında, haftalik-izleme-loop teslim adımında veya kullanıcı "haftalık rapor" istediğinde.
---
# /haftalik-fiyat-raporu

Girdi: `data/snapshots/` altındaki son 7 günün çekimleri (+ isteğe bağlı
kapsam filtresi: $ARGUMENTS, örn. tek rakip veya SKU grubu).

Çıktı — tek rapor, `raporlar/YYYY-WW-fiyat-raporu.md`:
1. **Başlık satırı:** izlenen SKU sayısı · değişim sayısı · en büyük hareket.
2. **Değişim tablosu:** `sku · ürün · rakip · eski→yeni · %Δ · stok · kampanya · kaynak`.
   Yalnız değişenler; sıralama |%Δ| azalan. Kaynaksız satır girmez.
3. **Kampanya özeti:** aktif rakip kampanyaları + agresiflik skoru (kampanya-analizi).
4. **Aksiyon listesi:** en fazla 5 madde, öncelik sıralı; her maddede
   aksiyon · gerekçe (kanıt URL) · marj etkisi · sorumlu/kontrol tarihi.
5. **Veri sağlığı:** çekilemeyen kaynaklar (🚩), 7 günden eski veriler.

Kurallar: sayı önce, yorum sonra; dolgu yok. Rapor sonunda damga altbilgisi:
⏱️[ts_start→ts_end] 🔍[GEÇTİ/KALDI] 📚[öğrenim] 🔗[önceki kullanıldı?]
Aksiyonlar AUDIT_LOG.jsonl'a `islem:"haftalik_rapor"` satırıyla loglanır.
