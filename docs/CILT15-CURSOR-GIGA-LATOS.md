# CILT15 — Cursor GIGA LATOS (Living AI Talent & Organization System)

**Statü:** Bootstrap + FAZ 1 light · **Dil:** Türkçe · **Repo:** `claude-otonom-sistem`

## Ne
Cursor Agent için **title/org/iş-kartı/uzman/yetenek OS**. Self-expanding; tek shot 900M = 🚩 RED.

## İlgili Ciltler
| Cilt | Konu | Not |
|---|---|---|
| [CILT13](CILT13-CURSOR-GIGA-CANVA.md) | Canva Creative Agency | Ayrı GIGA; additive |
| [CILT14](CILT14-CURSOR-GIGA-SECURITY.md) | Security Governance | Ayrı GIGA; additive |
| [CILT9 / UNVAN](UNVAN-HIYERARSISI.md) | Ünvan ladder + top-100 protokol | Title kaynağı |
| Bu cilt | LATOS | Talent & job-card OS |

## Harita

| Öğe | Yol |
|---|---|
| Paste prompt | `uretim/devir/CURSOR-GIGA-MASTER-LATOS.md` |
| Checklist FAZ 0–9 | `docs/IS-LISTESI-GIGA-LATOS.md` |
| Rules | `.cursor/rules/00-latos-core.mdc` … `50-forecast-calibration.mdc` |
| Commands | `.cursor/commands/baslat-latos.md` (+ shared devam/resume) |
| Skills | `.cursor/skills/{title-discovery,job-card-engine,…}/` |
| Agents | `.cursor/agents/latos-*.md` |
| Plan | `.cursor/plans/latos-master-plan.md` |
| STATE | `LATOS/STATE.md` (kök `STATE.md` bölümü) |
| Envanter | `ROSTER/TITLE_INVENTORY.md` |
| QA | `scripts/qa_check.py` · `scripts/citation_check.py` |

## Çalıştırma
```bash
# BAŞLAT / DEVAM (Agent chat)
/baslat-latos
/devam
/resume

# Yerel QA
python3 scripts/qa_check.py
python3 scripts/citation_check.py
python3 scripts/validate.py
```

## Karakter hedefleri (dürüst)
- İş kartı: ≥2000 karakter + 200 başlık hedef → `H00N` dosyalarıyla genişler
- Her başlık: 200+200+200 hedef → fazlı
- Prompt: 122+/title; 900M/prompt = **RED** → P00N parçaları
- Top-100: seed + `unverified`; uydurma liste yok

## Envanter kaynağı (bu repo)
1. `data/skill_title_haritasi.json`
2. `.claude/org/org.json`
3. `docs/UNVAN-HIYERARSISI.md`
4. `.claude/agents/**`
5. `git log --diff-filter=D -- uretim/rol-kartlari/`

## Hibrit
Skill keşfedildiyse skill; değilse master prompt inline — yol aynı.
