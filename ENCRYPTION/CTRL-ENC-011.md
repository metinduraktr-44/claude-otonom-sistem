# CTRL-ENC-011 — Şifre hash politikası (uygulama N/A)

```yaml
id: CTRL-ENC-011
ad: Şifre hash politikası (uygulama N/A)
açıklama: Bu repo auth DB yok; gelecek uygulamalar için Argon2/bcrypt standardı notu.
NIST_CSF: ['Protect']
800-53: ['IA-5']
ISO27001: ['A.8.5']
CIS: ['CIS-5']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Gap N/A + COMPLIANCE notu.
savunma_gerekçesi: Kapsam netliği; yanlış kontrol iddiası yok.
```

## Açıklama
Bu repo auth DB yok; gelecek uygulamalar için Argon2/bcrypt standardı notu.

## Doğrulama (ASSESS-ONLY)
- Gap N/A + COMPLIANCE notu.

## Savunma gerekçesi
Kapsam netliği; yanlış kontrol iddiası yok.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
