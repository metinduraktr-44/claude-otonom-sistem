# Algorithm inventory (starter)

| Kullanım | Şimdi | Not |
|----------|-------|-----|
| Git integrity | SHA-1 (git) / SHA-256 artefakt | Git protocol kısıtı |
| Secret scan | Regex patterns | Değer saklama yok |
| TLS egress | Provider default TLS | Client HTTPS |
| Password DB | N/A | Repo auth DB yok |

Zayıf listesi: MD5/SHA1 password, ECB, 1024-bit RSA (yeni).
Değişince ENCRYPTION CTRL-ENC-004 + bu tablo.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
