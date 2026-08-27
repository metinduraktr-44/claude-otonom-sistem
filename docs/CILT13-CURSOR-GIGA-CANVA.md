# CILT13 — Cursor GIGA Creative Agency OS (Canva Dual-Mode)

> Damga: 2026-08-27T00:24:00Z · Holding ek katmanı (`.claude/` bozulmaz)

## 🚩 Kırmızı bayrak
**≥900B / ≥900M karakter tek pront = RED.** Çalışan eşdeğer = fazlı çok-dosya OS + yapıştırma artifact.

## Ne
Cursor Agent için **Otonom AI Creative Agency OS**: brief→matrix→(opsiyonel Canva)→QA→arşiv.
Varsayılan: **`CANVA:BRIEF-ONLY`**. Canlı: kullanıcı `CANVA:ON` + MCP OAuth.

## Pointers
| Artefakt | Yol |
|----------|-----|
| Yapıştırma (Cursor Agent) | `uretim/devir/CURSOR-GIGA-MASTER-CANVA.md` |
| Plan | `.cursor/plans/master-plan.md` |
| Rules | `.cursor/rules/00-agency-core.mdc` … `40-canva-ops.mdc` |
| Commands | `.cursor/commands/{baslat,devam,…}.md` |
| Skills | `.cursor/skills/*/SKILL.md` |
| Critics | `.cursor/agents/critic-*.md` |
| MCP | `.cursor/mcp.json` → `https://mcp.canva.com/mcp` |
| Hooks | `.cursor/hooks.json` + `scripts/spec_validate.py` |
| Client scaffold | `tools/canva-client/` |
| İş listesi | `docs/IS-LISTESI-GIGA-CANVA.md` |
| STATE | `STATE.md` |

## OAuth
Cursor Settings → MCP → Canva → Authorize. Credential yoksa canlı üretim iddia etme.

## Çalıştır
```bash
python3 scripts/validate.py
python3 scripts/spec_validate.py --help
python3 scripts/spec_validate.py --self-test
```

## Holding bağ
Mevcut MEGA/CILT1–12 + `scripts/daily_agency.py` aynı kalır. Bu Cilt = creative üretim katmanı.
