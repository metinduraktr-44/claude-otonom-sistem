# /sec-arsivle — Güvenlik arşivi

## Objective
Tamamlanan assessment/compliance paketlerini `ARCHIVE/` altına taşı (kopya+indeks).

## Requirements
- Secret scrub önce (`secret_scan.py`)
- Orijinal yolları indeksle
- Silme yerine arşiv+işaret

## Output
`ARCHIVE/security/{id}/` + indeks satırı
