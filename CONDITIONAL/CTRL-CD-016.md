# CTRL-CD-016 — Koşullu: yasal/sözleşmesel kapsam (repo OS)

```yaml
id: CTRL-CD-016
ad: Koşullu: yasal/sözleşmesel kapsam (repo OS)
açıklama: Bu depo kişisel veri işlemcisi iddiası yok; lisans MIT vendored + holding içeriği. KVKK/GDPR pack ayrı tur.
NIST_CSF: ['Govern']
800-53: ['PL-1', 'AU-1']
ISO27001: ['A.5.31', 'A.5.34']
CIS: ['CIS-3']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: SECURITY.md raporlama yolu; LICENSE; COMPLIANCE SoA N/A gerekçeleri.
savunma_gerekçesi: Kapsam dışı iddia denetimde şişirme ve sahte sertifika riskini önler.
```

## Açıklama
Bu depo kişisel veri işlemcisi iddiası yok; lisans MIT vendored + holding içeriği. KVKK/GDPR pack ayrı tur.

## Doğrulama (ASSESS-ONLY)
- SECURITY.md raporlama yolu; LICENSE; COMPLIANCE SoA N/A gerekçeleri.

## Savunma gerekçesi
Kapsam dışı iddia denetimde şişirme ve sahte sertifika riskini önler.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
