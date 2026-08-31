# CTRL-ENC-009 — JWT/Bearer log redaksiyonu

```yaml
id: CTRL-ENC-009
ad: JWT/Bearer log redaksiyonu
açıklama: Bearer token’lar log/raporda <REDACTED>.
NIST_CSF: ['Protect']
800-53: ['AU-9', 'SI-12']
ISO27001: ['A.8.15']
CIS: ['CIS-8']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: secret_scan bearer_jwt_like.
savunma_gerekçesi: Oturum token sızıntısını keser.
```

## Açıklama
Bearer token’lar log/raporda <REDACTED>.

## Doğrulama (ASSESS-ONLY)
- secret_scan bearer_jwt_like.

## Savunma gerekçesi
Oturum token sızıntısını keser.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
