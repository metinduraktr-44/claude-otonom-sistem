# Security Master Plan — GIGA MASTER (Faz 0–8)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**MODE varsayılan:** `ASSESS-ONLY`  
**Karakter/derinlik hedefi:** fazlı (900k kümülatif — tek dump yok)  
**Agency track:** ayrı branch; birleştirmede additive

| Faz | Ad | Çıktı | Durum |
|-----|----|-------|-------|
| 0 | Bootstrap + Ingestion | rules, commands, hooks, CONTEXT inventory | **tamam (PR)** |
| 1 | Research | `SECURITY_RESEARCH/` DIGEST, tehdit modeli iskeleti | **bu tur kısmi** |
| 2 | Org + Experts | `ORG/ROLES/` genişlet, `EXPERTS/` DIGEST | **bu tur seed** |
| 3 | Control engines (batch) | LAYERS…CONDITIONAL stub→içerik | **120 kontrol** |
| 4 | Matrix + Mapping | `SECURITY_MATRIX` doldurma, NIST map | **120 satır** |
| 5 | Compliance packs | `COMPLIANCE/` NIST/CIS/ISO/SOC2 iskelet | bekliyor |
| 6 | Detection & IR | SecOps skill derinliği, playbook ASSESS | bekliyor |
| 7 | Skill depth | skill başına ~20k hedef (fazlı) | **6 skill başladı** |
| 8 | QA + Archive loop | `QA/`, `ARCHIVE/`, aylık döngü | bekliyor |

## Faz 0 kabul kriterleri
- [x] AGENTS.md Security OS
- [x] `.cursor/rules` security mdc
- [x] sec-* commands
- [x] hooks + scanner scripts
- [x] folder placeholders + matrix skeleton
- [x] skill skeletons (20)
- [x] inventory + attack-surface
- [ ] full 600 controls (**120/600** — devam)
- [ ] 20k/skill (**kısmi 6 skill** — devam)

## Faz 1–4 bu tur
- [x] threat-landscape / standards-currency / supply-chain
- [x] ORG roller + EXPERTS top100 seed
- [x] 6 skill references derinlik
- [x] controls-001-020 × 6 + matrix CSV
- [ ] GHA permissions matrisi
- [ ] controls 021–100

## Çakışma notları
- Canva MCP: dokunulmaz; security MCP yalnızca `mcp.security.example.json`
- Agency `30-file-structure`: bu branch’te security tree; merge’de birleştir veya `31-security-file-structure.mdc`
