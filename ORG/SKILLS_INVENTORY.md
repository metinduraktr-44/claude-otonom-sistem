# SKILLS_INVENTORY — Slash Skill Envanteri

> Kaynak: `data/slash_skill_katalog.json` · 688 skill · 9 domain · refresh 2026-08-27T12:56:59Z
> Bu dosya **özet + eşleme**; katalog duplicate edilmez.

## Özet

| Metrik | Değer |
|--------|------:|
| Toplam skill | 688 |
| Domain | 9 |
| Title (ünvan) | 30 |
| Prompt hedef (index) | 10980 |

## Domain özeti (katalog referansı)

| Kod | Domain | Skill adet (katalog) |
|-----|--------|---------------------:|
| INFRA | Infrastructure & Cloud | 68 |
| *(diğer 8)* | bkz. `data/slash_skill_katalog.json` → `domains[]` | — |

Tam domain kırılımı ve skill slug listesi: **tek kaynak JSON**.

## Creative Agency OS skills (`.cursor/skills/`)

14 ajans-özel skill — holding kataloğunu **duplicate etmez**, referans alır:

| Skill | Faz / kullanım |
|-------|----------------|
| `brief-writer` | Faz 3/5 — BRIEFS/ |
| `creative-scenarios` | Faz 3 — SCENARIOS/ |
| `spec-matrix` | Faz 4 — MATRIX doğrulama |
| `expert-engine` | Faz 2 — EXPERTS/ |
| `archive-loop` | Faz 6 |
| `canva-edit-design` | CANVA:ON only |
| `canva-brand-check` | CANVA:ON only |
| `canva-design-feedback` | CANVA:ON only |
| `canva-implement-feedback` | CANVA:ON only |
| `canva-resize-for-social` | CANVA:ON / resize plan |
| `canva-bulk-create` | CANVA:ON |
| `canva-export-pipeline` | CANVA:ON |
| `canva-production-pipeline` | CANVA:ON uçtan uca |

## Holding skill katalog referansı

- Tam katalog: `data/slash_skill_katalog.json`
- Üretim script: `scripts/slash_skill_katalog_uret.py`
- Skill-title haritası: `data/skill_title_haritasi.json`
- Skill envanteri: `data/skill_envanteri.json`
- Departman eşlemesi: `ORG/SKILL_MATRIX.md`

## Red flag

🚩 ≥900M/900B karakter/prompt RED — sözleşme: 122×4–12 KiB + referans zinciri
