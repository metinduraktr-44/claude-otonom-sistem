# RESEARCH — AN-PH PostHog / Pendo skill dalgası

> ts: `2026-11-27T10:35:00Z` · Europe/Istanbul `2026-11-27T13:35:00+03:00`  
> Tür: iç doküman + web kaynak notu · **uydurma kişi yok** · tenant yok → dry-run  
> Domain: **12 skill** (`AN-PH` pending kuyruk; 75’in tamamı **değil**)

## İç doküman (önce oku)

| Dosya | Sinyal |
|-------|--------|
| `data/skill_envanteri.json` | 696 skill / 50 domain · AN-PH=75 |
| `data/skill_loop_index.json` | 11-16: 9 partial AN-CH+AN-MIX; bu tur +12 AN-PH |
| `ROSTER/TITLE_INVENTORY.md` | `adops-anl-ga4-tagging` bağ |
| `ARCHIVE/2026-11/latos/skill-loop-2026-11.md` | Kasım damgası → skill_loop calendar **SKIP** |

## Web kaynaklar (URL + ts)

| Skill | Kaynak | URL | ts |
|-------|--------|-----|-----|
| (PH genel) | Product analytics | https://posthog.com/docs/product-analytics/ | 2026-11-27T10:35:00Z |
| add-analytics-instrumentation | Capturing events | https://posthog.com/docs/product-analytics/capture-events | 2026-11-27T10:35:00Z |
| add-analytics-instrumentation | Identifying users | https://posthog.com/docs/product-analytics/identify | 2026-11-27T10:35:00Z |
| account-health, analyze-account-health | Customer health tracking (handbook) | https://posthog.com/handbook/customer-success/health-tracking | 2026-11-27T10:35:00Z |
| analyze-chart | Product analytics insights | https://posthog.com/docs/product-analytics/ | 2026-11-27T10:35:00Z |
| analyze-dashboard | LLM analytics dashboard (örnek dashboard yüzeyi) | https://posthog.com/docs/llm-analytics/dashboard | 2026-11-27T10:35:00Z |
| analyze-ai-topics | LLM analytics basics (`$ai_generation`) | https://posthog.com/docs/llm-analytics/basics | 2026-11-27T10:35:00Z |
| analyze-feedback | Creating surveys | https://posthog.com/docs/surveys/creating-surveys | 2026-11-27T10:35:00Z |
| analyze-feedback | Custom surveys | https://posthog.com/docs/surveys/implementing-custom-surveys | 2026-11-27T10:35:00Z |
| assessing-heatmaps | Heatmaps | https://posthog.com/docs/toolbar/heatmaps/ | 2026-11-27T10:35:00Z |
| authoring-log-alerts | Alerts | https://posthog.com/docs/alerts | 2026-11-27T10:35:00Z |
| authoring-signals-scouts | Signals | https://posthog.com/docs/self-driving/signals | 2026-11-27T10:35:00Z |
| authoring-signals-scouts | Scout examples | https://posthog.com/docs/self-driving/scout-examples | 2026-11-27T10:35:00Z |
| daily-brief | Signal sources / inbox | https://posthog.com/docs/self-driving/inbox/sources | 2026-11-27T10:35:00Z |
| debug-replay | Session replay | https://posthog.com/docs/session-replay/ | 2026-11-27T10:35:00Z |
| debug-replay | How to watch recordings | https://posthog.com/docs/session-replay/how-to-watch-recordings | 2026-11-27T10:35:00Z |
| (Pendo çapraz) | Get started with Pendo | https://support.pendo.io/hc/en-us/articles/15691778509211-Get-started-with-Pendo | 2026-11-27T10:35:00Z |
| (Pendo çapraz) | Understand user behavior with reports | https://support.pendo.io/hc/en-us/articles/22172817933595-Understand-user-behavior-with-reports | 2026-11-27T10:35:00Z |
| (Pendo çapraz) | Data Explorer | https://support.pendo.io/hc/en-us/articles/360033574351-Build-a-Data-Explorer-report | 2026-11-27T10:35:00Z |

## Sentez (sinyal)

- PostHog product analytics: events + persons; insights (trends/funnels/paths) aynı event katmanı. Tenant **yok** → spec şablon.
- Heatmaps: `enable_heatmaps`; clickmap autocapture; scrollmap pageleave; free plan 3 URL limiti (docs).
- Session replay: SDK kayıt + privacy mask; scout raporları capture cliff / friction cluster; **PR açmaz** (docs). Replay izleme = ASSESS; exploit yok.
- Alerts: trends, funnels (steps/trends), SQL/HogQL; eşik veya anomali.
- Signals vs scouts: source = sürekli/exhaustive; scout = zamanlanmış/judgement. Log alerts source stream’de.
- LLM analytics: `$ai_generation` wrapping; maliyet OpenRouter pricing fallback (docs). Holding LLM key **UNSET** olabilir → dry-run.
- Handbook health score = PostHog **kendi** CS hesabı (0–10 engagement+stickiness). Holding müşteri skoru **uydurulmaz**.
- Pendo: snippet/launcher kurulum; Analytics reports (Data Explorer, Funnel, Path). Credential yok → kod kurulum yok.

## Yapılmayan

- PostHog/Pendo project, snippet, API key
- Session replay PII mask atlama
- 75 AN-PH skill’in tamamı (INDEX satırı pending kalır)
- 900M prompt · top-100 kişi
- FAZ6 SoA **yeniden yazılmadı**; #39 additive dosyalar bu dalda kopyalandı
