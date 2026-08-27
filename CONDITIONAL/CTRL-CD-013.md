# CTRL-CD-013 — Koşullu: MCP enable kullanıcı onayı

```yaml
id: CTRL-CD-013
ad: Koşullu: MCP enable kullanıcı onayı
açıklama: Güvenlik MCP canlıya alınmadan önce kullanıcı enable.
NIST_CSF: ['Protect', 'Govern']
800-53: ['AC-3', 'CM-7']
ISO27001: ['A.8.9']
CIS: ['CIS-4']
OWASP: ['A05:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: mcp stubs example only.
savunma_gerekçesi: Yetkisiz tool yüzeyi açılmaz.
```

## Açıklama
Güvenlik MCP canlıya alınmadan önce kullanıcı enable.

## Doğrulama (ASSESS-ONLY)
- mcp stubs example only.

## Savunma gerekçesi
Yetkisiz tool yüzeyi açılmaz.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
