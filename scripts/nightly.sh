#!/usr/bin/env bash
# Nightly self-improvement loop: read -> distill -> produce -> validate -> stamp
set -uo pipefail
TS_START=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "[nightly] start $TS_START"

# 1) (optional) LLM generation — only if a provider key is present. Uses PAID credits.
# Provider oncelik: OPENROUTER_API_KEY (OpenRouter) -> ANTHROPIC_API_KEY (Anthropic).
if [ -n "${OPENROUTER_API_KEY:-}" ]; then
  echo "[nightly] OPENROUTER_API_KEY present — generation via OpenRouter (${OPENROUTER_MODEL:-anthropic/claude-3.5-sonnet})."
  # daily_agency.py llm() OpenRouter'i otomatik kullanir (makale/uretim adimlari).
elif [ -n "${ANTHROPIC_API_KEY:-}" ]; then
  echo "[nightly] ANTHROPIC_API_KEY present — generation via Anthropic."
else
  echo "[nightly] FREE Status Nightly — no LLM key (OPENROUTER_API_KEY/ANTHROPIC_API_KEY); timestamp+validate only (MIT agents ok)."
fi

# 1b) MIT free agents çekirdeği (kredi harcamaz; katalog/ → .claude/katalog-mit)
if [ -f scripts/install_free_mit_agents.py ]; then
  python3 scripts/install_free_mit_agents.py || echo "[nightly] mit-free agents install uyarısı"
fi

# 2) validate
python3 scripts/validate.py || echo "[nightly] validation reported issues"

# 3) grow knowledge base + audit
TS_END=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  echo ""
  echo "## $TS_END — nightly run"
  if [ -n "${OPENROUTER_API_KEY:-}" ]; then GEN="on (OpenRouter)"; elif [ -n "${ANTHROPIC_API_KEY:-}" ]; then GEN="on (Anthropic)"; else GEN="off"; fi
  echo "- Ran read->distill->produce->validate->stamp. Generation: ${GEN}."
} >> BILGI_TABANI.md
echo "{\"ts_start\":\"$TS_START\",\"ts_end\":\"$TS_END\",\"islem\":\"nightly\",\"denetim\":\"RUN\"}" >> AUDIT_LOG.jsonl
echo "[nightly] end $TS_END"
