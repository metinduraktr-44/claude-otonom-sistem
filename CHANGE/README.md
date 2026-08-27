# CHANGE

Starter control catalog (FAZ 3 expansion). MODE=`ASSESS-ONLY`.

| ID | Ad | NIST CSF |
|----|----|----------|
| [CTRL-CH-001](CTRL-CH-001.md) | PR zorunlu inceleme (branch protection ASSESS) | Protect, Govern |
| [CTRL-CH-002](CTRL-CH-002.md) | CI validate gate | Protect, Detect |
| [CTRL-CH-003](CTRL-CH-003.md) | Secret scan gate | Protect, Detect |
| [CTRL-CH-004](CTRL-CH-004.md) | Ethics check gate | Govern |
| [CTRL-CH-005](CTRL-CH-005.md) | MODE=IMPLEMENT açık kapsam | Govern |
| [CTRL-CH-006](CTRL-CH-006.md) | Changelog / AUDIT satırı (anlamlı tur) | Govern, Detect |
| [CTRL-CH-007](CTRL-CH-007.md) | Dependabot/actions pin ASSESS | Protect |
| [CTRL-CH-008](CTRL-CH-008.md) | Geri alma prosedürü | Recover |
| [CTRL-CH-009](CTRL-CH-009.md) | Doküman vs kod ayrımı | Govern |
| [CTRL-CH-010](CTRL-CH-010.md) | FEATURE branch adlandırma | Govern |
| [CTRL-CH-011](CTRL-CH-011.md) | Bot commit sınırları | Protect |
| [CTRL-CH-012](CTRL-CH-012.md) | Spec validate (creative+security) | Protect |

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
