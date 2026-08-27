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
- [ ] `RESEARCH/_ORG_BEST_PRACTICE.md`
- [ ] `TASKS/MASTER_TASKS.md` P0–P3

## FAZ 3 — Org
- [ ] `ORG/ORG_CHART.md`
- [ ] `ORG/SKILLS_INVENTORY.md` + `SKILL_MATRIX.md`
- [ ] RACI / span of control

## FAZ 4 — İş kartları
- [x] Örnek kart: `JOB_CARDS/CISO/` (H001… kısmi, dürüst)
- [ ] Envanterdeki her title için CARD.md iskeleti
- [ ] 200 başlık hedefine `DEVAM` ile yaklaşım (QA gate)

## FAZ 5 — Uzman motoru
- [ ] Seed top-N + `unverified` işaret
- [ ] `CALENDAR/EXPERTS_UPDATE.md`
- [ ] READ→DELTA→DIFF→WRITE→DIGEST

## FAZ 6 — Yetenek motoru
- [ ] `SKILLS_TALENT/TALENT_TAXONOMY.md`
- [ ] `TITLE_TO_TALENT_MAP.md`
- [ ] Örnek yetenek top-list (doğrulanabilir mini)

## FAZ 7 — Roadmap / 7-24
- [ ] `ROADMAP/{title}.md` örnekleri
- [ ] `OPERATIONS/247_WORKFLOWS.md`

## FAZ 8 — Prompt üretimi
- [ ] `PROMPTS/TITLES/{title}/P001…` (122 hedef, parçalı)
- [ ] TEAMS + EXECUTION setleri
- [ ] 🚩 900M tek dosya yok — parçalı genişleme

## FAZ 9 — Canlı döngü
- [ ] Günlük tahmin örneği + kalibrasyon stub
- [ ] `/aylik-dongu` Cloud Automation (opsiyonel)
- [ ] ARCHIVE snapshot ritüeli

## QA / CI
- [x] `python3 scripts/validate.py` → GECTI
- [x] qa_check / citation_check self-test log
- [ ] Hook IDE kanalı doğrulama (kullanıcı restart)
