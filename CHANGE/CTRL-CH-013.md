# CTRL-CH-013 — Kaynak koda erişim — branch/CODEOWNERS ASSESS

```yaml
id: CTRL-CH-013
ad: Kaynak koda erişim — branch/CODEOWNERS ASSESS
açıklama: Kaynak (scripts/, .github/, SECURITY_*) değişikliği PR ile; fork secret izolasyonu hedefi.
NIST_CSF: ['Protect']
800-53: ['AC-3', 'CM-5']
ISO27001: ['A.8.4', 'A.8.3']
CIS: ['CIS-6', 'CIS-16']
OWASP: ['A01:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: CODEOWNERS varlığı ASSESS; branch protection insan teyidi (gh api).
savunma_gerekçesi: Kaynak bütünlüğü tedarik zinciri ve yetkisiz değişiklik riskini keser.
```

## Açıklama
Kaynak (scripts/, .github/, SECURITY_*) değişikliği PR ile; fork secret izolasyonu hedefi.

## Doğrulama (ASSESS-ONLY)
- CODEOWNERS varlığı ASSESS; branch protection insan teyidi (gh api).

## Savunma gerekçesi
Kaynak bütünlüğü tedarik zinciri ve yetkisiz değişiklik riskini keser.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
