# Master Plan — Creative Agency OS (Canva Dual-Mode)

## Faz 0 — Bootstrap
Dizinler, `.cursor/*`, hooks, mcp, `STATE.md`, validate scripts.

## Faz 1 — Context
`CONTEXT/BRAND.md` · `PRODUCT.md` · `VOICE.md` · `FORBIDDEN.md`

## Faz 2 — Research
`RESEARCH/` kaynaklı notlar (URL + ts). Uydurma yok.

## Faz 3 — Org + Experts
`ORG/` creative ladder · `EXPERTS/` seed+status+sources.

## Faz 4 — Scenarios
2–3 paralel ajan → `SCENARIOS/{urun}/{n}/` izole brief/varyant.

## Faz 5 — Matrix + Briefs
`MATRIX/SPEC.md` · `CHECKLIST.md` · `BRIEFS/{urun}/BRIEF.md`

## Faz 6 — Canva Ops
BRIEF-ONLY (default) veya CANVA:ON → MCP/client · registry · validation.

## Faz 7 — QA + Archive
`QA/REPORT.md` · `ARCHIVE/{YYYY-MM}/` · aylık döngü kancası.

## Exit criteria (sistem)
- `python3 scripts/validate.py` → GECTI
- `python3 scripts/spec_validate.py --help` çalışır
- Kullanıcı BAŞLAT/DEVAM/CANVA:ON akışını çalıştırabilir
