# CTRL-CH-004 — Ethics check gate

```yaml
id: CTRL-CH-004
ad: Ethics check gate
açıklama: ethics_check.py offensive pattern taraması.
NIST_CSF: ['Govern']
800-53: ['PL-4']
ISO27001: ['A.5.1']
CIS: ['CIS-14']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: scripts/ethics_check.py --self-test.
savunma_gerekçesi: Dual-use içerik üretimini engeller.
```

## Açıklama
ethics_check.py offensive pattern taraması.

## Doğrulama (ASSESS-ONLY)
- scripts/ethics_check.py --self-test.

## Savunma gerekçesi
Dual-use içerik üretimini engeller.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
