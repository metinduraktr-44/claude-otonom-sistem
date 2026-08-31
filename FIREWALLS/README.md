# FIREWALLS

Starter control catalog (FAZ 3 expansion). MODE=`ASSESS-ONLY`.

| ID | Ad | NIST CSF |
|----|----|----------|
| [CTRL-FW-001](CTRL-FW-001.md) | Egress allowlist politikası (doküman) | Protect |
| [CTRL-FW-002](CTRL-FW-002.md) | CI network izolasyon notu | Protect |
| [CTRL-FW-003](CTRL-FW-003.md) | MCP stub varsayılan OFF | Protect, Govern |
| [CTRL-FW-004](CTRL-FW-004.md) | Webhook imza doğrulama standardı | Protect |
| [CTRL-FW-005](CTRL-FW-005.md) | DNS/trust: yalnızca bilinen registry | Protect |
| [CTRL-FW-006](CTRL-FW-006.md) | SSH/port yönetim politikası | Protect |
| [CTRL-FW-007](CTRL-FW-007.md) | WAF/CDN kontrolü (uygulanabilirlik notu) | Protect |
| [CTRL-FW-008](CTRL-FW-008.md) | API rate-limit beklentisi | Protect |
| [CTRL-FW-009](CTRL-FW-009.md) | İç/dış trafik sınıflandırması | Identify |
| [CTRL-FW-010](CTRL-FW-010.md) | Host firewall baseline (ASSESS) | Protect |
| [CTRL-FW-011](CTRL-FW-011.md) | TLS zorunluluğu (harici) | Protect |
| [CTRL-FW-012](CTRL-FW-012.md) | Segregasyon: katalog vs runtime | Protect |

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
