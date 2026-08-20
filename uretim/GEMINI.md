# Gemini entegrasyonu
> 2026-08-10 · https://ai.google.dev/gemini-api/docs

## Durum
- Client: `scripts/gemini_client.py`
- daily_agency LLM öncelik: **Gemini → Anthropic → iskelet**
- İlk smoke: LIVE (`gemini-flash-latest` → `gemini-3.6-flash`)
- Sonraki çağrılar: **HTTP 429 free-tier quota** (20 req limit) — bekleyin veya billing açın

## Key
```bash
# .env (gitignore) — ASLA commit etme
GEMINI_API_KEY=...
GEMINI_MODEL=gemini-flash-latest
python3 scripts/gemini_client.py smoke
```

Key oluştur / rotate: https://aistudio.google.com/apikey  
Rate limits: https://ai.google.dev/gemini-api/docs/rate-limits

🚩 Chat’te paylaşılan key ifşa sayılır → rotate et.
