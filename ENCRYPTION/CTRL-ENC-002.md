# CTRL-ENC-002 — Transit TLS 1.2+

```yaml
id: CTRL-ENC-002
ad: Transit TLS 1.2+
açıklama: Harici API’lerde TLS; zayıf cipher önerisi yok (ASSESS).
NIST_CSF: ['Protect']
800-53: ['SC-8', 'SC-13']
ISO27001: ['A.8.24']
CIS: ['CIS-3']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Client kütüphaneleri HTTPS kullanımı.
savunma_gerekçesi: Transit gizlilik.
```

## Açıklama
Harici API’lerde TLS; zayıf cipher önerisi yok (ASSESS).

## Doğrulama (ASSESS-ONLY)
- Client kütüphaneleri HTTPS kullanımı.

## Savunma gerekçesi
Transit gizlilik.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
