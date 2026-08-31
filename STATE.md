# STATE — Holding + Creative Agency + Security OS

> Tek kaynak: oturum durumu. Her `/devam`, `/sec-devam` veya `/latos-devam` öncesi ilgili bölümü oku, sonra güncelle.

## Holding (mevcut)
- **runtime:** Python 3 stdlib + Bash + GHA
- **validate:** `python3 scripts/validate.py`

---

## Creative Agency OS

### Faz
- **phase:** `5` (BRIEF-ONLY brief üretimi tamam — S01/S02; Faz 1–4 içerik de bu turda)
- **last_command:** `/devam` continuum (Faz 0 refresh → 1 Research → 2 Org → 3 Scenarios → 4 Matrix → 5 Briefs → QA)
- **last_updated_utc:** 2026-08-27T13:01:29Z

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
- **brief_id:** `ADOPs-CRE-SEED-2026Q3` (S01/S02 × 3 kanal)
- **scenario_id:** `S01`…`S08` (INDEX: `SCENARIOS/INDEX.md`)
- **design_id:** — (BRIEF-ONLY)

### Sonraki adım (Agency)
1. Müşteri/marka kit → `CONTEXT/INBOX/` (TBD kilidi)
2. S03–S08 için brief dalgası (`/brief-uret`)
3. critic-copy / critic-spec tam PASS döngüsü
4. (Opsiyonel) Canva OAuth — yalnızca CANVA:ON istendiğinde
5. Cursor restart → `/devam` smoke

---

## Security OS

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

### Faz
- **phase:** `1–4` (Research + Org/Experts seed + Skill depth tranche + Controls 001–020×6)
- **MODE:** `ASSESS-ONLY` (varsayılan — gap/doküman; agresif kod değişikliği yok)
- **last_command:** `sec-devam` / Faz 1+2+3+4 tranche
- **last_updated_utc:** 2026-08-27T13:05:00Z

### Guardrails
- defense-only · secret-redakte · exploit-yok · tehlikeli shell yok
- Faz başı/sonu damgası zorunlu

### Ingestion özeti (Faz 0)
- **inventory:** `SECURITY_CONTEXT/inventory.md`
- **attack-surface:** `SECURITY_CONTEXT/attack-surface.md` (savunma perspektifi)
- **secrets found:** konum+tip only — değer yok (bkz. inventory)
- **holding çapraz:** `docs/SECRETS-DRYRUN-MATRISI.md`, `infra/`, workflows

### Bu tur özeti
- **Faz 1:** `SECURITY_RESEARCH/` threat-landscape · standards-currency · supply-chain
- **Faz 2:** `ORG/ROLES/` 11 rol · `EXPERTS/` DIGEST + top100 CISO/AppSec/Crypto seed
- **Faz 3:** 6 skill derinlik (secret-hygiene, threat-modeling, compliance-mapper, layers-engine, encryption-engine, transparent-code-engine)
- **Faz 4:** **120 kontrol** (6×20) + `SECURITY_MATRIX/matrix.md` + CSV

### Aktif iş
- **assessment_id:** sec-2026-08-27-faz1-4
- **control_batch:** `001-020` × 6 motors (120/600)
- **compliance_pack:** crosswalk seed (pack Faz 5)

### Sonraki adım (Security)
1. Kontroller **021–100** (batch'li) — 6 motor
2. Skill references → ~20k hedefe doğru ek derinlik
3. GHA permissions matrisi + SHA pin gap ASSESS
4. Faz 5 compliance pack iskeleti
5. Canva MCP dokunulmadı — security MCP örnek kapalı

---

## LATOS (Living AI Talent & Organization System)

### Faz
- **phase:** `0–1` (Bootstrap + Title Discovery START)
- **last_command:** `latos-baslat` / Faz 0 bootstrap
- **last_updated_utc:** 2026-08-27T20:20:00Z

### Envanter
- **title_count:** 633 (`data/holding_istirak_org.json`)
- **master_list:** `ROSTER/TITLE_INVENTORY.md`
- **job_cards_skeleton:** 2 (hq-ceo, adops-ceo)
- **git_deleted_rol_kartlari:** 72 (dokümante; restore insan onaylı)

### Karakter hedefleri (fazlı — tamamlanmadı)
- İş kartı 2000+/200 başlık → Faz 4
- 122 prompt/title → Faz 8
- 200 tahmin/gün → Faz 9
- 900M char/prompt → imkânsız; fazlı yaklaşım dokümante

### Sonraki adım (LATOS)
1. Faz 1 tamamla: git deleted title detay dokümantasyonu
2. Faz 2: `RESEARCH/_ORG_BEST_PRACTICE.md` genişlet
3. Faz 3: `ORG/ORG_CHART.md` görsel/HTML
4. Skill restart: Cursor restart + yeni chat + `/latos-devam`
5. JOB_CARDS batch skeleton (10 title pilot)
