# CTRL-TC-012 — Araştırma kaynak zorunluluğu

```yaml
id: CTRL-TC-012
ad: Araştırma kaynak zorunluluğu
açıklama: SECURITY_RESEARCH notlarında URL/kaynak.
NIST_CSF: ['Identify']
800-53: ['PM-15']
ISO27001: ['A.5.7']
CIS: ['CIS-1']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: SECURITY_RESEARCH/*.md frontmatter.
savunma_gerekçesi: Uydurma uzman/ranking yasaklanır.
```

## Açıklama
SECURITY_RESEARCH notlarında URL/kaynak.

## Doğrulama (ASSESS-ONLY)
- SECURITY_RESEARCH/*.md frontmatter.

## Savunma gerekçesi
Uydurma uzman/ranking yasaklanır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
