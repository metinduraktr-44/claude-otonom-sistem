# CTRL-CH-007 — Dependabot/actions pin ASSESS

```yaml
id: CTRL-CH-007
ad: Dependabot/actions pin ASSESS
açıklama: GitHub Actions major pin; dependabot PR incelemesi.
NIST_CSF: ['Protect']
800-53: ['SA-12', 'CM-2']
ISO27001: ['A.5.21']
CIS: ['CIS-16']
OWASP: ['A06:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: dependabot PR listesi + workflow uses: pin.
savunma_gerekçesi: Tedarik zinciri sürprizlerini azaltır.
```

## Açıklama
GitHub Actions major pin; dependabot PR incelemesi.

## Doğrulama (ASSESS-ONLY)
- dependabot PR listesi + workflow uses: pin.

## Savunma gerekçesi
Tedarik zinciri sürprizlerini azaltır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
