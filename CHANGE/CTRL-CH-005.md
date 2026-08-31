# CTRL-CH-005 — MODE=IMPLEMENT açık kapsam

```yaml
id: CTRL-CH-005
ad: MODE=IMPLEMENT açık kapsam
açıklama: IMPLEMENT yalnız kullanıcı kapsamı + STATE güncellemesi.
NIST_CSF: ['Govern']
800-53: ['CM-3']
ISO27001: ['A.8.32']
CIS: ['CIS-16']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: SECURITY/STATE.md.
savunma_gerekçesi: Sessiz prod değişikliği yok.
```

## Açıklama
IMPLEMENT yalnız kullanıcı kapsamı + STATE güncellemesi.

## Doğrulama (ASSESS-ONLY)
- SECURITY/STATE.md.

## Savunma gerekçesi
Sessiz prod değişikliği yok.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
