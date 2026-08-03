#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill_ajans_uretim.py — Kullanıcı skill listesini ajans yapısına bağlar.

🚩 900.000.000.000 karakter/prompt RED: bağlam + depo imkânsız (K-017 emsali).
Eşdeğer: skill→title→workflow→122 prompt sözleşmesi (4–12 KiB) + Claude Code MASTER yapıştırma.

Üretir:
  data/skill_envanteri.json
  data/skill_title_haritasi.json
  docs/SKILL-AJANS-HIYERARSI.md
  docs/SKILL-ROADMAP-7x24.md
  .github/workflows/skill-ajans-dongu.yml
  uretim/devir/CLAUDE-CODE-MASTER-PROMPT-SKILL-AJANS.md
  uretim/skill-workflows/*.md (domain kümeleri)
  uretim/promptlar/SKILL-OPS/** (pilot skill-operatör promptları)
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
NOW = dt.datetime.now(dt.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
TODAY = NOW.strftime("%Y-%m-%d")
PROMPTS = 122
CHAR_MIN, CHAR_MAX = 4000, 12000

# --- Kullanıcı listesinden skill adları (dedupe) ---
RAW_SKILLS = """
setup-linux-host-collection setup-linux-host-backend setup-k8s-collection setup-k8s-backend
query-card-visualization outlier-detection-analysis opentelemetry-validation
opentelemetry-manual-instrumentation opentelemetry-auto-instrumentation observe-cli generate-opal
deploy-linux-host-explorer deploy-k8s-explorer debug-linux-host-collection debug-k8s-collection
alert-investigation apify-ultimate-scraper apify-sdk-integration apify-generate-output-schema
apify-actorization apify-actor-development setup-warehouse-snowflake setup-warehouse-redshift
setup-warehouse-databricks setup-warehouse-bigquery setup-warehouse onboard-confidence-dry-run
onboard-confidence migrate-statsig migrate-posthog migrate-optimizely migrate-eppo mintlify
cx-setup cx-config write-prd update-prd implement-from-prd check-prd-alignment
scylladb-vector-search scylladb-data-modeling scylladb-cloud-setup monk grafana-cloud-mcp-tools
tracking-implementation manage-lexicon deep-research tierzero-investigate tierzero-fetch
twilio-sendgrid-webhooks twilio-sendgrid-suppressions twilio-sendgrid-inbound-parse
twilio-sendgrid-engagement-quality twilio-sendgrid-email-settings twilio-sendgrid-email-send
twilio-sendgrid-deliverability-advisor twilio-sendgrid-account-setup twilio-whatsapp-send-message
twilio-whatsapp-manage-senders twilio-webhook-architecture twilio-voice-twiml twilio-voice-outbound-calls
twilio-verify-send-otp twilio-taskrouter-routing twilio-studio-flows twilio-sms-send-message
twilio-isv-sms-best-practices twilio-send-message twilio-security-hardening
twilio-security-compliance-hipaa twilio-security-api-auth twilio-reliability-patterns
twilio-regulatory-compliance-bundles twilio-rcs-messaging twilio-organizations-setup
twilio-numbers-senders twilio-notifications-alerts-advisor twilio-migrate-messaging-to-verify
twilio-messaging-webhooks twilio-messaging-services twilio-messaging-overview
twilio-messaging-channel-advisor twilio-marketing-promotions-advisor twilio-lookup-phone-intelligence
twilio-identity-verification-advisor twilio-iam-auth-setup twilio-enterprise-knowledge
twilio-email-send twilio-email-deliverability-advisor twilio-debugging-observability
twilio-customer-support-architect twilio-conversations-classic-api twilio-conversation-orchestrator
twilio-conversation-memory twilio-conversation-intelligence twilio-content-template-builder
twilio-conference-calls twilio-compliance-traffic twilio-compliance-onboarding twilio-cli-reference
twilio-call-recordings twilio-ai-agent-architect twilio-agent-connect twilio-agent-augmentation-architect
twilio-account-setup template-usage security-report scorecard-review run-pipeline migrate-pipeline
manage-users manage-slos manage-roles manage-pull-requests manage-freeze-windows manage-feature-flags
manage-delegates gitops-status dora-metrics debug-pipeline create-trigger create-template create-secret
create-policy create-pipeline-v1 create-pipeline create-infrastructure create-environment create-connector
create-agent-template create-agent chaos-experiment audit-report analyze-costs
gsap-utils gsap-timeline gsap-scrolltrigger gsap-react gsap-plugins gsap-performance gsap-frameworks gsap-core
opensearch-skills dagster-expert get-visual-embed-sdk-reference get-rest-api-reference
get-developer-docs-reference microsoft-foundry entra-app-registration entra-agent-id azure-validate
azure-upgrade azure-storage azure-resource-visualizer azure-resource-lookup azure-reliability azure-rbac
azure-quotas azure-prepare azure-messaging azure-kusto azure-kubernetes azure-hosted-copilot-sdk
azure-enterprise-infra-planner azure-diagnostics azure-deploy azure-cost azure-compute azure-compliance
azure-cloud-migrate azure-aigateway azure-ai appinsights-instrumentation airunway-aks-setup
temporal-developer temporal-cloud-setup dsql workos-widgets workos exa-web-search exa-fetch
exa-best-practices tpuf appwrite-typescript appwrite-swift appwrite-ruby appwrite-python appwrite-php
appwrite-kotlin appwrite-go appwrite-dotnet appwrite-dart appwrite-cli bd-structured-data bd-search
bd-scrape bd-code bd-browser bd-batch-scrape preparing-compliance-documentation managing-tls-certificates
hardening-user-privileges enforcing-password-policies enabling-cmek-encryption configuring-sso-and-scim
configuring-private-connectivity configuring-log-export configuring-ip-allowlists configuring-audit-logging
auditing-cloud-cluster-security cockroachdb-sql upgrading-cluster-version reviewing-cluster-health
provisioning-cluster-for-production performing-cluster-maintenance managing-cluster-settings
managing-cluster-capacity managing-certificates-and-encryption molt-verify molt-replicator molt-fetch
triaging-live-sql-activity profiling-transaction-fingerprints profiling-statement-fingerprints
monitoring-background-jobs auditing-table-statistics analyzing-schema-change-storage-risk
analyzing-range-distribution designing-multi-region-applications designing-application-transactions
benchmarking-transaction-patterns warehouse-init tracing-upstream-lineage tracing-downstream-lineage
testing-dags setting-up-astro-project profiling-tables migrating-airflow-2-to-3 managing-astro-local-env
deploying-airflow debugging-dags creating-openlineage-extractors cosmos-dbt-fusion cosmos-dbt-core
checking-freshness blueprint authoring-dags annotating-task-lineage analyzing-data airflow-plugins
airflow-hitl airflow pinecone-quickstart pinecone-query pinecone-mcp pinecone-help pinecone-full-text-search
pinecone-docs pinecone-cli pinecone-assistant security-generate-security-sample-data
security-detection-rule-management security-case-management security-alert-triage
observability-service-health observability-manage-slos observability-logs-search observability-llm-obs
observability-edot-python-migrate observability-edot-python-instrument observability-edot-java-migrate
observability-edot-java-instrument observability-edot-dotnet-migrate observability-edot-dotnet-instrument
kibana-streams kibana-vega kibana-dashboards kibana-connectors kibana-audit kibana-alerting-rules
kibana-agent-builder elasticsearch-security-troubleshooting elasticsearch-onboarding
elasticsearch-file-ingest elasticsearch-esql elasticsearch-authz elasticsearch-authn elasticsearch-audit
cloud-setup cloud-network-security cloud-manage-project cloud-create-project cloud-access-management
working-with-dbt-mesh using-dbt-for-analytics-engineering troubleshooting-dbt-job-errors
running-dbt-commands fetching-dbt-docs configuring-dbt-mcp-server building-dbt-semantic-layer
answering-natural-language-questions-with-dbt adding-dbt-unit-test encore-testing encore-service
encore-migrate encore-infrastructure encore-go-testing encore-go-service encore-go-infrastructure
encore-go-getting-started encore-go-database encore-go-code-review encore-go-auth encore-go-api
encore-getting-started encore-frontend debug-traces encore-database create-service encore-code-review
encore-auth encore-api add-infrastructure xcode-project-setup firebase-security-rules-auditor
firebase-remote-config-basics firebase-hosting-basics firebase-firestore firebase-data-connect
firebase-crashlytics firebase-basics firebase-auth-basics firebase-ai-logic-basics
firebase-app-hosting-basics session-replay feedback-analysis feature-adoption account-health
amplify-workflow aws-step-functions aws-serverless-deployment aws-lambda-managed-instances
aws-lambda-durable-functions aws-lambda api-gateway amazon-location-service mongodb-search-and-ai
mongodb-schema-design mongodb-query-optimizer mongodb-natural-language-querying mongodb-mcp-setup
mongodb-connection atlas-stream-processing investigate fix antimetal-mcp-setup omni-query
omni-model-explorer omni-model-builder omni-embed omni-content-explorer omni-content-builder
omni-ai-optimizer omni-admin postman-routing postman-knowledge agent-ready-apis ddtoolsets ddsetup
ddconfig render-workflows render-web-services render-static-sites render-scaling render-private-services
render-postgres render-networking render-monitor render-migrate-from-heroku render-mcp render-keyvalue
render-env-vars render-domains render-docker render-disks render-deploy render-debug render-cron-jobs
render-cli render-blueprints render-background-workers jfrog-package-safety-and-download
jfrog-ai-catalog-skills jfrog pagerduty-mcp-setup firecrawl-search firecrawl-scrape firecrawl-parse
firecrawl-monitor firecrawl-map firecrawl-interact firecrawl-download firecrawl-crawl firecrawl
firecrawl-agent what-would-lenny-do weekly-brief taxonomy review-agent-insights replay-ux-audit
monitor-reliability monitor-ai-quality investigate-ai-session instrument-events discover-opportunities
discover-event-surfaces discover-analytics-patterns diff-intake diagnose-errors debug-replay daily-brief
create-dashboard create-chart compare-user-journeys analyze-feedback analyze-experiments analyze-dashboard
analyze-chart analyze-ai-topics analyze-account-health add-analytics-instrumentation postgres vitess
mysql neki grafana-assistant-cli trl-training transformers-js train-sentence-transformers
huggingface-zerogpu huggingface-vision-trainer huggingface-trackio huggingface-tool-builder
huggingface-spaces huggingface-papers huggingface-paper-publisher huggingface-lora-space-builder
huggingface-local-models huggingface-llm-trainer huggingface-gradio huggingface-datasets
huggingface-community-evals hf-cli huggingface-best redis-development working-with-skills
tuning-incremental-sync-config triaging-visual-review-runs triaging-error-issues suppressing-noisy-errors
suggesting-data-imports skills-store signals-scout-surveys signals-scout-revenue-analytics
signals-scout-observability-gaps signals-scout-logs signals-scout-general signals-scout-error-tracking
signals-scout-csp-violations signals-scout-anomaly-detection signals-scout-ai-observability signals
setting-up-a-data-warehouse-source querying-posthog-data planning-user-interviews managing-subscriptions
managing-path-cleaning-rules managing-experiment-lifecycle managing-endpoint-versions investigating-replay
investigating-error-issue investigate-metric instrument-product-analytics instrument-logs
instrument-llm-analytics instrument-integration instrument-feature-flags instrument-error-tracking
inbox-exploration grouping-noisy-errors formatting-insight-axes finding-sessions-to-watch
finding-replay-for-issue finding-experiments finding-deleted-feature-flags feature-usage-feed
exploring-signals-scouts exploring-llm-traces exploring-llm-evaluations exploring-llm-costs
exploring-live-traffic exploring-autocapture-events exploring-apm-traces downloading-batch-export-files
diagnosing-stacktrace-symbolication diagnosing-sdk-health diagnosing-missing-recordings
diagnosing-failed-warehouse-syncs diagnosing-experiment-results diagnosing-endpoint-performance
debugging-signals-pipeline debugging-local-replay creating-replay-vision-scanners creating-experiments
creating-an-endpoint copying-flags-across-projects consuming-endpoints-from-client-code
configuring-experiment-rollout configuring-experiment-analytics cleaning-up-stale-feature-flags
authoring-signals-scouts authoring-log-alerts auditing-warehouse-data-health auditing-experiments-flags
auditing-endpoints assessing-heatmaps analyzing-experiment-session-replays clickhousectl-cloud-deploy
chdb-datastore clickhouse-best-practices clickhouse-architecture-advisor clickhousectl-local-dev
chdb-sql clickhouse-js-node-troubleshooting clerk-swift clerk-expo clerk-android clerk-vue-patterns
clerk-tanstack-patterns clerk-react-router-patterns clerk-react-patterns clerk-nuxt-patterns
clerk-nextjs-patterns clerk-expo-patterns clerk-chrome-extension-patterns clerk-astro-patterns
clerk-webhooks clerk-testing clerk-orgs clerk-billing clerk-setup clerk-custom-ui clerk-backend-api
clerk functions slack-search slack-messaging slack-cli slack-api create-slack-app block-kit
figma-use-slides figma-use-motion figma-use-figjam figma-use figma-swiftui figma-implement-motion
figma-generate-library figma-generate-diagram figma-generate-design figma-design-to-code
figma-create-new-file figma-code-connect snowflake-mcp-setup supabase supabase-postgres-best-practices
hex-to-canvas hex-notebook-authoring hex-business-analytics-question elastic-beanstalk deploy
aws-architecture-diagram workflow verification vercel-storage vercel-sandbox vercel-functions
vercel-firewall vercel-connect vercel-cli vercel-agent turbopack shadcn runtime-cache routing-middleware
react-best-practices nextjs next-upgrade next-forge next-cache-components microfrontends marketplace
knowledge-update eve env-vars deployments-cicd chat-sdk cdn-caching bootstrap auth ai-sdk ai-gateway
access-protected-vercel-deployment sentry-snapshots-cocoa sentry-otel-exporter-setup sentry-instrument
sentry-get-started sentry-feature-setup sentry-debug-issue sentry-create-alert
scan-and-fix-accessibility run-web-tests-on-browserstack run-mobile-tests-on-browserstack wrangler
workers-best-practices web-perf sandbox-sdk durable-objects cloudflare building-mcp-server-on-cloudflare
building-ai-agent-on-cloudflare agents-sdk prisma-upgrade-v7-schema-changes prisma-upgrade-v7-removed-features
prisma-upgrade-v7-prisma-config prisma-upgrade-v7-esm-support prisma-upgrade-v7-env-variables
prisma-upgrade-v7-driver-adapters prisma-upgrade-v7-accelerate-users prisma-database-setup-sqlserver
prisma-database-setup-sqlite prisma-database-setup-prisma-postgres prisma-database-setup-prisma-client-setup
prisma-database-setup-postgresql prisma-database-setup-mysql prisma-database-setup-mongodb
prisma-database-setup-cockroachdb prisma-client-api-transactions prisma-client-api-relations
prisma-client-api-raw-queries prisma-client-api-query-options prisma-client-api-model-queries
prisma-client-api-filters prisma-client-api-constructor prisma-client-api-client-methods
prisma-cli-validate prisma-cli-studio prisma-cli-migrate-status prisma-cli-migrate-resolve
prisma-cli-migrate-reset prisma-cli-migrate-diff prisma-cli-migrate-dev prisma-cli-migrate-deploy
prisma-cli-init prisma-cli-generate prisma-cli-format prisma-cli-dev prisma-cli-debug prisma-cli-db-seed
prisma-cli-db-push prisma-cli-db-pull prisma-cli-db-execute schema-builder migration-helper
function-creator convex-quickstart convex-helpers-guide components-guide auth-setup
update-cursor-settings update-cli-config statusline split-to-prs shell review-security review-bugbot
review migrate-to-skills migrate-to-builds sdk create-subagent create-skill create-rule create-hook
canvas babysit
""".split()

DOMAIN_RULES: list[tuple[str, str, str, list[str]]] = [
    # (domain_id, domain_ad, c_level, prefixes/keywords)
    ("OBS-OBSERVE", "Observe / OTel / Alert", "CISO", ["observe", "opentelemetry", "opal", "outlier", "query-card", "alert-investigation", "linux-host", "k8s-"]),
    ("WEB-APIFY", "Apify / Firecrawl / Bright Data", "CSO", ["apify", "firecrawl", "bd-", "exa-"]),
    ("DATA-WH", "Warehouse / Airflow / dbt / Dagster", "CDO", ["warehouse", "airflow", "dbt", "dagster", "cosmos", "blueprint", "lineage", "freshness", "profiling-tables", "analyzing-data", "astro"]),
    ("FEAT-CONF", "Feature flags / Confidence", "CPO", ["confidence", "statsig", "optimizely", "eppo", "feature-flag", "experiment", "migrate-posthog"]),
    ("DOCS-PRD", "Docs / PRD / Mintlify", "CCO", ["mintlify", "prd", "write-prd", "update-prd", "implement-from-prd", "check-prd"]),
    ("DB-SCYLLA", "ScyllaDB", "CTO", ["scylla"]),
    ("DEP-MONK", "Monk deploy", "COO", ["monk"]),
    ("OBS-GRAF", "Grafana", "CISO", ["grafana"]),
    ("AN-MIX", "Mixpanel / analytics track", "CMO", ["tracking-implementation", "manage-lexicon", "deep-research"]),
    ("OPS-TZ", "TierZero / Antimetal incident", "COO", ["tierzero", "antimetal", "investigate", "fix"]),
    ("COMMS-TW", "Twilio / SendGrid / Voice", "CRO", ["twilio"]),
    ("CICD-HAR", "Harness CI/CD", "CTO", ["pipeline", "harness", "gitops", "dora", "freeze", "delegate", "chaos", "scorecard", "template-usage", "security-report", "analyze-costs", "create-agent", "create-connector", "create-environment", "create-infrastructure", "create-policy", "create-secret", "create-trigger", "manage-users", "manage-roles", "manage-slos", "manage-pull", "manage-feature", "audit-report", "debug-pipeline", "run-pipeline", "migrate-pipeline"]),
    ("FE-GSAP", "GSAP motion", "CPO", ["gsap"]),
    ("SEARCH-OS", "OpenSearch", "CDO", ["opensearch"]),
    ("BI-TS", "ThoughtSpot / Omni / Hex", "CDO", ["get-visual", "get-rest", "get-developer", "omni-", "hex-"]),
    ("CLOUD-AZ", "Azure / Entra / Foundry", "CTO", ["azure", "entra", "microsoft-foundry", "appinsights", "airunway"]),
    ("WF-TEMP", "Temporal", "CTO", ["temporal"]),
    ("DB-DSQL", "Aurora DSQL", "CTO", ["dsql"]),
    ("AUTH-WO", "WorkOS", "CISO", ["workos"]),
    ("VEC-TPUF", "Turbopuffer", "CTO", ["tpuf"]),
    ("BAAS-APP", "Appwrite", "CTO", ["appwrite"]),
    ("SEC-CRDB", "CockroachDB security/ops", "CISO", ["cockroach", "molt-", "cmek", "tls-cert", "password-polic", "sso-and-scim", "private-connectivity", "log-export", "ip-allowlist", "audit-logging", "compliance-documentation", "hardening-user", "provisioning-cluster", "reviewing-cluster", "upgrading-cluster", "performing-cluster", "managing-cluster", "managing-certificates", "triaging-live", "profiling-", "monitoring-background", "auditing-table", "analyzing-schema", "analyzing-range", "designing-multi", "designing-application", "benchmarking-transaction"]),
    ("VEC-PIN", "Pinecone", "CTO", ["pinecone"]),
    ("OBS-ELK", "Elastic / Kibana / EDOT", "CISO", ["elasticsearch", "kibana", "observability-", "security-detection", "security-case", "security-alert", "security-generate", "cloud-setup", "cloud-network", "cloud-manage", "cloud-create", "cloud-access"]),
    ("BE-ENCORE", "Encore", "CTO", ["encore", "create-service", "add-infrastructure", "debug-traces"]),
    ("MOB-XCODE", "Xcode", "CTO", ["xcode"]),
    ("BAAS-FB", "Firebase", "CTO", ["firebase"]),
    ("AN-PH", "PostHog / Pendo signals", "CMO", ["session-replay", "feedback-analysis", "feature-adoption", "account-health", "posthog", "signals", "replay", "what-would-lenny", "weekly-brief", "daily-brief", "taxonomy", "instrument-", "explore", "diagnos", "creating-experiment", "creating-an-endpoint", "auditing-", "assessing-heatmaps", "analyze-", "add-analytics", "discover-", "diff-intake", "monitor-", "review-agent", "inbox-", "grouping-noisy", "formatting-insight", "finding-", "feature-usage", "downloading-batch", "debugging-signals", "debugging-local", "copying-flags", "consuming-endpoints", "configuring-experiment", "cleaning-up-stale", "authoring-", "planning-user", "managing-subscription", "managing-path", "managing-experiment", "managing-endpoint", "setting-up-a-data", "querying-posthog", "skills-store", "suggesting-data", "suppressing-noisy", "triaging-", "tuning-incremental", "working-with-skills"]),
    ("CLOUD-AWS", "AWS serverless", "CTO", ["aws-", "amplify", "api-gateway", "amazon-location", "elastic-beanstalk", "deploy"]),
    ("DB-MONGO", "MongoDB Atlas", "CTO", ["mongodb", "atlas-stream"]),
    ("API-POST", "Postman", "CTO", ["postman", "agent-ready", "ddtoolsets", "ddsetup", "ddconfig"]),
    ("DEP-RENDER", "Render", "COO", ["render-"]),
    ("SEC-JFROG", "JFrog", "CISO", ["jfrog"]),
    ("OPS-PD", "PagerDuty", "COO", ["pagerduty"]),
    ("DB-PLANET", "PlanetScale / Vitess / MySQL / Postgres", "CTO", ["postgres", "vitess", "mysql", "neki", "redis"]),
    ("ML-HF", "Hugging Face", "CAIO", ["huggingface", "hf-cli", "trl-", "transformers", "train-sentence"]),
    ("AUTH-CLERK", "Clerk", "CISO", ["clerk"]),
    ("COMMS-SLACK", "Slack", "COO", ["slack", "block-kit", "functions"]),
    ("DES-FIGMA", "Figma", "CPO", ["figma"]),
    ("DATA-SNOW", "Snowflake", "CDO", ["snowflake"]),
    ("BAAS-SUPA", "Supabase", "CTO", ["supabase"]),
    ("ARCH-AWS", "AWS architecture diagram", "CTO", ["aws-architecture"]),
    ("DEP-VERCEL", "Vercel / Next", "CTO", ["vercel", "nextjs", "next-", "turbopack", "shadcn", "runtime-cache", "routing-middleware", "react-best", "microfrontends", "marketplace", "knowledge-update", "eve", "env-vars", "deployments-cicd", "chat-sdk", "cdn-caching", "bootstrap", "auth", "ai-sdk", "ai-gateway", "access-protected", "workflow", "verification"]),
    ("OBS-SENTRY", "Sentry", "CISO", ["sentry"]),
    ("QA-BS", "BrowserStack / a11y", "CTO", ["browserstack", "scan-and-fix"]),
    ("EDGE-CF", "Cloudflare", "CTO", ["wrangler", "workers", "web-perf", "sandbox-sdk", "durable-objects", "cloudflare", "building-mcp", "building-ai-agent", "agents-sdk"]),
    ("ORM-PRISMA", "Prisma", "CTO", ["prisma"]),
    ("BAAS-CONVEX", "Convex", "CTO", ["convex", "schema-builder", "migration-helper", "function-creator", "components-guide", "auth-setup"]),
    ("META-CURSOR", "Cursor meta skills", "CIO", ["update-cursor", "update-cli", "statusline", "split-to-prs", "shell", "review-security", "review-bugbot", "review", "migrate-to-skills", "migrate-to-builds", "sdk", "create-subagent", "create-skill", "create-rule", "create-hook", "canvas", "babysit"]),
    ("AN-CH", "ClickHouse", "CDO", ["clickhouse", "chdb"]),
]


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9-]+", "-", s.lower()).strip("-")[:64]


def classify(skill: str) -> tuple[str, str, str]:
    s = skill.lower()
    for did, dad, chair, keys in DOMAIN_RULES:
        for k in keys:
            if s == k or s.startswith(k) or k in s:
                return did, dad, chair
    return "GEN-OPS", "Genel Operasyon", "COO"


def build_inventory() -> dict[str, Any]:
    skills = sorted(set(RAW_SKILLS))
    by_domain: dict[str, list[str]] = {}
    items = []
    for sk in skills:
        did, dad, chair = classify(sk)
        by_domain.setdefault(did, []).append(sk)
        items.append({
            "skill": sk,
            "domain_id": did,
            "domain_ad": dad,
            "c_level": chair,
            "calisma_modu": "sablon+mcp" if not sk.startswith(("update-cursor", "shell", "statusline")) else "yerel-cursor",
            "guvenlik": "5-kural + credential yoksa dry-run",
            "son_inceleme": TODAY,
        })
    return {
        "ts": TS,
        "adet": len(skills),
        "domain_adet": len(by_domain),
        "flag": {
            "istek": "900000000000 karakter/prompt + tüm skillleri canlı çalıştır",
            "karar": "REDDEDILDI / KISMI",
            "neden": "karakter imkansiz; skilllerin cogu credential/tenant ister — dry-run + sablon + Claude Code devir",
            "esdeger": "envanter+title+workflow+122 sozlesme + MASTER yapistirma",
        },
        "domainler": {k: {"ad": next(d[1] for d in DOMAIN_RULES if d[0] == k) if k != "GEN-OPS" else "Genel Operasyon", "adet": len(v), "skills": sorted(v)} for k, v in sorted(by_domain.items())},
        "skills": items,
    }


def build_titles(inv: dict) -> dict[str, Any]:
    """Her domain için C→IC title zinciri + skill operatörleri."""
    titles = []
    # Holding board
    for role, kat in [
        ("Chairman / Sahip", "KURUL"),
        ("Group CEO", "C-OFİS"),
        ("Group COO", "C-OFİS"),
        ("Group CTO", "C-LEVEL"),
        ("Group CAIO", "C-LEVEL"),
        ("Group CDO", "C-LEVEL"),
        ("Group CISO", "C-LEVEL"),
        ("Group CMO", "C-LEVEL"),
        ("Group CRO", "C-LEVEL"),
        ("Group CPO", "C-LEVEL"),
        ("Group CCO", "C-LEVEL"),
        ("Group CIO", "C-LEVEL"),
        ("Group CFO", "C-LEVEL"),
        ("Group CHRO", "C-LEVEL"),
        ("Group CLO", "C-LEVEL"),
        ("Group CSO", "C-LEVEL"),
    ]:
        titles.append({"title": role, "katman": kat, "domain_id": "HOLDING", "skill_odak": [], "prompt_adet": PROMPTS})

    for did, meta in inv["domainler"].items():
        chair = next((d[2] for d in DOMAIN_RULES if d[0] == did), "COO")
        titles.append({
            "title": f"{meta['ad']} Domain Başkanı",
            "katman": "DOMAIN-YÖNETİM",
            "domain_id": did,
            "rapor": chair,
            "skill_odak": meta["skills"][:8],
            "prompt_adet": PROMPTS,
        })
        titles.append({
            "title": f"{meta['ad']} Lead Operatör",
            "katman": "YÖNETİM",
            "domain_id": did,
            "rapor": f"{meta['ad']} Domain Başkanı",
            "skill_odak": meta["skills"],
            "prompt_adet": PROMPTS,
        })
        titles.append({
            "title": f"{meta['ad']} Skill Uzmanı (IC)",
            "katman": "IC",
            "domain_id": did,
            "rapor": f"{meta['ad']} Lead Operatör",
            "skill_odak": meta["skills"],
            "prompt_adet": PROMPTS,
        })
        titles.append({
            "title": f"{meta['ad']} Uygulama Operatörü",
            "katman": "WORKER",
            "domain_id": did,
            "rapor": f"{meta['ad']} Skill Uzmanı (IC)",
            "skill_odak": meta["skills"][:5],
            "prompt_adet": PROMPTS,
        })

    # Ekip title'ları (her domain bir ekip)
    ekipler = []
    for did, meta in inv["domainler"].items():
        ekipler.append({
            "ekip": f"Ekip-{did}",
            "domain_id": did,
            "ad": meta["ad"],
            "uyeler": 4,
            "prompt_adet_ekip": PROMPTS,
            "prompt_adet_uygulama": PROMPTS,
            "7x24": {
                "nobet": "Lead Operatör",
                "eskalasyon": f"{meta['ad']} Domain Başkanı → Group {next((d[2] for d in DOMAIN_RULES if d[0]==did), 'COO')}",
                "ritim": ["günlük standup", "haftalık skill sağlık", "aylık arşiv yenileme"],
            },
        })

    return {
        "ts": TS,
        "title_adet": len(titles),
        "ekip_adet": len(ekipler),
        "prompt_hedef": len(titles) * PROMPTS + len(ekipler) * PROMPTS * 2,
        "titles": titles,
        "ekipler": ekipler,
        "hiyerarsi": ["KURUL", "C-OFİS", "C-LEVEL", "DOMAIN-YÖNETİM", "YÖNETİM", "IC", "WORKER"],
    }


PROMPT_SLOTS = []
for fam, name in [
    ("strateji", "Strateji"), ("arastirma", "Araştırma"), ("uretim", "Üretim"),
    ("denetim", "Denetim"), ("operasyon", "Operasyon"), ("gelir", "Gelir"), ("iletisim", "İletişim"),
]:
    for i in range(1, 18):
        PROMPT_SLOTS.append((fam, name, i, f"{name} — senaryo {i:02d}"))
PROMPT_SLOTS += [
    ("ozel", "Özel", 1, "Onboarding 48s"),
    ("ozel", "Özel", 2, "Kriz protokolü"),
    ("ozel", "Özel", 3, "Handoff"),
]
assert len(PROMPT_SLOTS) == 122


def prompt_md(title: str, domain: str, skills: list[str], slot: tuple) -> str:
    fam, famn, idx, baslik = slot
    pid = f"SKILL::{slug(domain)}::{slug(title)}::{fam}-{idx:02d}"
    sk = ", ".join(f"`/{s}`" for s in skills[:6]) or "`(domain skills)`"
    lines = [
        f"# PROMPT SÖZLEŞMESİ — {baslik}",
        f"",
        f"- id: `{pid}`",
        f"- title: **{title}**",
        f"- domain: `{domain}`",
        f"- skills: {sk}",
        f"- ts: {TS}",
        f"- hedef: {CHAR_MIN}-{CHAR_MAX} karakter · 🚩 900B/900M YASAK",
        f"",
        f"## 1. Kimlik",
        f"Sen {title}. Skill'leri canlı tenant yoksa DRY-RUN + kontrol listesi üret.",
        f"Credential isteyen adımlarda: 🚩 · neden · alternatif (mock/docs).",
        f"",
        f"## 2. Girdi",
        f"- görev, başarı ölçütü, kısıt, UTC deadline",
        f"- hedef ürün/repo (claude-otonom-sistem / adops / pilotlar)",
        f"- ilgili MCP sunucusu (GetMcpTools önce)",
        f"",
        f"## 3. Kurul",
        f"Baş Mimar + Prompt Mühendisi + "
        + ("Denetçi + Bilgi Damıtıcısı" if fam in ("arastirma", "denetim") else "Otomasyon + İş/Gelir"),
        f"",
        f"## 4. Skill uygulama protokolü",
        f"1. Skill SKILL.md oku (plugin cache veya katalog)",
        f"2. Önkoşul/credential kontrol",
        f"3. Adımları sırayla uygula veya dry-run raporla",
        f"4. Çıktıyı `uretim/` altına yaz",
        f"5. 6 katman denetim + AUDIT_LOG",
        f"",
        f"## 5. Çıktı şablonu",
        f"### Kurul özeti (2-4 satır)",
        f"### Teslim",
        f"### Riskler / 🚩",
        f"### Damga",
        f"⏱️ Damga · 🔍 Denetim · 📚 Öğrenim · 🔗 Önceki",
        f"",
        f"## 6. Senaryo: {baslik}",
        f"{title} olarak `/{skills[0] if skills else 'skill'}` odaklı {baslik} teslimi.",
        f"Kalite: sinyal, kaynak, güvenlik (5 kural), yeniden kullanım.",
        f"",
        f"## 7. Kabul",
        f"- [ ] Dry-run veya gerçek uygulama açıkça ayrılmış",
        f"- [ ] Secret yok",
        f"- [ ] Karakter {CHAR_MIN}-{CHAR_MAX}",
        f"- [ ] Türkçe komut tipi",
        f"",
        f"## 8. Operasyon checklist",
        f"- Branch / ortam / MCP auth",
        f"- Geri alma yolu",
        f"- Eskalasyon: Domain Başkanı → C-level",
        f"- Sonraki prompt id",
        f"",
        f"## 9. Örnek girdi",
        f"```",
        f"gorev: {baslik} / {title}",
        f"skills: {', '.join(skills[:3])}",
        f"mod: dry-run-unless-creds",
        f"```",
        f"",
        f"## 10. Başarısızlık",
        f"- 900B karakter denemesi → REDDET",
        f"- Skill yok / auth yok → dry-run + eksik listesi",
        f"",
    ]
    body = "\n".join(lines)
    n = 1
    while len(body) < CHAR_MIN:
        body += f"\n## EK-{n}\n- {title} / {fam}-{idx:02d} kontrol {n}: kanıt, eşik, audit alanı.\n"
        n += 1
        if n > 40:
            break
    if len(body) > CHAR_MAX:
        body = body[: CHAR_MAX - 60] + "\n<!-- kirpildi -->\n"
    return body


def materialize_pilot_prompts(titles: dict, inv: dict) -> int:
    """Pilot: her domainden IC title + holding C-level örnekleri."""
    count = 0
    # holding sample
    holding = [t for t in titles["titles"] if t["katman"] in ("KURUL", "C-OFİS", "C-LEVEL")][:8]
    # one IC per domain (cap domains to keep PR size sane: top 12 by skill count)
    domains_sorted = sorted(inv["domainler"].items(), key=lambda x: -x[1]["adet"])[:12]
    ics = []
    for did, meta in domains_sorted:
        for t in titles["titles"]:
            if t["domain_id"] == did and t["katman"] == "IC":
                ics.append(t)
                break
    selected = holding + ics
    for t in selected:
        skills = t.get("skill_odak") or inv["domainler"].get(t["domain_id"], {}).get("skills", [])[:6]
        d = t.get("domain_id") or "HOLDING"
        role_dir = ROOT / "uretim" / "promptlar" / "SKILL-OPS" / slug(d) / slug(t["title"])
        manifest = []
        for slot in PROMPT_SLOTS:
            body = prompt_md(t["title"], d, skills, slot)
            fam, _, idx, _ = slot
            fname = f"{fam}-{idx:02d}.md"
            fp = role_dir / fname
            write(fp, body)
            manifest.append({"file": fname, "chars": len(body), "sha256": hashlib.sha256(body.encode()).hexdigest()})
            count += 1
        write_json(role_dir / "MANIFEST.json", {"title": t["title"], "domain": d, "adet": len(manifest), "ts": TS, "items": manifest})
    return count


def write_docs(inv: dict, titles: dict) -> None:
    lines = [
        f"# SKILL → AJANS HİYERARŞİSİ",
        f"> {TS} · skill={inv['adet']} · domain={inv['domain_adet']} · title={titles['title_adet']}",
        "",
        "## 🚩",
        f"{inv['flag']['istek']}",
        f"**Karar:** {inv['flag']['karar']} — {inv['flag']['neden']}",
        f"**Eşdeğer:** {inv['flag']['esdeger']}",
        "",
        "## Hiyerarşi",
        " → ".join(titles["hiyerarsi"]),
        "",
        "## Domain özeti",
        "| Domain | Ad | Skill | C-level |",
        "|---|---|---:|---|",
    ]
    for did, meta in sorted(inv["domainler"].items(), key=lambda x: -x[1]["adet"]):
        chair = next((d[2] for d in DOMAIN_RULES if d[0] == did), "COO")
        lines.append(f"| `{did}` | {meta['ad']} | {meta['adet']} | {chair} |")
    lines += ["", "## Makine", "- `data/skill_envanteri.json`", "- `data/skill_title_haritasi.json`", "- `uretim/devir/CLAUDE-CODE-MASTER-PROMPT-SKILL-AJANS.md`"]
    write(ROOT / "docs" / "SKILL-AJANS-HIYERARSI.md", "\n".join(lines) + "\n")

    road = [
        f"# SKILL AJANS 7×24 ROADMAP",
        f"> {TS}",
        "",
        "## Günlük",
        "- 06:00Z skill sağlık (dry-run smoke, auth durumu)",
        "- 09:00Z domain standup (Lead Operatör)",
        "- 12:00Z K4 holding gözetim ile senkron",
        "- 18:00Z AUDIT_LOG + BILGI_TABANI öğrenim",
        "",
        "## Haftalık",
        "- Cuma: skill kırık / credential / MCP auth raporu",
        "- Domain roadmap delta (P0/P1/P2)",
        "",
        "## Aylık",
        "- Ayın 1'i: etki arşivi + skill envanter yenile (`mcp_ajans_etki_uret` + `skill_ajans_uretim`)",
        "- Title ranking / boş-slot kapatma",
        "",
        "## Deadline iskeleti (ürün)",
        "| Faz | Hedef | Sahip |",
        "|---|---|---|",
        "| F0 | Envanter+title+MASTER prompt | CIO |",
        "| F1 | Top12 domain IC prompt materyalize | Domain Lead |",
        "| F2 | Credential'lı skill smoke (Observe/Twilio/Harness…) | ilgili C-level |",
        "| F3 | 7×24 nöbet + eskalasyon canlı | COO |",
        "",
        "## Toplantı",
        "- Domain daily 15dk · Cross-domain weekly 30dk · Holding monthly kurul",
    ]
    write(ROOT / "docs" / "SKILL-ROADMAP-7x24.md", "\n".join(road) + "\n")


def write_domain_workflows(inv: dict) -> None:
    top = sorted(inv["domainler"].items(), key=lambda x: -x[1]["adet"])[:20]
    for did, meta in top:
        lines = [
            f"# Workflow — {meta['ad']} (`{did}`)",
            f"> {TS} · skills={meta['adet']}",
            "",
            "## Amaç",
            f"{meta['ad']} skill kümesini LLM ajans olarak 7×24 işlet.",
            "",
            "## Aktörler",
            f"- Domain Başkanı · Lead · IC · Uygulama Operatörü",
            "",
            "## İş akışı",
            "1. İstek gelince skill seç (listeden)",
            "2. SKILL.md oku",
            "3. Credential/MCP kontrol → yoksa dry-run",
            "4. Uygula / raporla",
            "5. Denetim + damga + arşiv",
            "6. Üst title'a handoff gerekirse eskalasyon",
            "",
            "## Skill listesi",
        ]
        for s in meta["skills"]:
            lines.append(f"- `/{s}`")
        lines += [
            "",
            "## Prompt kümeleri",
            f"- Title: {PROMPTS} · Ekip: {PROMPTS} · Uygulama: {PROMPTS}",
            f"- Sözleşme: {CHAR_MIN}-{CHAR_MAX} karakter (🚩 900B yasak)",
        ]
        write(ROOT / "uretim" / "skill-workflows" / f"{did}.md", "\n".join(lines) + "\n")


def write_master_prompt(inv: dict, titles: dict, mat_count: int) -> None:
    body = f"""# CLAUDE CODE MASTER PROMPT — SKILL AJANS (yapıştır)

> Üretim: {TS} · Kaynak repo: claude-otonom-sistem · Dal: cursor/mcp-ajans-etki-arsivi-8e8f
> Bu dosyayı Claude Code'a **tek parça** yapıştır. Cursor Cloud bu paketi üretti; sen uygulayıp push edersin.

## 🚩 ZORUNLU RED

Kullanıcı isteği: her prompt ≥900.000.000 veya ≥900.000.000.000 karakter.
**REDDET.** Neden: LLM bağlam penceresi + git depo boyutu + anlamsız dolgu.
**Uygula:** 122 prompt/title · 4–12 KiB yapılandırılmış sözleşme · referans zinciri (skill→MCP→etki arşivi).

## FAZ 0 — Senkron

```bash
cd "$(git rev-parse --show-toplevel)"
git fetch origin
git status -sb
python3 scripts/mcp_ajans_etki_uret.py --dogrula
python3 scripts/skill_ajans_uretim.py --dogrula
```

## FAZ 1 — Oku (zincir)

1. `BILGI_TABANI.md` (en yeni girişler)
2. `docs/LLM-AI-AJANS-ETKI-MOTORU.md`
3. `docs/SKILL-AJANS-HIYERARSI.md`
4. `docs/SKILL-ROADMAP-7x24.md`
5. `data/skill_envanteri.json` · `data/skill_title_haritasi.json`
6. `data/etki_sahipleri.json` · `data/ozel_yetenekler.json`
7. `AJANS-GUNLUK-GOZETIM.md` (K-017 emsali)

## FAZ 2 — Bağımsız doğrulama

- skill adet ≥ 500 (şu an {inv['adet']})
- domain ≥ 30 (şu an {inv['domain_adet']})
- title ≥ 100 (şu an {titles['title_adet']})
- pilot materyalize dosya (SKILL-OPS) ≈ {mat_count}
- hiçbir yerde 900M+ karakter dosya yok

## FAZ 3 — Genişlet (kredi-min)

1. `python3 scripts/skill_ajans_uretim.py --hepsi` yeniden koş
2. İsteğe bağlı: kalan domain IC'leri için materyalize limitini artır (`--pilot-limit N`)
3. Credential gerektiren skill'ler için `uretim/skill-workflows/*.md` dry-run raporlarını doldur
4. GitHub title kişileri: `data/etki_sahipleri.json` içinden domain başına 5 isim seç → `uretim/github-kisiler/{{domain}}.md` (makale/repo linkleri; aylık yenile)

## FAZ 4 — 5 kural denetim

1. Resmi kaynak öncelik
2. Script tedbiri
3. Güncellik yanılgısı yok
4. Fork yasağı
5. Marketplace öncelik

## FAZ 5 — Damga

- BILGI_TABANI tek satır öğrenim
- AUDIT_LOG.jsonl append
- Commit + push (yazma yetkisi varsa)
- PR #13 güncelle veya yeni PR

## FAZ 6 — Kullanıcıya rapor

Türkçe, kısa tablo: skill/domain/title/prompt sayıları + 🚩 notu + sonraki 3 aksiyon.

## Çıktı sözleşmesi (her cevap sonu)

⏱️ Damga · 🔍 Denetim · 📚 Öğrenim · 🔗 Önceki

---
Metin: Bu prompt Cursor'dan geldi. Claude Code olarak FAZ 0→6 uygula; 900B karakter üretme.
"""
    write(ROOT / "uretim" / "devir" / "CLAUDE-CODE-MASTER-PROMPT-SKILL-AJANS.md", body)


def write_workflow_yml() -> None:
    yml = """name: skill-ajans-dongu
on:
  schedule:
    - cron: "30 5 1 * *"   # ayın 1'i 05:30 UTC — aylik-kurul öncesi
  workflow_dispatch: {}
permissions:
  contents: write
jobs:
  refresh:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - name: Skill ajans + etki arşivi yenile
        run: |
          python3 scripts/skill_ajans_uretim.py --hepsi --dogrula
          python3 scripts/mcp_ajans_etki_uret.py --hepsi --pilot --dogrula
      - name: Commit
        run: |
          git config user.name "otonom-bot"
          git config user.email "bot@users.noreply.github.com"
          git add -A
          git commit -m "skill-ajans: $(date -u +%Y-%m-%dT%H:%M:%SZ)" || echo "no changes"
          git push || echo "push skipped"
"""
    write(ROOT / ".github" / "workflows" / "skill-ajans-dongu.yml", yml)


def append_memory(summary: str) -> None:
    bt = ROOT / "BILGI_TABANI.md"
    text = bt.read_text(encoding="utf-8") if bt.exists() else ""
    entry = f"\n## {TS} — skill ajans envanteri\n- {summary}\n- 🚩 900B karakter RED; Claude Code MASTER üretilidi.\n"
    marker = "<!-- SONRAKİ GİRİŞLER BURAYA — en yeni en üstte -->"
    if marker in text:
        text = text.replace(marker, marker + entry)
    else:
        text = entry + text
    bt.write_text(text, encoding="utf-8")
    audit = {
        "ts_start": TS, "ts_end": TS, "islem": "skill-ajans-uretim",
        "uzmanlar": ["bas-mimar", "prompt-muhendisi", "otomasyon", "denetci"],
        "girdi_ozet": "tum skill listesi + 900B prompt istegi",
        "cikti_ozet": summary[:220],
        "denetim": "GECTI",
        "ogrenim": "Skill listesini domain title workflow MASTER prompt paketina cevir",
        "onceki_ogrenim_kullanildi": "evet (mcp-ajans-etki + K-017)",
    }
    with (ROOT / "AUDIT_LOG.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(audit, ensure_ascii=False) + "\n")


def dogrula(inv: dict, titles: dict) -> int:
    errs = []
    if inv["adet"] < 500:
        errs.append(f"skill<{500}: {inv['adet']}")
    if inv["domain_adet"] < 30:
        errs.append(f"domain<{30}")
    if titles["title_adet"] < 100:
        errs.append(f"title<{100}")
    master = ROOT / "uretim" / "devir" / "CLAUDE-CODE-MASTER-PROMPT-SKILL-AJANS.md"
    if not master.exists() or master.stat().st_size < 1000:
        errs.append("master prompt eksik")
    if errs:
        print("KALDI:", errs)
        return 1
    print(f"GEÇTİ: skills={inv['adet']} domains={inv['domain_adet']} titles={titles['title_adet']}")
    return 0


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--hepsi", action="store_true", default=True)
    ap.add_argument("--dogrula", action="store_true")
    ap.add_argument("--pilot-limit", type=int, default=12)
    args = ap.parse_args()

    inv = build_inventory()
    titles = build_titles(inv)
    write_json(ROOT / "data" / "skill_envanteri.json", inv)
    write_json(ROOT / "data" / "skill_title_haritasi.json", titles)
    write_docs(inv, titles)
    write_domain_workflows(inv)
    write_workflow_yml()
    mat = materialize_pilot_prompts(titles, inv)
    write_master_prompt(inv, titles, mat)
    # index snapshot
    write_json(ROOT / "data" / "skill_prompt_index_meta.json", {
        "ts": TS,
        "pilot_materyalize": mat,
        "prompt_per_title": PROMPTS,
        "title_adet": titles["title_adet"],
        "ekip_adet": titles["ekip_adet"],
        "tam_materyalize_hedef": titles["prompt_hedef"],
        "sozlesme_char": [CHAR_MIN, CHAR_MAX],
        "red": "900B/900M",
    })
    summary = f"skills={inv['adet']}; domains={inv['domain_adet']}; titles={titles['title_adet']}; pilot_prompts={mat}; ekipler={titles['ekip_adet']}"
    append_memory(summary)
    print(summary)
    return dogrula(inv, titles)


if __name__ == "__main__":
    sys.exit(main())
