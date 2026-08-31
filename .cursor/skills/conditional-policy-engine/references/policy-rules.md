# Conditional policy engine — if/then güvenlik

## Politika örnekleri (repo gerçeği)
| Koşul | Sonuç |
|-------|--------|
| `CANVA:ON` yok | BRIEF-ONLY; mutate yok |
| `MODE` ≠ IMPLEMENT | Yalnız assess/doküman |
| LLM key yok | Dry-run iskelet |
| `GITHUB_TOKEN` yok | holding_report static |
| ethics_check KALDI | Üretim dur / refuse |
| secret_scan KALDI | Commit engeli |
| MCP stub | Canlı Semgrep/Snyk iddiası yok |
| Ethics vs hız çakışması | Ethics kazanır |

## Uygulama yeri
- `STATE.md` / `SECURITY/STATE.md`
- `AGENTS.md` dual OS
- `CTRL-CD-*.md` kartları
- Cursor rules `05-ethics-guardrail`

## Test
Self-test scanner’lar + manuel flag okuma. IMPLEMENT’te otomasyon genişletilebilir.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
