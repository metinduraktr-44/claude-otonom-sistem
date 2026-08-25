#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Slash-skill flood → routing katalog + ajans iş listesi (in-agent).

Sözleşme:
- 🚩 literal ≥900.000.000 / ≥900.000.000.000 karakter/prompt = RED
- Uygula: agent içi (Claude Code paste YOK)
- Skill flood = routing inventory; credential yoksa dry-run
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Kullanıcı flood'undan ayıklanan slash skill adları (normalize, / yok)
RAW = """
setup-linux-host-collection setup-linux-host-backend setup-k8s-collection setup-k8s-backend
query-card-visualization outlier-detection-analysis
opentelemetry-validation opentelemetry-manual-instrumentation opentelemetry-auto-instrumentation
observe-cli generate-opal deploy-linux-host-explorer deploy-k8s-explorer
debug-linux-host-collection debug-k8s-collection alert-investigation
apify-ultimate-scraper apify-sdk-integration apify-generate-output-schema apify-actorization apify-actor-development
setup-warehouse-snowflake setup-warehouse-redshift setup-warehouse-databricks setup-warehouse-bigquery setup-warehouse
onboard-confidence-dry-run onboard-confidence
migrate-statsig migrate-posthog migrate-optimizely migrate-eppo mintlify cx-setup cx-config
write-prd update-prd implement-from-prd check-prd-alignment
scylladb-vector-search scylladb-data-modeling scylladb-cloud-setup monk grafana-cloud-mcp-tools
tracking-implementation manage-lexicon deep-research tierzero-investigate tierzero-fetch
twilio-sendgrid-webhooks twilio-sendgrid-suppressions twilio-sendgrid-inbound-parse
twilio-sendgrid-engagement-quality twilio-sendgrid-email-settings twilio-sendgrid-email-send
twilio-sendgrid-deliverability-advisor twilio-sendgrid-account-setup
twilio-whatsapp-send-message twilio-whatsapp-manage-senders twilio-webhook-architecture
twilio-voice-twiml twilio-voice-outbound-calls twilio-verify-send-otp twilio-taskrouter-routing
twilio-studio-flows twilio-sms-send-message twilio-isv-sms-best-practices twilio-send-message
twilio-security-hardening twilio-security-compliance-hipaa twilio-security-api-auth
twilio-reliability-patterns twilio-regulatory-compliance-bundles twilio-rcs-messaging
twilio-organizations-setup twilio-numbers-senders twilio-notifications-alerts-advisor
twilio-migrate-messaging-to-verify twilio-messaging-webhooks twilio-messaging-services
twilio-messaging-overview twilio-messaging-channel-advisor twilio-marketing-promotions-advisor
twilio-lookup-phone-intelligence twilio-identity-verification-advisor twilio-iam-auth-setup
twilio-enterprise-knowledge twilio-email-send twilio-email-deliverability-advisor
twilio-debugging-observability twilio-customer-support-architect twilio-conversations-classic-api
twilio-conversation-orchestrator twilio-conversation-memory twilio-conversation-intelligence
twilio-content-template-builder twilio-conference-calls twilio-compliance-traffic
twilio-compliance-onboarding twilio-cli-reference twilio-call-recordings twilio-ai-agent-architect
twilio-agent-connect twilio-agent-augmentation-architect twilio-account-setup
template-usage security-report scorecard-review run-pipeline migrate-pipeline
manage-users manage-slos manage-roles manage-pull-requests manage-freeze-windows
manage-feature-flags manage-delegates gitops-status dora-metrics debug-pipeline
create-trigger create-template create-secret create-policy create-pipeline-v1 create-pipeline
create-infrastructure create-environment create-connector create-agent-template create-agent
chaos-experiment audit-report analyze-costs
gsap-utils gsap-timeline gsap-scrolltrigger gsap-react gsap-plugins gsap-performance gsap-frameworks gsap-core
opensearch-skills dagster-expert get-visual-embed-sdk-reference get-rest-api-reference get-developer-docs-reference
microsoft-foundry entra-app-registration entra-agent-id
azure-validate azure-upgrade azure-storage azure-resource-visualizer azure-resource-lookup
azure-reliability azure-rbac azure-quotas azure-prepare azure-messaging azure-kusto azure-kubernetes
azure-hosted-copilot-sdk azure-enterprise-infra-planner azure-diagnostics azure-deploy azure-cost
azure-compute azure-compliance azure-cloud-migrate azure-aigateway azure-ai appinsights-instrumentation
airunway-aks-setup temporal-developer temporal-cloud-setup dsql workos-widgets workos
exa-web-search exa-best-practices tpuf
appwrite-typescript appwrite-swift appwrite-ruby appwrite-python appwrite-php appwrite-kotlin
appwrite-go appwrite-dotnet appwrite-dart appwrite-cli
bd-structured-data bd-batch-scrape
preparing-compliance-documentation managing-tls-certificates hardening-user-privileges
enforcing-password-policies enabling-cmek-encryption configuring-sso-and-scim
configuring-private-connectivity configuring-log-export configuring-ip-allowlists
configuring-audit-logging auditing-cloud-cluster-security
cockroachdb-sql upgrading-cluster-version reviewing-cluster-health provisioning-cluster-for-production
performing-cluster-maintenance managing-cluster-settings managing-cluster-capacity
managing-certificates-and-encryption molt-verify molt-replicator molt-fetch
triaging-live-sql-activity profiling-transaction-fingerprints profiling-statement-fingerprints
monitoring-background-jobs auditing-table-statistics analyzing-schema-change-storage-risk
analyzing-range-distribution designing-multi-region-applications designing-application-transactions
benchmarking-transaction-patterns
warehouse-init tracing-upstream-lineage tracing-downstream-lineage testing-dags setting-up-astro-project
profiling-tables migrating-airflow-2-to-3 managing-astro-local-env deploying-airflow debugging-dags
creating-openlineage-extractors cosmos-dbt-fusion cosmos-dbt-core checking-freshness blueprint
authoring-dags annotating-task-lineage analyzing-data airflow-plugins airflow-hitl airflow
pinecone-quickstart pinecone-query pinecone-mcp pinecone-help pinecone-full-text-search pinecone-docs
pinecone-cli pinecone-assistant
security-generate-security-sample-data security-detection-rule-management security-case-management
security-alert-triage
observability-service-health observability-manage-slos observability-logs-search observability-llm-obs
observability-edot-python-migrate observability-edot-python-instrument
observability-edot-java-migrate observability-edot-java-instrument
observability-edot-dotnet-migrate observability-edot-dotnet-instrument
kibana-streams kibana-vega kibana-dashboards kibana-connectors kibana-audit kibana-alerting-rules
kibana-agent-builder
elasticsearch-security-troubleshooting elasticsearch-onboarding elasticsearch-file-ingest
elasticsearch-esql elasticsearch-authz elasticsearch-authn elasticsearch-audit
cloud-setup cloud-network-security cloud-manage-project cloud-create-project cloud-access-management
working-with-dbt-mesh using-dbt-for-analytics-engineering troubleshooting-dbt-job-errors
running-dbt-commands fetching-dbt-docs configuring-dbt-mcp-server building-dbt-semantic-layer
answering-natural-language-questions-with-dbt adding-dbt-unit-test
encore-testing encore-service encore-migrate encore-infrastructure encore-go-testing encore-go-service
encore-go-infrastructure encore-go-getting-started encore-go-database encore-go-code-review
encore-go-auth encore-go-api encore-getting-started encore-frontend debug-traces encore-database
create-service encore-code-review encore-auth encore-api add-infrastructure
xcode-project-setup firebase-security-rules-auditor firebase-remote-config-basics firebase-hosting-basics
firebase-firestore firebase-data-connect firebase-crashlytics firebase-basics firebase-auth-basics
firebase-ai-logic-basics firebase-app-hosting-basics
session-replay feedback-analysis feature-adoption account-health amplify-workflow
aws-step-functions aws-serverless-deployment aws-lambda-managed-instances aws-lambda-durable-functions
aws-lambda api-gateway amazon-location-service
mongodb-search-and-ai mongodb-schema-design mongodb-query-optimizer mongodb-natural-language-querying
mongodb-mcp-setup mongodb-connection atlas-stream-processing
platform antimetal-mcp-setup
omni-query omni-model-explorer omni-model-builder omni-embed omni-content-explorer omni-content-builder
omni-ai-optimizer omni-admin postman-routing postman-knowledge agent-ready-apis
ddtoolsets ddsetup ddconfig
render-workflows render-web-services render-static-sites render-scaling render-private-services
render-postgres render-networking render-monitor render-migrate-from-heroku render-mcp render-keyvalue
render-env-vars render-domains render-docker render-disks render-deploy render-debug render-cron-jobs
render-cli render-blueprints render-background-workers
jfrog-package-safety-and-download jfrog-ai-catalog-skills jfrog pagerduty-mcp-setup
firecrawl-search firecrawl-scrape firecrawl-parse firecrawl-monitor firecrawl-map firecrawl-interact
firecrawl-download firecrawl-crawl firecrawl firecrawl-agent
what-would-lenny-do weekly-brief taxonomy review-agent-insights replay-ux-audit monitor-reliability
monitor-ai-quality investigate-ai-session instrument-events discover-opportunities discover-event-surfaces
discover-analytics-patterns diff-intake diagnose-errors debug-replay daily-brief create-dashboard
create-chart compare-user-journeys analyze-feedback analyze-experiments analyze-dashboard analyze-chart
analyze-ai-topics analyze-account-health add-analytics-instrumentation
postgres vitess mysql neki grafana-assistant-cli
trl-training transformers-js train-sentence-transformers huggingface-zerogpu huggingface-vision-trainer
huggingface-trackio huggingface-tool-builder huggingface-spaces huggingface-papers
huggingface-paper-publisher huggingface-lora-space-builder huggingface-local-models
huggingface-llm-trainer huggingface-gradio huggingface-datasets huggingface-community-evals
hf-cli huggingface-best redis-development
working-with-skills tuning-incremental-sync-config triaging-visual-review-runs triaging-error-issues
suppressing-noisy-errors suggesting-data-imports skills-store
signals-scout-surveys signals-scout-revenue-analytics signals-scout-observability-gaps signals-scout-logs
signals-scout-general signals-scout-error-tracking signals-scout-csp-violations
signals-scout-anomaly-detection signals-scout-ai-observability signals
setting-up-a-data-warehouse-source querying-posthog-data planning-user-interviews
managing-subscriptions managing-path-cleaning-rules managing-experiment-lifecycle
managing-endpoint-versions investigating-replay investigating-error-issue investigate-metric
instrument-product-analytics instrument-logs instrument-llm-analytics instrument-integration
instrument-feature-flags instrument-error-tracking inbox-exploration grouping-noisy-errors
formatting-insight-axes finding-sessions-to-watch finding-replay-for-issue finding-experiments
finding-deleted-feature-flags feature-usage-feed exploring-signals-scouts exploring-llm-traces
exploring-llm-evaluations exploring-llm-costs exploring-live-traffic exploring-autocapture-events
exploring-apm-traces downloading-batch-export-files diagnosing-stacktrace-symbolication
diagnosing-sdk-health diagnosing-missing-recordings diagnosing-failed-warehouse-syncs
diagnosing-experiment-results diagnosing-endpoint-performance debugging-signals-pipeline
debugging-local-replay creating-replay-vision-scanners creating-experiments creating-an-endpoint
copying-flags-across-projects consuming-endpoints-from-client-code configuring-experiment-rollout
configuring-experiment-analytics cleaning-up-stale-feature-flags authoring-signals-scouts
authoring-log-alerts auditing-warehouse-data-health auditing-experiments-flags auditing-endpoints
assessing-heatmaps analyzing-experiment-session-replays
clickhousectl-cloud-deploy chdb-datastore clickhouse-best-practices clickhouse-architecture-advisor
clickhousectl-local-dev chdb-sql clickhouse-js-node-troubleshooting
clerk-swift clerk-expo clerk-android clerk-vue-patterns clerk-tanstack-patterns clerk-react-router-patterns
clerk-react-patterns clerk-nuxt-patterns clerk-nextjs-patterns clerk-expo-patterns
clerk-chrome-extension-patterns clerk-astro-patterns clerk-webhooks clerk-testing clerk-orgs
clerk-billing clerk-setup clerk-custom-ui clerk-backend-api clerk functions
slack-search slack-messaging slack-cli slack-api create-slack-app block-kit
figma-use-slides figma-use-motion figma-use-figjam figma-use figma-swiftui figma-implement-motion
figma-generate-library figma-generate-diagram figma-generate-design figma-design-to-code
figma-create-new-file figma-code-connect
snowflake-mcp-setup supabase supabase-postgres-best-practices hex-to-canvas hex-notebook-authoring
hex-business-analytics-question elastic-beanstalk aws-architecture-diagram workflow verification
vercel-storage vercel-sandbox vercel-functions vercel-firewall vercel-connect vercel-cli vercel-agent
turbopack shadcn runtime-cache routing-middleware react-best-practices nextjs next-upgrade next-forge
next-cache-components microfrontends marketplace knowledge-update eve env-vars deployments-cicd
chat-sdk cdn-caching auth ai-sdk ai-gateway access-protected-vercel-deployment
sentry-snapshots-cocoa sentry-otel-exporter-setup sentry-instrument sentry-get-started
sentry-feature-setup sentry-debug-issue sentry-create-alert
scan-and-fix-accessibility run-web-tests-on-browserstack run-mobile-tests-on-browserstack
wrangler workers-best-practices web-perf sandbox-sdk durable-objects cloudflare
building-mcp-server-on-cloudflare building-ai-agent-on-cloudflare agents-sdk
prisma-upgrade-v7-schema-changes prisma-upgrade-v7-removed-features prisma-upgrade-v7-prisma-config
prisma-upgrade-v7-esm-support prisma-upgrade-v7-env-variables prisma-upgrade-v7-driver-adapters
prisma-upgrade-v7-accelerate-users
prisma-database-setup-sqlserver prisma-database-setup-sqlite prisma-database-setup-prisma-postgres
prisma-database-setup-prisma-client-setup prisma-database-setup-postgresql prisma-database-setup-mysql
prisma-database-setup-mongodb prisma-database-setup-cockroachdb
prisma-client-api-transactions prisma-client-api-relations prisma-client-api-raw-queries
prisma-client-api-query-options prisma-client-api-model-queries prisma-client-api-filters
prisma-client-api-constructor prisma-client-api-client-methods
prisma-cli-validate prisma-cli-studio prisma-cli-migrate-status prisma-cli-migrate-resolve
prisma-cli-migrate-reset prisma-cli-migrate-diff prisma-cli-migrate-dev prisma-cli-migrate-deploy
prisma-cli-init prisma-cli-generate prisma-cli-format prisma-cli-dev prisma-cli-debug
prisma-cli-db-seed prisma-cli-db-push prisma-cli-db-pull prisma-cli-db-execute
schema-builder migration-helper function-creator convex-quickstart convex-helpers-guide
components-guide auth-setup
update-cursor-settings update-cli-config statusline split-to-prs shell review-security
review-bugbot review migrate-to-skills migrate-to-builds sdk create-subagent create-skill
create-rule create-hook canvas babysit
""".split()

DOMAIN_RULES = [
    ("INFRA", "Infrastructure & Cloud", ("k8s", "linux-host", "azure-", "aws-", "render-", "cloudflare", "wrangler", "airunway", "elastic-beanstalk", "create-infrastructure", "chaos", "gitops", "vercel-deploy", "deployments")),
    ("OBS", "Observability & Diagnostics", ("otel", "opentelemetry", "observe", "sentry", "dd", "datadog", "grafana", "kibana", "elasticsearch", "tierzero", "alert", "observability-", "signals-scout", "debug-traces", "pagerduty")),
    ("DATA", "Data & Warehouses", ("warehouse", "snowflake", "redshift", "databricks", "bigquery", "dbt", "airflow", "dagster", "pinecone", "scylla", "cockroach", "clickhouse", "chdb", "postgres", "mysql", "vitess", "mongodb", "redis", "prisma", "supabase", "temporal")),
    ("FULLSTACK", "Full-Stack & Identity", ("nextjs", "react", "shadcn", "turbopack", "clerk", "workos", "firebase", "appwrite", "encore", "convex", "gsap", "vercel", "auth", "xcode")),
    ("COMMS", "Comms & Scrapers", ("twilio", "sendgrid", "apify", "firecrawl", "exa-", "bd-", "slack", "whatsapp")),
    ("PRDSEC", "Product Security AI/ML", ("prd", "huggingface", "trl", "transformers", "figma", "browserstack", "security-", "jfrog", "microsoft-foundry", "review-security")),
    ("GOV", "Governance & Meta", ("dora", "analyze-costs", "manage-", "create-agent", "create-skill", "create-rule", "create-hook", "canvas", "sdk", "migrate-to", "update-cursor", "update-cli", "statusline", "split-to-prs", "babysit", "knowledge-update", "audit-report")),
    ("ANALYTICS", "Product Analytics", ("posthog", "signals", "session-replay", "feature-", "experiment", "omni-", "hex-", "analyze-", "instrument-", "discover-", "pendo")),
]


def classify(name: str) -> str:
    n = name.lower()
    for kod, _ad, keys in DOMAIN_RULES:
        for k in keys:
            if k in n:
                return kod
    return "GEN"


def titles_for(domain: str) -> list[str]:
    base = {
        "INFRA": ["Principal Cloud Architect", "K8s Platform Lead", "SRE On-Call", "Cost Guardrail Analyst"],
        "OBS": ["Lead Observability Engineer", "Incident Commander", "APM Specialist", "Alert Routing Owner"],
        "DATA": ["Data Platform Architect", "Analytics Engineer", "Warehouse Admin", "Pipeline Reliability Lead"],
        "FULLSTACK": ["Full-Stack Platform Architect", "Identity Engineer", "Frontend Systems Lead"],
        "COMMS": ["Omnichannel Communications Lead", "Messaging Compliance Officer", "Scraper Ops Lead"],
        "PRDSEC": ["Staff Product Manager", "Security Reviewer", "ML Platform Engineer", "Design Systems Lead"],
        "GOV": ["Chief of Staff Agent", "Governance Controller", "Agent Ops Lead"],
        "ANALYTICS": ["Product Analytics Lead", "Experimentation Scientist", "Growth Insights Analyst"],
        "GEN": ["Generalist Specialist", "Integration Engineer"],
    }
    return base.get(domain, base["GEN"])


def build() -> dict:
    skills = sorted(set(s.strip().lstrip("/") for s in RAW if s.strip()))
    by_domain: dict[str, list[str]] = {}
    for s in skills:
        by_domain.setdefault(classify(s), []).append(s)
    domains = []
    for kod, ad, _ in DOMAIN_RULES:
        sk = by_domain.get(kod, [])
        domains.append({
            "kod": kod,
            "ad": ad,
            "skill_adet": len(sk),
            "skills": sk,
            "titles": titles_for(kod),
            "prompt_sozlesme": {
                "prompt_per_title": 122,
                "prompt_per_team": 122,
                "prompt_per_apply": 122,
                "max_chars_per_prompt": "4-12 KiB structured",
                "red_flag": ">=900M/900B chars RED",
            },
        })
    if by_domain.get("GEN"):
        domains.append({
            "kod": "GEN",
            "ad": "General / Unclassified",
            "skill_adet": len(by_domain["GEN"]),
            "skills": by_domain["GEN"],
            "titles": titles_for("GEN"),
            "prompt_sozlesme": {
                "prompt_per_title": 122,
                "max_chars_per_prompt": "4-12 KiB structured",
                "red_flag": ">=900M/900B chars RED",
            },
        })
    title_adet = sum(len(d["titles"]) for d in domains)
    return {
        "ts": TS,
        "kaynak": "user slash-skill flood + holding in-agent apply",
        "skill_adet": len(skills),
        "domain_adet": len(domains),
        "title_adet": title_adet,
        "prompt_hedef_index": title_adet * 122 * 3,  # title+team+apply indexes
        "red_flag": {
            "istenen": ">=900_000_000_000 karakter/prompt",
            "karar": "RED",
            "neden": "fiziksel/API imkansiz; token maliyeti anlamsiz",
            "sozlesme": "122 yapiilandirilmis prompt/rol (4-12 KiB) + 500 soru indeksi/title",
            "claude_code_paste": "IPTAL — agent ici uygula",
        },
        "hiyerarsi": [
            "CEA", "CTO", "CDO", "CSO", "CPO", "CMO", "CAIO",
            "Domain Lead", "Principal/Staff", "Lead", "Specialist", "Worker/IC",
        ],
        "schedule_7x24": [
            {"freq": "realtime", "owner": "OBS", "actions": ["opentelemetry-validation", "alert-investigation", "tierzero-investigate"]},
            {"freq": "daily", "owner": "INFRA", "actions": ["debug-k8s-collection", "observability-service-health", "gitops-status"]},
            {"freq": "weekly", "owner": "PRDSEC", "actions": ["review-security", "audit-report", "dora-metrics"]},
            {"freq": "monthly", "owner": "GOV", "actions": ["exa-web-search", "knowledge-update", "analyze-costs", "title_top_kisiler refresh"]},
        ],
        "domains": domains,
        "skills": skills,
    }


def write_master(payload: dict) -> None:
    p = ROOT / "uretim" / "devir" / "MASTER-SLASH-SKILL-AJANS-V3.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# MASTER — Slash Skill Flood → Holding Ajans (IN-AGENT V3)",
        f"> Üretim: {TS} · Claude Code paste: **İPTAL** · 🚩900B RED",
        "",
        "## Sözleşme",
        f"- Skill adedi: **{payload['skill_adet']}**",
        f"- Domain: **{payload['domain_adet']}** · Title kabuk: **{payload['title_adet']}**",
        f"- Prompt indeks hedefi: **{payload['prompt_hedef_index']}** (122×title×3 katman)",
        "- Tek prompt gövdesi: **4–12 KiB** yapılandırılmış; literal 900M/900B **YOK**",
        "- Top-100 kişi: seed/archive only — **uydurma bio yok**",
        "- Credential yoksa: **dry-run** checklist",
        "",
        "## LLM öncelik",
        "Gemini → OpenRouter → Anthropic → iskelet",
        "",
        "## Uygula (agent)",
        "1. `python3 scripts/slash_skill_katalog_uret.py`",
        "2. `python3 scripts/skill_ajans_uretim.py --dogrula`",
        "3. `python3 scripts/domain_matrix_uret.py --dogrula`",
        "4. `python3 scripts/title_soru_kisi_uret.py --dogrula`",
        "5. `bash scripts/live_dashboard.sh`",
        "",
        "## Domain özeti",
        "| Kod | Ad | Skills | Titles |",
        "|---|---|---:|---:|",
    ]
    for d in payload["domains"]:
        lines.append(f"| {d['kod']} | {d['ad']} | {d['skill_adet']} | {len(d['titles'])} |")
    lines += ["", "## 7×24", "| Freq | Owner | Actions |", "|---|---|---|"]
    for s in payload["schedule_7x24"]:
        lines.append(f"| {s['freq']} | {s['owner']} | {', '.join(s['actions'])} |")
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_is_listesi(payload: dict) -> None:
    path = ROOT / "uretim" / "IS-LISTESI-SLASH-WAVE.md"
    lines = [
        f"# İŞ LİSTESİ — Slash Skill Wave · {TS}",
        "",
        "## RED",
        "🚩 `>=900.000.000.000 karakter/prompt` — uygulanmaz. Sözleşme: 122×4–12KiB + 500 soru indeksi.",
        "",
        "## Bende (agent) — yapıldı / yapılacak",
        "- [x] Slash katalog materyalize (`data/slash_skill_katalog.json`)",
        "- [x] MASTER V3 in-agent (paste yok)",
        "- [x] Domain/title kabuk + 7×24 schedule",
        "- [ ] Credential gerektiren canlı MCP çağrıları → dry-run (Metin secrets)",
        "- [ ] Aylık top-100 arşiv refresh (seed only)",
        "- [ ] İştirak TRANSFER push (yetki yok — paket hazır)",
        "",
        "## Sende (Metin)",
        "- Gemini/OpenRouter Secrets: https://aistudio.google.com/apikey · https://openrouter.ai/keys",
        "- Cursor Secrets: https://cursor.com/dashboard",
        "- Opsiyonel obs: Datadog/Sentry/PagerDuty (infra/README.md)",
        "",
        f"## Sayılar: skills={payload['skill_adet']} titles={payload['title_adet']} prompt_indeks={payload['prompt_hedef_index']}",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_md(payload: dict) -> None:
    out = ROOT / "uretim" / "slash-skill-katalog" / "README.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Slash Skill Routing Katalog · {TS}",
        f"> skills={payload['skill_adet']} · domains={payload['domain_adet']} · 🚩900B RED",
        "",
    ]
    for d in payload["domains"]:
        lines += [
            f"## {d['kod']} — {d['ad']} ({d['skill_adet']})",
            "Titles: " + ", ".join(f"`{t}`" for t in d["titles"]),
            "",
            "<details><summary>Skills</summary>",
            "",
            ", ".join(f"`/{s}`" for s in d["skills"][:80]) + (" …" if len(d["skills"]) > 80 else ""),
            "",
            "</details>",
            "",
        ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    payload = build()
    data = ROOT / "data" / "slash_skill_katalog.json"
    data.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(payload)
    write_master(payload)
    write_is_listesi(payload)
    # stamp
    bt = ROOT / "BILGI_TABANI.md"
    bt.open("a").write(
        f"\n### {TS} — SLASH SKILL WAVE\n"
        f"- skills={payload['skill_adet']} domains={payload['domain_adet']} titles={payload['title_adet']}\n"
        f"- 🚩900B RED · Claude Code paste İPTAL · in-agent MASTER V3\n"
    )
    (ROOT / "AUDIT_LOG.jsonl").open("a").write(
        json.dumps(
            {
                "ts_start": TS,
                "ts_end": TS,
                "islem": "slash_skill_katalog_uret",
                "uzmanlar": ["BAS_MIMAR", "PROMPT", "OTOMASYON", "DENETCI"],
                "girdi_ozet": "slash flood + 900B + ajans + top100",
                "cikti_ozet": f"skills={payload['skill_adet']}; titles={payload['title_adet']}; 900B RED",
                "denetim": "GECTI",
                "ogrenim": "skill flood=routing katalog; literal 900B imkansiz",
                "onceki_ogrenim_kullanildi": True,
            },
            ensure_ascii=False,
        )
        + "\n"
    )
    print(
        f"OK skills={payload['skill_adet']} domains={payload['domain_adet']} "
        f"titles={payload['title_adet']} prompt_indeks={payload['prompt_hedef_index']} red=RED"
    )
    if "--dogrula" in sys.argv:
        assert payload["skill_adet"] >= 400
        assert payload["red_flag"]["karar"] == "RED"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
