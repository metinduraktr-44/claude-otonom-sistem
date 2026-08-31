# CTRL-CD-011 — Koşullu: research kaynaksız yayın yok

```yaml
id: CTRL-CD-011
ad: Koşullu: research kaynaksız yayın yok
açıklama: EXPERTS/SECURITY_RESEARCH kaynaksız satır eklenmez.
NIST_CSF: ['Govern']
800-53: ['PM-15']
ISO27001: ['A.5.7']
CIS: ['CIS-1']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: EXPERTS/_SEED.md sources sütunu.
savunma_gerekçesi: Uydurma otorite riskini keser.
```

## Açıklama
EXPERTS/SECURITY_RESEARCH kaynaksız satır eklenmez.

## Doğrulama (ASSESS-ONLY)
- EXPERTS/_SEED.md sources sütunu.

## Savunma gerekçesi
Uydurma otorite riskini keser.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
