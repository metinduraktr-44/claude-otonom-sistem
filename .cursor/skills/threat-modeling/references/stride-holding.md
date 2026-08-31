# STRIDE (Holding otomasyon)

| Tehdit | Örnek yüzey | Savunma |
|--------|-------------|---------|
| Spoofing | Sahte bot commit | Branch protection, signed commits ASSESS |
| Tampering | Workflow zehirleme | pin + review |
| Repudiation | AUDIT eksik | AUDIT_LOG + damga |
| Info disc. | Secret commit | secret_scan |
| DoS | LLM rate | client retry/limit |
| Elevation | Agent IMPLEMENT | MODE + CONDITIONAL |

DREAD skorları opsiyonel; howto exploit yok.
Ayrıca: references/stride-dread.md

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
