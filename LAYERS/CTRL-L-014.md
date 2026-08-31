# CTRL-L-014 — Şeffaflık katmanı — karar gerekçesi

```yaml
id: CTRL-L-014
ad: Şeffaflık katmanı — karar gerekçesi
açıklama: Her kontrol kartında savunma_gerekçesi ve doğrulama yöntemi zorunlu.
NIST_CSF: ['Govern']
800-53: ['AU-3']
ISO27001: ['A.5.8']
CIS: ['CIS-1']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: compliance-mapper field contract.
savunma_gerekçesi: Denetlenebilir, tekrar edilebilir güvenlik kararları.
```

## Açıklama
Her kontrol kartında savunma_gerekçesi ve doğrulama yöntemi zorunlu.

## Doğrulama (ASSESS-ONLY)
- compliance-mapper field contract.

## Savunma gerekçesi
Denetlenebilir, tekrar edilebilir güvenlik kararları.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
