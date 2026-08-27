# SECURITY_CONTEXT — Repo envanteri (gerçek)

> Damga: 2026-08-27T12:55:00Z · Kaynak: workspace gözlemi · Uydurma secret/servis YOK

## Runtime gerçeği
| Öğe | Durum |
|-----|--------|
| Dil | Python 3 stdlib (+ Bash) |
| Web sunucu / DB | Yok |
| Root `package.json` / `requirements.txt` | Yok (çalıştırılabilir app için) |
| `katalog/` | Vendored üçüncü parti; **app dependency değil** |
| Secrets | Yalnız `${VAR}` / GitHub `secrets.*` / `<REDACTED>` |

## Kritik yollar
| Yol | Rol |
|-----|-----|
| `scripts/` | Çalıştırılabilir otomasyon |
| `.github/workflows/` | CI (validate, daily, nightly, holding, …) |
| `docs/` · `uretim/` · `pilots/` | İçerik / tanımlar |
| `.cursor/` | Cursor rules/commands/skills (Security + Canva) |
| `tools/security-scanners/` | secret/ethics wrapper |
| `tools/canva-client/` | Canva scaffold (BRIEF-ONLY default) |
| `infra/otel` · `infra/terraform` | Observability iskeleti |

## Workflow envanteri (örnek)
`validate.yml`, `validate-components.yml`, `daily-agency.yml`, `nightly-improve.yml`, `holding-konsolide.yml`, `repo-health.yml`, `enterprise-k8s-otel-pipeline.yml`, …

## Veri sınıfları
→ `data-classes.md`

## Trust boundaries
→ `trust-boundaries.md`

## Varlıklar
→ `assets.md`

MODE=`ASSESS-ONLY`.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
