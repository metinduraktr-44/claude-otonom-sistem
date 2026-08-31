# CTRL-CD-002 — Koşullu: MODE=IMPLEMENT kapsamı

```yaml
id: CTRL-CD-002
ad: Koşullu: MODE=IMPLEMENT kapsamı
açıklama: IMPLEMENT yalnız listelenmiş kontrol ID’leri.
NIST_CSF: ['Govern']
800-53: ['CM-3', 'AC-3']
ISO27001: ['A.8.32']
CIS: ['CIS-16']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: TASKS/ veya komut argümanı.
savunma_gerekçesi: Kapsam taşmasını önler.
```

## Açıklama
IMPLEMENT yalnız listelenmiş kontrol ID’leri.

## Doğrulama (ASSESS-ONLY)
- TASKS/ veya komut argümanı.

## Savunma gerekçesi
Kapsam taşmasını önler.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
