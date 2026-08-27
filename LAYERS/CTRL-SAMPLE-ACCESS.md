# CTRL-SAMPLE-ACCESS — Least privilege access

```yaml
id: CTRL-SAMPLE-ACCESS
title: Least privilege access
nist_csf: [Protect]
nist_800_53: [AC-2, AC-3, AC-6]
iso27001: [A.5.15, A.8.2]
d3fend: [D3-LRA, D3-UAP]
attack_detect: [T1078]  # detection coverage label only
owner: IAM Lead
status: assess
evidence: []
secrets: []  # use ${VAR} / vault:// only if referencing
```

## Objective
Enforce least privilege for human and workload identities.

## Assessment checklist (ASSESS-ONLY)
- [ ] Inventory of roles documented
- [ ] Break-glass procedure exists (vault://)
- [ ] MFA required for privileged paths
- [ ] Periodic access review scheduled (`CALENDAR/`)

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
