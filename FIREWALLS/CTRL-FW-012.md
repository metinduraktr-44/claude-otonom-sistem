# CTRL-FW-012 — Segregasyon: katalog vs runtime

```yaml
id: CTRL-FW-012
ad: Segregasyon: katalog vs runtime
açıklama: katalog/ CI/secret_scan skip; runtime scripts/ izole.
NIST_CSF: ['Protect']
800-53: ['SC-2', 'CM-7']
ISO27001: ['A.8.22']
CIS: ['CIS-12']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: secret_scan SKIP_DIRS.
savunma_gerekçesi: Vendored gürültü ve yanlış pozitifleri ayırır.
```

## Açıklama
katalog/ CI/secret_scan skip; runtime scripts/ izole.

## Doğrulama (ASSESS-ONLY)
- secret_scan SKIP_DIRS.

## Savunma gerekçesi
Vendored gürültü ve yanlış pozitifleri ayırır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
