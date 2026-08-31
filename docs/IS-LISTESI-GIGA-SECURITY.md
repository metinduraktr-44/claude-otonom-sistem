# İŞ LİSTESİ — GIGA Security OS (FAZ 0–8)

> Damga: 2026-08-27T13:00:00Z · MODE=`ASSESS-ONLY` default · DEFENSE-ONLY

| Faz | Durum | İş | Kanıt / çıktı |
|-----|-------|-----|----------------|
| 0 BOOTSTRAP | [x] | rules/commands/skills/hooks/agents/plan + scanners | `.cursor/` · `scripts/secret_scan.py` |
| 1 CONTEXT | [x] | SECURITY_CONTEXT assets & trust boundaries | `SECURITY_CONTEXT/{inventory,assets,data-classes,trust-boundaries}.md` |
| 2 RESEARCH | [x] seed | Kaynaklı NIST pointer | `SECURITY_RESEARCH/nist-csf-2-pointer.md` |
| 3 ORG+EXPERTS | [x] seed+ | Roller (10) + EXPERTS/_SEED | `ORG/ROLES/ROLE-*.md` · `EXPERTS/_SEED.md` |
| 4 ENGINES | [x] refs+ | 20 skill + deep refs (sürekli genişleme) | `.cursor/skills/*/references/` |
| 5 MATRIX | [x] starter | matrix.md + 78 CTRL katalog | `SECURITY_MATRIX/matrix.md` · `LAYERS|FIREWALLS|ENCRYPTION|CHANGE|TRANSPARENT_CODE|CONDITIONAL/CTRL-*.md` |
| 6 COMPLIANCE | [ ] | NIST/ISO paket doldur | `COMPLIANCE/` |
| 7 QA+IR | [x] stub | IR playbook skeleton + QA rubric | skills/incident-response · `QA/` · security-qa |
| 8 ARCHIVE | [ ] | Aylık snapshot + CALENDAR | `ARCHIVE/{YYYY-MM}/security/` |

## FAZ 3 continuous (dürüst not)
Tek PR’da 20×20k karakter **yapılmadı / yapılmamalı**. Starter kataloglar + motor başına derin ref eklendi.
Sonraki **DEVAM**: FAZ 6 COMPLIANCE paket · ek kontrol derinliği · ARCHIVE iskeleti.
Üretici: `python3 scripts/giga_security_faz3_seed.py` (idempotent).

## Komut sırası
1. Paste `CURSOR-GIGA-MASTER-SECURITY.md` veya `/baslat-security`
2. Cursor restart / yeni Agent → skills yükle
3. `/gap-analizi` → `/kontrol-uret` → `/compliance-paket`
4. `/etik-denetim` her anlamlı turda
5. `/arsivle` ay sonunda
6. Kullanıcı **「DEVAM」** → sonraki boş FAZ (şimdi: 6)
