# CTRL-TC-007 — Raporlarda kanıt yolu

```yaml
id: CTRL-TC-007
ad: Raporlarda kanıt yolu
açıklama: Her gap satırı evidence path ister.
NIST_CSF: ['Detect', 'Govern']
800-53: ['AU-6', 'CA-7']
ISO27001: ['A.5.35']
CIS: ['CIS-8']
OWASP: ['A09:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: GAP-TEMPLATE.md.
savunma_gerekçesi: İddia ≠ kanıt ayrımı.
```

## Açıklama
Her gap satırı evidence path ister.

## Doğrulama (ASSESS-ONLY)
- GAP-TEMPLATE.md.

## Savunma gerekçesi
İddia ≠ kanıt ayrımı.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
