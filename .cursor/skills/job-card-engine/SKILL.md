---
name: job-card-engine
description: İş kartı motoru — CARD.md + H00N self-expand; dolgu yok.
---

# job-card-engine

## Instructions
1. Hibrit: bu skill yoksa / yüklenmediyse LATOS master prompt inline adımlarını uygula — çıktı yolu aynı.
2. Girdi: `ROSTER/TITLE_INVENTORY.md` + `LATOS/STATE.md`.
3. Kanıt yoksa `unverified`; uydurma yok.
4. Bitince STATE güncelle + ≤10 satır rapor.

## Examples
- `/title-kesif` → title-discovery
- `/is-karti` → job-card-engine

## References
- `references/TODO.md` — derinleşme stub (FAZ’larda genişler)
