<<<<<<< HEAD
# AGENTS.md

## Cursor Cloud specific instructions

This repository (`claude-otonom-sistem`) is a **Python 3 (standard-library only) + Bash automation system** orchestrated by GitHub Actions. There is no compiled app, web server, database, or external package dependency for the runnable code — so no install/build step is required. `python3` (3.11 in CI, 3.12 on the cloud VM) is all that's needed.

### What this repo is
- The runnable "application" is the scripts in `scripts/`. Everything else (`docs/`, `pilots/`, `katalog/`) is content/definitions.
- `katalog/` is a vendored third-party component catalog (davila7/claude-code-templates). The `requirements.txt` / `package.json` files under `katalog/**` belong to those catalog entries and are **not** dependencies of this repo — do not install them.
- `pilots/` are Claude Code plugin definitions (markdown/JSON), not runnable programs.

### Core scripts (run from repo root)
- `python3 scripts/validate.py` — the project's lint/validation ("6-layer" lite: structural + semantic + integrity). Prints `DENETIM: GECTI` on success (exit 0). This is what CI (`.github/workflows/validate.yml`, `validate-components.yml`) runs on every push/PR.
- `python3 scripts/daily_agency.py --dogrula` — deterministic rotation self-test (the closest thing to a unit test). Prints `DOĞRULAMA: GEÇTİ`.
- `python3 scripts/daily_agency.py` — core generator; writes `uretim/gunluk/{date}-{DEPT}.md` and appends to `AUDIT_LOG.jsonl` + `BILGI_TABANI.md`. Modes: `--haftalik` (weekly), `--aylik` (monthly), `--org-json`.
- `python3 scripts/holding_report.py` — writes `docs/HOLDING-KONSOLIDE.md` from `data/holding.json`.
- `bash scripts/nightly.sh` — nightly loop (validate + stamp).

### Non-obvious gotchas
- **Idempotent daily output:** `daily_agency.py` (default mode) writes `uretim/gunluk/{today}-{DEPT}.md` and prints `SKIP (...)` without regenerating if today's file already exists. This is expected — to see a fresh generation, use `--haftalik`/`--aylik` or a day without an existing file.
- **Running scripts mutates tracked files:** the generators append to `AUDIT_LOG.jsonl` / `BILGI_TABANI.md` and overwrite `docs/HOLDING-KONSOLIDE.md`. In CI these are auto-committed by bots. If you run them only to verify the environment, revert with `git restore AUDIT_LOG.jsonl BILGI_TABANI.md docs/HOLDING-KONSOLIDE.md` and delete any new `uretim/**` files so your PR stays focused.
- **Optional `ANTHROPIC_API_KEY`:** `daily_agency.py` and `nightly.sh` call the Anthropic API only when `ANTHROPIC_API_KEY` is set (paid). Without it they run deterministically (skeleton output) — no key is needed for setup/testing.
- **Optional `GITHUB_TOKEN`:** `holding_report.py` enriches output via the GitHub API when `GITHUB_TOKEN` is set; otherwise it runs in static mode.
- All text/output is Turkish; `GECTI`/`GEÇTİ` mean "passed", `KALDI` means "failed".
=======
# AGENTS.md — Claude Otonom Sistem

## Product
Self-improving Claude orchestration (Holding HQ). Runtime = Python 3 stdlib + Bash + GitHub Actions. `katalog/` = MIT vendored templates (davila7), not app dependencies.

## Cursor Cloud specific instructions

- **Update script** should only refresh nothing heavy: `python3 --version` is enough (no root package.json/requirements).
- Do **not** `npm install` under `katalog/` for day-to-day work.
- Generators (`build_org_cards.py`, `build_question_bank.py`, `daily_agency.py`, `install_free_mit_agents.py`) mutate tracked files — after smoke tests, keep intentional commits only.
- **MIT free Status Agents:** `python3 scripts/install_free_mit_agents.py` → `.claude/katalog-mit/` + `data/mit_free_agents_manifest.json`. Docs: `docs/MIT-UCRETSIZ-AGENTS-NIGHTLY.md`.
- **Nightly free mode:** without `OPENROUTER_API_KEY` / `ANTHROPIC_API_KEY`, `scripts/nightly.sh` only stamps + validates (no paid generation).
- Optional LLM priority: OpenRouter → Gemini (`GEMINI_API_KEY`, optional `GEMINI_MODEL=gemini-flash-latest`) → Anthropic. Smoke: `python3 scripts/llm_smoke.py`. Never paste keys in chat; use Secrets panel.
- Standard commands: see `README.md`, `KULLANIM-KILAVUZU.md`, `docs/MEGA-PRONT-MASTER.md`, `docs/CILT11-ENTERPRISE-MCP-ROUTING.md`.
- Slash-skill floods (Twilio/Azure/…): treat as routing inventory (`docs/SKILL-AJANS-HIYERARSI.md`), not mandatory live MCP execution in this VM.
>>>>>>> origin/main
