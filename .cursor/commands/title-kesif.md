# /title-kesif — Faz 1 Title Keşif & Kurtarma

## Objective
Mevcut + silinmiş + arşiv title'ları keşfet; `ROSTER/TITLE_INVENTORY.md` güncelle.

## Requirements
- `data/holding_istirak_org.json` (633 rol) entegre
- Git: `git log --all --diff-filter=D -- uretim/rol-kartlari/`
- `ARCHIVE/`, `CONTEXT/INBOX/` tara
- Hiçbir title düşürülmez

## Output
- Güncellenmiş envanter
- Git kurtarma bulguları (restore insan onaylı)
- `python3 scripts/build_title_inventory.py` çalıştır
