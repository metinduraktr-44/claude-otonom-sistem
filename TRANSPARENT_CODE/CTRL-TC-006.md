# CTRL-TC-006 — Hook davranış dokümantasyonu

```yaml
id: CTRL-TC-006
ad: Hook davranış dokümantasyonu
açıklama: fail-open vs failClosed yazılı; sürpriz yok.
NIST_CSF: ['Govern']
800-53: ['CM-6']
ISO27001: ['A.8.9']
CIS: ['CIS-4']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: .cursor/hooks.json + scanner docstring.
savunma_gerekçesi: Operasyonel öngörülebilirlik.
```

## Açıklama
fail-open vs failClosed yazılı; sürpriz yok.

## Doğrulama (ASSESS-ONLY)
- .cursor/hooks.json + scanner docstring.

## Savunma gerekçesi
Operasyonel öngörülebilirlik.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
