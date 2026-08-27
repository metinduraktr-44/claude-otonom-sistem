# CTRL-TC-002 — Karar gerekçesi zorunlu alan

```yaml
id: CTRL-TC-002
ad: Karar gerekçesi zorunlu alan
açıklama: Kontrol kartlarında savunma_gerekçesi boş olamaz.
NIST_CSF: ['Govern']
800-53: ['AU-3']
ISO27001: ['A.5.8']
CIS: ['CIS-1']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Seed script / QA checklist.
savunma_gerekçesi: Kara kutu güvenlik kararlarını önler.
```

## Açıklama
Kontrol kartlarında savunma_gerekçesi boş olamaz.

## Doğrulama (ASSESS-ONLY)
- Seed script / QA checklist.

## Savunma gerekçesi
Kara kutu güvenlik kararlarını önler.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
