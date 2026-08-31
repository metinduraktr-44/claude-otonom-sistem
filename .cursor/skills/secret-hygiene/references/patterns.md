# Secret hygiene patterns

- Never commit real or fake-looking secrets.
- Placeholders only: `${VAR}`, `vault://path`, `op://vault/item`, `<REDACTED>`.
- Scanner: `python3 scripts/secret_scan.py`
- AWS-like key pattern `AKIA[0-9A-Z]{16}` → flag + redact in reports; do not store match.
- Pre-commit / afterFileEdit hook fail-open if script missing; intent failClosed in IDE.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
