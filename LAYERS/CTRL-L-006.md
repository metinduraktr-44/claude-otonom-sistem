# CTRL-L-006 — Veri katmanı — sınıflandırma şeması

```yaml
id: CTRL-L-006
ad: Veri katmanı — sınıflandırma şeması
açıklama: Public / Internal / Confidential / Secret sınıfları; Secret yalnızca ${VAR}|vault://.
NIST_CSF: ['Identify', 'Protect']
800-53: ['MP-3', 'SC-28']
ISO27001: ['A.5.12', 'A.8.11']
CIS: ['CIS-3']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: SECURITY_CONTEXT/data-classes.md.
savunma_gerekçesi: Şifreleme ve erişim kontrollerinin kapsamını belirler.
```

## Açıklama
Public / Internal / Confidential / Secret sınıfları; Secret yalnızca ${VAR}|vault://.

## Doğrulama (ASSESS-ONLY)
- SECURITY_CONTEXT/data-classes.md.

## Savunma gerekçesi
Şifreleme ve erişim kontrollerinin kapsamını belirler.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
