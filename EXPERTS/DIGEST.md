# EXPERTS DIGEST — Uzman Persona Özeti

> Faz 2 seed · ts: 2026-08-27T12:56:59Z · **Uydurma bio yok** — yalnızca repo/holding referansları

## Critic subagents (`.cursor/agents/`)

| Agent | Görev |
|-------|-------|
| `critic-copy` | Brief/senaryo metin, claim, CTA, karakter limiti |
| `critic-design` | Görsel yön, safe zone, hiyerarşi (BRIEF-ONLY'de yön notu) |
| `critic-spec` | Kanal×boyut×ratio doğrulama |

## Holding referans rolleri (kartlar mevcut — bio icat etme)

| Referans | Yol | Not |
|----------|-----|-----|
| AdOps CRE EVP | `uretim/rol-kartlari/adops-evp-kreatif-stüdyo-dco.md` | OKR, kalite bar, CRE 4 unit |
| Holding org | `data/holding_istirak_org.json` | 633 rol slug |
| Org doküman | `docs/HOLDING-ISTIRAK-ORG.md` | İnsan-okur özet |
| Title top kişiler | `data/title_top_kisiler.json` / `docs/TITLE-TOP-KISILER.md` | Araştırma seed; persona uydurma yok |
| MIT agents | `.claude/katalog-mit/` | Harici agent katalog |

## Agency OS persona eşlemesi (Cursor)

| Persona | Kaynak tip | Skill |
|---------|------------|-------|
| Brief Writer | skill | `brief-writer` |
| Scenario Lead | skill | `creative-scenarios` |
| Spec Engineer | skill | `spec-matrix` |
| Expert Engine | skill | `expert-engine` |
| QA Lead | agents + QA/ | critic-* |

## Rotasyon kuralı

- `/uzman-guncelle` → bu DIGEST + ilgili rol kartını oku; **yeni bio yazma**
- Eksik uzman: holding JSON'dan slug bul → `uretim/rol-kartlari/` veya katalog; yoksa 🚩 + alternatif
- Title top-5 listeleri EVP kartlarında seed — aylık yenileme araştırma döngüsüne bağlı

## Slash skill

688 skill: `data/slash_skill_katalog.json` — `ORG/SKILLS_INVENTORY.md` özet
