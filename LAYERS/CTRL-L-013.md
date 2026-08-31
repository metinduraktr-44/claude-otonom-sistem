# CTRL-L-013 — Değişiklik katmanı — MODE geçiş kaydı

```yaml
id: CTRL-L-013
ad: Değişiklik katmanı — MODE geçiş kaydı
açıklama: ASSESS-ONLY → IMPLEMENT geçişleri açık kapsam + STATE damgası.
NIST_CSF: ['Govern']
800-53: ['CM-3']
ISO27001: ['A.8.32']
CIS: ['CIS-16']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: SECURITY/STATE.md mode alanı.
savunma_gerekçesi: Kontrol uygulamasında yetkisiz değişiklik riskini keser.
```

## Açıklama
ASSESS-ONLY → IMPLEMENT geçişleri açık kapsam + STATE damgası.

## Doğrulama (ASSESS-ONLY)
- SECURITY/STATE.md mode alanı.

## Savunma gerekçesi
Kontrol uygulamasında yetkisiz değişiklik riskini keser.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
