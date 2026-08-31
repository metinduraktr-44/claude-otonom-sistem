# Security Inventory — Faz 0 Ingestion

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**MODE:** ASSESS-ONLY · **ts:** 2026-08-27T12:37:54Z · **branch track:** `cursor/security-giga-bootstrap-8e8f`

## Repo kimliği
| Alan | Değer |
|------|-------|
| Repo | `metinduraktr-44/claude-otonom-sistem` |
| Tip | Holding HQ otomasyon (Python 3 stdlib + Bash + GHA) |
| Uygulama sunucusu | Yok (script/CI odaklı) |
| Vendored | `katalog/` (MIT templates — tarama kapsamı dışı önerilir) |

## Dil / artefakt dağılımı (katalog hariç kabaca)
| Tür | Gözlem |
|-----|--------|
| Markdown | Ağır içerik (`docs/`, `uretim/`, `pilots/`) |
| Python | `scripts/` (~16 dosya) — LLM client, rapor, validate |
| YAML | `.github/workflows/` (12 workflow) |
| Terraform | `infra/terraform/observability/` |
| OTel | `infra/otel/opentelemetry-collector.yaml` |
| JSON data | `data/*.json` (holding/skill envanter) |

## CI/CD
- `validate.yml`, `validate-components.yml`, `repo-health.yml`
- `nightly-improve.yml`, `daily-agency.yml`, holding/skill döngüleri
- `enterprise-k8s-otel-pipeline.yml` (observability pipeline şablonu)
- `upstream-sync.yml`

## Auth / secret tüketimi (değer yok — tip+konum)
| Konum | Tip | Not |
|-------|-----|-----|
| `.env.example` | placeholder env keys (boş değer) | OK — örnek |
| `docs/SECRETS-DRYRUN-MATRISI.md` | secret **adları** kataloğu | değer yok |
| `scripts/gemini_client.py` | `GEMINI_API_KEY` / `GOOGLE_API_KEY` env | dry-run yoksa |
| `scripts/openrouter_client.py` | `OPENROUTER_API_KEY` | dry-run |
| `scripts/holding_report.py` | `GITHUB_TOKEN` | dry-run statik |
| `scripts/llm_smoke.py` | OpenRouter/Gemini/Anthropic keys | smoke |
| `infra/terraform/observability/variables.tf` | sensitive vars: datadog/sentry token **tipleri** | tfvars.example kullan |
| `SECURITY.md` | vulnerability reporting policy | e-posta iletişim |

**Bulunan gerçek secret değeri:** yok (Faz 0 tarama — pattern scan sonrası teyit).

## Bağımlılıklar
- Root `requirements.txt` / `package.json` **yok** (bilinçli stdlib-only)
- `katalog/` nested npm/pip → **vendored**; günlük işte install yok
- GHA: `actions/checkout`, `actions/setup-python`

## Holding / agency çapraz
- Holding org & skill verisi: `data/`, `docs/HOLDING-*`
- Creative Agency GIGA: ayrı branch `cursor/giga-master-bootstrap-8e8f` (`.cursor/` agency) — bu track security additive
- Mevcut güvenlik dokümanı: `SECURITY.md`, `docs/SECRETS-DRYRUN-MATRISI.md`, `docs/CILT4-COWORK-MASTER-TALIMATI.md` (5 güvenlik kuralı)

## IaC / observability yüzey
- Terraform observability modülü (Datadog/Sentry değişkenleri sensitive)
- OTel collector config
- K8s otel pipeline workflow (şablon)

## Güvenlik OS eklenenler (bu bootstrap)
- `.cursor/rules` security · hooks · sec commands · skills iskelet
- `scripts/secret_scan.py`, `scripts/ethics_check.py`
- `tools/security-scanners/` scaffold
