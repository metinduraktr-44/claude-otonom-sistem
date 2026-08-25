# Workflow — Observe / OTel / Alert (`OBS-OBSERVE`)
> 2026-08-25T14:48:45Z · skills=16

## Amaç
Observe / OTel / Alert skill kümesini LLM ajans olarak 7×24 işlet.

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
- `/alert-investigation`
- `/debug-k8s-collection`
- `/debug-linux-host-collection`
- `/deploy-k8s-explorer`
- `/deploy-linux-host-explorer`
- `/generate-opal`
- `/observe-cli`
- `/opentelemetry-auto-instrumentation`
- `/opentelemetry-manual-instrumentation`
- `/opentelemetry-validation`
- `/outlier-detection-analysis`
- `/query-card-visualization`
- `/setup-k8s-backend`
- `/setup-k8s-collection`
- `/setup-linux-host-backend`
- `/setup-linux-host-collection`

## Prompt kümeleri
- Title: 122 · Ekip: 122 · Uygulama: 122
- Sözleşme: 4000-12000 karakter (🚩 900B yasak)
