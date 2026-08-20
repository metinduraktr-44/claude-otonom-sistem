# HOLDING HQ — TEK SAYFA RAPOR
> Damga: 2026-08-20T11:25:26Z · main @ 753dcfe5 · Onay: Metin (her şey merge)

## HEALTHY
| Kontrol | Durum |
|---|---|
| Open PR | **0** (hepsi merge/closed) |
| PR #17 Domain+OTel+Gemini | MERGED |
| PR #16 OpenRouter | MERGED |
| PR #14 Mega/MIT/Gemini | MERGED |
| PR #13 Holding 500 soru | MERGED |
| Dependabot #10/#11/#15 | MERGED |
| LLM zinciri | Gemini → OpenRouter → Anthropic → iskelet |
| 🚩900M prompt | RED (sözleşme: 122/rol + 500 soru indeksi) |
| Secret commit | YOK (.env gitignore) |

## ROADMAP (healthy path)
1. **Secrets canlı** — Gemini rotate + OpenRouter + (opsiyonel) DD/Sentry/PD
2. **LLM smoke yeşil** — kota/billing sonrası `gemini_client.py smoke`
3. **Observability apply** — TF plan/apply + OTel kubectl (cluster)
4. **Holding ritmi** — daily/weekly/monthly workflows (zaten CI)
5. **İştirak TRANSFER** — adops/performer/… paketlerini hedef repolara sen uygula
6. **Aylık etki arşivi** — top-100 refresh (uydurma bio yok)

## İŞ LİSTESİ — BENDE (agent)
| # | İş | Not |
|---|---|---|
| A1 | AGENTS.md birleşik sürümü main’e | bu PR |
| A2 | Live dashboard LLM satırları | main’de |
| A3 | Domain matrix / OTel / TF artefakt bakımı | `infra/` `data/domain_matrix.json` |
| A4 | Dry-run CI izleme | workflow yeşil tut |
| A5 | Cross-repo push | **yapamam** — TRANSFER paketleri hazır |

## İŞ LİSTESİ — SENDE (Metin)
| # | İş | URL |
|---|---|---|
| M1 | Gemini key **rotate** + Secrets | https://aistudio.google.com/apikey |
| M2 | Gemini kota/billing | https://ai.google.dev/gemini-api/docs/rate-limits |
| M3 | OpenRouter key (2. sıra LLM) | https://openrouter.ai/keys |
| M4 | Cursor Cloud Secrets paneli | https://cursor.com/dashboard |
| M5 | Datadog keys (opsiyonel TF) | https://app.datadoghq.com/organization-settings/api-keys |
| M6 | Sentry token (opsiyonel) | https://sentry.io/settings/account/api/auth-tokens/ |
| M7 | PagerDuty token (opsiyonel) | https://support.pagerduty.com/main/docs/api-access-keys |
| M8 | Slack `#alerts-critical` / `#alerts-warnings` | https://api.slack.com/apps |
| M9 | Cluster’a OTel apply (opsiyonel) | `infra/README.md` |
| M10 | İştirak repolara TRANSFER uygula | `uretim/devir/istirak/*-TRANSFER.md` |

## KOMUTLAR
```bash
python3 scripts/validate.py
python3 scripts/gemini_client.py smoke
python3 scripts/openrouter_client.py smoke
bash scripts/live_dashboard.sh
```
