# CTRL-L-010 — Tedarik zinciri katmanı — bağımlılık sınırı

```yaml
id: CTRL-L-010
ad: Tedarik zinciri katmanı — bağımlılık sınırı
açıklama: katalog/ vendored; root’ta pip/npm yok; CI pin’li actions.
NIST_CSF: ['Protect', 'Identify']
800-53: ['SA-12', 'CM-8']
ISO27001: ['A.5.19', 'A.5.21']
CIS: ['CIS-16']
OWASP: ['A06:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: AGENTS.md + validate workflows; SBOM stub sbom-provenance.
savunma_gerekçesi: Üçüncü parti risk yüzeyini bilinçli tutar.
```

## Açıklama
katalog/ vendored; root’ta pip/npm yok; CI pin’li actions.

## Doğrulama (ASSESS-ONLY)
- AGENTS.md + validate workflows; SBOM stub sbom-provenance.

## Savunma gerekçesi
Üçüncü parti risk yüzeyini bilinçli tutar.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
