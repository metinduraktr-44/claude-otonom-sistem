variable "environment" {
  type    = string
  default = "production"
}

variable "service_name" {
  type    = string
  default = "api-service-prod"
}

variable "datadog_api_key" {
  type      = string
  sensitive = true
}

variable "datadog_app_key" {
  type      = string
  sensitive = true
}

variable "sentry_auth_token" {
  type      = string
  sensitive = true
}

variable "sentry_organization" {
  type = string
}

variable "sentry_project_slug" {
  type = string
}

variable "pagerduty_user_email" {
  type = string
}

variable "slack_channel_critical" {
  type    = string
  default = "alerts-critical"
}

variable "slack_channel_warnings" {
  type    = string
  default = "alerts-warnings"
}
