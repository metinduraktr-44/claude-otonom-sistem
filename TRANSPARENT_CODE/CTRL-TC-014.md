# CTRL-TC-014 — Geliştirme güvenlik testi — validate/ethics/secret kapısı

```yaml
id: CTRL-TC-014
ad: Geliştirme güvenlik testi — validate/ethics/secret kapısı
açıklama: Kabul testi analogu: validate.py GECTI, ethics failClosed, secret warn/redact.
NIST_CSF: ['Protect', 'Detect']
800-53: ['SA-11', 'SI-10']
ISO27001: ['A.8.29', 'A.8.28']
CIS: ['CIS-16']
OWASP: ['A04:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: python3 scripts/validate.py; ethics_check; spec_validate --self-test.
savunma_gerekçesi: Kod kabulünde savunma kapısı olmazsa SoA kâğıtta kalır.
```

## Açıklama
Kabul testi analogu: validate.py GECTI, ethics failClosed, secret warn/redact.

## Doğrulama (ASSESS-ONLY)
- python3 scripts/validate.py; ethics_check; spec_validate --self-test.

## Savunma gerekçesi
Kod kabulünde savunma kapısı olmazsa SoA kâğıtta kalır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
