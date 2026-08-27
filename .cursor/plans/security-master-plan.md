# Security Master Plan — GIGA MASTER (Faz 0–8)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**MODE varsayılan:** `ASSESS-ONLY`  
**Karakter/derinlik hedefi:** fazlı (900k kümülatif — tek dump yok)  
**Agency track:** ayrı branch; birleştirmede additive

| Faz | Ad | Çıktı | Durum |
|-----|----|-------|-------|
| 0 | Bootstrap + Ingestion | rules, commands, hooks, CONTEXT inventory | **bu PR** |
| 1 | Research | `SECURITY_RESEARCH/` DIGEST, tehdit modeli iskeleti | sonraki `/sec-devam` |
| 2 | Org + Experts | `ORG/ROLES/` genişlet, `EXPERTS/` DIGEST | bekliyor |
| 3 | Control engines (batch) | LAYERS…CONDITIONAL stub→içerik (≤10/tur) | bekliyor |
| 4 | Matrix + Mapping | `SECURITY_MATRIX` doldurma, NIST/D3FEND map | bekliyor |
| 5 | Compliance packs | `COMPLIANCE/` NIST/CIS/ISO/SOC2 iskelet | bekliyor |
| 6 | Detection & IR | SecOps skill derinliği, playbook ASSESS | bekliyor |
| 7 | Skill depth | skill başına ~20k hedef (fazlı) | bekliyor |
| 8 | QA + Archive loop | `QA/`, `ARCHIVE/`, aylık döngü | bekliyor |

## Faz 0 kabul kriterleri
- [x] AGENTS.md Security OS
- [x] `.cursor/rules` security mdc
- [x] sec-* commands
- [x] hooks + scanner scripts
- [x] folder placeholders + matrix skeleton
- [x] skill skeletons (20)
- [x] inventory + attack-surface
- [ ] full 600 controls (ERTALANDI)
- [ ] 20k/skill (ERTALANDI)

## Çakışma notları
- Canva MCP: dokunulmaz; security MCP yalnızca `mcp.security.example.json`
- Agency `30-file-structure`: bu branch’te security tree; merge’de birleştir veya `31-security-file-structure.mdc`
