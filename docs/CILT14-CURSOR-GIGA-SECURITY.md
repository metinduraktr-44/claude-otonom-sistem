# CILT14 — Cursor GIGA Security Architecture & Governance OS

> Damga: 2026-08-27T12:40:00Z · Holding ek katmanı (`.claude/` + CILT13 Canva bozulmaz)

## 🚩 Ethics & boyut
- **DEFENSE-ONLY.** Exploit / phishing / malware / C2 / ransomware / bypass howto / weaponized PoC = refuse.
- ATT&CK yalnızca **detection / D3FEND** eşlemesi.
- **≥900B tek pront = RED.** Hybrid: kısa `SKILL.md` + `references/` stub; full ~20k/skill = **FAZ 3 continuous expansion** (bu PR kaliteli iskelet + deep sample).
- Secrets: `${VAR}` · `vault://` · `op://` · `<REDACTED>` only.

## Default mode
**`MODE=ASSESS-ONLY`**. IMPLEMENT yalnızca açık kapsam.

## Hybrid skill / inline
| Katman | Ne |
|--------|-----|
| Inline rules | `.cursor/rules/00-security-core.mdc` … `05-ethics` … `31-security-file-structure` (alwaysApply, kısa) |
| Agent Requested | `40-secops.mdc` + 20 security skills |
| Paste prompt | `uretim/devir/CURSOR-GIGA-MASTER-SECURITY.md` |
| Deep refs | skill `references/` — 1–2 örnek/engine; TODO stub geri kalan |

Creative `expert-engine` korundu; güvenlik ikizi: `security-expert-engine`.

## Pointers
| Artefakt | Yol |
|----------|-----|
| Yapıştırma (BAŞLAT) | `uretim/devir/CURSOR-GIGA-MASTER-SECURITY.md` |
| Plan | `.cursor/plans/security-master-plan.md` |
| Rules | `.cursor/rules/00-security-core.mdc` … |
| Commands | `/baslat-security` `/kontrol-uret` `/gap-analizi` `/compliance-paket` `/etik-denetim` |
| Skills | `.cursor/skills/{layers-engine,…}/` |
| Agents | `security-reviewer` · `compliance-auditor` · `ethics-checker` |
| Hooks | `.cursor/hooks.json` + `scripts/secret_scan.py` + `ethics_check.py` |
| MCP stubs (OFF) | `.cursor/mcp.security.stubs.example.json` |
| Scanners | `tools/security-scanners/` |
| State | `SECURITY/STATE.md` (+ kök `STATE.md` creative) |
| İş listesi | `docs/IS-LISTESI-GIGA-SECURITY.md` |
| Sibling Canva | `docs/CILT13-CURSOR-GIGA-CANVA.md` |

## Çalıştır
```bash
python3 scripts/validate.py
python3 scripts/secret_scan.py --self-test
python3 scripts/ethics_check.py --self-test
python3 scripts/spec_validate.py --self-test
```

Canlı Semgrep/Snyk iddia etme — credential + kullanıcı enable gerekir.

## Holding bağ
MEGA/CILT1–13 + daily_agency aynı. Cilt14 = güvenlik governance katmanı.
