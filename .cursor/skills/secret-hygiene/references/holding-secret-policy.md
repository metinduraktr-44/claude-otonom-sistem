# Holding Secret Policy (ASSESS)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

## İlkeler
1. Dokümanda yalnızca `${OPENROUTER_API_KEY}`, `vault:///<REDACTED>`, `<REDACTED>`.
2. `.env` commit yok; `.env.example` boş/placeholder.
3. LLM client: key yoksa dry-run (mevcut `scripts/*_client.py` davranışı korunur).
4. Terraform: sensitive vars; `*.tfvars` (örnek hariç) gitignore ASSESS.
5. Chat/PR’a yapıştırılan log’larda key satırı redakte.

## Holding konum haritası (tip only)
| Konum | Tip | Beklenen kontrol |
|-------|-----|------------------|
| `scripts/gemini_client.py` | env API key | dry-run / mask |
| `scripts/openrouter_client.py` | env API key | dry-run |
| `scripts/holding_report.py` | GITHUB_TOKEN | dry-run statik |
| `infra/terraform/observability/variables.tf` | sensitive token tipleri | tfvars.example |
| `docs/SECRETS-DRYRUN-MATRISI.md` | ad kataloğu | değer yok doğrula |

## Redaksiyon sözleşmesi
- Bulgu log: `{"type","file","line","value":"<REDACTED>"}`
- İnsan raporu: `tip @ yol:satır` — değer asla.

## NIST / CIS map (kısa)
- CSF 2.0: PR.DS (data security), PR.AA (auth)
- 800-53: IA-5, SC-12, SC-28, AU-9
- CIS: Control 3 Data Protection; Control 5 Account Mgmt
- ISO 27001:2022: A.5.15, A.8.24 (crypto), A.8.3

## Yasak
Key üretme, key decode YASAK; phishing kit / credential harvest page üretimi YASAK (detect+block only).
