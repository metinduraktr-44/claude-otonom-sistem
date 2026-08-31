---
name: baslat-latos
description: LATOS FAZ 0 bootstrap + ingestion başlat; STATE yaz; DEVAM bekle.
---

# /baslat-latos

## Objective
LATOS FAZ 0: eksiği tamamla, CONTEXT brief, STATE güncelle.

## Requirements
- Canva/Security/Cloud bölümlerini silme.
- Rule ID çakışması yaratma (`32-latos-*`).
- 🚩 900M tek shot yok.

## Output
- `LATOS/STATE.md` faz=0→1 hazır
- ≤10 satır rapor + `DEVAM` iste
