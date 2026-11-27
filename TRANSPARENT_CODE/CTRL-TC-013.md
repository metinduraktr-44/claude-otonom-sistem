# CTRL-TC-013 — Teknik zafiyet yönetimi — scanner + Dependabot ASSESS

```yaml
id: CTRL-TC-013
ad: Teknik zafiyet yönetimi — scanner + Dependabot ASSESS
açıklama: Zafiyet süreci: secret_scan, ethics_check, Dependabot Actions; exploit PoC yok.
NIST_CSF: ['Identify', 'Detect']
800-53: ['RA-5', 'SI-2']
ISO27001: ['A.8.8']
CIS: ['CIS-7']
OWASP: ['A06:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: .github/dependabot.yml; python3 scripts/secret_scan.py; ethics_check.py.
savunma_gerekçesi: Tespit ve yama hipotezi; silahlandırılmış repro yasak.
```

## Açıklama
Zafiyet süreci: secret_scan, ethics_check, Dependabot Actions; exploit PoC yok.

## Doğrulama (ASSESS-ONLY)
- .github/dependabot.yml; python3 scripts/secret_scan.py; ethics_check.py.

## Savunma gerekçesi
Tespit ve yama hipotezi; silahlandırılmış repro yasak.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
