# CTRL-L-012 — Gizlilik katmanı — PII minimizasyonu

```yaml
id: CTRL-L-012
ad: Gizlilik katmanı — PII minimizasyonu
açıklama: AUDIT/raporlarda kişisel veri yok; örneklerde <REDACTED>.
NIST_CSF: ['Protect']
800-53: ['SI-12', 'MP-6']
ISO27001: ['A.5.34']
CIS: ['CIS-3']
OWASP: ['A01:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: secret_scan + manuel örnek tarama.
savunma_gerekçesi: KVKK/GDPR uyumlu dokümantasyon hijyeni.
```

## Açıklama
AUDIT/raporlarda kişisel veri yok; örneklerde <REDACTED>.

## Doğrulama (ASSESS-ONLY)
- secret_scan + manuel örnek tarama.

## Savunma gerekçesi
KVKK/GDPR uyumlu dokümantasyon hijyeni.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
