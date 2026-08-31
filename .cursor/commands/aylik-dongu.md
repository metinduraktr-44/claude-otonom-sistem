---
name: aylik-dongu
description: Aylık uzman/yetenek arşiv döngüsü.
---

# /aylik-dongu

## Objective
Tüm motorlarda READ→DELTA→DIFF→WRITE→DIGEST; ARCHIVE snapshot.

## Output
Digest + STATE güncellemesi.

## Security OS
If `SECURITY/STATE.md` active: follow `.cursor/plans/security-master-plan.md`. MODE=ASSESS-ONLY unless scoped.
