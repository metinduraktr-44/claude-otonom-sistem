# CTRL-CD-012 — Koşullu: arşiv ay sonu

```yaml
id: CTRL-CD-012
ad: Koşullu: arşiv ay sonu
açıklama: /arsivle yalnızca aylık veya açık talep.
NIST_CSF: ['Recover', 'Govern']
800-53: ['AU-7']
ISO27001: ['A.5.33']
CIS: ['CIS-8']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: CALENDAR/ + ARCHIVE/.
savunma_gerekçesi: Arşiv şişkinliğini önler.
```

## Açıklama
/arsivle yalnızca aylık veya açık talep.

## Doğrulama (ASSESS-ONLY)
- CALENDAR/ + ARCHIVE/.

## Savunma gerekçesi
Arşiv şişkinliğini önler.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
