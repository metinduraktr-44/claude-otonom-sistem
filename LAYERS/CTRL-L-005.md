# CTRL-L-005 — Uygulama katmanı — girdi doğrulama standardı

```yaml
id: CTRL-L-005
ad: Uygulama katmanı — girdi doğrulama standardı
açıklama: Python CLI argümanları ve agent çıktıları için doğrulama/sanitize standardı (defense).
NIST_CSF: ['Protect']
800-53: ['SI-10']
ISO27001: ['A.8.28']
CIS: ['CIS-16']
OWASP: ['A03:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: scripts/ argparse kullanımı örnek incelemesi; SECURITY_QA checklist.
savunma_gerekçesi: Injection ve path traversal sınıfı kusurları önler (kod üretimi bağlamında).
```

## Açıklama
Python CLI argümanları ve agent çıktıları için doğrulama/sanitize standardı (defense).

## Doğrulama (ASSESS-ONLY)
- scripts/ argparse kullanımı örnek incelemesi; SECURITY_QA checklist.

## Savunma gerekçesi
Injection ve path traversal sınıfı kusurları önler (kod üretimi bağlamında).

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
