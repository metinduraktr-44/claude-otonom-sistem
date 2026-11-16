# 24/7 Workflows — Follow-the-sun + skill links

> Updated: 2026-11-16T13:20:00Z · Europe/Istanbul 2026-11-16T16:20:00+03:00 · skills-wave
> Matrix: `ORG/SKILL_WAVE_MATRIX.md`

## Shifts (stub)
| Window (UTC) | Focus | Owner stub | Skills |
|--------------|-------|------------|--------|
| 00–08 | Nightly validate · AUDIT append | `scripts/nightly.sh` | archive-loop (light) |
| 08–16 | Europe/Istanbul deep work (Metin) | Human gates | — |
| 16–24 | Agency brief/QA · LATOS cards | Cloud agents | job-card / prompt / expert |

## LATOS daily (bounded — pick ONE cluster)
1. Read `STATE.md` (Agency + Security + LATOS)
2. `python3 scripts/validate.py`
3. Triage open PRs / `CONTEXT/INBOX/`
4. One cluster from matrix:
   - `title-discovery` → ROSTER delta
   - `job-card-engine` → +N skeletons
   - `latos-expert-engine` → CALENDAR DELTA
   - `latos-talent-engine` → EXPERTS_TALENT stubs
   - `prompt-engine` → +Pxxx samples (≠122 complete; ≠900M)
   - `forecast-engine` → +≤20/day seed
   - `roadmap-engine` → ROADMAP/247 refresh
   - `archive-loop` → DIGEST/ARCHIVE
5. Stamp AUDIT + BILGI

## Sample team weekly (AdOps CRE)
- Mon: `brief-writer` backlog
- Tue: `creative-scenarios` critique (`PROMPTS/TEAMS/adops-cre/T002.md`)
- Wed: `spec-matrix` + `spec_validate.py`
- Thu: expert/talent DELTA
- Fri: DIGEST + archive candidates

## Automation hooks
- GHA: validate, daily-agency, nightly, holding-konsolide
- Cursor hooks: secret_scan, ethics_check, qa_check
- Execution prompt: `PROMPTS/EXECUTION/validate-stamp/E002.md`

## Non-goals this stub
- Live paging / on-call rotations
- CANVA:ON production without human gate
- Security IMPLEMENT mode
- Infinite skill loops
