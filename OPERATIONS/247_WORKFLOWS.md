# 24/7 Workflows — Follow-the-sun stubs

> Updated: 2026-11-15T10:05:00Z · Europe/Istanbul 2026-11-15T13:05:00+03:00

## Shifts (stub)
| Window (UTC) | Focus | Owner stub |
|--------------|-------|------------|
| 00–08 | Nightly validate · AUDIT append | `scripts/nightly.sh` |
| 08–16 | Europe/Istanbul deep work (Metin) | Human gates |
| 16–24 | Agency brief/QA · LATOS cards | Cloud agents |

## C-level daily (5 lines)
1. Read STATE.md (Agency + Security + LATOS)
2. `python3 scripts/validate.py`
3. Triage open PRs / INBOX
4. One bounded wave (cards OR experts OR prompts — not all 633)
5. Stamp AUDIT + BILGI

## Sample team weekly (AdOps CRE)
- Mon: brief backlog
- Tue: scenario critique
- Wed: spec_validate
- Thu: expert/talent delta
- Fri: DIGEST + archive candidates

## Automation hooks
- GHA: validate, daily-agency, nightly, holding-konsolide
- Cursor hooks: secret_scan, ethics_check, qa_check

## Non-goals this stub
- Live paging / on-call rotations
- CANVA:ON production without human gate
- Security IMPLEMENT mode
