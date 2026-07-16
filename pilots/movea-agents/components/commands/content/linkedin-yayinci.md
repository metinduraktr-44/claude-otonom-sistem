---
allowed-tools: Read, Write, Glob, WebFetch
argument-hint: "<girdi: dosya|URL|konu> [varyant-sayisi]"
description: Verilen içeriği LinkedIn formatına çevirir — TR profesyonel ton, hook-önce, link ilk yoruma. "LinkedIn'e çevir", "LinkedIn postu yap", "bunu LinkedIn'de paylaş" dendiğinde kullan. Örnek; /linkedin-yayinci icerik/lansman.md 2 → 2 varyant + ilk yorum + görsel önerisi.
---
# /linkedin-yayinci
Girdi: `$ARGUMENTS` → içerik kaynağı + istenen varyant sayısı (varsayılan 2).

## Süreç
1. **Girdiyi algıla**: `/` veya uzantı içeriyorsa dosya (Read) · `http` ile başlıyorsa URL (WebFetch) ·
   aksi halde konu başlığı — `icerik/**` içinde Glob ile eşleşen taslağı ara, yoksa konudan üret.
2. **Ton rehberini oku**: `TON_REHBERI.md` (ses sıfatları + hitap + yasaklı kelimeler).
3. **Postu üret** (LinkedIn kuralları):
   - İlk satır = hook; "devamını gör" kırılmasından önce merak yaratmalı.
   - 1.200-1.500 karakter; kısa paragraflar, bol satır boşluğu.
   - Link gövdeye DEĞİL → ayrı "İLK YORUM" bloğu olarak ver.
   - 2-4 hashtag, sona; kişi etiketi yalnızca gerçekten ilgiliyse.
   - Kanıtlı somutluk: sayı/dönem/sonuç — kaynağı içerikte olmayan sayı uydurma.
4. **Kaçış**: metin API/otomasyona gidecekse LinkedIn LTF rezervli karakterlerini kaçır:
   `| { } @ [ ] ( ) < > # * _ ~`
5. **Teslim** (kopyala-yapıştır — yayınlama manueldir, kimlik/anahtar istenmez):

## Çıktı formatı
```
VARYANT 1 (açı: [ör. kurucu hikâyesi]) — [karakter sayısı]
[post metni]
---
VARYANT 2 (açı: [ör. sektör içgörüsü]) — [karakter sayısı]
[post metni]
---
İLK YORUM: [link + 1 cümle bağlam]
GÖRSEL ÖNERİSİ: [tek görsel/döküman-carousel + 1 satır brief]
YAYIN SAATİ: Sal-Per 08:00-09:00 veya 12:30 TRT
SES UYUMU: [ton rehberi maddesi]
```
