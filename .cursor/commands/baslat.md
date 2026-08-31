---
description: Bootstrap doğrula, STATE=READY, Faz 0
---

# /baslat — BAŞLAT

1. Doğrula: `.cursor/`, dizin iskeleti, `STATE.md`, `docs/CILT13-CURSOR-GIGA-CANVA.md`.
2. Yoksa stub oluştur (mevcut zengin içeriği silme).
3. `STATE.md`: `faz: 0`, `flag: CANVA:BRIEF-ONLY`, `ts` UTC.
4. Kullanıcıya ürün sor; yoksa varsayım yaz → `CONTEXT/` stub.
5. Çıktı: faz tablosu + sonraki adım (`/devam` veya CONTEXT doldur).
