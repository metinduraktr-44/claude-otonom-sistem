# Crosswalk Seed — Holding Security OS

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**Currency:** `SECURITY_RESEARCH/standards-currency.md` (2026-08-27)

## Kolon sözlüğü
| Kolon | Biçim örneği |
|-------|----------------|
| NIST_CSF | `PR.DS-01` / `GV.OC` |
| 800-53 | `AC-3` / `AU-2` / `SA-12` |
| ISO27001 | `A.8.8` / `A.5.21` |
| CIS | `CIS-3` / `CIS-16` (v8.1 control no) |
| OWASP | `ASVS-5 L1` tema / `A02` |

## Holding hızlı map
| Konu | CSF | 800-53 | ISO | CIS |
|------|-----|--------|-----|-----|
| Secret hygiene | PR.DS | IA-5 SC-28 | A.5.15 A.8.24 | 3 5 |
| Action pin / SBOM | ID.SC PR.DS | SA-12 SI-7 | A.5.21 A.8.28 | 15 16 |
| Logging | DE.CM | AU-2 AU-12 | A.8.15 | 8 |
| Least privilege | PR.AA | AC-3 AC-6 | A.5.15 A.8.2 | 5 6 |
| Crypto/TLS | PR.DS | SC-8 SC-13 | A.8.24 | 3 |
| Change control | GV.PO ID.RA | CM-3 CM-4 | A.8.32 | 4 16 |
| IR | RS.* RC.* | IR-4 IR-5 | A.5.24–26 | 17 |

## Kaynak URL (metin kopyalama yok)
- CSF 2.0: https://doi.org/10.6028/NIST.CSWP.29
- 800-53 R5: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
- ASVS 5.0: https://asvs.dev/
- CIS Controls: https://www.cisecurity.org/controls

## Kural
Belirsiz map → `TBD` + varsayım notu; uydurma kontrol ID yok.
