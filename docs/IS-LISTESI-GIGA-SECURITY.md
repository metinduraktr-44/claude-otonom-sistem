# İŞ LİSTESİ — GIGA Security OS (FAZ 0–8)

> Damga: 2026-11-03T11:50:00Z · MODE=`ASSESS-ONLY` default · DEFENSE-ONLY

| Faz | Durum | İş | Kanıt / çıktı |
|-----|-------|-----|----------------|
| 0 BOOTSTRAP | [x] | rules/commands/skills/hooks/agents/plan + scanners | `.cursor/` · `scripts/secret_scan.py` |
| 1 CONTEXT | [x] | SECURITY_CONTEXT assets & trust boundaries | `SECURITY_CONTEXT/{inventory,assets,data-classes,trust-boundaries}.md` |
| 2 RESEARCH | [x] seed | Kaynaklı NIST pointer | `SECURITY_RESEARCH/nist-csf-2-pointer.md` |
| 3 ORG+EXPERTS | [x] seed+ | Roller (10) + EXPERTS/_SEED | `ORG/ROLES/ROLE-*.md` · `EXPERTS/_SEED.md` |
| 4 ENGINES | [x] refs+ | 20 skill + deep refs (sürekli genişleme) | `.cursor/skills/*/references/` |
| 5 MATRIX | [x] starter | matrix.md 120 satır + katalog CTRL | `SECURITY_MATRIX/{matrix,coverage}.md` |
| 6 COMPLIANCE | [x] iskelet | ISO 27001:2022 SoA (93) ASSESS-ONLY | `COMPLIANCE/ISO27001-2022-SOA.md` · pack · gap-evidence |
| 7 QA+IR | [x] stub | IR playbook skeleton + QA rubric | skills/incident-response · `QA/` · security-qa |
| 8 ARCHIVE | [x] stub | 2026-11 pointer snapshot + takvim | `ARCHIVE/2026-11/security/MANIFEST.md` · `CALENDAR/SECURITY_ARCHIVE.md` |

## FAZ 6 dürüst not
SoA = uygulanabilirlik tablosu; **ISO sertifikası yok**. NIST/CIS/SOC2 pack **yapılmadı**. Katalog 600 değil (**89** `CTRL-*.md` = 88 numbered + SAMPLE). Matris 120 kavramsal satır duruyor.
Sonraki **DEVAM**: LATOS FAZ4 iş kartı batch **veya** katalog 021+ **veya** NIST pack.
Üretici: `python3 scripts/giga_security_faz6_soa.py` (idempotent). FAZ3 seed matrix crosswalk’ı ezmez.

## Komut sırası
1. Paste `CURSOR-GIGA-MASTER-SECURITY.md` veya `/baslat-security`
2. Cursor restart / yeni Agent → skills yükle
3. `/gap-analizi` → `/kontrol-uret` → `/compliance-paket`
4. `/etik-denetim` her anlamlı turda
5. `/arsivle` ay sonunda
6. Kullanıcı **「DEVAM」** → Security COMPLIANCE derinliği (NIST pack) veya LATOS FAZ4 kart; merge-all değil.
