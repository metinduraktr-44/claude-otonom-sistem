# Datadog + Sentry + PagerDuty + Slack — Domain 2 alert automation
# Kaynak: yüklenen alarm/PagerDuty/Slack dokümanları · 2026-08-10
# Secret ASLA commit edilmez — tfvars / env kullan.

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    datadog = {
      source  = "DataDog/datadog"
      version = "~> 3.35.0"
    }
    sentry = {
      source  = "jianyuan/sentry"
      version = "~> 0.12.0"
    }
    pagerduty = {
      source  = "PagerDuty/pagerduty"
      version = "~> 3.11.0"
    }
  }
}

provider "datadog" {
  api_key = var.datadog_api_key
  app_key = var.datadog_app_key
  api_url = "https://api.datadoghq.com"
}

provider "sentry" {
  token    = var.sentry_auth_token
  base_url = "https://sentry.io/api/"
}

provider "pagerduty" {
  # PAGERDUTY_TOKEN env
}

data "pagerduty_user" "oncall_engineer" {
  email = var.pagerduty_user_email
}

resource "pagerduty_escalation_policy" "backend_escalation" {
  name      = "[${upper(var.environment)}] Backend On-Call Escalation Policy"
  num_loops = 2

  rule {
    escalation_delay_in_minutes = 15
    target {
      type = "user_reference"
      id   = data.pagerduty_user.oncall_engineer.id
    }
  }
}

resource "pagerduty_service" "backend_api_service" {
  name                    = "${var.service_name}-service"
  auto_resolve_timeout    = 14400
  acknowledgement_timeout = 1800
  escalation_policy       = pagerduty_escalation_policy.backend_escalation.id
  alert_creation          = "create_alerts_and_incidents"
}

resource "pagerduty_service_integration" "datadog_integration" {
  name    = "Datadog Integration"
  service = pagerduty_service.backend_api_service.id
  type    = "events_api_v2_inbound_integration"
}

resource "pagerduty_service_integration" "sentry_integration" {
  name    = "Sentry Integration"
  service = pagerduty_service.backend_api_service.id
  type    = "events_api_v2_inbound_integration"
}

resource "datadog_monitor" "service_error_rate" {
  name = "[${upper(var.environment)}] ${var.service_name} - High Exception & Error Rate"
  type = "query alert"

  message = <<-EOT
    {{#is_alert}}
    CRITICAL: Error rate for ${var.service_name} exceeded 5%!
    Trace: https://app.datadoghq.com/apm/traces?query=service%3A${var.service_name}
    @pagerduty-${pagerduty_service_integration.datadog_integration.name}
    @slack-${var.slack_channel_critical}
    {{/is_alert}}
    {{#is_warning}}
    WARNING: Error rate reached 2%.
    @slack-${var.slack_channel_warnings}
    {{/is_warning}}
    {{#is_recovery}}
    RECOVERED: Error rate normalized.
    @slack-${var.slack_channel_critical}
    {{/is_recovery}}
  EOT

  escalation_message = "Re-notification: ${var.service_name} error rate still critical."

  query = "sum(last_5m):sum:trace.servlet.request.errors{env:${var.environment},service:${var.service_name}}.as_count() / sum:trace.servlet.request.hits{env:${var.environment},service:${var.service_name}}.as_count() * 100 > 5"

  monitor_thresholds {
    critical = 5.0
    warning  = 2.0
  }

  notify_no_data    = true
  no_data_timeframe = 10
  renotify_interval = 30

  tags = [
    "env:${var.environment}",
    "service:${var.service_name}",
    "tier:c-suite",
    "managed-by:terraform",
    "domain:2-observability",
  ]
}

resource "datadog_monitor" "service_p99_latency" {
  name = "[${upper(var.environment)}] ${var.service_name} - P99 Latency SLA Breach"
  type = "query alert"

  message = <<-EOT
    WARNING: P99 Latency for ${var.service_name} > 1200ms (10m).
    @slack-${var.slack_channel_warnings}
  EOT

  query = "avg(last_10m):p99:trace.servlet.request.duration{env:${var.environment},service:${var.service_name}} > 1.2"

  monitor_thresholds {
    critical = 1.2
    warning  = 0.8
  }

  notify_no_data = false
  tags = [
    "env:${var.environment}",
    "service:${var.service_name}",
    "type:latency",
    "domain:2-observability",
  ]
}

resource "sentry_issue_alert" "new_uncaught_exception" {
  organization = var.sentry_organization
  project      = var.sentry_project_slug
  name         = "[${upper(var.environment)}] New Uncaught Exception Triggered"
  action_match = "any"
  filter_match = "all"
  frequency    = 30

  conditions = [
    {
      id = "sentry.rules.conditions.first_seen_event.FirstSeenEventCondition"
    }
  ]

  filters = [
    {
      id = "sentry.rules.filters.assigned_to.AssignedToFilter"
      target_type = "Unassigned"
    },
    {
      id    = "sentry.rules.filters.level.LevelFilter"
      match = "greater_or_equal"
      level = "error"
    }
  ]

  actions = [
    {
      id      = "sentry.integrations.slack.notify_service.SlackNotifyServiceAction"
      channel = "#${var.slack_channel_warnings}"
      tags    = "environment,level,exception"
    }
  ]
}

resource "sentry_issue_alert" "exception_spike_alert" {
  organization = var.sentry_organization
  project      = var.sentry_project_slug
  name         = "[${upper(var.environment)}] High Exception Spike (>50/min)"
  action_match = "any"
  filter_match = "all"
  frequency    = 15

  conditions = [
    {
      id       = "sentry.rules.conditions.event_frequency.EventFrequencyCondition"
      value    = 50
      interval = "1m"
    }
  ]

  actions = [
    {
      id      = "sentry.integrations.slack.notify_service.SlackNotifyServiceAction"
      channel = "#${var.slack_channel_critical}"
      tags    = "environment,level,exception"
    }
  ]
}

output "pagerduty_service_id" {
  value = pagerduty_service.backend_api_service.id
}

output "datadog_integration_key" {
  value     = pagerduty_service_integration.datadog_integration.integration_key
  sensitive = true
}

output "sentry_integration_key" {
  value     = pagerduty_service_integration.sentry_integration.integration_key
  sensitive = true
}
