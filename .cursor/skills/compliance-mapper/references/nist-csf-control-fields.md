# NIST CSF control field contract

Every control card under `LAYERS/` or `SECURITY_MATRIX/` MUST include:

```yaml
id: CTRL-XXX
title: <short>
nist_csf: [Identify|Protect|Detect|Respond|Recover]
nist_800_53: []  # optional
iso27001: []     # optional
d3fend: []       # defensive techniques only
attack_detect: []  # ATT&CK IDs for DETECTION mapping only
owner: <role>
status: planned|assess|implement|verify
evidence: []
```

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
