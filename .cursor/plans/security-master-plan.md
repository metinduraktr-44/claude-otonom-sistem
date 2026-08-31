# Security Master Plan — FAZ 0–8

Default **MODE=ASSESS-ONLY**.

| Faz | Ad | Çıktı | Durum (2026-08-27) |
|-----|-----|-------|---------------------|
| 0 | BOOTSTRAP | rules/commands/skills/hooks + SECURITY/STATE | done |
| 1 | CONTEXT | SECURITY_CONTEXT/ assets & boundaries | done |
| 2 | RESEARCH | SECURITY_RESEARCH/ sourced | seed |
| 3 | ORG+EXPERTS | ORG/ROLES + EXPERTS/_SEED | seed+ |
| 4 | ENGINES | layers/firewall/encryption/… + skill refs | refs+ |
| 5 | MATRIX | SECURITY_MATRIX + starter CTRL catalogs | starter (78) |
| 6 | COMPLIANCE | COMPLIANCE/ paket | next |
| 7 | QA+IR | QA + incident-response stubs | stub |
| 8 | ARCHIVE | ARCHIVE + CALENDAR monthly | open |

FAZ 3 continuous: deepen skill `references/` (not one-shot 20k×20). Seed script: `scripts/giga_security_faz3_seed.py`.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
