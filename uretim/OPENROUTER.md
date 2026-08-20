# OpenRouter entegrasyonu
> 2026-08-04T12:50:48Z · https://openrouter.ai/

## Durum
Bu cloud agent oturumunda `OPENROUTER_API_KEY` **yok** → dry-run.
Wire hazır: key gelince `daily_agency` + `openrouter_client` canlı çağırır.

## Key ekle (1 adım)
1. https://openrouter.ai/keys → Create Key  
2. Cursor Cloud Agent **Secrets** (veya yerel `.env`, gitignore’da):

```bash
export OPENROUTER_API_KEY='sk-or-v1-...'
export OPENROUTER_MODEL='anthropic/claude-sonnet-4'   # opsiyonel
```

3. Doğrula:

```bash
python3 scripts/openrouter_client.py smoke
```

Beklenen: `"ok": true`, `"mode": "LIVE"`.

## Komutlar
| Komut | Ne yapar |
|---|---|
| `python3 scripts/openrouter_client.py status` | configured / model |
| `python3 scripts/openrouter_client.py models` | /models probe |
| `python3 scripts/openrouter_client.py smoke` | PONG ping |
| `bash scripts/live_dashboard.sh` | OPENROUTER satırı |

## Öncelik sırası (LLM)
1. `OPENROUTER_API_KEY` → OpenRouter chat/completions  
2. `ANTHROPIC_API_KEY` → Anthropic Messages  
3. Yok → deterministik iskelet (döngü kırılmaz)

🚩 Secret ASLA commit edilmez.
