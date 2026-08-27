# SBOM & SLSA (Holding)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

## SBOM
- Format: CycloneDX veya SPDX.
- Kapsam (öncelik): `.github/workflows` action graph; opsiyonel `katalog/` ayrı SBOM (vendored).
- Root pip yok → uygulama SBOM minimal; **CI SBOM** asıl değer.
- Saklama: `REPORTS/sbom/` (sonraki tur) veya release asset.

## SLSA ilkeleri → holding
| İlke | ASSESS sorusu |
|------|----------------|
| Provenance | Build kim tarafından, hangi commit? |
| Authenticity | Attestation / immutable release var mı? |
| Integrity | Tag mutable mi? SHA pin mi? |
| Isolation | Job permissions least privilege mi? |

## ISO / CIS / CSF
A.5.21 ICT supply chain · CIS 15/16 · CSF ID.SC / PR.DS · 800-53 SA-12 SI-7

## Kaynak
- SLSA: https://slsa.dev/
- GitHub immutable releases: https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases
- SSDF: NIST SP 800-218
