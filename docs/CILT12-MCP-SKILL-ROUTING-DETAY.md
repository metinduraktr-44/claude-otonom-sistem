# CILT12 — MCP/Skill Routing Detay (minimal + tam envanter)
> Üretim: 2026-08-25T14:47:16Z · skill=696 · domain=50 · title=216 · mcp=174

## 🚩 Gerçeklik (atlanmaz)
| İstek | Karar | Eşdeğer |
|---|---|---|
| ≥900.000.000.000 karakter tek pront | **RED** | Modüler MEGA-PRONT + 122×(4–12 KiB) sözleşme |
| Tüm slash-skill native canlı runtime | **KISMI** | Credential yoksa dry-run; routing → MIT ajan / MCP |
| Tek turda tüm title top-100 uydurma | **RED** | `data/title_top_kisiler.json` kaynaklı + aylık arşiv |

## Kullanım kuralı (her skill)
1. Skill adını `data/skill_envanteri.json` içinde bul → `domain_id` + `c_level`.
2. Title: `data/skill_title_haritasi.json` → ilgili IC/Worker.
3. Workflow: `uretim/skill-workflows/{domain_id}.md`.
4. Credential yoksa: dry-run + şablon + AUDIT satırı. Mutate etme.
5. MCP varsa: `data/mcp_hiyerarsi.json` katman sırası (`is_akis_sirasi`).

## Domain → skill envanteri (tam)

### `AN-CH` — ClickHouse · C=CDO · n=6

| Skill | Mod | Güvenlik |
|---|---|---|
| `chdb-datastore` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `chdb-sql` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clickhouse-architecture-advisor` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clickhouse-best-practices` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clickhouse-js-node-troubleshooting` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clickhousectl-local-dev` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `AN-MIX` — Mixpanel / analytics track · C=CMO · n=3

| Skill | Mod | Güvenlik |
|---|---|---|
| `deep-research` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `manage-lexicon` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `tracking-implementation` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `AN-PH` — PostHog / Pendo signals · C=CMO · n=75

| Skill | Mod | Güvenlik |
|---|---|---|
| `account-health` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `add-analytics-instrumentation` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `analyze-account-health` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `analyze-ai-topics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `analyze-chart` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `analyze-dashboard` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `analyze-feedback` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `assessing-heatmaps` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `auditing-cloud-cluster-security` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `auditing-endpoints` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `authoring-dags` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `authoring-log-alerts` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `authoring-signals-scouts` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `consuming-endpoints-from-client-code` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `copying-flags-across-projects` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `creating-an-endpoint` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `creating-replay-vision-scanners` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `daily-brief` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `debug-replay` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `debugging-local-replay` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `diagnose-errors` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `diagnosing-endpoint-performance` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `diagnosing-missing-recordings` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `diagnosing-sdk-health` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `diagnosing-stacktrace-symbolication` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `diff-intake` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `discover-analytics-patterns` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `discover-event-surfaces` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `discover-opportunities` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `downloading-batch-export-files` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `exploring-signals-scouts` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `feature-adoption` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `feature-usage-feed` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `feedback-analysis` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `finding-replay-for-issue` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `finding-sessions-to-watch` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `formatting-insight-axes` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `grouping-noisy-errors` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `inbox-exploration` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `instrument-error-tracking` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `instrument-events` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `instrument-integration` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `instrument-llm-analytics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `instrument-logs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `instrument-product-analytics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `investigating-replay` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `managing-endpoint-versions` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `managing-path-cleaning-rules` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `managing-subscriptions` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `monitor-ai-quality` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `monitor-reliability` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `planning-user-interviews` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `querying-posthog-data` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `replay-ux-audit` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `review-agent-insights` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `session-replay` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `signals` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `signals-scout-ai-observability` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `signals-scout-anomaly-detection` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `signals-scout-csp-violations` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `signals-scout-error-tracking` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `signals-scout-general` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `signals-scout-logs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `signals-scout-revenue-analytics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `signals-scout-surveys` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `skills-store` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `suggesting-data-imports` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `suppressing-noisy-errors` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `taxonomy` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `triaging-error-issues` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `triaging-visual-review-runs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `tuning-incremental-sync-config` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `weekly-brief` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `what-would-lenny-do` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `working-with-skills` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `API-POST` — Postman · C=CTO · n=6

| Skill | Mod | Güvenlik |
|---|---|---|
| `agent-ready-apis` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `ddconfig` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `ddsetup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `ddtoolsets` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `postman-knowledge` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `postman-routing` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `AUTH-CLERK` — Clerk · C=CISO · n=19

| Skill | Mod | Güvenlik |
|---|---|---|
| `clerk` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-android` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-backend-api` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-billing` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-chrome-extension-patterns` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-custom-ui` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-expo` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-expo-patterns` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-nextjs-patterns` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-nuxt-patterns` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-orgs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-react-patterns` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-react-router-patterns` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-swift` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-tanstack-patterns` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-testing` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-vue-patterns` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-webhooks` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `AUTH-WO` — WorkOS · C=CISO · n=2

| Skill | Mod | Güvenlik |
|---|---|---|
| `workos` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `workos-widgets` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `BAAS-APP` — Appwrite · C=CTO · n=10

| Skill | Mod | Güvenlik |
|---|---|---|
| `appwrite-cli` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `appwrite-dart` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `appwrite-dotnet` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `appwrite-go` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `appwrite-kotlin` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `appwrite-php` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `appwrite-python` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `appwrite-ruby` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `appwrite-swift` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `appwrite-typescript` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `BAAS-CONVEX` — Convex · C=CTO · n=6

| Skill | Mod | Güvenlik |
|---|---|---|
| `components-guide` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `convex-helpers-guide` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `convex-quickstart` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `function-creator` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `migration-helper` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `schema-builder` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `BAAS-FB` — Firebase · C=CTO · n=10

| Skill | Mod | Güvenlik |
|---|---|---|
| `firebase-ai-logic-basics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firebase-app-hosting-basics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firebase-auth-basics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firebase-basics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firebase-crashlytics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firebase-data-connect` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firebase-firestore` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firebase-hosting-basics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firebase-remote-config-basics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firebase-security-rules-auditor` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `BAAS-SUPA` — Supabase · C=CTO · n=1

| Skill | Mod | Güvenlik |
|---|---|---|
| `supabase` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `BE-ENCORE` — Encore · C=CTO · n=21

| Skill | Mod | Güvenlik |
|---|---|---|
| `add-infrastructure` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-service` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `debug-traces` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-api` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-auth` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-code-review` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-database` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-frontend` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-getting-started` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-go-api` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-go-auth` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-go-code-review` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-go-database` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-go-getting-started` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-go-infrastructure` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-go-service` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-go-testing` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-infrastructure` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-migrate` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-service` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `encore-testing` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `BI-TS` — ThoughtSpot / Omni / Hex · C=CDO · n=14

| Skill | Mod | Güvenlik |
|---|---|---|
| `get-developer-docs-reference` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `get-rest-api-reference` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `get-visual-embed-sdk-reference` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `hex-business-analytics-question` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `hex-notebook-authoring` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `hex-to-canvas` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `omni-admin` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `omni-ai-optimizer` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `omni-content-builder` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `omni-content-explorer` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `omni-embed` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `omni-model-builder` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `omni-model-explorer` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `omni-query` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `CICD-HAR` — Harness CI/CD · C=CTO · n=28

| Skill | Mod | Güvenlik |
|---|---|---|
| `analyze-costs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `audit-report` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-agent` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-agent-template` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-connector` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-environment` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-infrastructure` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-pipeline` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-pipeline-v1` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-policy` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-secret` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-trigger` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `debug-pipeline` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `debugging-signals-pipeline` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `dora-metrics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `gitops-status` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `manage-delegates` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `manage-freeze-windows` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `manage-pull-requests` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `manage-roles` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `manage-slos` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `manage-users` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `migrate-pipeline` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `observability-manage-slos` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `run-pipeline` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `scorecard-review` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `security-report` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `template-usage` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `CLOUD-AWS` — AWS serverless · C=CTO · n=16

| Skill | Mod | Güvenlik |
|---|---|---|
| `access-protected-vercel-deployment` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `amazon-location-service` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `amplify-workflow` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `api-gateway` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `aws-architecture-diagram` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `aws-lambda` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `aws-lambda-durable-functions` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `aws-lambda-managed-instances` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `aws-serverless-deployment` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `aws-step-functions` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clickhousectl-cloud-deploy` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `deploy` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `deployments-cicd` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `elastic-beanstalk` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-migrate-deploy` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-deploy` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `CLOUD-AZ` — Azure / Entra / Foundry · C=CTO · n=27

| Skill | Mod | Güvenlik |
|---|---|---|
| `airunway-aks-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `appinsights-instrumentation` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-ai` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-aigateway` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-cloud-migrate` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-compliance` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-compute` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-cost` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-deploy` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-diagnostics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-enterprise-infra-planner` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-hosted-copilot-sdk` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-kubernetes` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-kusto` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-messaging` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-prepare` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-quotas` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-rbac` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-reliability` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-resource-lookup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-resource-visualizer` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-storage` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-upgrade` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `azure-validate` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `entra-agent-id` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `entra-app-registration` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `microsoft-foundry` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `COMMS-SLACK` — Slack · C=COO · n=8

| Skill | Mod | Güvenlik |
|---|---|---|
| `block-kit` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-slack-app` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `functions` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `slack-api` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `slack-cli` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `slack-messaging` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `slack-search` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `vercel-functions` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `COMMS-TW` — Twilio / SendGrid / Voice · C=CRO · n=56

| Skill | Mod | Güvenlik |
|---|---|---|
| `twilio-account-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-agent-augmentation-architect` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-agent-connect` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-ai-agent-architect` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-call-recordings` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-cli-reference` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-compliance-onboarding` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-compliance-traffic` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-conference-calls` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-content-template-builder` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-conversation-intelligence` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-conversation-memory` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-conversation-orchestrator` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-conversations-classic-api` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-customer-support-architect` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-debugging-observability` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-email-deliverability-advisor` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-email-send` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-enterprise-knowledge` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-iam-auth-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-identity-verification-advisor` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-isv-sms-best-practices` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-lookup-phone-intelligence` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-marketing-promotions-advisor` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-messaging-channel-advisor` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-messaging-overview` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-messaging-services` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-messaging-webhooks` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-migrate-messaging-to-verify` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-notifications-alerts-advisor` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-numbers-senders` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-organizations-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-rcs-messaging` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-regulatory-compliance-bundles` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-reliability-patterns` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-security-api-auth` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-security-compliance-hipaa` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-security-hardening` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-send-message` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-sendgrid-account-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-sendgrid-deliverability-advisor` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-sendgrid-email-send` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-sendgrid-email-settings` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-sendgrid-engagement-quality` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-sendgrid-inbound-parse` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-sendgrid-suppressions` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-sendgrid-webhooks` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-sms-send-message` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-studio-flows` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-taskrouter-routing` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-verify-send-otp` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-voice-outbound-calls` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-voice-twiml` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-webhook-architecture` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-whatsapp-manage-senders` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `twilio-whatsapp-send-message` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `DATA-SNOW` — Snowflake · C=CDO · n=1

| Skill | Mod | Güvenlik |
|---|---|---|
| `snowflake-mcp-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `DATA-WH` — Warehouse / Airflow / dbt / Dagster · C=CDO · n=38

| Skill | Mod | Güvenlik |
|---|---|---|
| `adding-dbt-unit-test` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `airflow` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `airflow-hitl` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `airflow-plugins` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `analyzing-data` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `annotating-task-lineage` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `answering-natural-language-questions-with-dbt` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `auditing-warehouse-data-health` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `blueprint` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `building-dbt-semantic-layer` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `checking-freshness` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `clerk-astro-patterns` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `configuring-dbt-mcp-server` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `cosmos-dbt-core` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `cosmos-dbt-fusion` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `creating-openlineage-extractors` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `dagster-expert` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `deploying-airflow` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `diagnosing-failed-warehouse-syncs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `fetching-dbt-docs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `managing-astro-local-env` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `migrating-airflow-2-to-3` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `profiling-tables` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-blueprints` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `running-dbt-commands` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `setting-up-a-data-warehouse-source` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `setting-up-astro-project` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `setup-warehouse` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `setup-warehouse-bigquery` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `setup-warehouse-databricks` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `setup-warehouse-redshift` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `setup-warehouse-snowflake` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `tracing-downstream-lineage` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `tracing-upstream-lineage` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `troubleshooting-dbt-job-errors` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `using-dbt-for-analytics-engineering` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `warehouse-init` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `working-with-dbt-mesh` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `DB-DSQL` — Aurora DSQL · C=CTO · n=1

| Skill | Mod | Güvenlik |
|---|---|---|
| `dsql` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `DB-MONGO` — MongoDB Atlas · C=CTO · n=8

| Skill | Mod | Güvenlik |
|---|---|---|
| `atlas-stream-processing` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `mongodb-connection` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `mongodb-mcp-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `mongodb-natural-language-querying` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `mongodb-query-optimizer` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `mongodb-schema-design` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `mongodb-search-and-ai` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-database-setup-mongodb` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `DB-PLANET` — PlanetScale / Vitess / MySQL / Postgres · C=CTO · n=9

| Skill | Mod | Güvenlik |
|---|---|---|
| `mysql` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `neki` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `postgres` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-database-setup-mysql` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-database-setup-postgresql` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-database-setup-prisma-postgres` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `redis-development` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `supabase-postgres-best-practices` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `vitess` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `DB-SCYLLA` — ScyllaDB · C=CTO · n=3

| Skill | Mod | Güvenlik |
|---|---|---|
| `scylladb-cloud-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `scylladb-data-modeling` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `scylladb-vector-search` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `DEP-MONK` — Monk deploy · C=COO · n=1

| Skill | Mod | Güvenlik |
|---|---|---|
| `monk` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `DEP-RENDER` — Render · C=COO · n=19

| Skill | Mod | Güvenlik |
|---|---|---|
| `render-background-workers` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-cli` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-cron-jobs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-debug` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-disks` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-docker` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-domains` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-env-vars` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-keyvalue` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-mcp` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-migrate-from-heroku` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-monitor` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-networking` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-postgres` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-private-services` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-scaling` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-static-sites` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-web-services` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `render-workflows` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `DEP-VERCEL` — Vercel / Next · C=CTO · n=30

| Skill | Mod | Güvenlik |
|---|---|---|
| `ai-gateway` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `ai-sdk` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `auth` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `auth-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `bootstrap` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `cdn-caching` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `chat-sdk` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `env-vars` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `eve` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `exploring-autocapture-events` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `knowledge-update` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `marketplace` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `microfrontends` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `next-cache-components` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `next-forge` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `next-upgrade` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `nextjs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `react-best-practices` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `routing-middleware` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `runtime-cache` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `shadcn` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `turbopack` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `vercel-agent` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `vercel-cli` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `vercel-connect` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `vercel-firewall` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `vercel-sandbox` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `vercel-storage` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `verification` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `workflow` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `DES-FIGMA` — Figma · C=CPO · n=12

| Skill | Mod | Güvenlik |
|---|---|---|
| `figma-code-connect` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `figma-create-new-file` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `figma-design-to-code` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `figma-generate-design` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `figma-generate-diagram` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `figma-generate-library` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `figma-implement-motion` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `figma-swiftui` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `figma-use` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `figma-use-figjam` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `figma-use-motion` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `figma-use-slides` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `DOCS-PRD` — Docs / PRD / Mintlify · C=CCO · n=5

| Skill | Mod | Güvenlik |
|---|---|---|
| `check-prd-alignment` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `implement-from-prd` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `mintlify` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `update-prd` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `write-prd` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `EDGE-CF` — Cloudflare · C=CTO · n=9

| Skill | Mod | Güvenlik |
|---|---|---|
| `agents-sdk` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `building-ai-agent-on-cloudflare` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `building-mcp-server-on-cloudflare` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `cloudflare` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `durable-objects` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `sandbox-sdk` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `web-perf` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `workers-best-practices` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `wrangler` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `FE-GSAP` — GSAP motion · C=CPO · n=8

| Skill | Mod | Güvenlik |
|---|---|---|
| `gsap-core` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `gsap-frameworks` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `gsap-performance` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `gsap-plugins` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `gsap-react` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `gsap-scrolltrigger` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `gsap-timeline` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `gsap-utils` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `FEAT-CONF` — Feature flags / Confidence · C=CPO · n=20

| Skill | Mod | Güvenlik |
|---|---|---|
| `analyze-experiments` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `analyzing-experiment-session-replays` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `auditing-experiments-flags` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `chaos-experiment` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `cleaning-up-stale-feature-flags` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `configuring-experiment-analytics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `configuring-experiment-rollout` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `creating-experiments` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `diagnosing-experiment-results` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `finding-deleted-feature-flags` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `finding-experiments` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `instrument-feature-flags` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `manage-feature-flags` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `managing-experiment-lifecycle` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `migrate-eppo` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `migrate-optimizely` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `migrate-posthog` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `migrate-statsig` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `onboard-confidence` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `onboard-confidence-dry-run` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `GEN-OPS` — Genel Operasyon · C=COO · n=14

| Skill | Mod | Güvenlik |
|---|---|---|
| `compare-user-journeys` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-chart` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-dashboard` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-template` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `cx-config` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `cx-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `debugging-dags` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `exploring-apm-traces` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `exploring-live-traffic` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `exploring-llm-costs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `exploring-llm-evaluations` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `exploring-llm-traces` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `investigating-error-issue` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `testing-dags` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `META-CURSOR` — Cursor meta skills · C=CIO · n=17

| Skill | Mod | Güvenlik |
|---|---|---|
| `babysit` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `canvas` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-hook` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-rule` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-skill` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `create-subagent` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `migrate-to-builds` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `migrate-to-skills` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `review` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `review-bugbot` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `review-security` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `sdk` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `shell` | yerel-cursor | 5-kural + credential yoksa dry-run |
| `split-to-prs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `statusline` | yerel-cursor | 5-kural + credential yoksa dry-run |
| `update-cli-config` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `update-cursor-settings` | yerel-cursor | 5-kural + credential yoksa dry-run |

### `ML-HF` — Hugging Face · C=CAIO · n=18

| Skill | Mod | Güvenlik |
|---|---|---|
| `hf-cli` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-best` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-community-evals` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-datasets` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-gradio` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-llm-trainer` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-local-models` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-lora-space-builder` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-paper-publisher` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-papers` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-spaces` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-tool-builder` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-trackio` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-vision-trainer` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `huggingface-zerogpu` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `train-sentence-transformers` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `transformers-js` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `trl-training` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `MOB-XCODE` — Xcode · C=CTO · n=1

| Skill | Mod | Güvenlik |
|---|---|---|
| `xcode-project-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `OBS-ELK` — Elastic / Kibana / EDOT · C=CISO · n=33

| Skill | Mod | Güvenlik |
|---|---|---|
| `cloud-access-management` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `cloud-create-project` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `cloud-manage-project` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `cloud-network-security` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `cloud-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `elasticsearch-audit` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `elasticsearch-authn` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `elasticsearch-authz` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `elasticsearch-esql` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `elasticsearch-file-ingest` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `elasticsearch-onboarding` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `elasticsearch-security-troubleshooting` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `kibana-agent-builder` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `kibana-alerting-rules` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `kibana-audit` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `kibana-connectors` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `kibana-dashboards` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `kibana-streams` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `kibana-vega` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `observability-edot-dotnet-instrument` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `observability-edot-dotnet-migrate` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `observability-edot-java-instrument` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `observability-edot-java-migrate` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `observability-edot-python-instrument` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `observability-edot-python-migrate` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `observability-llm-obs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `observability-logs-search` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `observability-service-health` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `security-alert-triage` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `security-case-management` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `security-detection-rule-management` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `security-generate-security-sample-data` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `signals-scout-observability-gaps` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `OBS-GRAF` — Grafana · C=CISO · n=2

| Skill | Mod | Güvenlik |
|---|---|---|
| `grafana-assistant-cli` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `grafana-cloud-mcp-tools` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `OBS-OBSERVE` — Observe / OTel / Alert · C=CISO · n=16

| Skill | Mod | Güvenlik |
|---|---|---|
| `alert-investigation` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `debug-k8s-collection` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `debug-linux-host-collection` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `deploy-k8s-explorer` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `deploy-linux-host-explorer` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `generate-opal` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `observe-cli` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `opentelemetry-auto-instrumentation` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `opentelemetry-manual-instrumentation` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `opentelemetry-validation` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `outlier-detection-analysis` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `query-card-visualization` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `setup-k8s-backend` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `setup-k8s-collection` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `setup-linux-host-backend` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `setup-linux-host-collection` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `OBS-SENTRY` — Sentry · C=CISO · n=7

| Skill | Mod | Güvenlik |
|---|---|---|
| `sentry-create-alert` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `sentry-debug-issue` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `sentry-feature-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `sentry-get-started` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `sentry-instrument` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `sentry-otel-exporter-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `sentry-snapshots-cocoa` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `OPS-PD` — PagerDuty · C=COO · n=1

| Skill | Mod | Güvenlik |
|---|---|---|
| `pagerduty-mcp-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `OPS-TZ` — TierZero / Antimetal incident · C=COO · n=8

| Skill | Mod | Güvenlik |
|---|---|---|
| `antimetal-mcp-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `fix` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `investigate` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `investigate-ai-session` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `investigate-metric` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `scan-and-fix-accessibility` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `tierzero-fetch` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `tierzero-investigate` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `ORM-PRISMA` — Prisma · C=CTO · n=34

| Skill | Mod | Güvenlik |
|---|---|---|
| `prisma-cli-db-execute` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-db-pull` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-db-push` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-db-seed` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-debug` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-dev` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-format` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-generate` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-init` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-migrate-dev` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-migrate-diff` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-migrate-reset` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-migrate-resolve` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-migrate-status` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-studio` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-cli-validate` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-client-api-client-methods` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-client-api-constructor` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-client-api-filters` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-client-api-model-queries` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-client-api-query-options` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-client-api-raw-queries` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-client-api-relations` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-client-api-transactions` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-database-setup-prisma-client-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-database-setup-sqlite` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-database-setup-sqlserver` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-upgrade-v7-accelerate-users` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-upgrade-v7-driver-adapters` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-upgrade-v7-env-variables` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-upgrade-v7-esm-support` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-upgrade-v7-prisma-config` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-upgrade-v7-removed-features` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-upgrade-v7-schema-changes` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `QA-BS` — BrowserStack / a11y · C=CTO · n=2

| Skill | Mod | Güvenlik |
|---|---|---|
| `run-mobile-tests-on-browserstack` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `run-web-tests-on-browserstack` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `SEARCH-OS` — OpenSearch · C=CDO · n=1

| Skill | Mod | Güvenlik |
|---|---|---|
| `opensearch-skills` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `SEC-CRDB` — CockroachDB security/ops · C=CISO · n=32

| Skill | Mod | Güvenlik |
|---|---|---|
| `analyzing-range-distribution` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `analyzing-schema-change-storage-risk` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `auditing-table-statistics` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `benchmarking-transaction-patterns` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `cockroachdb-sql` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `configuring-audit-logging` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `configuring-ip-allowlists` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `configuring-log-export` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `configuring-private-connectivity` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `configuring-sso-and-scim` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `designing-application-transactions` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `designing-multi-region-applications` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `enabling-cmek-encryption` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `enforcing-password-policies` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `hardening-user-privileges` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `managing-certificates-and-encryption` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `managing-cluster-capacity` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `managing-cluster-settings` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `managing-tls-certificates` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `molt-fetch` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `molt-replicator` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `molt-verify` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `monitoring-background-jobs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `performing-cluster-maintenance` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `preparing-compliance-documentation` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `prisma-database-setup-cockroachdb` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `profiling-statement-fingerprints` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `profiling-transaction-fingerprints` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `provisioning-cluster-for-production` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `reviewing-cluster-health` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `triaging-live-sql-activity` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `upgrading-cluster-version` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `SEC-JFROG` — JFrog · C=CISO · n=3

| Skill | Mod | Güvenlik |
|---|---|---|
| `jfrog` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `jfrog-ai-catalog-skills` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `jfrog-package-safety-and-download` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `VEC-PIN` — Pinecone · C=CTO · n=8

| Skill | Mod | Güvenlik |
|---|---|---|
| `pinecone-assistant` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `pinecone-cli` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `pinecone-docs` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `pinecone-full-text-search` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `pinecone-help` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `pinecone-mcp` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `pinecone-query` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `pinecone-quickstart` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `VEC-TPUF` — Turbopuffer · C=CTO · n=1

| Skill | Mod | Güvenlik |
|---|---|---|
| `tpuf` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `WEB-APIFY` — Apify / Firecrawl / Bright Data · C=CSO · n=24

| Skill | Mod | Güvenlik |
|---|---|---|
| `apify-actor-development` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `apify-actorization` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `apify-generate-output-schema` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `apify-sdk-integration` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `apify-ultimate-scraper` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `bd-batch-scrape` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `bd-browser` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `bd-code` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `bd-scrape` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `bd-search` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `bd-structured-data` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `exa-best-practices` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `exa-fetch` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `exa-web-search` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firecrawl` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firecrawl-agent` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firecrawl-crawl` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firecrawl-download` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firecrawl-interact` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firecrawl-map` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firecrawl-monitor` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firecrawl-parse` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firecrawl-scrape` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `firecrawl-search` | sablon+mcp | 5-kural + credential yoksa dry-run |

### `WF-TEMP` — Temporal · C=CTO · n=2

| Skill | Mod | Güvenlik |
|---|---|---|
| `temporal-cloud-setup` | sablon+mcp | 5-kural + credential yoksa dry-run |
| `temporal-developer` | sablon+mcp | 5-kural + credential yoksa dry-run |

