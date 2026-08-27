# CTRL-L-007 — Tespit katmanı — log/telemetri minimum set

```yaml
id: CTRL-L-007
ad: Tespit katmanı — log/telemetri minimum set
açıklama: AUDIT_LOG.jsonl, workflow logları, secret_scan/ethics_check çıktıları için minimum görünürlük.
NIST_CSF: ['Detect']
800-53: ['AU-2', 'AU-6']
ISO27001: ['A.8.15', 'A.8.16']
CIS: ['CIS-8']
OWASP: ['A09:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: validate.yml + secret_scan hook kanıtı REPORTS/.
savunma_gerekçesi: Olay yanıtı ve uyumluluk için izlenebilirlik.
```

## Açıklama
AUDIT_LOG.jsonl, workflow logları, secret_scan/ethics_check çıktıları için minimum görünürlük.

## Doğrulama (ASSESS-ONLY)
- validate.yml + secret_scan hook kanıtı REPORTS/.

## Savunma gerekçesi
Olay yanıtı ve uyumluluk için izlenebilirlik.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
