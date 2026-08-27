# Master Plan — Otonom AI Creative Agency (Faz 0–7)

> Kaynak: GIGA MASTER PROMPT BÖLÜM 13 · Bootstrap: BÖLÜM 0.5

## Faz 0 — Bootstrap ✅ (bu PR)
- [x] `.cursor/rules/*.mdc` (agency core, brand, spec, structure, canva)
- [x] `.cursor/commands/` slash komutları
- [x] `.cursor/skills/` Canva + agency skills
- [x] `STATE.md`, `CONTEXT/`, klasör iskeleti
- [x] `tools/canva-client/` scaffold
- [x] `scripts/spec_validate.py` (Pillow pixel/ratio/size)
- [x] Faz 0 ingestion — CONTEXT_BRIEF, ORG, MATRIX
- [ ] Cursor restart + `/baslat` smoke

## Faz 1 — Context Ingestion
- [ ] CONTEXT_BRIEF doldur (marka, KPI, kanal)
- [ ] INBOX materyal işleme
- [ ] İlk RESEARCH notları
- [ ] `.cursorrules` → `.mdc` tam migrasyon

## Faz 2 — Expert Engine
- [ ] EXPERTS/ seed persona (copy, design, media)
- [ ] ORG/SKILLS_INVENTORY senkron
- [ ] Critic subagents entegrasyon testi
- [ ] `/uzman-guncelle` döngüsü

## Faz 3 — Brief & Scenario Pipeline
- [ ] `/brief-uret` → BRIEFS/ şablon
- [ ] `creative-scenarios` → SCENARIOS/
- [ ] critic-copy PASS döngüsü
- [ ] TASKS/MASTER_TASKS güncelleme

## Faz 4 — Canva Integration
- [ ] OAuth PKCE (`tools/canva-client/`)
- [ ] CANVA:ON flag + MCP smoke
- [ ] DESIGN_REGISTRY operasyonel
- [ ] `/canva-uret` dry-run → live

## Faz 5 — QA & Validation
- [ ] spec_validate.py Pillow tam implementasyon
- [ ] `/spec-dogrula` CI hook
- [ ] QA/ rapor şablonu
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
