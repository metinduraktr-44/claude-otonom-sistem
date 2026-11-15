# İŞ LİSTESİ — GIGA LATOS (FAZ 0–9)

> Checklist. `[x]` = bu PR’da yapıldı; `[ ]` = sonraki `DEVAM` turları.

## FAZ 0 — Bootstrap
- [x] `.cursor/rules` LATOS (00/10/20/32/40/50)
- [x] `.cursor/commands` (`baslat-latos` + shared)
- [x] `.cursor/hooks.json` merge-ready + guard/phase-audit
- [x] `scripts/qa_check.py` + `citation_check.py`
- [x] 8 skill iskeleti (kısa SKILL.md + references stub)
- [x] Agents: latos-critic / trainer / archivist
- [x] `.cursor/plans/latos-master-plan.md`
- [x] Dizin iskeleti + `LATOS/STATE.md`
- [x] `AGENTS.md` LATOS bölümü (additive)
- [x] Paste + CILT15 + bu checklist
- [ ] Cursor restart sonrası skill keşif doğrulama (kullanıcı)

## FAZ 1 — Title keşif
- [x] `ROSTER/TITLE_INVENTORY.md` (gerçek sayılar)
- [x] git silinmiş `uretim/rol-kartlari/` envantere
- [ ] Silinmiş dosya içeriği restore (insan onayı)
- [ ] ARCHIVE/ backup tarama derinleştirme

## FAZ 2 — Research + tasks
- [ ] `CONTEXT/CONTEXT_BRIEF.md` dolu
- [x] `RESEARCH/_ORG_BEST_PRACTICE.md` (seed 2026-11-15)
- [x] `TASKS/LATOS_MASTER_TASKS.md` P0–P2 (L-004 eklendi)

## FAZ 3 — Org
- [ ] `ORG/ORG_CHART.md`
- [ ] `ORG/SKILLS_INVENTORY.md` + `SKILL_MATRIX.md`
- [ ] RACI / span of control

## FAZ 4 — İş kartları
- [x] Örnek kart: `JOB_CARDS/CISO/` (H001… kısmi, dürüst)
- [x] +10 envanter slug skeleton (2026-11-15; 200 başlık yok)
- [ ] Envanterdeki her title için CARD.md iskeleti (~620 backlog)
- [ ] 200 başlık hedefine `DEVAM` ile yaklaşım (QA gate)

## FAZ 5 — Uzman motoru
- [x] Seed top-N + `unverified` (hq-ceo, adops-ceo; ranking yok)
- [x] `CALENDAR/LATOS_RESEARCH_LOOP.md` + EXPERTS_UPDATE iskelet
- [x] READ→DELTA→DIFF→WRITE→DIGEST (ilk ARCHIVE/2026-11/latos)

## FAZ 6 — Yetenek motoru
- [x] `SKILLS_TALENT/TALENT_TAXONOMY.md` (101 INDEX)
- [x] `TITLE_TO_TALENT_MAP.md` (6 satır)
- [x] Örnek yetenek stub (satranç, hitabet — `unverified`)

## FAZ 7 — Roadmap / 7-24
- [x] `ROADMAP/hq-ceo.md` + `hq-caio.md` örnek
- [x] `OPERATIONS/247_WORKFLOWS.md` (GHA kırılmadan bağ)

## FAZ 8 — Prompt üretimi
- [x] `PROMPTS/TITLES/hq-ceo/` INDEX 122 + P001–P003
- [x] TEAMS + EXECUTION INDEX (pending slot)
- [x] 🚩 900M tek dosya yok — parçalı genişleme dokümante

## FAZ 9 — Canlı döngü
- [ ] Günlük tahmin örneği + kalibrasyon stub
- [ ] `/aylik-dongu` Cloud Automation (opsiyonel)
- [ ] ARCHIVE snapshot ritüeli

## QA / CI
- [x] `python3 scripts/validate.py` → GECTI
- [x] qa_check / citation_check self-test log
- [ ] Hook IDE kanalı doğrulama (kullanıcı restart)
