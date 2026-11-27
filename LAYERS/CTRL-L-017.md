# CTRL-L-017 — Kimlik doğrulama bilgisi — secret placeholder standardı

```yaml
id: CTRL-L-017
ad: Kimlik doğrulama bilgisi — secret placeholder standardı
açıklama: Parola/token/API anahtarı yalnızca ${VAR}|vault://|op://|<REDACTED>; gerçek değer commit ve sohbet yasağı.
NIST_CSF: ['Protect']
800-53: ['IA-5']
ISO27001: ['A.5.17', 'A.8.5']
CIS: ['CIS-5']
OWASP: ['A07:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: python3 scripts/secret_scan.py; docs/SECRETS-DRYRUN-MATRISI.md.
savunma_gerekçesi: Kimlik doğrulama sırrının sızması diğer kontrolleri geçersiz kılar.
```

## Açıklama
Parola/token/API anahtarı yalnızca ${VAR}|vault://|op://|<REDACTED>; gerçek değer commit ve sohbet yasağı.

## Doğrulama (ASSESS-ONLY)
- python3 scripts/secret_scan.py; docs/SECRETS-DRYRUN-MATRISI.md.

## Savunma gerekçesi
Kimlik doğrulama sırrının sızması diğer kontrolleri geçersiz kılar.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
