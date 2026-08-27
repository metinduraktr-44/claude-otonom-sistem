# /canva-uret — Canva tasarım üretimi

## Objective
CANVA:ON modunda brief'ten Canva design create/edit/export pipeline çalıştır.

## Requirements
- Kullanıcı açık onay veya STATE'de CANVA:ON
- Aktif brief: `BRIEFS/` veya CONTEXT_BRIEF
- MCP: `.cursor/mcp.json` canva server
- OAuth yapılandırılmamışsa dry-run + TODO raporla

## Output
- Design ID + export path
- `CANVA_OPS/DESIGN_REGISTRY.csv` satırı
- Spec validation sonucu
