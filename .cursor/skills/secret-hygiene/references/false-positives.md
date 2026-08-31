# False Positive Katalog (seed)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

| Örnek satır | Beklenen | Not |
|-------------|----------|-----|
| `API_KEY=${API_KEY}` | allow | placeholder |
| `vault:///<REDACTED>` | allow | vault pattern |
| `api_key=""` | allow | boş |
| dokümanda “Bearer token kullanma” | allow if guardrail | ethics ALLOW_CONTEXT |
| gerçek `AKIA…` 20 char | bulgu | rotate prosedür (değer yazma) |

## Triage
1. Tip+konum kaydet
2. Değer asla ticket’a
3. Rotate sağlayıcı konsolunda
4. Commit history scrub ASSESS (filtre-repo notu — komut dump yok)

## TODO 20k
Provider-specific rotate linkleri (resmi docs), pre-commit örnek, dil pattern tablosu.
