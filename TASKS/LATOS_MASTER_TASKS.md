# LATOS Master Tasks

> Faz 2 çıktısı iskelet · Plan: `.cursor/plans/latos-master-plan.md`

## P0 — Aktif

| ID | Görev | Sahip | Çıktı | Kabul |
|----|-------|-------|-------|-------|
| L-001 | Title envanter 633 doğrula | title-discovery | `ROSTER/TITLE_INVENTORY.md` | Satır sayısı = role_adet |
| L-002 | Git deleted rol dokümante | title-discovery | CONTEXT_BRIEF + envanter status | İnsan onaysız restore yok |
| L-003 | 2 örnek iş kartı skeleton | job-card-engine | `JOB_CARDS/hq-ceo/`, `adops-ceo/` | CARD.md + INDEX.md |

## P1 — Sıradaki

| ID | Görev | Sahip | Çıktı |
|----|-------|-------|-------|
| L-010 | Org chart LATOS view | roadmap-engine | `ORG/ORG_CHART.md` |
| L-011 | Research org best practice | — | `RESEARCH/_ORG_BEST_PRACTICE.md` |
| L-020 | EXPERTS hq-ceo seed | latos-expert-engine | skeleton top100 |
| L-030 | SKILL_MATRIX | — | `ORG/SKILL_MATRIX.md` |

## P2 — Backlog (Faz 4+)

- 633 × JOB_CARDS tam üretim (fazlı, paralel agent)
- 633 × 122 prompt (fazlı)
- 633 × 200 tahmin/gün (Cloud Agent)

## Bağımlılıklar

L-003 → L-001 tamam · L-010 → L-001 · Faz 4 → Faz 1–3
