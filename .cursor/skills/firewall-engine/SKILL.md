---
name: firewall-engine
description: Network/policy firewall design (hardening, not bypass). DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phish…
---

# firewall-engine

Network/policy firewall design (hardening, not bypass).

**Mode:** `ASSESS-ONLY` unless user sets `MODE=IMPLEMENT` with explicit scope.

**Guardrail:** DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.

## Expansion (FAZ 3)
Full ~20k char depth is **continuous expansion**, not this PR. Fill `references/TODO.md` stubs iteratively; keep PRs reviewable.

## Inputs / Outputs
- In: SECURITY_CONTEXT/, SECURITY_MATRIX/, TASKS/
- Out: control cards, assessments, REPORTS/ (no secrets)
