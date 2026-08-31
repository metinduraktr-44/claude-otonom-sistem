# Workflow — AWS serverless (`CLOUD-AWS`)
> 2026-08-25T14:48:45Z · skills=16

## Amaç
AWS serverless skill kümesini LLM ajans olarak 7×24 işlet.

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
- `/access-protected-vercel-deployment`
- `/amazon-location-service`
- `/amplify-workflow`
- `/api-gateway`
- `/aws-architecture-diagram`
- `/aws-lambda`
- `/aws-lambda-durable-functions`
- `/aws-lambda-managed-instances`
- `/aws-serverless-deployment`
- `/aws-step-functions`
- `/clickhousectl-cloud-deploy`
- `/deploy`
- `/deployments-cicd`
- `/elastic-beanstalk`
- `/prisma-cli-migrate-deploy`
- `/render-deploy`

## Prompt kümeleri
- Title: 122 · Ekip: 122 · Uygulama: 122
- Sözleşme: 4000-12000 karakter (🚩 900B yasak)
