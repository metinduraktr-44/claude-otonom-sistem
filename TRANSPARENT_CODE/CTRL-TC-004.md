# CTRL-TC-004 — Prompt/skill boyut sinyali

```yaml
id: CTRL-TC-004
ad: Prompt/skill boyut sinyali
açıklama: ≥900B tek pront RED; hybrid skill+refs.
NIST_CSF: ['Govern']
800-53: ['PL-2']
ISO27001: ['A.5.1']
CIS: ['CIS-1']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: CILT14 + IS-LISTESI notu.
savunma_gerekçesi: Bakım ve güvenlik incelemesi ölçeklenebilir kalır.
```

## Açıklama
≥900B tek pront RED; hybrid skill+refs.

## Doğrulama (ASSESS-ONLY)
- CILT14 + IS-LISTESI notu.

## Savunma gerekçesi
Bakım ve güvenlik incelemesi ölçeklenebilir kalır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
