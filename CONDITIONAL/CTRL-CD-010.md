# CTRL-CD-010 — Koşullu: compliance paket yalnız map

```yaml
id: CTRL-CD-010
ad: Koşullu: compliance paket yalnız map
açıklama: ASSESS-ONLY’de compliance = eşleme; sertifika iddiası yok.
NIST_CSF: ['Govern']
800-53: ['CA-2']
ISO27001: ['A.5.35']
CIS: ['CIS-1']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: /compliance-paket komutu.
savunma_gerekçesi: Sahte sertifikasyon iddiasını önler.
```

## Açıklama
ASSESS-ONLY’de compliance = eşleme; sertifika iddiası yok.

## Doğrulama (ASSESS-ONLY)
- /compliance-paket komutu.

## Savunma gerekçesi
Sahte sertifikasyon iddiasını önler.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
