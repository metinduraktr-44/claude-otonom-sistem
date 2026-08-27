# CTRL-L-011 — Agent güvenlik katmanı — ethics guardrail

```yaml
id: CTRL-L-011
ad: Agent güvenlik katmanı — ethics guardrail
açıklama: 05-ethics-guardrail + ethics_check.py; offensive içerik reddi.
NIST_CSF: ['Govern', 'Protect']
800-53: ['PL-4', 'SI-4']
ISO27001: ['A.5.1']
CIS: ['CIS-14']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: python3 scripts/ethics_check.py --self-test.
savunma_gerekçesi: AI ajanların dual-use üretmesini engeller.
```

## Açıklama
05-ethics-guardrail + ethics_check.py; offensive içerik reddi.

## Doğrulama (ASSESS-ONLY)
- python3 scripts/ethics_check.py --self-test.

## Savunma gerekçesi
AI ajanların dual-use üretmesini engeller.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
