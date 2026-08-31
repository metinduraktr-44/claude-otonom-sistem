# CTRL-ENC-001 — Secret at-rest: repo’da plaintext yok

```yaml
id: CTRL-ENC-001
ad: Secret at-rest: repo’da plaintext yok
açıklama: Gerçek secret commit yasak; yalnızca ${VAR}|vault://|op://|<REDACTED>.
NIST_CSF: ['Protect']
800-53: ['SC-28', 'IA-5']
ISO27001: ['A.8.24']
CIS: ['CIS-3']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: python3 scripts/secret_scan.py.
savunma_gerekçesi: Sızıntı ve credential stuffing yüzeyini keser.
```

## Açıklama
Gerçek secret commit yasak; yalnızca ${VAR}|vault://|op://|<REDACTED>.

## Doğrulama (ASSESS-ONLY)
- python3 scripts/secret_scan.py.

## Savunma gerekçesi
Sızıntı ve credential stuffing yüzeyini keser.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
