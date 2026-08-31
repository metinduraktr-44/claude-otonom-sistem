# CTRL-CH-011 — Bot commit sınırları

```yaml
id: CTRL-CH-011
ad: Bot commit sınırları
açıklama: CI botları yalnız bilinen dosyaları (AUDIT/HOLDING) günceller.
NIST_CSF: ['Protect']
800-53: ['CM-5', 'AC-6']
ISO27001: ['A.8.32']
CIS: ['CIS-5']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Workflow commit path filter ASSESS.
savunma_gerekçesi: Beklenmeyen bot yazımı engellenir.
```

## Açıklama
CI botları yalnız bilinen dosyaları (AUDIT/HOLDING) günceller.

## Doğrulama (ASSESS-ONLY)
- Workflow commit path filter ASSESS.

## Savunma gerekçesi
Beklenmeyen bot yazımı engellenir.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
