# CTRL-CD-015 — Koşullu: dual-OS çakışma önceliği

```yaml
id: CTRL-CD-015
ad: Koşullu: dual-OS çakışma önceliği
açıklama: Security ethics vs Canva üretimi çakışırsa ethics kazanır.
NIST_CSF: ['Govern']
800-53: ['PL-4']
ISO27001: ['A.5.1']
CIS: ['CIS-14']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: AGENTS.md dual sections + ethics rule.
savunma_gerekçesi: İş hızı etik sınırın üstüne çıkamaz.
```

## Açıklama
Security ethics vs Canva üretimi çakışırsa ethics kazanır.

## Doğrulama (ASSESS-ONLY)
- AGENTS.md dual sections + ethics rule.

## Savunma gerekçesi
İş hızı etik sınırın üstüne çıkamaz.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
