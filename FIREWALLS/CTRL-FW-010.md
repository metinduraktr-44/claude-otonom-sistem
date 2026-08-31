# CTRL-FW-010 — Host firewall baseline (ASSESS)

```yaml
id: CTRL-FW-010
ad: Host firewall baseline (ASSESS)
açıklama: Geliştirici host için varsayılan deny inbound checklist.
NIST_CSF: ['Protect']
800-53: ['SC-7', 'CM-6']
ISO27001: ['A.8.9']
CIS: ['CIS-4']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: ASSESSMENTS checklist satırı.
savunma_gerekçesi: Yanlışlıkla açık servis riskini düşürür.
```

## Açıklama
Geliştirici host için varsayılan deny inbound checklist.

## Doğrulama (ASSESS-ONLY)
- ASSESSMENTS checklist satırı.

## Savunma gerekçesi
Yanlışlıkla açık servis riskini düşürür.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
