# CTRL-CH-006 — Changelog / AUDIT satırı (anlamlı tur)

```yaml
id: CTRL-CH-006
ad: Changelog / AUDIT satırı (anlamlı tur)
açıklama: Anlamlı güvenlik turlarında AUDIT_LOG tek satır (spam yok).
NIST_CSF: ['Govern', 'Detect']
800-53: ['AU-2']
ISO27001: ['A.8.15']
CIS: ['CIS-8']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: AUDIT_LOG.jsonl örnek satır.
savunma_gerekçesi: İzlenebilirlik vs gürültü dengesi.
```

## Açıklama
Anlamlı güvenlik turlarında AUDIT_LOG tek satır (spam yok).

## Doğrulama (ASSESS-ONLY)
- AUDIT_LOG.jsonl örnek satır.

## Savunma gerekçesi
İzlenebilirlik vs gürültü dengesi.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
