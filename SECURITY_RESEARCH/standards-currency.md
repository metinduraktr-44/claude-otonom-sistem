# Standards Currency — Security OS Crosswalk Seed

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**ts_research:** 2026-08-27T12:54:55Z · **MODE:** ASSESS-ONLY  
Amaç: kontrol motorları ve `compliance-mapper` için güncel sürüm baseline. PoC yok.

## Özet tablo

| Standart | Sürüm / durum | Yayın | Holding OS kullanımı |
|----------|---------------|-------|----------------------|
| NIST CSF | **2.0** (CSWP 29) | 2024-02-26 | Matris kolonları GV/ID/PR/DE/RS/RC |
| NIST SP 800-53 | **Rev. 5** | güncel baseline | Kontrol crosswalk (AC/AU/CM/IA/SC/SI…) |
| ISO/IEC 27001 | **:2022** | 2022-10 | Annex A 93 kontrol temaları |
| CIS Controls | **v8.1** | 2024 güncelleme | IG1 öncelikli holding hygiene |
| OWASP ASVS | **5.0.0** | 2025-05-30 | App/LLM/CI verification checklist |
| PQC FIPS | **203 / 204 / 205** | 2024-08-13 | ENC + crypto-agility roadmap |
| SLSA | **1.0** levels | OpenSSF | TC provenance hedefi |
| NIST ZTMM | Zero Trust Maturity Model | CISA/NIST referans | COND + ZTA skill |

## NIST CSF 2.0
- **Değişiklik:** Govern (GV) fonksiyonu eklendi; SCRM vurgusu.
- **Kaynak:** https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20 · PDF https://nvlpubs.nist.gov/nistpubs/cswp/nist.cswp.29.pdf · DOI https://doi.org/10.6028/NIST.CSWP.29  
- **Holding map:** CISO politika → GV; inventory → ID; secret_scan → PR; hooks → DE; IR skill → RS/RC.

## NIST SP 800-53 Revision 5
- Federal/high-assurance crosswalk için birincil kontrol kataloğu.
- Holding seed: AU (audit), CM (config/CI), IA (tokens), SC (crypto/egress), SI (integrity), SA (supply chain), RA (risk).
- **Kaynak:** https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final (*erişim 2026-08-27*)

## ISO/IEC 27001:2022
- Annex A: 93 kontrol; supply-chain A.5.19–A.5.23; secure coding A.8.28; vulnerability A.8.8.
- **Kaynak özeti (üçüncü parti uyum notu):** ISO 27001:2022 supply-chain kontrolleri yaygın crosswalk’larda A.5.19–23 olarak geçer — resmi metin üyelik gerektirir; ASSESS’te kontrol ID referansı kullanılır, tam metin kopyalanmaz.

## CIS Controls v8.1
- 18 kontrol · 153 safeguard · IG1/IG2/IG3.
- Holding IG1 adayları: Inventory (1), Secure Config (4), Account Mgmt (5), Access Control (6), Continuous Vuln (7), Audit Log (8), Email/Browser N/A düşük, Malware N/A, Data Protection (3), Network (12) egress ASSESS, Security Awareness (14), Service Provider (15) Actions, Application (16) scripts, Incident (17).
- **Kaynak:** CIS Controls overview — https://www.cisecurity.org/controls (*erişim 2026-08-27*); v8.1 cloud/hybrid vurgusu.

## OWASP ASVS 5.0.0
- Canlı: 2025-05-30 Global AppSec EU.
- Holding: Level 1 “impactful few” yaklaşımı CI/secret/integrity checklist’e uyarlanır (klasik web L1 değil).
- **Kaynak:** https://asvs.dev/ · https://github.com/OWASP/ASVS/releases/tag/v5.0.0_release

## Post-Quantum Cryptography (FIPS 203/204/205)
| FIPS | Algoritma | Rol |
|------|-----------|-----|
| 203 | ML-KEM | Key encapsulation |
| 204 | ML-DSA | Primary signatures |
| 205 | SLH-DSA | Hash-based signatures |

- **Kaynak:** https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips · https://csrc.nist.gov/pubs/fips/203/final (*erişim 2026-08-27*)
- Holding: şu an TLS outbound istemci; PQC = crypto-agility **roadmap ASSESS** (acil migrasyon zorunlu değil).

## SLSA + SSDF
- SLSA: provenance, build integrity, dependency verification levels.
- SSDF (NIST SP 800-218): PO/PS/PW/RV — federal yazılım beyanı bağlamı.
- Holding hedef: TC motorunda SBOM (CycloneDX/SPDX) + workflow provenance ASSESS.

## Zero Trust Maturity Model (ZTMM)
- Pillars: Identity, Devices, Networks, Applications/Workloads, Data (+ Cross-cutting Governance/Automation/Visibility).
- Holding: Identity = GHA/OIDC; Workloads = workflows; Data = secrets; Network = egress allowlist ASSESS.

## Currency policy (Security OS)
- Aylık: `/sec-uzman-guncelle` + standards DIGEST yenile.
- Matris satırları sürüm etiketini (`CSF2`, `800-53R5`, `ISO2022`, `CISv8.1`, `ASVS5`) taşır.
- Ücretli tam metin standartlar kopyalanmaz — ID + URL + ASSESS kriteri.

## Damga
Araştırma oturumu: 2026-08-27T12:54:55Z · Denetim hedefi: kaynak URL’leri doğrulanabilir · Exploit içerik: yok
