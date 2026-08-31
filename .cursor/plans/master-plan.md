# Master Plan — Otonom AI Creative Agency (Faz 0–7)

> Kaynak: GIGA MASTER PROMPT BÖLÜM 13 · Bootstrap: BÖLÜM 0.5
> Refresh: 2026-08-27T12:56:59Z

## Faz 0 — Bootstrap ✅
- [x] `.cursor/rules/*.mdc` (agency core, brand, spec, structure, canva)
- [x] `.cursor/commands/` slash komutları
- [x] `.cursor/skills/` Canva + agency skills
- [x] `STATE.md`, `CONTEXT/`, klasör iskeleti
- [x] `tools/canva-client/` scaffold
- [x] `scripts/spec_validate.py` (Pillow pixel/ratio/size)
- [x] Faz 0 ingestion — CONTEXT_BRIEF, ORG, MATRIX
- [x] CONTEXT_BRIEF refresh (marka TBD, AdOps CRE ürün yolu)
- [ ] Cursor restart + `/baslat` smoke

## Faz 1 — Context / Research ✅ (seed)
- [x] CONTEXT_BRIEF doldur (marka TBD işaretli, KPI proxy, kanal)
- [ ] INBOX materyal işleme (INBOX boş — müşteri kit bekleniyor)
- [x] İlk RESEARCH notları (`RESEARCH_NOTES`, `COMPETITORS`, `INSIGHTS` + URL/ts)
- [ ] `.cursorrules` → `.mdc` tam migrasyon

## Faz 2 — Expert Engine ✅ (seed)
- [x] EXPERTS/DIGEST seed (bio uydurma yok; holding referans)
- [x] ORG/SKILLS_INVENTORY senkron
- [ ] Critic subagents entegrasyon testi
- [ ] `/uzman-guncelle` döngüsü

## Faz 3 — Brief & Scenario Pipeline ✅ (seed)
- [x] `/brief-uret` → BRIEFS/ (S01–S02 × 3 kanal)
- [x] `creative-scenarios` → SCENARIOS/01–08
- [ ] critic-copy PASS döngüsü (hafif QA notu var)
- [x] TASKS/MASTER_TASKS güncelleme

## Faz 4 — Matrix / Canva Integration (kısmi)
- [x] CHANNEL_MATRIX + PRODUCTION_GRID senaryo×kanal genişletme
- [ ] OAuth PKCE (`tools/canva-client/`) — CANVA:ON kapalı, bilinçli
- [ ] CANVA:ON flag + MCP smoke
- [ ] DESIGN_REGISTRY operasyonel
- [ ] `/canva-uret` dry-run → live

## Faz 5 — QA & Validation (kısmi)
- [ ] spec_validate.py Pillow tam implementasyon (export sonrası)
- [ ] `/spec-dogrula` CI hook
- [x] QA/ rapor şablonu + hafif QA_REPORT
- [ ] critic-spec otomasyon

## Faz 6 — Archive & Learning
- [ ] `/arsivle` manifest
- [ ] BILGI_TABANI + AUDIT zinciri
- [ ] `/aylik-dongu` ritmi
- [ ] ARCHIVE indeks

## Faz 7 — Production Automation
- [ ] `canva-production-pipeline` uçtan uca
- [ ] Bulk create + resize batch
- [ ] Export pipeline + delivery
- [ ] 7×24 nightly agency hook (opsiyonel)

## Kümülatif prompt notu
900k+ karakter tek dosyada üretilmez. Kurallar fazlı `.mdc` + skills + commands ile kümülatif büyür.
