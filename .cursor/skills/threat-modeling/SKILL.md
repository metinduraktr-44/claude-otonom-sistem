---
name: threat-modeling
description: STRIDE/DREAD threat modeling for remediation. DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phish…
---

# threat-modeling

STRIDE/DREAD threat modeling for remediation.

**Mode:** `ASSESS-ONLY` unless user sets `MODE=IMPLEMENT` with explicit scope.

**Guardrail:** DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.

## Expansion (FAZ 3)
Full ~20k char depth is **continuous expansion**, not this PR. Fill `references/TODO.md` stubs iteratively; keep PRs reviewable.

Deep sample: `references/stride-dread.md`

## Inputs / Outputs
- In: SECURITY_CONTEXT/, SECURITY_MATRIX/, TASKS/
- Out: control cards, assessments, REPORTS/ (no secrets)
