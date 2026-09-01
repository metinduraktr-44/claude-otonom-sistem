# Workflow — Render (`DEP-RENDER`)
> 2026-09-01T10:22:05Z · skills=19

## Amaç
Render skill kümesini LLM ajans olarak 7×24 işlet.

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
- `/render-background-workers`
- `/render-cli`
- `/render-cron-jobs`
- `/render-debug`
- `/render-disks`
- `/render-docker`
- `/render-domains`
- `/render-env-vars`
- `/render-keyvalue`
- `/render-mcp`
- `/render-migrate-from-heroku`
- `/render-monitor`
- `/render-networking`
- `/render-postgres`
- `/render-private-services`
- `/render-scaling`
- `/render-static-sites`
- `/render-web-services`
- `/render-workflows`

## Prompt kümeleri
- Title: 122 · Ekip: 122 · Uygulama: 122
- Sözleşme: 4000-12000 karakter (🚩 900B yasak)
