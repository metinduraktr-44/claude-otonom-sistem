# Supply Chain — Defense ASSESS (Holding CI/CD)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**ts_research:** 2026-08-27T12:54:55Z · **MODE:** ASSESS-ONLY

## Neden kritik
Bu repo’nun birincil yürütme yüzeyi **GitHub Actions + generator script’ler**. Üçüncü parti Action / tag mutability, holding sırlarını (API key tipleri, tokens) log’a dökme riski taşır. Saldırı tarifi yok — yalnızca sertleştirme.

## Risk envanteri (holding)

| Bağımlılık yüzeyi | Durum | Risk | Savunma |
|-------------------|-------|------|---------|
| Root pip/npm | Yok (stdlib-only) | Düşük | Koru — yeni dep ekleme gate |
| `katalog/` vendored | MIT templates | Orta (yanlış install) | Runtime dep sayma; tarama skip |
| GHA `actions/*` | checkout, setup-python | Orta | SHA pin ASSESS; permissions |
| Üçüncü parti Actions | workflow tarama gerekli | Yüksek (tag float) | Pin + allowlist |
| Terraform modules | observability | Orta | lock / registry pin ASSESS |
| LLM API providers | OpenRouter/Gemini/Anthropic | Orta (key) | dry-run; `${VAR}` |

## Kontroller (ASSESS checklist)

1. **Pin Actions to full 40-char SHA** (+ sürüm yorumu). Tag `@v4` mutable.  
   Ref: https://safeguard.sh/resources/blog/how-to-pin-github-actions-to-shas-correctly (*erişim 2026-08-27*)
2. **Least privilege `permissions:`** — workflow default read; job bazlı write.
3. **Dependabot `github-actions` ecosystem** — SHA-preserving updates.
4. **Immutable releases** (org/repo) — https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases · GA: https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available/ (*erişim 2026-08-27*)
5. **SBOM** — repo artefaktları için CycloneDX/SPDX üretimi ASSESS (TC motoru).
6. **SLSA provenance** — build attestation hedef seviyesi belgele (L1→L2 roadmap).
7. **Secret masking + dry-run matrisi** — `docs/SECRETS-DRYRUN-MATRISI.md`.
8. **`pull_request_target` / fork PR** — tehlikeli pattern taraması (ethics/policy); ASSESS only.
9. **upstream-sync.yml gözlemi** — vendored katalog senkronunda diff review.
10. **Scorecard / zizmor ASSESS** — workflow dangerous pattern tespiti (araç kurulumu sonraki tur).

## Olay sınıfı (tespit odaklı)
2025 civarı yaygın Action compromise / tag-repoint sınıfı (ör. CVE-2025-30066 tartışmaları): SHA-pin’li tüketiciler etkilenmez; floating tag tüketicileri secret dump riski. Bu OS’ta yanıt: pin gap listesi + TC-00x kontrolleri — exploit adımı yok.

## SLSA × holding map

| SLSA ilkesi | Holding artefakt | Kontrol ID adayı |
|-------------|------------------|------------------|
| Provenance | GHA run → artefact | TC-001.. |
| Integrity | commit SHA + signed release | TC / CHANGE |
| Isolation | job permissions | COND / FW egress |
| Dependencies | action graph | TC SBOM |

## ISO 27001:2022 supply-chain (ID only)
A.5.19–A.5.23 supplier/ICT/cloud; A.8.28 secure coding — `compliance-mapper` crosswalk.

## Gap (Faz 0 sonrası bilinen)
- [ ] Workflow SHA pin oranı ölçümü
- [ ] Action allowlist dokümanı
- [ ] SBOM CI job stub
- [ ] Provenance attestation ASSESS

## Kaynak damgaları
Tüm URL’ler bu dosyada · erişim **2026-08-27T12:54:55Z** · defense-only.
