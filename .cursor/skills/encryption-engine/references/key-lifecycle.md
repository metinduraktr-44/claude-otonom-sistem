# Key Lifecycle ASSESS

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

1. **Create** — sağlayıcıda; repoya yazma
2. **Store** — Actions secrets / vault://
3. **Use** — env inject; log mask
4. **Rotate** — periyot + olay sonrası (compromise sınıfı)
5. **Revoke** — eski key disable
6. **Audit** — tip+zaman AUDIT (değer yok)

Holding anahtar tipleri: OpenRouter, Gemini, Anthropic, GitHub, Datadog/Sentry (TF).
