# CTRL-FW-002 — CI network izolasyon notu

```yaml
id: CTRL-FW-002
ad: CI network izolasyon notu
açıklama: GitHub Actions job’larında gereksiz network yok; secrets yalnızca ${{ secrets.* }}.
NIST_CSF: ['Protect']
800-53: ['SC-7', 'AC-4']
ISO27001: ['A.8.21']
CIS: ['CIS-12']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: .github/workflows/*.yml gözden geçirme checklist.
savunma_gerekçesi: Runner üzerinden yan kanal riskini azaltır.
```

## Açıklama
GitHub Actions job’larında gereksiz network yok; secrets yalnızca ${{ secrets.* }}.

## Doğrulama (ASSESS-ONLY)
- .github/workflows/*.yml gözden geçirme checklist.

## Savunma gerekçesi
Runner üzerinden yan kanal riskini azaltır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
