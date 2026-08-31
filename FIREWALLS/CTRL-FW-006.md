# CTRL-FW-006 — SSH/port yönetim politikası

```yaml
id: CTRL-FW-006
ad: SSH/port yönetim politikası
açıklama: Repo’da açılacak servis yok; port açma talepleri ASSESS kaydı.
NIST_CSF: ['Protect']
800-53: ['CM-7', 'SC-7']
ISO27001: ['A.8.20']
CIS: ['CIS-4']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: AGENTS.md: no web server runtime.
savunma_gerekçesi: Saldırı yüzeyini sıfırda tutar (stdlib otomasyon).
```

## Açıklama
Repo’da açılacak servis yok; port açma talepleri ASSESS kaydı.

## Doğrulama (ASSESS-ONLY)
- AGENTS.md: no web server runtime.

## Savunma gerekçesi
Saldırı yüzeyini sıfırda tutar (stdlib otomasyon).

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
