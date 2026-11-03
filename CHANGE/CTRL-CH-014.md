# CTRL-CH-014 — Ortam ayrımı — local agent vs CI vs yok-prod

```yaml
id: CTRL-CH-014
ad: Ortam ayrımı — local agent vs CI vs yok-prod
açıklama: Üretim uygulama sunucusu yok; ayrım: geliştirici workspace / GHA runner / main branch artefaktı.
NIST_CSF: ['Protect']
800-53: ['CM-2', 'SC-2']
ISO27001: ['A.8.31']
CIS: ['CIS-4', 'CIS-16']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: inventory.md ‘uygulama sunucusu yok’ + workflow job sınırları.
savunma_gerekçesi: Yanlışlıkla runner’da canlı secret veya prod mutasyonu önlenir.
```

## Açıklama
Üretim uygulama sunucusu yok; ayrım: geliştirici workspace / GHA runner / main branch artefaktı.

## Doğrulama (ASSESS-ONLY)
- inventory.md ‘uygulama sunucusu yok’ + workflow job sınırları.

## Savunma gerekçesi
Yanlışlıkla runner’da canlı secret veya prod mutasyonu önlenir.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
