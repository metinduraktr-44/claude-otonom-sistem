# LATOS Master Plan — Faz 0–9

> Plan Mode kaydı · `.cursor/plans/latos-master-plan.md`
> **Durum:** Faz 0–1 bootstrap (2026-08-27)

## Faz Özeti

| Faz | Ad | Çıktı | Durum |
|-----|-----|-------|-------|
| 0 | Bootstrap + Ingestion | `.cursor/`, AGENTS.md, hooks, envanter iskelet | ✅ |
| 1 | Title Keşif/Kurtarma | `ROSTER/TITLE_INVENTORY.md` (633) | 🔄 |
| 2 | Research + Master Tasks | `RESEARCH/`, `TASKS/LATOS_MASTER_TASKS.md` | ⏳ |
| 3 | Org + Hiyerarşi | `ORG/ORG_CHART.md`, RACI | ⏳ |
| 4 | İş Kartları | `JOB_CARDS/{title}/` skeleton→tam | ⏳ |
| 5 | Uzman Motoru | `EXPERTS/{title}/top100_*` | ⏳ |
| 6 | Yetenek Motoru | `SKILLS_TALENT/`, `EXPERTS_TALENT/` | ⏳ |
| 7 | Roadmap/7-24 | `ROADMAP/`, `OPERATIONS/` | ⏳ |
| 8 | Prompt Üretimi | `PROMPTS/` (122+/set, fazlı) | ⏳ |
| 9 | Canlı Döngü+Arşiv | FORECASTS, MEMORY, ARCHIVE | ⏳ |

## Karakter Hedefleri (FAZLI — dürüst)

| Hedef | Faz | Not |
|-------|-----|-----|
| İş kartı 2.000+ char, 200 başlık | 4+ | Skeleton Faz 0–1 OK |
| 122 prompt/title/ekip | 8+ | Alt dosya `P001.md`… |
| 200 tahmin/gün/title | 9+ | Cloud Agent zamanlı |
| 900M char/prompt | — | 🚩 Fiziksel imkânsız; hedef korunur, fazlı genişler |

## Paralel Agent Stratejisi
- Faz 4: 2–3 paralel agent ile başla → 8'e ölçekle
- Her agent `JOB_CARDS/{title}/` izolasyonu

## QA Kapıları
- `scripts/qa_check.py` — envanter diff
- `scripts/citation_check.py` — URL/timestamp
- İnsan onay: uzman listesi, git restore, self-modification

## Sonraki DEVAM
1. Faz 1 tamamla: git deleted title dokümantasyonu
2. Faz 2: `RESEARCH/_ORG_BEST_PRACTICE.md` seed
3. 2 örnek iş kartı skeleton genişlet
