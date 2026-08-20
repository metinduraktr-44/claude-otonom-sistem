# FAZ 4 — 5 Güvenlik Kuralı Kontrolü
> 2026-08-04T08:44:30Z

| # | Kural | Durum | Kanıt |
|---|---|---|---|
| 1 | Resmi kaynak öncelik | GEÇTİ | Anthropic/Cursor/platform docs linkleri kartlarda |
| 2 | Script tedbiri | GEÇTİ | Üreticiler okunabilir; bundle çalıştırılmadı |
| 3 | Güncellik yanılgısı yok | GEÇTİ | Zaman damgası + arşiv zinciri |
| 4 | Fork yasağı | GEÇTİ | Kanonik org metinduraktr-44 |
| 5 | Marketplace öncelik | GEÇTİ | Skill/MCP resmi katalog tercih |
| + | Secret hijyeni | GEÇTİ | .env gitignore; .env.example boş; dry-run |
| + | 900B dolgu | GEÇTİ | 900M+ dosya = 0 |
