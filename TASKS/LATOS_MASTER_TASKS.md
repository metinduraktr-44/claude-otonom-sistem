# LATOS Master Tasks

> Güncelleme: 2026-11-15T10:15:00Z · Plan: `.cursor/plans/latos-master-plan.md`

## P0 — Aktif / bu dalgada yapılan

| ID | Görev | Sahip | Çıktı | Durum |
|----|-------|-------|-------|-------|
| L-001 | Title envanter 633 | title-discovery | `ROSTER/TITLE_INVENTORY.md` | done |
| L-010b | Org C→worker hierarchy | roadmap-engine | `ORG/ORG_HIERARCHY_C_TO_WORKER.md` | **done 2026-11-15** |
| L-020 | EXPERTS hq-ceo / CISO / adops-cdo seed | latos-expert-engine | `EXPERTS/*/top100_2026-11-15.md` | **done (40+TODO)** |
| L-021 | Experts calendar loop | — | `CALENDAR/EXPERTS_UPDATE.md` | **done** |
| L-040 | Talent taxonomy ~100 + 5 stubs | latos-talent-engine | `SKILLS_TALENT/` + `EXPERTS_TALENT/` | **done** |
| L-050 | Prompts samples (2 titles + team + exec) | prompt-engine | `PROMPTS/...` | **done (not 122×900M)** |
| L-060 | +10 JOB_CARDS | job-card-engine | 53 cumulative | **done** |

## P1 — Sıradaki

| ID | Görev | Sahip | Çıktı |
|----|-------|-------|-------|
| L-022 | Experts Dec DELTA (10 TODO) | latos-expert-engine | new top100 date file |
| L-051 | +5 prompts/title (P006–P010) | prompt-engine | PROMPTS/TITLES |
| L-061 | +10 JOB_CARDS (kalan C-level) | job-card-engine | JOB_CARDS/ |
| L-011 | Research org best practice | — | `RESEARCH/_ORG_BEST_PRACTICE.md` |
| L-070 | #39 SoA rebase note → Metin | security | COMPLIANCE |

## P2 — Backlog (Faz 4+)

- 633 × JOB_CARDS tam üretim (fazlı)
- 633 × 122 prompt (fazlı; 🚩 900M yok)
- 633 × 200 tahmin/gün (Cloud Agent)
- 72 git restore — **yalnızca Metin onayı**

## Bağımlılıklar

L-060 → L-001 · Experts monthly → CALENDAR · Prompts 122 → çoklu wave
