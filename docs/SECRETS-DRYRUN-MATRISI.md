# SECRETS & DRY-RUN MATRİSİ
> Üretim: 2026-08-27T12:16:43Z · İlke: secret ASLA commit edilmez · free tier tercih · credential yoksa dry-run

## Onay politikası (Metin)
Kullanıcı free API/profil açmaya onay verdi. Bu ortamda **yüzlerce satıcı hesabı açılmadı** (kimlik/ödeme/ToS).
Yapılan: şablon + dry-run matrisi + `.env.example`. Gerçek anahtarlar GitHub Secrets / Cursor env.

| Secret | Kullanım | Nereden | Credential yoksa | Zorunlu |
|---|---|---|---|---|
| `GITHUB_TOKEN` | GitHub API (holding_report) | PAT/fine-grained | dry-run: statik rapor | opsiyonel |
| `ANTHROPIC_API_KEY` | Claude Code / API | console.anthropic.com | dry-run: MASTER prompt uygula | opsiyonel |
| `OPENAI_API_KEY` | opsiyonel LLM | platform.openai.com | dry-run | opsiyonel |
| `EXA_API_KEY` | Exa search MCP | dashboard.exa.ai | WebSearch fallback | opsiyonel |
| `BRIGHT_DATA_API_TOKEN` | Bright Data MCP | brightdata.com | dry-run scrape checklist | opsiyonel |
| `TWILIO_ACCOUNT_SID / AUTH_TOKEN` | Twilio skills | console.twilio.com | dry-run account-setup | opsiyonel |
| `SENDGRID_API_KEY` | SendGrid | Twilio SendGrid | dry-run | opsiyonel |
| `SENTRY_AUTH_TOKEN` | Sentry | sentry.io | dry-run debug-issue | opsiyonel |
| `VERCEL_TOKEN` | Vercel | vercel.com | dry-run | opsiyonel |
| `CLOUDFLARE_API_TOKEN` | Cloudflare | dash.cloudflare.com | dry-run | opsiyonel |
| `AWS_*` | AWS MCP | IAM user/role | dry-run; asla commit etme | opsiyonel |
| `AZURE_*` | Azure MCP | Service principal | dry-run | opsiyonel |
| `GCP_* / BIGQUERY_*` | Warehouse skills | GCP SA | dry-run | opsiyonel |
| `SNOWFLAKE_*` | Snowflake | account/user | dry-run | opsiyonel |
| `DATABRICKS_*` | Databricks | workspace token | dry-run | opsiyonel |
| `POSTHOG_*` | PostHog | project API key | dry-run | opsiyonel |
| `CLERK_*` | Clerk | dashboard | dry-run | opsiyonel |
| `SUPABASE_*` | Supabase | project settings | dry-run | opsiyonel |
| `PINECONE_API_KEY` | Pinecone | console | dry-run | opsiyonel |
| `CONVEX_*` | Convex | CONVEX_AGENT_MODE=anonymous cloud | agent mode | opsiyonel |
| `RENDER_API_KEY` | Render | dashboard | dry-run | opsiyonel |
| `HARNESS_API_KEY` | Harness | account | fail-open hooks | opsiyonel |
| `PAGERDUTY_*` | PagerDuty | API token | dry-run | opsiyonel |
| `DATADOG_*` | Datadog | API/APP key | dry-run | opsiyonel |
| `GRAFANA_*` | Grafana Cloud | SA token | dry-run | opsiyonel |
| `LINEAR_API_KEY` | Linear | API | dry-run | opsiyonel |
| `SLACK_BOT_TOKEN` | Slack | app | dry-run messaging | opsiyonel |
| `APIFY_TOKEN` | Apify | console | dry-run actor | opsiyonel |
| `FIRECRAWL_API_KEY` | Firecrawl | dashboard | dry-run | opsiyonel |
| `BROWSERSTACK_*` | BrowserStack | automate | dry-run | opsiyonel |
| `CURSOR_API_KEY` | Cursor SDK | dashboard integrations | local/cloud agent | opsiyonel |

## Dry-run protokolü
1. Skill/MCP çağrısı credential isterse → checklist yaz, canlı çağrı yapma
2. Sonucu `uretim/skill-workflows/` veya AUDIT_LOG'a damgala
3. Secret sızıntısı = P0 → Group CCO

## Dosyalar
- `.env.example` (boş değerler)
- Bu matris: `docs/SECRETS-DRYRUN-MATRISI.md`
