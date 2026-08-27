# CTRL-TC-003 — ATT&CK yalnız detection etiketi

```yaml
id: CTRL-TC-003
ad: ATT&CK yalnız detection etiketi
açıklama: attack_detect alanı howto değil; D3FEND ile eşleşir.
NIST_CSF: ['Detect']
800-53: ['SI-4']
ISO27001: ['A.8.16']
CIS: ['CIS-8']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: ethics_check + peer review.
savunma_gerekçesi: Etik sınırın teknik ifadesi.
```

## Açıklama
attack_detect alanı howto değil; D3FEND ile eşleşir.

## Doğrulama (ASSESS-ONLY)
- ethics_check + peer review.

## Savunma gerekçesi
Etik sınırın teknik ifadesi.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
