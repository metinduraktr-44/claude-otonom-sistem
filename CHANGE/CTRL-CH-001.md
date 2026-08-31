# CTRL-CH-001 — PR zorunlu inceleme (branch protection ASSESS)

```yaml
id: CTRL-CH-001
ad: PR zorunlu inceleme (branch protection ASSESS)
açıklama: main’e doğrudan push yok; PR + review beklentisi.
NIST_CSF: ['Protect', 'Govern']
800-53: ['CM-3', 'CM-5']
ISO27001: ['A.8.32']
CIS: ['CIS-16']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: GitHub branch protection ASSESS notu ORG/.
savunma_gerekçesi: Kontrolsüz değişiklik riskini düşürür.
```

## Açıklama
main’e doğrudan push yok; PR + review beklentisi.

## Doğrulama (ASSESS-ONLY)
- GitHub branch protection ASSESS notu ORG/.

## Savunma gerekçesi
Kontrolsüz değişiklik riskini düşürür.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
