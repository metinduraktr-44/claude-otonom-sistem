# CTRL-FW-007 — WAF/CDN kontrolü (uygulanabilirlik notu)

```yaml
id: CTRL-FW-007
ad: WAF/CDN kontrolü (uygulanabilirlik notu)
açıklama: Bu repo için N/A; holding web varlıkları için pointer.
NIST_CSF: ['Protect']
800-53: ['SC-7']
ISO27001: ['A.8.20']
CIS: ['CIS-13']
OWASP: ['A05:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Gap: N/A bu repo; MATRIX’te işaretle.
savunma_gerekçesi: Kapsam kaymasını önler; yanlış WAF iddiası yok.
```

## Açıklama
Bu repo için N/A; holding web varlıkları için pointer.

## Doğrulama (ASSESS-ONLY)
- Gap: N/A bu repo; MATRIX’te işaretle.

## Savunma gerekçesi
Kapsam kaymasını önler; yanlış WAF iddiası yok.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
