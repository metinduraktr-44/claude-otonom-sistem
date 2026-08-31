# CTRL-TC-011 — Matris ↔ kontrol çift yönlü link

```yaml
id: CTRL-TC-011
ad: Matris ↔ kontrol çift yönlü link
açıklama: matrix.md her kontrolü listeler; kontrol matrix’e pointer.
NIST_CSF: ['Govern']
800-53: ['CA-2']
ISO27001: ['A.5.35']
CIS: ['CIS-1']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: SECURITY_MATRIX/matrix.md.
savunma_gerekçesi: Gap analizinde tek kaynak.
```

## Açıklama
matrix.md her kontrolü listeler; kontrol matrix’e pointer.

## Doğrulama (ASSESS-ONLY)
- SECURITY_MATRIX/matrix.md.

## Savunma gerekçesi
Gap analizinde tek kaynak.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
