# DOMAIN MATRIX 1–7 — Enterprise MCP Orchestration
> Üretim: 2026-08-10T10:13:01Z · 🚩900M RED · sözleşme: 122 prompt/rol

## 7×24 Schedule
| Freq | Agent | Actions |
|---|---|---|
| realtime | Telemetry & Observability | opentelemetry-validation, alert-investigation, tierzero-investigate |
| daily | DevOps & Infrastructure | debug-k8s-collection, observability-service-health, gitops-status |
| weekly | Security & Compliance | review-security, auditing-cloud-cluster-security, twilio-security-hardening |
| monthly | Chief Architect & Research | exa-web-search, dora-metrics, analyze-costs, knowledge-update |

## Domain 1: Infrastructure, Kubernetes & Cloud (`INFRA`)
- C-Suite: **CTO**
- Skills (19): `/setup-linux-host-collection`, `/setup-linux-host-backend`, `/setup-k8s-collection`, `/setup-k8s-backend`, `/deploy-linux-host-explorer`, `/deploy-k8s-explorer`, `/debug-linux-host-collection`, `/debug-k8s-collection`…
- Directives: **20** (≥20 hedef)

1. Dry-run önce: onboard-confidence-dry-run + azure-validate
2. K8s pod crash → debug-k8s-collection
3. Host bottleneck → debug-linux-host-collection
4. Deploy öncesi maliyet: azure-cost + analyze-costs
5. AKS: airunway-aks-setup + azure-kubernetes
6. Lambda cold-start: aws-lambda-managed-instances
7. Edge: workers-best-practices + wrangler
8. Private net: configuring-private-connectivity
9. RBAC: azure-rbac least privilege
10. Step Functions state doğrula
11. Render: render-blueprints + render-scaling
12. TLS: managing-tls-certificates
13. Haftalık chaos-experiment
14. Tag uyumu: azure-resource-lookup
15. Env izolasyonu: create-environment
16. Connector: create-connector
17. IP allowlist güncelle
18. Container image audit: render-docker
19. UTC timestamp → audit-report
20. Pipeline blok: debug-pipeline

Artefaktlar: `infra/otel/opentelemetry-collector.yaml`, `.github/workflows/enterprise-k8s-otel-pipeline.yml`

## Domain 2: Telemetry, Observability & Diagnostics (`OBS`)
- C-Suite: **CTO/CAIO**
- Skills (16): `/opentelemetry-validation`, `/opentelemetry-manual-instrumentation`, `/opentelemetry-auto-instrumentation`, `/observe-cli`, `/generate-opal`, `/alert-investigation`, `/tierzero-investigate`, `/tierzero-fetch`…
- Directives: **20** (≥20 hedef)

1. Servis start → opentelemetry-auto-instrumentation
2. Özel logic → opentelemetry-manual-instrumentation spans
3. Kesinti → tierzero-investigate + alert-investigation
4. Grafana sapma → grafana-assistant-cli
5. Hata → sentry-debug-issue stacktrace
6. Datadog agent: ddsetup + ddconfig
7. Log query: elasticsearch-esql
8. PII mask: configuring-log-export
9. Kibana alert rules otomatik
10. LLM token/latency: observability-llm-obs
11. Frontend lock: finding-replay-for-issue
12. 7/24: observability-service-health
13. Python/Java/.NET EDOT migrate
14. Vega: kibana-vega
15. Anomaly: signals-scout-anomaly-detection
16. OpenSearch index optimize
17. sentry-create-alert thresholds
18. diagnose-errors ilk adım
19. debug-traces microservice map
20. Telemetry arşiv zaman damgalı

Artefaktlar: `infra/terraform/observability/main.tf`, `infra/otel/opentelemetry-collector.yaml`

## Domain 3: Data Engineering, Pipelines & Storage (`DATA`)
- C-Suite: **CDO**
- Skills (15): `/setup-warehouse-snowflake`, `/setup-warehouse-redshift`, `/setup-warehouse-databricks`, `/setup-warehouse-bigquery`, `/cockroachdb-sql`, `/scylladb-vector-search`, `/scylladb-data-modeling`, `/postgres`…
- Directives: **20** (≥20 hedef)

1. warehouse-init şema standardı
2. dbt lineage: upstream + downstream
3. DAG hata: debugging-dags + testing-dags
4. Vector: scylladb-vector-search + pinecone-query
5. MongoDB query optimizer
6. Cockroach fingerprint kilit çöz
7. Multi-region: designing-multi-region-applications
8. dbt unit tests
9. Temporal state persistence
10. ClickHouse columnar
11. Postgres best practices
12. profiling-tables
13. Airflow 2→3 migrate
14. annotating-task-lineage
15. cosmos-dbt-core
16. CMEK encryption
17. checking-freshness
18. redis-development
19. querying-posthog-data
20. Pipeline çıktısı zaman damgalı delta

## Domain 4: Full-Stack Platform, Identity & Frontend (`FULLSTACK`)
- C-Suite: **CPO/CTO**
- Skills (13): `/nextjs`, `/react-best-practices`, `/turbopack`, `/shadcn`, `/workos`, `/clerk`, `/entra-app-registration`, `/appwrite-typescript`…
- Directives: **20** (≥20 hedef)

1. Next.js App Router standartları
2. SSO/SCIM: workos
3. Clerk nextjs patterns
4. Prisma migrate-diff önce
5. Firebase security rules audit
6. GSAP performance
7. Appwrite typescript
8. Microfrontends router
9. Encore Go API
10. Entra app registration dar yetki
11. Convex helpers
12. Hydration: react-best-practices
13. runtime-cache + cdn-caching
14. shadcn UI
15. turbopack flags
16. xcode-project-setup
17. scan-and-fix-accessibility
18. manage-feature-flags
19. figma-code-connect
20. next-upgrade bağımlılık

## Domain 5: Communications, Engagement & Scrapers (`COMMS`)
- C-Suite: **CMO**
- Skills (10): `/twilio-sendgrid-email-send`, `/twilio-whatsapp-send-message`, `/twilio-voice-twiml`, `/twilio-verify-send-otp`, `/twilio-ai-agent-architect`, `/apify-ultimate-scraper`, `/firecrawl-crawl`, `/firecrawl-scrape`…
- Directives: **20** (≥20 hedef)

1. SMS: twilio-isv-sms-best-practices
2. SendGrid deliverability advisor
3. Apify ultimate-scraper + actorization
4. Exa semantic search
5. Firecrawl depth limit
6. Voice TwiML
7. WhatsApp senders manage
8. OTP: verify-send-otp
9. HIPAA: twilio-security-compliance-hipaa
10. Apify output schema
11. Content template builder
12. Webhook signature architecture
13. deep-research + bd-search
14. Twilio AI agent memory
15. BrightData browser session
16. SendGrid suppressions sync
17. TaskRouter routing
18. Inbound parse
19. RCS messaging
20. Scraping JSONL zaman damgalı

## Domain 6: Product, Security & AI/ML (`PRDSEC`)
- C-Suite: **CPO/CSO/CAIO**
- Skills (11): `/write-prd`, `/update-prd`, `/implement-from-prd`, `/check-prd-alignment`, `/review-security`, `/audit-report`, `/transformers-js`, `/trl-training`…
- Directives: **20** (≥20 hedef)

1. PRD: ölçülebilir KPI
2. Kod öncesi check-prd-alignment
3. review-security + audit-report
4. HF trainer + trl-training
5. DORA haftalık
6. figma-design-to-code
7. Slack: create-slack-app + block-kit
8. compare-user-journeys
9. monitor-ai-quality
10. experiment rollout
11. microsoft-foundry responsible AI
12. feedback-analysis
13. BrowserStack web tests
14. certificates encryption
15. manage-pull-requests + bugbot
16. hardening-user-privileges
17. analyze-experiments
18. jfrog package safety
19. replay-ux-audit
20. PRD sürüm zaman damgalı

## Domain 7: Governance, Workflow & Self-Improvement (`GOV`)
- C-Suite: **CEA**
- Skills (8): `/dora-metrics`, `/analyze-costs`, `/review-agent-insights`, `/knowledge-update`, `/exa-web-search`, `/gitops-status`, `/manage-slos`, `/manage-freeze-windows`
- Directives: **20** (≥20 hedef)

1. DORA velocity/stability
2. analyze-costs bütçe sapması
3. review-agent-insights
4. knowledge-update
5. Aylık exa-web-search benchmark
6. gitops-status
7. manage-slos
8. manage-freeze-windows
9. manage-feature-flags + delegates
10. create-policy
11. create-secret rotasyon
12. create-agent-template
13. create-subagent
14. create-skill standart
15. create-rule
16. create-hook event
17. canvas mimari
18. create-trigger pipeline
19. manage-users + manage-roles
20. Aylık UTC delta arşiv

Artefaktlar: `uretim/devir/MASTER-ENTERPRISE-ORCHESTRATOR.md`, `scripts/live_dashboard.sh`

