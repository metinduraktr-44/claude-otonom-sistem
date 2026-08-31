---
description: CANVA:ON ise üret; değilse brief-only dry-run
---

# /canva-uret

- Flag `CANVA:BRIEF-ONLY` → brief + dry-run queue (`CANVA_OPS/QUEUE.md`); MCP yazma yok.
- Flag `CANVA:ON` + MCP auth → skill `canva-production-pipeline`; kullanıcı onayıyla commit.
- Her export → `DESIGN_REGISTRY.csv` + `spec_validate.py`.
