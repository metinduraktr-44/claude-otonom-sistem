# CTRL-CH-003 — Secret scan gate

```yaml
id: CTRL-CH-003
ad: Secret scan gate
açıklama: secret_scan.py hook/CI; failClosed IDE, fail-open eksik script.
NIST_CSF: ['Protect', 'Detect']
800-53: ['SI-4', 'IA-5']
ISO27001: ['A.8.24']
CIS: ['CIS-3']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: scripts/secret_scan.py --self-test.
savunma_gerekçesi: Secret commit’i erken yakalar.
```

## Açıklama
secret_scan.py hook/CI; failClosed IDE, fail-open eksik script.

## Doğrulama (ASSESS-ONLY)
- scripts/secret_scan.py --self-test.

## Savunma gerekçesi
Secret commit’i erken yakalar.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
