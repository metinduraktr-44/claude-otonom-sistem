# CTRL-TC-001 — Kaynak görünürlüğü — stdlib only runtime

```yaml
id: CTRL-TC-001
ad: Kaynak görünürlüğü — stdlib only runtime
açıklama: Çalışan kod Python stdlib; gizli native blob yok.
NIST_CSF: ['Identify', 'Protect']
800-53: ['SA-15', 'CM-8']
ISO27001: ['A.8.25']
CIS: ['CIS-16']
OWASP: ['A08:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: AGENTS.md + scripts/ import tarama.
savunma_gerekçesi: Tedarik ve denetim şeffaflığı.
```

## Açıklama
Çalışan kod Python stdlib; gizli native blob yok.

## Doğrulama (ASSESS-ONLY)
- AGENTS.md + scripts/ import tarama.

## Savunma gerekçesi
Tedarik ve denetim şeffaflığı.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
