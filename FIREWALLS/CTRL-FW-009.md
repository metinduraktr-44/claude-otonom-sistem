# CTRL-FW-009 — İç/dış trafik sınıflandırması

```yaml
id: CTRL-FW-009
ad: İç/dış trafik sınıflandırması
açıklama: GitHub API vs public web vs LLM provider ayrımı.
NIST_CSF: ['Identify']
800-53: ['CA-3']
ISO27001: ['A.5.14']
CIS: ['CIS-12']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: trust-boundaries.md tablosu.
savunma_gerekçesi: Firewall kurallarının semantik haritası.
```

## Açıklama
GitHub API vs public web vs LLM provider ayrımı.

## Doğrulama (ASSESS-ONLY)
- trust-boundaries.md tablosu.

## Savunma gerekçesi
Firewall kurallarının semantik haritası.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
