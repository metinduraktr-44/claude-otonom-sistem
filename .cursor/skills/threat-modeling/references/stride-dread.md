# STRIDE / DREAD (defense)

Use STRIDE for design review; DREAD for prioritization of *findings* already in scope for remediation — not for attack recipes.

| STRIDE | Control focus |
|--------|---------------|
| Spoofing | AuthN, MFA, mTLS |
| Tampering | Integrity, signing, WORM logs |
| Repudiation | Audit trails, non-repudiation |
| Info disclosure | Encryption, least privilege |
| DoS | Rate limits, capacity, circuit breakers |
| Elevation | RBAC/ABAC, privilege boundaries |

Map findings → NIST CSF / D3FEND. MODE=ASSESS-ONLY by default.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
