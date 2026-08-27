# İŞ LİSTESİ — GIGA Security OS (FAZ 0–8)

> Damga: 2026-08-27T12:40:00Z · MODE=`ASSESS-ONLY` default · DEFENSE-ONLY

| Faz | Durum | İş | Kanıt / çıktı |
|-----|-------|-----|----------------|
| 0 BOOTSTRAP | [x] | rules/commands/skills/hooks/agents/plan + scanners | `.cursor/` · `scripts/secret_scan.py` |
| 1 CONTEXT | [ ] | SECURITY_CONTEXT assets & trust boundaries | `SECURITY_CONTEXT/` |
| 2 RESEARCH | [ ] | Kaynaklı notlar | `SECURITY_RESEARCH/` |
| 3 ORG+EXPERTS | [x] seed | Roller + EXPERTS/_SEED (Kaminsky deceased) | `EXPERTS/_SEED.md` · `ORG/ROLES/` |
| 4 ENGINES | [x] stub | 20 skill kısa + refs TODO; deep samples | `.cursor/skills/*` |
| 5 MATRIX | [x] template | Gap şablon + sample control | `SECURITY_MATRIX/` · `LAYERS/CTRL-SAMPLE-*` |
| 6 COMPLIANCE | [ ] | NIST/ISO paket doldur | `COMPLIANCE/` |
| 7 QA+IR | [x] stub | IR playbook skeleton + QA | skills/incident-response · `QA/` |
| 8 ARCHIVE | [ ] | Aylık snapshot + CALENDAR | `ARCHIVE/{YYYY-MM}/security/` |

## FAZ 3 continuous (dürüst not)
Tek PR’da 20×20k karakter **yapılmadı / yapılmamalı**. Her skill `references/TODO.md` + seçilmiş deep sample.
Sonraki PR’lar: motor başına 1–2 derin referans doldur (SIGNAL > LENGTH).

## Komut sırası
1. Paste `CURSOR-GIGA-MASTER-SECURITY.md` veya `/baslat-security`
2. Cursor restart / yeni Agent → skills yükle
3. `/gap-analizi` → `/kontrol-uret` → `/compliance-paket`
4. `/etik-denetim` her anlamlı turda
5. `/arsivle` ay sonunda
