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

> Separate from Cloud Agent testing guidance above. Holding HQ scripts unchanged. Full Canva tree may live on its PR; stub index on this branch.

| Item | Path |
|------|------|
| Index (stub/full) | `docs/CILT13-CURSOR-GIGA-CANVA.md` |
| Checklist | `docs/IS-LISTESI-GIGA-CANVA.md` (Canva PR) |
| Paste | `uretim/devir/CURSOR-GIGA-MASTER-CANVA.md` (Canva PR) |

**Default flag:** `CANVA:BRIEF-ONLY`. Additive with LATOS/Security.

---

## Security Architecture & Governance OS (GIGA)

> Additive to Cloud + Creative Agency. Defense-only. Full tree may live on Security PR; stub index here.

| Item | Path |
|------|------|
| Index (stub/full) | `docs/CILT14-CURSOR-GIGA-SECURITY.md` |
| Checklist | `docs/IS-LISTESI-GIGA-SECURITY.md` (Security PR) |
| Paste | `uretim/devir/CURSOR-GIGA-MASTER-SECURITY.md` (Security PR) |

**Default mode:** `MODE=ASSESS-ONLY`. No exploits / weaponized PoCs.

---

## LATOS — Living AI Talent & Organization System (GIGA)

> Additive to Cloud + Canva + Security. Title/job-card/talent OS. Not a 900M single prompt — 🚩 RED; phased self-expand.

| Item | Path |
|------|------|
| Paste prompt | `uretim/devir/CURSOR-GIGA-MASTER-LATOS.md` |
| Index | `docs/CILT15-CURSOR-GIGA-LATOS.md` |
| Checklist | `docs/IS-LISTESI-GIGA-LATOS.md` |
| Rules | `.cursor/rules/00-latos-core.mdc` … `50-forecast-calibration.mdc` (`32-latos-file-structure` — avoids Canva `30-file-structure`) |
| State | `LATOS/STATE.md` (+ section in root `STATE.md`) |
| Inventory | `ROSTER/TITLE_INVENTORY.md` |
| QA | `python3 scripts/qa_check.py` · `python3 scripts/citation_check.py` |

**Agent commands:** `/baslat-latos` · `/title-kesif` · `/is-karti` · `/uzman-guncelle` · `/yetenek-guncelle` · `/roadmap` · `/prompt-uret` · `/tahmin` · `/aylik-dongu` (+ shared `/devam` `/resume` `/faz-raporu` `/arsivle`)

**Inventory sources:** `data/skill_title_haritasi.json` · `.claude/org/org.json` · `docs/UNVAN-HIYERARSISI.md` · `.claude/agents` · git-deleted `uretim/rol-kartlari/`

**Hybrid:** skill if discovered after restart; else master-prompt inline — same output paths.

**Do not** invent title lists or verified top-100 people; mark `unverified`.
