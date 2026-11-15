# Cursor Secrets vs repo — ASSESS

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**ts:** 2026-11-10T11:55:00Z · SIGNAL > LENGTH · 20k fluff yok

## Kural
LLM anahtarları (`GEMINI_API_KEY`, `OPENROUTER_API_KEY`, Anthropic) yalnızca Cursor Secrets / `${VAR}`. Repo, chat, PR body’si, `AUDIT_LOG` **değer yazmaz**.

| Yüzey | Beklenen | ASSESS |
|-------|----------|--------|
| Cursor Dashboard | https://cursor.com/dashboard | insan; ajan key koyamaz |
| `.env` | gitignore | commit yok |
| `scripts/secret_scan.py` | prefix hit → konum+tip | rotate insan |
| Canva OAuth | `tools/canva-client/` | CANVA:ON kapısı; şimdi BRIEF-ONLY |

## Anti-pattern
Gerçekçi `sk-ant-` / `sk-or-v1` / `ghp_` örneği **yasak**. Placeholder: `${GEMINI_API_KEY}` / `<REDACTED>`.

## Kanıt yolu (PASS değil)
`docs/SECRETS-DRYRUN-MATRISI.md` · `COMPLIANCE/CIS-IG1.md` CIS-3 satırı.
