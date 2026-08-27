---
name: archive-loop
description: READ→DELTA→DIFF→WRITE→DIGEST arşiv döngüsü; ARCHIVE snapshot; ancestor silinmez. Faz 9 + aylık döngü.
---

# Archive Loop

## Instructions
1. Eski sürümü oku (READ)
2. Değişimi tespit et (DELTA)
3. Farkı hesapla (DIFF)
4. Yeni sürüm yaz (WRITE) — timestamp'li
5. Digest üret (DIGEST) → `MEMORY/`, `REPORTS/`
6. Snapshot: `ARCHIVE/YYYY-MM-DD_HHMM/` — silme yok

**Hibrit:** `/latos-arsivle` + `/latos-aylik-dongu` inline.

## Examples
- Uzman listesi v2 → v1 ARCHIVE'da kalır

## Performance Notes
- İnsan onay: self-modification, reward hacking savunması

## Troubleshooting
- Disk büyümesi → compress arşiv, silme yok
