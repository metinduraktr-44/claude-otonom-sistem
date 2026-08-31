# CTRL-ENC-007 — Hash bütünlük (SBOM/artifact)

```yaml
id: CTRL-ENC-007
ad: Hash bütünlük (SBOM/artifact)
açıklama: Yayınlanan artefaktlar için SHA-256 kaydı.
NIST_CSF: ['Protect']
800-53: ['SI-7']
ISO27001: ['A.8.25']
CIS: ['CIS-16']
OWASP: ['A08:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: validate integrity katmanı / holding stamp.
savunma_gerekçesi: Kurcalama tespitini sağlar.
```

## Açıklama
Yayınlanan artefaktlar için SHA-256 kaydı.

## Doğrulama (ASSESS-ONLY)
- validate integrity katmanı / holding stamp.

## Savunma gerekçesi
Kurcalama tespitini sağlar.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
