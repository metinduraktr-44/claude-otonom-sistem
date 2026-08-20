# Workflow — CockroachDB security/ops (`SEC-CRDB`)
> 2026-08-04T08:44:49Z · skills=32

## Amaç
CockroachDB security/ops skill kümesini LLM ajans olarak 7×24 işlet.

## Aktörler
- Domain Başkanı · Lead · IC · Uygulama Operatörü

## İş akışı
1. İstek gelince skill seç (listeden)
2. SKILL.md oku
3. Credential/MCP kontrol → yoksa dry-run
4. Uygula / raporla
5. Denetim + damga + arşiv
6. Üst title'a handoff gerekirse eskalasyon

## Skill listesi
- `/analyzing-range-distribution`
- `/analyzing-schema-change-storage-risk`
- `/auditing-table-statistics`
- `/benchmarking-transaction-patterns`
- `/cockroachdb-sql`
- `/configuring-audit-logging`
- `/configuring-ip-allowlists`
- `/configuring-log-export`
- `/configuring-private-connectivity`
- `/configuring-sso-and-scim`
- `/designing-application-transactions`
- `/designing-multi-region-applications`
- `/enabling-cmek-encryption`
- `/enforcing-password-policies`
- `/hardening-user-privileges`
- `/managing-certificates-and-encryption`
- `/managing-cluster-capacity`
- `/managing-cluster-settings`
- `/managing-tls-certificates`
- `/molt-fetch`
- `/molt-replicator`
- `/molt-verify`
- `/monitoring-background-jobs`
- `/performing-cluster-maintenance`
- `/preparing-compliance-documentation`
- `/prisma-database-setup-cockroachdb`
- `/profiling-statement-fingerprints`
- `/profiling-transaction-fingerprints`
- `/provisioning-cluster-for-production`
- `/reviewing-cluster-health`
- `/triaging-live-sql-activity`
- `/upgrading-cluster-version`

## Prompt kümeleri
- Title: 122 · Ekip: 122 · Uygulama: 122
- Sözleşme: 4000-12000 karakter (🚩 900B yasak)
