# CTRL-CH-002 — CI validate gate

```yaml
id: CTRL-CH-002
ad: CI validate gate
açıklama: validate.yml / validate-components.yml her PR’da.
NIST_CSF: ['Protect', 'Detect']
800-53: ['SI-2', 'CM-4']
ISO27001: ['A.8.25']
CIS: ['CIS-16']
OWASP: ['A08:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: .github/workflows/validate.yml.
savunma_gerekçesi: Bozuk yapılandırma main’e girmez.
```

## Açıklama
validate.yml / validate-components.yml her PR’da.

## Doğrulama (ASSESS-ONLY)
- .github/workflows/validate.yml.

## Savunma gerekçesi
Bozuk yapılandırma main’e girmez.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
