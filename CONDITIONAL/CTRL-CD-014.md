# CTRL-CD-014 — Koşullu: gap owner boşsa escalate

```yaml
id: CTRL-CD-014
ad: Koşullu: gap owner boşsa escalate
açıklama: Gap satırında Owner boş → Security Architect kuyruğu.
NIST_CSF: ['Govern']
800-53: ['CA-7', 'PM-9']
ISO27001: ['A.5.2']
CIS: ['CIS-1']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: GAP-TEMPLATE + ORG/ROLES.
savunma_gerekçesi: Sahipsiz risk birikmez.
```

## Açıklama
Gap satırında Owner boş → Security Architect kuyruğu.

## Doğrulama (ASSESS-ONLY)
- GAP-TEMPLATE + ORG/ROLES.

## Savunma gerekçesi
Sahipsiz risk birikmez.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
