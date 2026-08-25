# MASTER — Slash Skill Flood → Holding Ajans (IN-AGENT V3)
> Üretim: 2026-08-25T14:48:10Z · Claude Code paste: **İPTAL** · 🚩900B RED

## Sözleşme
- Skill adedi: **688**
- Domain: **9** · Title kabuk: **30**
- Prompt indeks hedefi: **10980** (122×title×3 katman)
- Tek prompt gövdesi: **4–12 KiB** yapılandırılmış; literal 900M/900B **YOK**
- Top-100 kişi: seed/archive only — **uydurma bio yok**
- Credential yoksa: **dry-run** checklist

## LLM öncelik
Gemini → OpenRouter → Anthropic → iskelet

## Uygula (agent)
1. `python3 scripts/slash_skill_katalog_uret.py`
2. `python3 scripts/skill_ajans_uretim.py --dogrula`
3. `python3 scripts/domain_matrix_uret.py --dogrula`
4. `python3 scripts/title_soru_kisi_uret.py --dogrula`
5. `bash scripts/live_dashboard.sh`

## Domain özeti
| Kod | Ad | Skills | Titles |
|---|---|---:|---:|
| INFRA | Infrastructure & Cloud | 68 | 4 |
| OBS | Observability & Diagnostics | 63 | 4 |
| DATA | Data & Warehouses | 99 | 4 |
| FULLSTACK | Full-Stack & Identity | 88 | 3 |
| COMMS | Comms & Scrapers | 77 | 3 |
| PRDSEC | Product Security AI/ML | 44 | 4 |
| GOV | Governance & Meta | 34 | 3 |
| ANALYTICS | Product Analytics | 42 | 3 |
| GEN | General / Unclassified | 173 | 2 |

## 7×24
| Freq | Owner | Actions |
|---|---|---|
| realtime | OBS | opentelemetry-validation, alert-investigation, tierzero-investigate |
| daily | INFRA | debug-k8s-collection, observability-service-health, gitops-status |
| weekly | PRDSEC | review-security, audit-report, dora-metrics |
| monthly | GOV | exa-web-search, knowledge-update, analyze-costs, title_top_kisiler refresh |
