---
name: canva-export-pipeline
description: Export Canva designs and register in DESIGN_REGISTRY.csv
---

# canva-export-pipeline

Export PNG/PDF → `CANVA_OPS/exports/` → append registry row → `spec_validate.py`.
Fail soft; log errors to VALIDATION.log.

