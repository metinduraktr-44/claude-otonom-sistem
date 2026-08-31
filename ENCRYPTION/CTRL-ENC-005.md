# CTRL-ENC-005 — GitHub Actions secret şifreleme varsayımı

```yaml
id: CTRL-ENC-005
ad: GitHub Actions secret şifreleme varsayımı
açıklama: Secrets GitHub encrypted secrets; log’a echo yasak.
NIST_CSF: ['Protect']
800-53: ['IA-5', 'AU-9']
ISO27001: ['A.8.24']
CIS: ['CIS-3']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Workflow’larda echo ${{ secrets.* }} yok.
savunma_gerekçesi: CI log sızıntısını önler.
```

## Açıklama
Secrets GitHub encrypted secrets; log’a echo yasak.

## Doğrulama (ASSESS-ONLY)
- Workflow’larda echo ${{ secrets.* }} yok.

## Savunma gerekçesi
CI log sızıntısını önler.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
