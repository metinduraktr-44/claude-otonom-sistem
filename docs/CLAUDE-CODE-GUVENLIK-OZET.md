# Claude Code güvenlik — tek sayfa (Metin)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**Europe/Istanbul:** 2026-11-03T12:56:08+0300 · kaynak: yüklenen Gemini export (PDF≈DOCX) · **MODE:** ASSESS-ONLY

## Belge ne dedi

- Sosyal görsel **yanlış**: bedava ~1,6 milyar token (OmniRoute) ve “Anthropic resmi Claude Code Setup eklentisi” **yok**.
- GitHub yıldızı montaj olabilir; `claude-mem` resmi Anthropic ürünü değil.
- DM/üçüncü taraf script = anahtar ve kod hırsızlığı riski.
- Claude Code **gerçek** (Anthropic CLI); MCP **gerçek** — kurulum resmi allowlist’ten.
- Aynı sohbet 🚩 **900k karakter / 100 sayfa / 100 modül tek paste** istedi → LLM çıktı limiti; Holding bunu zaten RED eder.

## Uygulanan (bu PR)

- Damıtma: `SECURITY_RESEARCH/claude-code-guvenlik-uyarilari.md` (mega-prompt **yok**).
- Pointer: `docs/CILT14-CURSOR-GIGA-SECURITY.md` · `SECURITY.md`.
- Scanner: Anthropic `sk-ant-apiNN-` tespiti + `wget`→shell yasağı (`ethics_check`).
- Hafıza: `BILGI_TABANI.md` + `AUDIT_LOG.jsonl`.

## Senin işin

1. `docs.anthropic.com` · `github.com/anthropics` · `github.com/modelcontextprotocol` — başka “setup” eklentisi yok.  
2. Sosyal medya / DM kurulum **yok**.  
3. Anahtar: `${ANTHROPIC_API_KEY}` — sohbet/commit’te değer yok.  
4. Dev mega-prompt yapıştırma; `/sec-devam` / fazlı skill.

**Doğrulama:** `python3 scripts/validate.py` · `python3 scripts/ethics_check.py` · `python3 scripts/secret_scan.py`
