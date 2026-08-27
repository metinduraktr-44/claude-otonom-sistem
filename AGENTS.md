# AGENTS.md — Claude Otonom Sistem + Creative Agency OS

## Product
Self-improving Claude orchestration (Holding HQ) + **Otonom AI Creative Agency Operating System** (GIGA Master bootstrap). Runtime = Python 3 stdlib + Bash + GitHub Actions. `katalog/` = MIT vendored templates (davila7), not app dependencies.

## Creative Agency OS (GIGA Master — Faz 0 iskelet)
- **Durum:** `STATE.md` — phase=0, CANVA=BRIEF-ONLY (varsayılan)
- **Bağlam:** `CONTEXT/CONTEXT_BRIEF.md` — post-ingestion TODO
- **Kanal spec:** `MATRIX/CHANNEL_MATRIX.md`
- **Plan:** `.cursor/plans/master-plan.md` (Faz 0–7)
- **Komutlar:** `.cursor/commands/` — `/baslat`, `/devam`, `/canva-uret`, …
- **Skills:** `.cursor/skills/` — Canva pipeline, brief-writer, spec-matrix, …
- **Critics:** `.cursor/agents/` — critic-copy, critic-design, critic-spec (readonly)
- **Canva client:** `tools/canva-client/` (OAuth PKCE TODO)
- **Spec validator:** `python3 scripts/spec_validate.py` → `CANVA_OPS/VALIDATION.log`
- **🚩 Prompt boyutu:** 900k+ karakter tek dosyada YASAK; fazlı `.cursor/rules/*.mdc` + skills ile kümülatif
- **Legacy:** `.cursorrules` → `.cursor/rules/*.mdc` migrasyonu yap (not: eski dosya hâlâ referans)

### Klasör sözleşmeleri
| Klasör | Amaç |
|--------|------|
| `BRIEFS/` | Kampanya brief çıktıları |
| `SCENARIOS/` | Kreatif senaryo/storyboard |
| `MATRIX/` | Kanal × format spec matrisi |
| `CANVA_OPS/` | Design registry, validation log, export metadata |
| `EXPERTS/` | Uzman persona envanteri (Faz 2+) |
| `QA/` | Kalite kontrol raporları |
| `ARCHIVE/` | Arşivlenmiş kampanyalar |
| `RESEARCH/` | Pazar/rakip araştırması |
| `TASKS/` | Master görev listesi |
| `ORG/` | Org chart + skills envanteri |

### Agency komutları (Cursor slash)
`baslat` · `devam` · `resume` · `faz-raporu` · `aylik-dongu` · `canva-uret` · `brief-uret` · `uzman-guncelle` · `spec-dogrula` · `arsivle`

### TODO (post-ingestion — Faz 1+)
- [ ] CONTEXT_BRIEF doldur (marka, kanal, KPI)
- [ ] EXPERTS/ persona seed
- [ ] Canva OAuth PKCE (`tools/canva-client/`)
- [ ] `.cursorrules` → `.mdc` tam migrasyon
- [ ] İlk brief → spec-dogrula → QA döngüsü

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
