# CTRL-CH-010 — FEATURE branch adlandırma

```yaml
id: CTRL-CH-010
ad: FEATURE branch adlandırma
açıklama: cursor/*-<id> şablonu; case collision yok.
NIST_CSF: ['Govern']
800-53: ['CM-2']
ISO27001: ['A.8.9']
CIS: ['CIS-16']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Mevcut branch listesi.
savunma_gerekçesi: Çakışma ve kayıp iş riskini düşürür.
```

## Açıklama
cursor/*-<id> şablonu; case collision yok.

## Doğrulama (ASSESS-ONLY)
- Mevcut branch listesi.

## Savunma gerekçesi
Çakışma ve kayıp iş riskini düşürür.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
