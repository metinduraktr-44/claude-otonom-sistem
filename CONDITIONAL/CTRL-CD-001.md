# CTRL-CD-001 — Koşullu: CANVA:ON olmadan mutate yok

```yaml
id: CTRL-CD-001
ad: Koşullu: CANVA:ON olmadan mutate yok
açıklama: Canva yazma yalnız flag + OAuth; aksi BRIEF-ONLY.
NIST_CSF: ['Protect', 'Govern']
800-53: ['AC-3', 'AC-24']
ISO27001: ['A.5.15']
CIS: ['CIS-6']
OWASP: ['A01:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: STATE.md flag + AGENTS.md.
savunma_gerekçesi: Yanlışlıkla tasarım mutasyonu engellenir.
```

## Açıklama
Canva yazma yalnız flag + OAuth; aksi BRIEF-ONLY.

## Doğrulama (ASSESS-ONLY)
- STATE.md flag + AGENTS.md.

## Savunma gerekçesi
Yanlışlıkla tasarım mutasyonu engellenir.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
