# STATE — Otonom AI Creative Agency

> Tek kaynak: oturum durumu. Her `/devam` veya `/resume` öncesi oku, sonra güncelle.

## Faz
- **phase:** `5` (BRIEF-ONLY brief üretimi tamam — S01/S02; Faz 1–4 içerik de bu turda)
- **last_command:** `/devam` continuum (Faz 0 refresh → 1 Research → 2 Org → 3 Scenarios → 4 Matrix → 5 Briefs → QA)
- **last_updated_utc:** 2026-08-27T13:01:29Z

## CANVA modu
- **default:** `BRIEF-ONLY` — tasarım üretimi yok; brief + spec + senaryo çıktısı
- **CANVA:ON:** Kullanıcı açıkça istediğinde veya `/canva-uret` komutu ile MCP üzerinden Canva API/MCP devreye girer
- **OAuth:** Henüz yapılandırılmadı → `tools/canva-client/README.md`

## Ingestion özeti (Faz 0)
- **holding:** 8 iştirak · 633 rol · 688 slash skill
- **CONTEXT:** `CONTEXT/CONTEXT_BRIEF.md` refresh — marka TBD, ürün yolu AdOps CRE
- **MATRIX:** `CHANNEL_MATRIX.md` + `PRODUCTION_GRID.csv` senaryo satırları
- **ORG:** `ORG_CHART.md` + `SKILLS_INVENTORY.md` + `EXPERTS/DIGEST.md`

## Aktif iş
- **brief_id:** `ADOPs-CRE-SEED-2026Q3` (S01/S02 × 3 kanal)
- **scenario_id:** `S01`…`S08` (INDEX: `SCENARIOS/INDEX.md`)
- **design_id:** — (BRIEF-ONLY)

## Tamamlanan (bu tur)
- [x] Faz 0 CONTEXT refresh
- [x] Faz 1 RESEARCH_* 
- [x] Faz 2 ORG / EXPERTS seed
- [x] Faz 3 SCENARIOS 01–08
- [x] Faz 4 MATRIX expand
- [x] Faz 5 BRIEFS S01–S02 × Meta4:5 / Meta9:16 / TikTok9:16
- [x] QA hafif rapor

## Sonraki adım
1. Müşteri/marka kit → `CONTEXT/INBOX/` (TBD kilidi)
2. S03–S08 için brief dalgası (`/brief-uret`)
3. critic-copy / critic-spec tam PASS döngüsü
4. (Opsiyonel) Canva OAuth — yalnızca CANVA:ON istendiğinde
5. Cursor restart → `/devam` smoke
