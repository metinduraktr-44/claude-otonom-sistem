# AGENTS.md — Claude Otonom Sistem

## Product
Self-improving Claude orchestration (Holding HQ). Runtime = Python 3 stdlib + Bash + GitHub Actions. `katalog/` = MIT vendored templates (davila7), not app dependencies.

## Cursor Cloud specific instructions

This repository is a **Python 3 (standard-library only) + Bash automation system** orchestrated by GitHub Actions. No compiled app, web server, or root `package.json` / `requirements.txt` for runnable code — `python3` is enough. Do **not** `npm install` under `katalog/` for day-to-day work.

### What this repo is
- Runnable app = `scripts/`. Content = `docs/`, `pilots/`, `katalog/`, `uretim/`, `infra/`.
- `katalog/` is vendored third-party (davila7/claude-code-templates). Nested package files are **not** repo deps.
- `pilots/` are Claude Code plugin definitions (markdown/JSON), not runnable programs.

### Core scripts (repo root)
- `python3 scripts/validate.py` — `DENETIM: GECTI`
- `python3 scripts/daily_agency.py --dogrula` / günlük generator
- `python3 scripts/holding_report.py`
- `python3 scripts/gemini_client.py smoke` / `openrouter_client.py smoke`
- `python3 scripts/domain_matrix_uret.py --dogrula`
- `bash scripts/live_dashboard.sh` / `bash scripts/nightly.sh`

### LLM priority
**Gemini → OpenRouter → Anthropic → iskelet.** Keys in Cursor Secrets / `.env` (gitignore). Never paste keys in chat.

### Gotchas
- Daily output idempotent (`SKIP` if today’s file exists).
- Generators mutate `AUDIT_LOG.jsonl` / `BILGI_TABANI.md`.
- No key → dry-run skeleton. Turkish: GECTI=pass, KALDI=fail.
- 🚩 ≥900M chars/prompt RED. Contract: 122 prompts/role + 500 questions/title.

### Infra
`infra/otel/`, `infra/terraform/observability/`, `.github/workflows/enterprise-k8s-otel-pipeline.yml`

### Reading
`uretim/OZET-TEK-SAYFA.md`, `docs/SECRETS-DRYRUN-MATRISI.md`, `uretim/domain-matrix/README.md`

---

## Creative Agency OS / Canva Dual-Mode (GIGA)

> Separate from Cloud Agent testing guidance above. Holding HQ scripts unchanged.

Modular Cursor Creative Agency layer (not a 900B single prompt — 🚩 RED).

| Item | Path |
|------|------|
| Paste prompt | `uretim/devir/CURSOR-GIGA-MASTER-CANVA.md` |
| Index | `docs/CILT13-CURSOR-GIGA-CANVA.md` |
| Checklist | `docs/IS-LISTESI-GIGA-CANVA.md` |
| Rules / commands / skills | `.cursor/` |
| State | `STATE.md` |
| Spec validate | `python3 scripts/spec_validate.py` |
| Canva client scaffold | `tools/canva-client/` |

**Default flag:** `CANVA:BRIEF-ONLY` (no Canva mutate). Live: user says `CANVA:ON` + MCP OAuth (`https://mcp.canva.com/mcp` in `.cursor/mcp.json`). Do not claim Canva is live without credentials.

**Agent commands:** `/baslat` · `/devam` · `/resume` · `/faz-raporu` · `/canva-uret` · `/brief-uret` · `/spec-dogrula` · `/arsivle`

**Parallel agents:** start 2–3; isolate under `SCENARIOS/{urun}/{n}/`.
