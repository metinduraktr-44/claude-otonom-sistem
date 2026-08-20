#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Domain 1–7 MCP skill + directive matrix — yüklü dokümanlardan materyalize.

Sözleşme: skill adları indeks; 🚩900M karakter/prompt YOK.
Çıktı: data/domain_matrix.json + uretim/domain-matrix/*.md
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

DOMAINS = [
    {
        "id": 1,
        "kod": "INFRA",
        "ad": "Infrastructure, Kubernetes & Cloud",
        "c_suite": "CTO",
        "skills": [
            "setup-linux-host-collection", "setup-linux-host-backend", "setup-k8s-collection",
            "setup-k8s-backend", "deploy-linux-host-explorer", "deploy-k8s-explorer",
            "debug-linux-host-collection", "debug-k8s-collection", "azure-kubernetes",
            "airunway-aks-setup", "aws-step-functions", "aws-serverless-deployment",
            "aws-lambda", "render-workflows", "cloudflare", "wrangler",
            "create-infrastructure", "azure-deploy", "azure-compute",
        ],
        "directives": [
            "Dry-run önce: onboard-confidence-dry-run + azure-validate",
            "K8s pod crash → debug-k8s-collection",
            "Host bottleneck → debug-linux-host-collection",
            "Deploy öncesi maliyet: azure-cost + analyze-costs",
            "AKS: airunway-aks-setup + azure-kubernetes",
            "Lambda cold-start: aws-lambda-managed-instances",
            "Edge: workers-best-practices + wrangler",
            "Private net: configuring-private-connectivity",
            "RBAC: azure-rbac least privilege",
            "Step Functions state doğrula",
            "Render: render-blueprints + render-scaling",
            "TLS: managing-tls-certificates",
            "Haftalık chaos-experiment",
            "Tag uyumu: azure-resource-lookup",
            "Env izolasyonu: create-environment",
            "Connector: create-connector",
            "IP allowlist güncelle",
            "Container image audit: render-docker",
            "UTC timestamp → audit-report",
            "Pipeline blok: debug-pipeline",
        ],
        "artefaktlar": [
            "infra/otel/opentelemetry-collector.yaml",
            ".github/workflows/enterprise-k8s-otel-pipeline.yml",
        ],
    },
    {
        "id": 2,
        "kod": "OBS",
        "ad": "Telemetry, Observability & Diagnostics",
        "c_suite": "CTO/CAIO",
        "skills": [
            "opentelemetry-validation", "opentelemetry-manual-instrumentation",
            "opentelemetry-auto-instrumentation", "observe-cli", "generate-opal",
            "alert-investigation", "tierzero-investigate", "tierzero-fetch",
            "ddtoolsets", "ddsetup", "ddconfig", "grafana-cloud-mcp-tools",
            "sentry-instrument", "sentry-debug-issue", "kibana-dashboards",
            "elasticsearch-esql",
        ],
        "directives": [
            "Servis start → opentelemetry-auto-instrumentation",
            "Özel logic → opentelemetry-manual-instrumentation spans",
            "Kesinti → tierzero-investigate + alert-investigation",
            "Grafana sapma → grafana-assistant-cli",
            "Hata → sentry-debug-issue stacktrace",
            "Datadog agent: ddsetup + ddconfig",
            "Log query: elasticsearch-esql",
            "PII mask: configuring-log-export",
            "Kibana alert rules otomatik",
            "LLM token/latency: observability-llm-obs",
            "Frontend lock: finding-replay-for-issue",
            "7/24: observability-service-health",
            "Python/Java/.NET EDOT migrate",
            "Vega: kibana-vega",
            "Anomaly: signals-scout-anomaly-detection",
            "OpenSearch index optimize",
            "sentry-create-alert thresholds",
            "diagnose-errors ilk adım",
            "debug-traces microservice map",
            "Telemetry arşiv zaman damgalı",
        ],
        "artefaktlar": [
            "infra/terraform/observability/main.tf",
            "infra/otel/opentelemetry-collector.yaml",
        ],
        "alert_tiers": {
            "warning": ["error_rate>=2%", "p99>800ms", "first_seen_exception"],
            "critical": ["error_rate>=5%", "exception_spike>50/min"],
            "routing": {
                "warning": ["#alerts-warnings"],
                "critical": ["#alerts-critical", "PagerDuty Events API v2"],
            },
        },
    },
    {
        "id": 3,
        "kod": "DATA",
        "ad": "Data Engineering, Pipelines & Storage",
        "c_suite": "CDO",
        "skills": [
            "setup-warehouse-snowflake", "setup-warehouse-redshift",
            "setup-warehouse-databricks", "setup-warehouse-bigquery",
            "cockroachdb-sql", "scylladb-vector-search", "scylladb-data-modeling",
            "postgres", "vitess", "mysql", "mongodb-schema-design",
            "pinecone-query", "dagster-expert", "working-with-dbt-mesh",
            "temporal-developer",
        ],
        "directives": [
            "warehouse-init şema standardı",
            "dbt lineage: upstream + downstream",
            "DAG hata: debugging-dags + testing-dags",
            "Vector: scylladb-vector-search + pinecone-query",
            "MongoDB query optimizer",
            "Cockroach fingerprint kilit çöz",
            "Multi-region: designing-multi-region-applications",
            "dbt unit tests",
            "Temporal state persistence",
            "ClickHouse columnar",
            "Postgres best practices",
            "profiling-tables",
            "Airflow 2→3 migrate",
            "annotating-task-lineage",
            "cosmos-dbt-core",
            "CMEK encryption",
            "checking-freshness",
            "redis-development",
            "querying-posthog-data",
            "Pipeline çıktısı zaman damgalı delta",
        ],
        "artefaktlar": [],
    },
    {
        "id": 4,
        "kod": "FULLSTACK",
        "ad": "Full-Stack Platform, Identity & Frontend",
        "c_suite": "CPO/CTO",
        "skills": [
            "nextjs", "react-best-practices", "turbopack", "shadcn", "workos",
            "clerk", "entra-app-registration", "appwrite-typescript",
            "firebase-firestore", "prisma-cli-migrate-dev", "convex-quickstart",
            "encore-go-service", "gsap-timeline",
        ],
        "directives": [
            "Next.js App Router standartları",
            "SSO/SCIM: workos",
            "Clerk nextjs patterns",
            "Prisma migrate-diff önce",
            "Firebase security rules audit",
            "GSAP performance",
            "Appwrite typescript",
            "Microfrontends router",
            "Encore Go API",
            "Entra app registration dar yetki",
            "Convex helpers",
            "Hydration: react-best-practices",
            "runtime-cache + cdn-caching",
            "shadcn UI",
            "turbopack flags",
            "xcode-project-setup",
            "scan-and-fix-accessibility",
            "manage-feature-flags",
            "figma-code-connect",
            "next-upgrade bağımlılık",
        ],
        "artefaktlar": [],
    },
    {
        "id": 5,
        "kod": "COMMS",
        "ad": "Communications, Engagement & Scrapers",
        "c_suite": "CMO",
        "skills": [
            "twilio-sendgrid-email-send", "twilio-whatsapp-send-message",
            "twilio-voice-twiml", "twilio-verify-send-otp", "twilio-ai-agent-architect",
            "apify-ultimate-scraper", "firecrawl-crawl", "firecrawl-scrape",
            "exa-web-search", "bd-scrape",
        ],
        "directives": [
            "SMS: twilio-isv-sms-best-practices",
            "SendGrid deliverability advisor",
            "Apify ultimate-scraper + actorization",
            "Exa semantic search",
            "Firecrawl depth limit",
            "Voice TwiML",
            "WhatsApp senders manage",
            "OTP: verify-send-otp",
            "HIPAA: twilio-security-compliance-hipaa",
            "Apify output schema",
            "Content template builder",
            "Webhook signature architecture",
            "deep-research + bd-search",
            "Twilio AI agent memory",
            "BrightData browser session",
            "SendGrid suppressions sync",
            "TaskRouter routing",
            "Inbound parse",
            "RCS messaging",
            "Scraping JSONL zaman damgalı",
        ],
        "artefaktlar": [],
    },
    {
        "id": 6,
        "kod": "PRDSEC",
        "ad": "Product, Security & AI/ML",
        "c_suite": "CPO/CSO/CAIO",
        "skills": [
            "write-prd", "update-prd", "implement-from-prd", "check-prd-alignment",
            "review-security", "audit-report", "transformers-js", "trl-training",
            "huggingface-llm-trainer", "figma-design-to-code", "dora-metrics",
        ],
        "directives": [
            "PRD: ölçülebilir KPI",
            "Kod öncesi check-prd-alignment",
            "review-security + audit-report",
            "HF trainer + trl-training",
            "DORA haftalık",
            "figma-design-to-code",
            "Slack: create-slack-app + block-kit",
            "compare-user-journeys",
            "monitor-ai-quality",
            "experiment rollout",
            "microsoft-foundry responsible AI",
            "feedback-analysis",
            "BrowserStack web tests",
            "certificates encryption",
            "manage-pull-requests + bugbot",
            "hardening-user-privileges",
            "analyze-experiments",
            "jfrog package safety",
            "replay-ux-audit",
            "PRD sürüm zaman damgalı",
        ],
        "artefaktlar": [],
    },
    {
        "id": 7,
        "kod": "GOV",
        "ad": "Governance, Workflow & Self-Improvement",
        "c_suite": "CEA",
        "skills": [
            "dora-metrics", "analyze-costs", "review-agent-insights",
            "knowledge-update", "exa-web-search", "gitops-status",
            "manage-slos", "manage-freeze-windows",
        ],
        "directives": [
            "DORA velocity/stability",
            "analyze-costs bütçe sapması",
            "review-agent-insights",
            "knowledge-update",
            "Aylık exa-web-search benchmark",
            "gitops-status",
            "manage-slos",
            "manage-freeze-windows",
            "manage-feature-flags + delegates",
            "create-policy",
            "create-secret rotasyon",
            "create-agent-template",
            "create-subagent",
            "create-skill standart",
            "create-rule",
            "create-hook event",
            "canvas mimari",
            "create-trigger pipeline",
            "manage-users + manage-roles",
            "Aylık UTC delta arşiv",
        ],
        "artefaktlar": [
            "uretim/devir/MASTER-ENTERPRISE-ORCHESTRATOR.md",
            "scripts/live_dashboard.sh",
        ],
    },
]

SCHEDULE = [
    {"freq": "realtime", "agent": "Telemetry & Observability", "actions": [
        "opentelemetry-validation", "alert-investigation", "tierzero-investigate"]},
    {"freq": "daily", "agent": "DevOps & Infrastructure", "actions": [
        "debug-k8s-collection", "observability-service-health", "gitops-status"]},
    {"freq": "weekly", "agent": "Security & Compliance", "actions": [
        "review-security", "auditing-cloud-cluster-security", "twilio-security-hardening"]},
    {"freq": "monthly", "agent": "Chief Architect & Research", "actions": [
        "exa-web-search", "dora-metrics", "analyze-costs", "knowledge-update"]},
]

RED_FLAG = {
    "kural": "prompt_max_chars",
    "istenen": ">=900_000_000 karakter/prompt",
    "karar": "RED",
    "sozlesme": "122 yapilandirilmis prompt/rol (4-12 KiB) + 500 soru indeksi/title",
}


def build() -> dict:
    return {
        "ts": TS,
        "kaynak": "uploads/*.docx Domain 1-7 + OTel + Terraform alerts",
        "domain_adet": len(DOMAINS),
        "skill_directive_min": 20,
        "red_flag": RED_FLAG,
        "schedule_7x24": SCHEDULE,
        "domains": DOMAINS,
        "hiyerarsi": ["CEA", "CTO", "CDO", "CSO", "CPO", "Domain Leads", "Specialist Agents"],
    }


def write_md(payload: dict) -> None:
    out_dir = ROOT / "uretim" / "domain-matrix"
    out_dir.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# DOMAIN MATRIX 1–7 — Enterprise MCP Orchestration",
        f"> Üretim: {TS} · 🚩900M RED · sözleşme: 122 prompt/rol",
        "",
        "## 7×24 Schedule",
        "| Freq | Agent | Actions |",
        "|---|---|---|",
    ]
    for s in SCHEDULE:
        lines.append(f"| {s['freq']} | {s['agent']} | {', '.join(s['actions'])} |")
    lines.append("")
    for d in DOMAINS:
        lines += [
            f"## Domain {d['id']}: {d['ad']} (`{d['kod']}`)",
            f"- C-Suite: **{d['c_suite']}**",
            f"- Skills ({len(d['skills'])}): " + ", ".join(f"`/{s}`" for s in d["skills"][:8]) + ("…" if len(d["skills"]) > 8 else ""),
            f"- Directives: **{len(d['directives'])}** (≥20 hedef)",
            "",
        ]
        for i, di in enumerate(d["directives"], 1):
            lines.append(f"{i}. {di}")
        if d.get("artefaktlar"):
            lines.append("")
            lines.append("Artefaktlar: " + ", ".join(f"`{a}`" for a in d["artefaktlar"]))
        lines.append("")
    (out_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    dogrula = "--dogrula" in sys.argv
    payload = build()
    data_path = ROOT / "data" / "domain_matrix.json"
    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_md(payload)
    ok = all(len(d["directives"]) >= 20 for d in DOMAINS) and len(DOMAINS) == 7
    print(f"domain={len(DOMAINS)} directives_ok={ok} red={RED_FLAG['karar']}")
    if dogrula and not ok:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
