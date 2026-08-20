# TEK SAYFA RAPOR — Claude Otonom Sistem
> UTC: 2026-08-20T11:25:00Z · Repo: [metinduraktr-44/claude-otonom-sistem](https://github.com/metinduraktr-44/claude-otonom-sistem) · Durum: **healthy (Actions yeşil; LLM keysiz Free Nightly)**

## Healthy roadmap (sırayla)
1. **Merge PR #14** (ana paket: ajans + MIT Status Agents + Gemini LLM) → hemen  
2. **Secrets** (rotate edilmiş `GEMINI_API_KEY`; ops. OpenRouter) → Live LLM  
3. **PR #12** (AGENTS.md) — #14 merge sonrası kapat veya içerik zaten geldiyse close  
4. Dependabot (#8/#11/#15) — düşük risk; #10 katalog örneği, isteğe bağlı  
5. PR #16 / #17 — #14 sonrası **redundant/conflict**; close veya #14 içine alındıysa kapat  
6. Claude Code’a `.claude/system_prompt` + `uretim/devir/CLAUDE-CODE-MASTER-PROMPT-HOLDING-V2.md`  
7. Aylık top-N araştırma döngüsü + holding konsolide yeşil kalsın  

## İş listesi

### Sende bekleyen (ajan merge/secret yazamaz)
| # | Aksiyon | URL |
|---|---|---|
| 1 | **Merge #14** (MERGEABLE, Ready) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/14 |
| 2 | Gemini anahtarını **rotate** et, Secrets’a koy (`GEMINI_API_KEY`) | https://aistudio.google.com/apikey · Repo Secrets: https://github.com/metinduraktr-44/claude-otonom-sistem/settings/secrets/actions |
| 3 | (Opsiyonel) OpenRouter secret | https://openrouter.ai/keys |
| 4 | Draft #12 Ready + merge veya #14 sonrası close | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/12 |
| 5 | Dependabot merge (#8, #11, #15) | https://github.com/metinduraktr-44/claude-otonom-sistem/pulls?q=is%3Apr+is%3Aopen+label%3Adependencies |
| 6 | #16 / #17: close (çakışmalı / #14 ile örtüşen) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/16 · https://github.com/metinduraktr-44/claude-otonom-sistem/pull/17 |
| 7 | Branch protection aç (main force-push engeli) | https://github.com/metinduraktr-44/claude-otonom-sistem/settings/branches |

### Bende bekleyen (sen merge + secret sonrası)
| # | Aksiyon | Not |
|---|---|---|
| 1 | `llm_smoke.py` + live `daily_agency` Gemini ile | Secret gelince |
| 2 | Nightly/daily Actions yeşil + LLM on doğrula | https://github.com/metinduraktr-44/claude-otonom-sistem/actions |
| 3 | Conflict kalan PR’ları temizle / rebase | Senin close veya onay sonrası |
| 4 | Holding rotasyon + top-N arşiv turu | Otomatik cron; LLM ile zenginleşir |

## PR matrisi (şimdi)
| PR | Durum | Senin hareket |
|---|---|---|
| [#14](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/14) | **MERGEABLE · Ready** | **Merge et** |
| [#12](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/12) | MERGEABLE · draft | Ready + merge veya close |
| [#16](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/16) | CONFLICT · draft | Close (#14 kapsar) |
| [#17](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/17) | CONFLICT · draft | Close veya sonra rebase |
| [#8](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/8) / [#11](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/11) / [#15](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/15) | Dependabot | İsteğe bağlı merge |
| [#10](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/10) | katalog örnek deps | Düşük öncelik |

## 🚩 Ajan sınırı
Merge API / `gh pr merge` bu ortamda **yazamaz** (read-only). Onayın alındı; #14 conflict temizlendi ve Ready yapıldı — **Merge butonu sende**.

## Kısa sağlık
- Validate: GEÇTİ · Free Status Nightly: keysiz çalışır · MIT 32 ajan: `.claude/katalog-mit/`  
- LLM sırası: OpenRouter → Gemini → Anthropic  
- Yapıştır: `.claude/system_prompt` · `docs/MEGA-PRONT-MASTER.md` · `docs/MIT-UCRETSIZ-AGENTS-NIGHTLY.md`
