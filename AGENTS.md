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
