# CTRL-TC-008 — Redaksiyon standardı

```yaml
id: CTRL-TC-008
ad: Redaksiyon standardı
açıklama: Örneklerde sahte secret bile yasak; <REDACTED>.
NIST_CSF: ['Protect']
800-53: ['SI-12']
ISO27001: ['A.5.34']
CIS: ['CIS-3']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: secret_scan patterns.
savunma_gerekçesi: Eğitim materyalinden sızıntı yok.
```

## Açıklama
Örneklerde sahte secret bile yasak; <REDACTED>.

## Doğrulama (ASSESS-ONLY)
- secret_scan patterns.

## Savunma gerekçesi
Eğitim materyalinden sızıntı yok.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
