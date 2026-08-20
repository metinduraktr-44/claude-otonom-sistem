# Infra — Observability & Domain 1/2

| Artefakt | Rol |
|---|---|
| `otel/opentelemetry-collector.yaml` | K8s OTLP collector (4317/4318) |
| `terraform/observability/` | Datadog + Sentry + PagerDuty + Slack alerts |
| `../.github/workflows/enterprise-k8s-otel-pipeline.yml` | Dry-run CI contract |

## Uygulama
```bash
# OTel (cluster erişimi gerekir)
kubectl apply -f infra/otel/opentelemetry-collector.yaml

# Alerts (secrets gerekir)
cd infra/terraform/observability
cp terraform.tfvars.example terraform.tfvars  # doldur, commit etme
export TF_VAR_datadog_api_key=... TF_VAR_datadog_app_key=...
export TF_VAR_sentry_auth_token=... PAGERDUTY_TOKEN=...
terraform init && terraform plan
```

## Secret URL’leri
- Datadog: https://app.datadoghq.com/organization-settings/api-keys
- Sentry: https://sentry.io/settings/account/api/auth-tokens/
- PagerDuty: https://support.pagerduty.com/main/docs/api-access-keys
- Slack apps: https://api.slack.com/apps

🚩 Secret ASLA git’e girmez.
