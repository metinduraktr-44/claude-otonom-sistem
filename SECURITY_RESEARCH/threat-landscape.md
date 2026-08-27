# Threat Landscape — Holding Python/CI Repo (Defense ASSESS)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**MODE:** ASSESS-ONLY · **ts_research:** 2026-08-27T12:54:55Z  
**Kapsam:** `claude-otonom-sistem` — Python 3 stdlib + Bash + GHA; uygulama sunucusu yok.  
**Yasak:** exploit/PoC/saldırı adımları. Odak: tespit, yama, sertleştirme, gap.

## Stack-özgü tehdit sınıfları (yüksek seviye)

| Sınıf | Holding etkisi | Savunma önceliği | Kaynak notu |
|-------|----------------|------------------|-------------|
| CI/CD action tag mutability | Workflow’lar floating tag kullanırsa tedarik zinciri riski | P0 — SHA pin ASSESS | GHA hardening guides 2025–2026; CVE-2025-30066 sınıfı olaylar (tag repoint) — tespit/yama odaklı |
| Secret sızıntısı (env/log/commit) | LLM client + GITHUB_TOKEN dry-run path | P0 — secret_scan + vault placeholder | Repo inventory `SECURITY_CONTEXT/` |
| Workflow permission creep | `GITHUB_TOKEN` write default | P1 — least-privilege `permissions:` | GitHub docs + Scorecard ASSESS |
| Prompt/content injection via markdown | `katalog/` / `uretim/` untrusted ingest | P1 — isolation + çıktı denetimi | OWASP LLM/AppSec kategorileri (aşağı) |
| Terraform sensitive state/tfvars | Observability tokens tip olarak mevcut | P1 — gitignore + remote state encryption ASSESS | inventory |
| Vendored katalog drift | Nested npm/pip şablonları | P2 — runtime dep sayma; ethics_check | inventory |

## OWASP kategorileri (bu repo için ilgili)

Holding’in web app yüzeyi yok; yine de otomasyon/LLM/CI için ASVS 5.0 + klasik OWASP sınıfları ASSESS edilir:

| OWASP / ASVS odağı | Holding map | ASSESS kontrol |
|--------------------|-------------|----------------|
| A02 Cryptographic Failures / ASVS crypto | API key saklama, TLS outbound | ENC + secret-hygiene |
| A07 Identification & Auth Failures | GHA OIDC / token scope | COND + IAM |
| A08 Software & Data Integrity | Actions, SBOM, provenance | TC + SLSA |
| A09 Logging Failures | AUDIT_LOG, CI logs secret mask | LAY + SecOps |
| A10 SSRF (düşük) | LLM/API outbound allowlist | FW egress ASSESS |
| Supply Chain (ASVS 5 tema) | pin SHA, Dependabot Actions | TC / CHANGE |
| Prompt Injection (LLM) | untrusted markdown → model | LAY content trust boundary |

**ASVS 5.0.0** (2025-05-30): https://owasp.org/www-project-application-security-verification-standard/ · https://asvs.dev/ · https://github.com/OWASP/ASVS/releases/tag/v5.0.0_release  
*Erişim damgası: 2026-08-27T12:54:55Z*

## CVE / olay sınıfı özeti (PoC yok — yama/tespit)

1. **Third-party GitHub Action compromise / tag repoint** — savunma: full commit SHA pin, Dependabot `github-actions`, workflow audit (`zizmor` ASSESS), least privilege.  
   Örnek sınıf referansı (savunma makalesi): https://safeguard.sh/resources/blog/github-actions-supply-chain-security (*erişim 2026-08-27*).
2. **Secret scraping from CI logs** — savunma: mask, dry-run, `${VAR}` only in docs.
3. **Python ecosystem transitive risk** — root `requirements.txt` yok (olumlu); `katalog/` vendored → install etmeme politikası.

## STRIDE iskeleti (holding otomasyon)

| STRIDE | Örnek varlık | Savunma kontrol motoru |
|--------|--------------|------------------------|
| Spoofing | Sahte Action / fork PR | TC pin + COND merge gate |
| Tampering | Workflow / script değişimi | CHANGE + CODEOWNERS ASSESS |
| Repudiation | Denetlenmeyen LLM çıktısı | AUDIT_LOG + LAY logging |
| Information Disclosure | Key in chat/commit | secret-hygiene |
| Denial of Service | Nightly workflow flood | COND rate/quota ASSESS |
| Elevation of Privilege | Broad GITHUB_TOKEN | IAM / COND |

## Sonraki araştırma
- GHA permissions matrisi (workflow başına)
- Scorecard / pin gap listesi (ASSESS-ONLY)
- Threat model diyagramı → `threat-modeling` skill references

## Kaynaklar (alıntı + damga)
- NIST CSF 2.0: https://doi.org/10.6028/NIST.CSWP.29 (2024-02-26) — erişim 2026-08-27
- OWASP ASVS 5.0: https://asvs.dev/ — erişim 2026-08-27
- GitHub immutable releases: https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available/ — erişim 2026-08-27
