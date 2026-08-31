# CTRL-CH-008 — Geri alma prosedürü

```yaml
id: CTRL-CH-008
ad: Geri alma prosedürü
açıklama: git revert / restore prosedürü; force-push yasak (agent kuralı).
NIST_CSF: ['Recover']
800-53: ['CM-3', 'CP-10']
ISO27001: ['A.8.32']
CIS: ['CIS-16']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: CHANGE/rollback.md pointer.
savunma_gerekçesi: Hatalı değişiklikte hızlı toparlanma.
```

## Açıklama
git revert / restore prosedürü; force-push yasak (agent kuralı).

## Doğrulama (ASSESS-ONLY)
- CHANGE/rollback.md pointer.

## Savunma gerekçesi
Hatalı değişiklikte hızlı toparlanma.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
