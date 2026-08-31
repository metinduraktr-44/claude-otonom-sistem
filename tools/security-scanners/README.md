# tools/security-scanners — defense only

Wrappers around repo `scripts/secret_scan.py` + `scripts/ethics_check.py`.
**No attack tools.** Optional Semgrep/Snyk require user credentials — do not claim live without them.

```bash
python3 tools/security-scanners/run_secret_scan.py
python3 tools/security-scanners/run_ethics_check.py
```

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
