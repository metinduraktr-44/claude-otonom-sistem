# CTRL-CD-004 — Koşullu: GITHUB_TOKEN yoksa static holding

```yaml
id: CTRL-CD-004
ad: Koşullu: GITHUB_TOKEN yoksa static holding
açıklama: holding_report static mode.
NIST_CSF: ['Protect']
800-53: ['AC-3']
ISO27001: ['A.5.15']
CIS: ['CIS-5']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: holding_report.py davranış notu.
savunma_gerekçesi: Yetkisiz API zenginleştirmesi yok.
```

## Açıklama
holding_report static mode.

## Doğrulama (ASSESS-ONLY)
- holding_report.py davranış notu.

## Savunma gerekçesi
Yetkisiz API zenginleştirmesi yok.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
