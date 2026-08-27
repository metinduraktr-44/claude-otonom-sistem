# ENCRYPTION

Starter control catalog (FAZ 3 expansion). MODE=`ASSESS-ONLY`.

| ID | Ad | NIST CSF |
|----|----|----------|
| [CTRL-ENC-001](CTRL-ENC-001.md) | Secret at-rest: repo’da plaintext yok | Protect |
| [CTRL-ENC-002](CTRL-ENC-002.md) | Transit TLS 1.2+ | Protect |
| [CTRL-ENC-003](CTRL-ENC-003.md) | Anahtar yaşam döngüsü (doküman) | Protect |
| [CTRL-ENC-004](CTRL-ENC-004.md) | Kripto çeviklik — algoritma envanteri | Protect, Identify |
| [CTRL-ENC-005](CTRL-ENC-005.md) | GitHub Actions secret şifreleme varsayımı | Protect |
| [CTRL-ENC-006](CTRL-ENC-006.md) | Dosya şifreleme (hassas export) | Protect |
| [CTRL-ENC-007](CTRL-ENC-007.md) | Hash bütünlük (SBOM/artifact) | Protect |
| [CTRL-ENC-008](CTRL-ENC-008.md) | Özel anahtar yok (repo) | Protect |
| [CTRL-ENC-009](CTRL-ENC-009.md) | JWT/Bearer log redaksiyonu | Protect |
| [CTRL-ENC-010](CTRL-ENC-010.md) | Disk şifreleme (host ASSESS) | Protect |
| [CTRL-ENC-011](CTRL-ENC-011.md) | Şifre hash politikası (uygulama N/A) | Protect |
| [CTRL-ENC-012](CTRL-ENC-012.md) | Kriptografik rastgelelik (token üretimi) | Protect |

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
