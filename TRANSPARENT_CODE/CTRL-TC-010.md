# CTRL-TC-010 — Kod yorumunda güvenlik iddiası yok

```yaml
id: CTRL-TC-010
ad: Kod yorumunda güvenlik iddiası yok
açıklama: “Bu güvenli” yorumu yerine kontrol ID referansı.
NIST_CSF: ['Govern']
800-53: ['SA-15']
ISO27001: ['A.8.25']
CIS: ['CIS-16']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Code review checklist.
savunma_gerekçesi: Yeşil yıkama (security theater) önleme.
```

## Açıklama
“Bu güvenli” yorumu yerine kontrol ID referansı.

## Doğrulama (ASSESS-ONLY)
- Code review checklist.

## Savunma gerekçesi
Yeşil yıkama (security theater) önleme.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
