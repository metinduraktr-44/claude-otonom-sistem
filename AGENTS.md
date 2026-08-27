# AGENTS.md — Claude Otonom Sistem + Security OS

## Product
Self-improving Claude orchestration (Holding HQ) + **Güvenlik Odaklı GIGA MASTER — Otonom AI Security Architecture & Governance OS**. Runtime = Python 3 stdlib + Bash + GitHub Actions. `katalog/` = MIT vendored templates (davila7), not app dependencies.

## Security OS (GIGA Master — Faz 0)
# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

- **Durum:** `STATE.md` → Security OS section · **MODE=`ASSESS-ONLY`** (varsayılan)
- **Bağlam:** `SECURITY_CONTEXT/inventory.md` + `attack-surface.md`
- **Plan:** `.cursor/plans/security-master-plan.md` (Faz 0–8)
- **Matris:** `SECURITY_MATRIX/matrix.md` (6×100 kontrol iskeleti)
- **Komutlar:** `.cursor/commands/` — `/sec-baslat`, `/sec-devam`, `/gap-analizi`, …
- **Skills:** `.cursor/skills/` — layers/firewall/encryption/… engines (iskelet; hybrid inline)
- **Subagents:** `.cursor/agents/` — security-reviewer, compliance-auditor, ethics-checker (`readonly: true`)
- **Scanners:** `python3 scripts/secret_scan.py` · `python3 scripts/ethics_check.py`
- **Holding çapraz:** `docs/SECRETS-DRYRUN-MATRISI.md`, `SECURITY.md`, `infra/`, `.github/workflows/`
- **🚩 Prompt boyutu:** 900k+ tek dosyada YASAK; fazlı rules + skills; Creative Agency track ayrı branch (`cursor/giga-master-bootstrap-8e8f`) — birleştirmede additive tut

### Defense-only (zorunlu)
1. Exploit / malware / phishing / C2 / bypass PoC **YOK**
2. ATT&CK yalnızca tespit/karşı-önlem haritalama; odak **D3FEND**
3. Secret: yalnızca `${VAR}`, `vault://`, `op://`, `<REDACTED>` — gerçek/realistic secret **YOK**
4. Tehlikeli shell (`rm -rf`, `curl|bash`, credential exfil) **YOK**
5. Her faz başı/sonu: `# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok`

### 6×100 kontrol çerçevesi (özet)
| Motor | Klasör | Hedef |
|-------|--------|-------|
| Layers | `LAYERS/` | 100 katmanlı kontrol |
| Firewalls | `FIREWALLS/` | 100 ağ/uygulama engeli |
| Encryption | `ENCRYPTION/` | 100 kripto kontrolü |
| Change | `CHANGE/` | 100 değişiklik protokolü |
| Transparent Code | `TRANSPARENT_CODE/` | 100 şeffaflık/SBOM |
| Conditional | `CONDITIONAL/` | 100 koşullu politika |

### Security dosya ağacı
```
SECURITY_CONTEXT/  SECURITY_RESEARCH/  SECURITY_MATRIX/
LAYERS/ FIREWALLS/ ENCRYPTION/ CHANGE/ TRANSPARENT_CODE/ CONDITIONAL/
ORG/ROLES/  EXPERTS/  TASKS/SECURITY_MASTER.md
IMPLEMENTATION/ ASSESSMENTS/ COMPLIANCE/ ARCHIVE/ CALENDAR/
QA/ MEMORY/ REPORTS/  tools/security-scanners/
.cursor/rules/  .cursor/commands/sec-*  .cursor/skills/*-engine
```

### Security komutları (Cursor slash)
`sec-baslat` · `sec-devam` · `gap-analizi` · `compliance-paket` · `etik-denetim` · `kontrol-uret` · `sec-uzman-guncelle` · `sec-aylik-dongu` · `sec-faz-raporu` · `sec-arsivle`

### Standartlar (referans — ASSESS-ONLY)
NIST CSF 2.0 · CIS Controls · ISO 27001/27701 · SOC 2 · OWASP ASVS/SAMM · D3FEND · SLSA · SBOM (CycloneDX/SPDX) · Zero Trust (NIST 800-207)

### Secret hygiene
`.env` gitignore · `.env.example` boş değerler · Cursor Secrets / GitHub Secrets · `docs/SECRETS-DRYRUN-MATRISI.md` · hooks: secret_scan + redact-secrets

### TODO (Faz 1+)
- [x] SECURITY_RESEARCH derin tarama + kaynak DIGEST (threat/standards/supply-chain)
- [ ] 6×100 kontrol içerik üretimi (fazlı; **120/600** = 001–020×6)
- [ ] Skill derinlik genişletme (~20k/skill; **6 skill** ilk derinlik)
- [x] Canva MCP ile çakışma yok — security MCP örnek dosyada, varsayılan kapalı

## Cursor Cloud specific instructions

This repository is a **Python 3 (standard-library only) + Bash automation system** orchestrated by GitHub Actions. No compiled app, web server, or root `package.json` / `requirements.txt` for runnable code — `python3` is enough. Do **not** `npm install` under `katalog/` for day-to-day work. Optional: `tools/canva-client/` (agency track) / `tools/security-scanners/` (security track).

### What this repo is
- Runnable app = `scripts/`. Content = `docs/`, `pilots/`, `katalog/`, `uretim/`, `infra/`.
- `katalog/` is vendored third-party (davila7/claude-code-templates). Nested package files are **not** repo deps.
- `pilots/` are Claude Code plugin definitions (markdown/JSON), not runnable programs.

### Core scripts (repo root)
- `python3 scripts/validate.py` — `DENETIM: GECTI`
- `python3 scripts/secret_scan.py` — secret pattern warn/redact log
- `python3 scripts/ethics_check.py` — offensive/exploit pattern block
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
- Security MODE default **ASSESS-ONLY** — aggressive code changes yok unless scanner/hook scaffolding.

### Infra
`infra/otel/`, `infra/terraform/observability/`, `.github/workflows/enterprise-k8s-otel-pipeline.yml`

### Reading
`uretim/OZET-TEK-SAYFA.md`, `docs/SECRETS-DRYRUN-MATRISI.md`, `SECURITY_CONTEXT/inventory.md`, `.cursor/plans/security-master-plan.md`

---

## LATOS (Living AI Talent & Organization System)

**Track #LATOS** — Agency (#23) ve Security (#26) ile **additive**; mevcut bölümler silinmez.

### Misyon
Otonom AI org & talent OS: (a) tüm title/rol keşfi (mevcut+silinmiş+arşiv); (b) iş kartı; (c) org hiyerarşi; (d) top-100 uzman + ~100 yetenek; (e) roadmap/prompt/tahmin; (f) self-improving döngü.

### Durum
- **STATE:** `STATE.md` → LATOS bölümü
- **Plan:** `.cursor/plans/latos-master-plan.md` (Faz 0–9)
- **Envanter:** `ROSTER/TITLE_INVENTORY.md` — **633 title, hiçbir title atlanmaz**
- **MODE:** Faz 0–1 bootstrap → skeleton iş kartları

### Komutlar (Cursor slash)
`latos-baslat` · `latos-devam` · `latos-resume` · `latos-faz-raporu` · `latos-aylik-dongu` · `latos-arsivle` · `title-kesif` · `is-karti` · `yetenek-guncelle` · `roadmap` · `prompt-uret` · `tahmin`

### Karakter hedefleri (FAZLI — dürüst)
| Hedef | Faz | Not |
|-------|-----|-----|
| İş kartı 2.000+ char, 200 başlık | 4+ | Faz 0–1: skeleton+INDEX OK |
| 122 prompt/title/ekip | 8+ | Alt dosya `P001.md`… |
| 200 tahmin/gün/title | 9+ | Cloud Agent |
| 900M char/prompt | — | 🚩 Fiziksel imkânsız; hedef korunur, fazlı genişler |

**Hiçbir title atlanmaz** — master liste `ROSTER/TITLE_INVENTORY.md`. Uzman/yetenek listeleri ve tahminler **insan denetimi**; doğrulanamayan `unverified`.

### Dosya ağacı (özet)
```
ROSTER/  JOB_CARDS/  EXPERTS/  EXPERTS_TALENT/  SKILLS_TALENT/
FORECASTS/  PROMPTS/  ROADMAP/  OPERATIONS/  CONTEXT/  RESEARCH/
TASKS/LATOS_MASTER_TASKS.md  ORG/ORG_CHART.md  ARCHIVE/  QA/  MEMORY/
.cursor/skills/*-engine/  .cursor/rules/00-latos-*.mdc  scripts/qa_check.py
```

### Skills
`title-discovery` · `job-card-engine` · `latos-expert-engine` · `latos-talent-engine` · `roadmap-engine` · `prompt-engine` · `forecast-engine` · `archive-loop`

### Subagents (readonly)
`latos-critic` · `latos-trainer` · `latos-archivist`

### Hooks (additive)
`qa_check.py` · `citation_check.py` · `guard.sh` (git kurtarma izinli)
