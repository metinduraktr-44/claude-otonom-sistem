# Detection engineering notes

Prefer Sigma/YARA for *detection* content. Map to D3FEND.
ATT&CK technique IDs OK only as detection coverage labels.
Do not ship offensive payloads. MODE=ASSESS-ONLY default.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
