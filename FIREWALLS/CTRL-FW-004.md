# CTRL-FW-004 — Webhook imza doğrulama standardı

```yaml
id: CTRL-FW-004
ad: Webhook imza doğrulama standardı
açıklama: Gelecek webhook entegrasyonları için HMAC doğrulama şablonu (IMPLEMENT kapsamı ayrı).
NIST_CSF: ['Protect']
800-53: ['SC-8', 'IA-9']
ISO27001: ['A.8.24']
CIS: ['CIS-13']
OWASP: ['A07:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Şablon ASSESSMENTS/webhook-hmac.md (plan).
savunma_gerekçesi: Sahte olay enjeksiyonunu önler.
```

## Açıklama
Gelecek webhook entegrasyonları için HMAC doğrulama şablonu (IMPLEMENT kapsamı ayrı).

## Doğrulama (ASSESS-ONLY)
- Şablon ASSESSMENTS/webhook-hmac.md (plan).

## Savunma gerekçesi
Sahte olay enjeksiyonunu önler.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
