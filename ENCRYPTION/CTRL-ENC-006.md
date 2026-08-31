# CTRL-ENC-006 — Dosya şifreleme (hassas export)

```yaml
id: CTRL-ENC-006
ad: Dosya şifreleme (hassas export)
açıklama: Confidential sınıfı export’lar için şifreli arşiv politikası.
NIST_CSF: ['Protect']
800-53: ['SC-28', 'MP-4']
ISO27001: ['A.8.10']
CIS: ['CIS-3']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: CANVA_OPS/exports politikası + data-classes.
savunma_gerekçesi: Dışa aktarımda veri koruması.
```

## Açıklama
Confidential sınıfı export’lar için şifreli arşiv politikası.

## Doğrulama (ASSESS-ONLY)
- CANVA_OPS/exports politikası + data-classes.

## Savunma gerekçesi
Dışa aktarımda veri koruması.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
