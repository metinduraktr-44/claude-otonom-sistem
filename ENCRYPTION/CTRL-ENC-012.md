# CTRL-ENC-012 — Kriptografik rastgelelik (token üretimi)

```yaml
id: CTRL-ENC-012
ad: Kriptografik rastgelelik (token üretimi)
açıklama: Gerekirse secrets modülü; zayıf PRNG yasak listesi.
NIST_CSF: ['Protect']
800-53: ['SC-12', 'SC-13']
ISO27001: ['A.8.24']
CIS: ['CIS-3']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Kod inceleme ASSESS checklist.
savunma_gerekçesi: Tahmin edilebilir token riskini azaltır.
```

## Açıklama
Gerekirse secrets modülü; zayıf PRNG yasak listesi.

## Doğrulama (ASSESS-ONLY)
- Kod inceleme ASSESS checklist.

## Savunma gerekçesi
Tahmin edilebilir token riskini azaltır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
