# MCP HİYERARŞİSİ — mekanizma & katmanlar
> Üretim: 2026-08-03T15:49:56Z · katalog=93 · canlı=81 · toplam=174

## 🚩 Kapsam notu
900M karakterlik prompt üretimi reddedildi. Bu belge MCP envanteri + iş akışı katmanlarıdır.

## Katmanlar
### L0_orkestrasyon
Orkestratör (CLAUDE.md uzman kurulu) + cursor-cloud meta
- Örnekler: cursor-cloud, CLAUDE orkestratör, daily_agency

### L1_arastirma
Web/araştırma/doküman MCP
- Kategoriler: research, web, web-data, docs, Exa, Bright Data, Apify

### L2_veri_backend
DB/BaaS/vector/warehouse
- Kategoriler: database, data, vector, orm, backend

### L3_gozlem_guvenlik
Observability, güvenlik, olay
- Kategoriler: obs, security, ops, qa

### L4_teslim_gelir
Deploy, CI/CD, analytics, GTM, tasarım
- Kategoriler: deploy, cicd, cloud, analytics, marketing, design, prd

### L5_uretkenlik
Filesystem, productivity, integration, audio
- Kategoriler: filesystem, productivity, integration, audio, devtools

## İş akışı sırası
- 1) L1 araştırma → sinyal
- 2) L2 veri/backend doğrulama
- 3) L3 gözlem/güvenlik denetim
- 4) L4 teslim/gelir aksiyon
- 5) L0 damga → BILGI_TABANI + AUDIT_LOG

## Katalog kategorileri (adet)
- `audio`: 1
- `browser_automation`: 6
- `database`: 8
- `deepgraph`: 4
- `deepresearch`: 1
- `devtools`: 46
- `filesystem`: 1
- `integration`: 6
- `marketing`: 3
- `productivity`: 3
- `research`: 1
- `web`: 6
- `web-data`: 7

## Canlı Cursor MCP (örnek)
- `Railway` · cloud/deploy
- `Aws-mcp` · cloud/infra
- `Azure` · cloud/infra
- `Aurora-dsql` · data/db
- `Zscaler` · security/zt
- `Zscaler-mcp-server` · security/zt
- `Appwrite-api` · backend/baas
- `Appwrite-docs` · docs/docs
- `Cockroachdb-toolbox` · data/db
- `Cockroachdb-toolbox-http` · data/db
- `Cockroachdb-cloud` · data/db
- `Pinecone` · vector/vector
- `Encore-mcp` · backend/backend
- `Firebase` · cloud/baas
- `Aws-serverless-mcp` · cloud/serverless
- `Mongodb` · data/db
- `Awsiac` · cloud/iac
- `Awspricing` · cloud/cost
- `Browserstack` · qa/test
- `Convex` · backend/baas
- `Zoominfo` · sales/gtm
- `Mixpanel` · analytics/product-analytics
- `Opensearch-mcp-server` · search/search
- `Ddg-search` · search/search
- `Awslabs.aws-api-mcp-server` · cloud/infra
- `Aws-knowledge-mcp-server` · docs/docs
- `Bright Data` · web-data/scrape
- `Prisma-Local` · orm/orm
- `Prisma-Remote` · orm/orm
- `Figma` · design/design
- `Linear` · pm/pm
- `Coralogix` · obs/observability
- `Datadog` · obs/observability
- `Monk` · deploy/deploy
- `Twilio-docs` · docs/docs
- `Vantage` · finops/finops
- `Paradedb` · data/search-db
- `Awsknowledge` · docs/docs
- `Workos` · auth/auth
- `Turbopuffer` · vector/vector
- … toplam 81 canlı sunucu (`data/mcp_hiyerarsi.json`)

## Makine okunur
- `data/mcp_hiyerarsi.json`
