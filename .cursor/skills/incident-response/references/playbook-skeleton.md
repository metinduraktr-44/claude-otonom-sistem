# IR playbook skeleton (defense)

1. Detect → triage severity
2. Contain (isolate, revoke tokens via vault)
3. Eradicate (patch, rotate `${SECRETS}`)
4. Recover + lessons → `REPORTS/` + `ARCHIVE/`
5. Never include exploit steps; point to vendor advisories.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
