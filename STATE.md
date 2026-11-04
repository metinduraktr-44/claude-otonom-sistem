# STATE — Holding + Creative Agency + Security OS

> Tek kaynak: oturum durumu. Her `/devam`, `/sec-devam` veya `/latos-devam` öncesi ilgili bölümü oku, sonra güncelle.

## Holding (mevcut)
- **runtime:** Python 3 stdlib + Bash + GHA
- **validate:** `python3 scripts/validate.py`

---

## Creative Agency OS

### Faz
- **phase:** `5` (BRIEF-ONLY — S01–S08 × 3 kanal)
- **last_command:** `/devam` QA critic-copy/spec dürüst gap (PASS yok)
- **last_updated_utc:** 2026-11-04T11:40:00Z

### CANVA modu
- **default:** `BRIEF-ONLY` — tasarım üretimi yok; brief + spec + senaryo çıktısı
- **CANVA:ON:** Kullanıcı açıkça istediğinde veya `/canva-uret` komutu ile MCP üzerinden Canva API/MCP devreye girer
- **OAuth:** Henüz yapılandırılmadı → `tools/canva-client/README.md`

### Ingestion özeti (Faz 0)
- **holding:** 8 iştirak · 633 rol · 688 slash skill
- **CONTEXT:** `CONTEXT/CONTEXT_BRIEF.md` refresh — marka TBD, ürün yolu AdOps CRE
- **MATRIX:** `CHANNEL_MATRIX.md` + `PRODUCTION_GRID.csv` senaryo satırları
- **ORG:** `ORG_CHART.md` + `SKILLS_INVENTORY.md` + `EXPERTS/DIGEST.md`

### Aktif iş
- **brief_id:** `ADOPs-CRE-SEED-2026Q3` (S01–S08 × 3 kanal)
- **scenario_id:** `S01`…`S08` (INDEX: `SCENARIOS/INDEX.md`)
- **design_id:** — (BRIEF-ONLY)
- **brief_count:** 24 (6 eski S01–S02 + 18 yeni S03–S08)

### Sonraki adım (Agency)
1. Müşteri/marka kit → `CONTEXT/INBOX/` (TBD kilidi) — **PASS bloğu**
2. critic-copy REVISE kapat (kanal-özel hook; S02 sahte PASS headline)
3. critic-spec: CANVA:ON + pixel olmadan PASS yok
4. Cursor restart → `/devam` smoke

---

## Security OS

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

### Faz
- **phase:** `1–5` (Research + Org + Skills + Controls 600 + **COMPLIANCE INDEX**)
- **MODE:** `ASSESS-ONLY` (varsayılan — gap/doküman; agresif kod değişikliği yok)
- **last_command:** `sec-devam` / Faz 5 NIST-CSF-2.0 × ISO27001 × CIS INDEX
- **last_updated_utc:** 2026-11-04T11:40:00Z

### Guardrails
- defense-only · secret-redakte · exploit-yok · tehlikeli shell yok
- Faz başı/sonu damgası zorunlu

### Ingestion özeti (Faz 0)
- **inventory:** `SECURITY_CONTEXT/inventory.md`
- **attack-surface:** `SECURITY_CONTEXT/attack-surface.md` (savunma perspektifi)
- **secrets found:** konum+tip only — değer yok (bkz. inventory)
- **holding çapraz:** `docs/SECRETS-DRYRUN-MATRISI.md`, `infra/`, workflows

### Bu tur özeti
- **Faz 5:** `COMPLIANCE/INDEX.md` — NIST CSF 2.0 / ISO 27001:2022 / CIS v8 **INDEX** (SoA 93 / 900 sayfa yok)
- **Faz 4 (önceki):** 600 kontrol + matrix CSV — **yeniden yazılmadı**
- **GHA pin gap:** ASSESS notu duruyor; workflow değişmedi
- **Açık PR dokunulmadı:** #34/#35/#39 merge yok — DEVAM ≠ merge

### Aktif iş
- **assessment_id:** sec-2026-11-04-faz5-compliance-index
- **control_batch:** `001-100` × 6 (**600/600** katalog; bu tur 0 yeni kontrol)
- **compliance_pack:** INDEX iskelet (SOC2 işaretçi boş)

### Sonraki adım (Security)
1. Faz 5: GV.RM + CIS IG1 kanıt sütunu (hala ASSESS)
2. Skill references → ~20k
3. GHA SHA pin **uygulama** yalnızca MODE=IMPLEMENT
4. IR playbook ASSESS (Faz 6) — #39 ile çakıştırma yok
5. Canva MCP dokunulmadı

---

## LATOS (Living AI Talent & Organization System)

### Faz
- **phase:** `0–4-light` (Bootstrap + Title Discovery + C-level + **Director** skeleton)
- **last_command:** `latos-devam` / +10 Director JOB_CARDS (max 10 headings)
- **last_updated_utc:** 2026-11-04T11:40:00Z

### Envanter
- **title_count:** 633 (`data/holding_istirak_org.json`)
- **master_list:** `ROSTER/TITLE_INVENTORY.md`
- **job_cards_skeleton:** 23 (önceki 13 C-level + 10 Director)
- **git_deleted_rol_kartlari:** 72 (dokümante; restore insan onaylı)

### Karakter hedefleri (fazlı — tamamlanmadı)
- İş kartı 2000+/200 başlık → Faz 4 (şimdi 10 heading/title)
- 122 prompt/title → Faz 8
- 200 tahmin/gün → Faz 9
- 900M char/prompt → imkânsız; fazlı yaklaşım dokümante

### Sonraki adım (LATOS)
1. Faz 1: git deleted 72 **katalog** (restore değil)
2. Faz 2: `RESEARCH/_ORG_BEST_PRACTICE.md` genişlet
3. Faz 3: `ORG/ORG_CHART.md` görsel/HTML
4. Sonraki 10 JOB_CARDS (EVP/Director-2) — 200 heading uydurma yok
5. Skill restart: Cursor restart + yeni chat + `/latos-devam`
