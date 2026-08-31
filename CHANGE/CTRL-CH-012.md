# CTRL-CH-012 — Spec validate (creative+security)

```yaml
id: CTRL-CH-012
ad: Spec validate (creative+security)
açıklama: spec_validate.py self-test; yapısal bütünlük.
NIST_CSF: ['Protect']
800-53: ['CM-4', 'SI-7']
ISO27001: ['A.8.25']
CIS: ['CIS-16']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: python3 scripts/spec_validate.py --self-test.
savunma_gerekçesi: Şablon sapmasını erken yakalar.
```

## Açıklama
spec_validate.py self-test; yapısal bütünlük.

## Doğrulama (ASSESS-ONLY)
- python3 scripts/spec_validate.py --self-test.

## Savunma gerekçesi
Şablon sapmasını erken yakalar.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
