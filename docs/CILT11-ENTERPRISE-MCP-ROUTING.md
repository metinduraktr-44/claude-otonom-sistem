# CILT11 — Enterprise MCP / Skill Routing (ürün uyarlaması)
> Kaynak docx: ULTIMATE ENTERPRISE MCP & AI AGENCY ORCHESTRATION · 2026-08-10 uyarlama
> Bağlı: `docs/SKILL-AJANS-HIYERARSI.md` · `data/skill_envanteri.json` · `docs/MCP-HIYERARSI.md`

## 🚩 Gerçeklik
- Slash-skill listesindeki yüzlerce `/twilio-…`, `/azure-…` vb. **bu repoda native runtime değildir**.
- Çalışan eşdeğer: domain routing tablosu → ilgili MIT katalog ajanı / MCP dry-run / Claude Code skill çağrısı.
- "+900 milyar karakter pront" → imkânsız; bu cilt + MEGA-PRONT modüler sistemdir.

## Swarm hiyerarşisi (C → işçi)
CEA (Chief Executive Agent) → C-suite ajanları (CTO/CISO/CDO/CMO/…) → Domain lead → IC → Worker.
Repo karşılığı: `docs/UNVAN-HIYERARSISI.md` + `.claude/org/org.json` + `.claude/agents/{KOD}/`.

## Zaman damgalı öğrenme döngüsü
`ts_start` → arşivi oku → yap → 6 katman validate → `ts_end` → `AUDIT_LOG.jsonl` → `BILGI_TABANI.md`.
Nightly: `.github/workflows/nightly-improve.yml` + `scripts/nightly.sh`.

## Altı domain + yönlendirme (özet)

| Domain | Odak | Bu üründe birincil karşılık | Ücretsiz ajan çekirdeği |
|---|---|---|---|
| A Infra | K8s/cloud/serverless | `INF-*`, `ENG-DEV`, katalog devops-infrastructure | `workflow-orchestrator`, `commit-guardian` |
| B Observability | OTel/Sentry/ELK | `SEC-OPS`, skill domain `OBS-*` | `debugger`, `qa-expert` |
| C Data | Warehouse/dbt/DB | `DSC-*`, `data/skill_envanteri` DATA-WH | `research-analyst`, `fact-checker` |
| D Full-stack/Auth | Next/Clerk/WorkOS | `app/README.md`, AUTH-* envanter | `planner`, `technical-writer` |
| E Comms/Scrape | Twilio/Apify/Exa/Firecrawl | `WEB-APIFY`, `COMMS-TW` dry-run | `search-specialist`, `competitive-intelligence-analyst` |
| F Product/Sec/AI | PRD/security/HF | `STR-*`, `SEC-*`, `AI-*` | `prompt-engineer`, `security-auditor`, `multi-agent-coordinator` |

Her domain için +20 yönlendirme ilkesi kullanıcı docx'inde tanımlı; uygulama kuralı:

1. **DRY RUN FIRST** — credential yoksa mutate etme; şablon + audit yaz.
2. **OBSERVABILITY** — her anlamlı üretim damgalı JSONL/MD arşiv.
3. **SECURITY** — secret commit yok; `.env.example` isim-only.
4. **RECURRING ARCHIVE** — aylık takvim `docs/AYLIK-GUNCELLEME-TAKVIMI.md`.

## 7/24 schedule (repo Actions)

| Sıklık | Workflow | Ücretsiz mi? |
|---|---|---|
| Gece 03:00 TR | `nightly-improve.yml` | Evet (LLM yoksa) |
| Sabah daily | `daily-agency.yml` | Evet (LLM yoksa iskelet) |
| Holding | `holding-konsolide.yml` / `holding-istirak-dongu.yml` | Evet (script) |
| Aylık skill | `skill-ajans-dongu.yml` | Evet |
| Upstream SHA | `upstream-sync.yml` | Evet |

## Kurulum
```bash
python3 scripts/install_free_mit_agents.py
# Claude Code: .claude/system_prompt
# Cursor: .cursorrules
```
