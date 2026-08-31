# CTRL-TC-009 — Agent çıktı sözleşmesi

```yaml
id: CTRL-TC-009
ad: Agent çıktı sözleşmesi
açıklama: Damga + denetim + öğrenim satırı (Holding).
NIST_CSF: ['Govern']
800-53: ['AU-3']
ISO27001: ['A.5.8']
CIS: ['CIS-1']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: CLAUDE.md çıktı sözleşmesi.
savunma_gerekçesi: Zincirlenebilir öğrenme ve denetim.
```

## Açıklama
Damga + denetim + öğrenim satırı (Holding).

## Doğrulama (ASSESS-ONLY)
- CLAUDE.md çıktı sözleşmesi.

## Savunma gerekçesi
Zincirlenebilir öğrenme ve denetim.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
