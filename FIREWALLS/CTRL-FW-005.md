# CTRL-FW-005 — DNS/trust: yalnızca bilinen registry

```yaml
id: CTRL-FW-005
ad: DNS/trust: yalnızca bilinen registry
açıklama: Bağımlılık ve container registry allowlist dokümanı.
NIST_CSF: ['Protect']
800-53: ['SC-7', 'SA-12']
ISO27001: ['A.5.21']
CIS: ['CIS-16']
OWASP: ['A06:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: SECURITY_RESEARCH veya CONTEXT notu.
savunma_gerekçesi: Tedarik zinciri DNS hijack yüzeyini daraltır.
```

## Açıklama
Bağımlılık ve container registry allowlist dokümanı.

## Doğrulama (ASSESS-ONLY)
- SECURITY_RESEARCH veya CONTEXT notu.

## Savunma gerekçesi
Tedarik zinciri DNS hijack yüzeyini daraltır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
