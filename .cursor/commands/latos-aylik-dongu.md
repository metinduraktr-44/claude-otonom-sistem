# /latos-aylik-dongu — Aylık uzman/yetenek güncelleme

## Objective
EXPERTS + EXPERTS_TALENT için READ→DELTA→DIFF→WRITE→DIGEST döngüsü.

## Requirements
- Eski arşivi oku, değişimi tespit et
- Timestamp'li yeni sürüm yaz
- İnsan onayı kapısı — unverified temizlemeden yayınlama
- `CALENDAR/EXPERTS_UPDATE.md` güncelle

## Output
- Delta özeti + digest satırı
