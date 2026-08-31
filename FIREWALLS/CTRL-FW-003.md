# CTRL-FW-003 — MCP stub varsayılan OFF

```yaml
id: CTRL-FW-003
ad: MCP stub varsayılan OFF
açıklama: Güvenlik MCP’leri example stub; canlı Semgrep/Snyk iddiası yok.
NIST_CSF: ['Protect', 'Govern']
800-53: ['CM-7']
ISO27001: ['A.8.9']
CIS: ['CIS-4']
OWASP: ['A05:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: .cursor/mcp.security.stubs.example.json varlığı.
savunma_gerekçesi: Yanlışlıkla açık tarayıcı/tool yüzeyi oluşturmaz.
```

## Açıklama
Güvenlik MCP’leri example stub; canlı Semgrep/Snyk iddiası yok.

## Doğrulama (ASSESS-ONLY)
- .cursor/mcp.security.stubs.example.json varlığı.

## Savunma gerekçesi
Yanlışlıkla açık tarayıcı/tool yüzeyi oluşturmaz.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
