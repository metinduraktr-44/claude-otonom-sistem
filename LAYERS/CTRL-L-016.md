# CTRL-L-016 — Kimlik katmanı — iş yükü ve insan kimlik envanteri

```yaml
id: CTRL-L-016
ad: Kimlik katmanı — iş yükü ve insan kimlik envanteri
açıklama: Repo OS kapsamında GitHub org üyeliği, GITHUB_ACTOR ve yerel agent kimliği envanteri; yerel IAM store yok.
NIST_CSF: ['Protect', 'Govern']
800-53: ['IA-2', 'AC-2']
ISO27001: ['A.5.16', 'A.5.18']
CIS: ['CIS-5', 'CIS-6']
OWASP: ['A07:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: ORG/ROLES + inventory.md kimlik satırları; GHA actor koşulları ASSESS.
savunma_gerekçesi: Kimliksiz erişim ve sahte bot hesabı yüzeyini daraltır.
```

## Açıklama
Repo OS kapsamında GitHub org üyeliği, GITHUB_ACTOR ve yerel agent kimliği envanteri; yerel IAM store yok.

## Doğrulama (ASSESS-ONLY)
- ORG/ROLES + inventory.md kimlik satırları; GHA actor koşulları ASSESS.

## Savunma gerekçesi
Kimliksiz erişim ve sahte bot hesabı yüzeyini daraltır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
