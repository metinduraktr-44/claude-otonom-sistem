# SBOM Minimal Alanlar

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

CycloneDX/SPDX minimal:

| Alan | Örnek holding |
|------|---------------|
| component name | actions/checkout |
| version / hash | SHA veya tag+pin |
| supplier | GitHub / vendor |
| license | MIT/Apache… |
| relationship | workflow → action |

CI SBOM birincil; uygulama pip SBOM N/A (root deps yok).

SLSA: provenance statement bağlama (TC-004).
