# Workflow — Feature flags / Confidence (`FEAT-CONF`)
> 2026-08-25T14:48:45Z · skills=20

## Amaç
Feature flags / Confidence skill kümesini LLM ajans olarak 7×24 işlet.

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
- `/analyze-experiments`
- `/analyzing-experiment-session-replays`
- `/auditing-experiments-flags`
- `/chaos-experiment`
- `/cleaning-up-stale-feature-flags`
- `/configuring-experiment-analytics`
- `/configuring-experiment-rollout`
- `/creating-experiments`
- `/diagnosing-experiment-results`
- `/finding-deleted-feature-flags`
- `/finding-experiments`
- `/instrument-feature-flags`
- `/manage-feature-flags`
- `/managing-experiment-lifecycle`
- `/migrate-eppo`
- `/migrate-optimizely`
- `/migrate-posthog`
- `/migrate-statsig`
- `/onboard-confidence`
- `/onboard-confidence-dry-run`

## Prompt kümeleri
- Title: 122 · Ekip: 122 · Uygulama: 122
- Sözleşme: 4000-12000 karakter (🚩 900B yasak)
