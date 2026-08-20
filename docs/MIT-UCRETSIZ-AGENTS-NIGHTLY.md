# MIT ÜCRETSİZ — Status Agents + Nightly
> Üretim: 2026-08-10 · Lisans kaynağı: `katalog/LICENSE-UPSTREAM` (MIT, davila7)

## Ne ücretsiz, ne ücretli?

| Katman | Ücret | Ne yapar |
|---|---|---|
| `katalog/` (8 kategori ajan/skill/mcp…) | **MIT / ücretsiz** | Vendored şablon kütüphanesi |
| `.claude/katalog-mit/` (kürasyon) | **MIT / ücretsiz** | `scripts/install_free_mit_agents.py` ile işe alınan çekirdek ajanlar |
| `.claude/agents/{DEPT}/` (holding rol kartları) | ücretsiz (repo içi) | `scripts/build_org_cards.py` |
| GitHub Actions: `nightly-improve`, `daily-agency`, `validate`, `upstream-sync` | Actions dakikası (public repo genelde ücretsiz kota) | Damga / validate / org döngüsü |
| LLM üretimi (makale, top-100 damıtma) | **ücretli kredi** | `OPENROUTER_API_KEY` veya `ANTHROPIC_API_KEY` |

🚩 "Tüm skill/MCP'leri canlı çalıştır" → çoğu tenant/credential ister. Eşdeğer: envanter + dry-run + Claude Code'da seçerek çağır (`docs/SKILL-AJANS-HIYERARSI.md`, `data/skill_envanteri.json`).

## Status Agents (ücretsiz çekirdek) kurulumu

```bash
python3 scripts/install_free_mit_agents.py
# çıktı: .claude/katalog-mit/** + data/mit_free_agents_manifest.json
```

Yeniden kurulum idempotenttir. Upstream delta için `upstream-sync.yml` yalnızca SHA kaydı tutar (oto-vendorlama yok — CILT kuralı).

## Nightly ücretsiz mod (Status Nightly)

`scripts/nightly.sh` davranışı:

1. `OPENROUTER_API_KEY` varsa → OpenRouter ile üretim
2. yoksa `ANTHROPIC_API_KEY` → Anthropic
3. **ikisi de yoksa** → generation skip; timestamp + `validate.py` + `BILGI_TABANI` satırı (**ücretsiz Status Nightly**)

Workflow secret'ları (repo Settings → Secrets):

- İsteğe bağlı: `OPENROUTER_API_KEY`, `OPENROUTER_MODEL`, `ANTHROPIC_API_KEY`
- Secret yokken nightly yine yeşil kalmalı (damga+validate).

## Claude Code / Cursor'a yapıştır

1. `.claude/system_prompt` — Claude Code system prompt
2. `.cursorrules` — Cursor kuralları
3. Tam mega blok: `docs/MEGA-PRONT-MASTER.md`
4. 6 domain MCP routing: `docs/CILT11-ENTERPRISE-MCP-ROUTING.md`

## Doğrulama

```bash
python3 scripts/install_free_mit_agents.py --dry-run
python3 scripts/validate.py
bash scripts/nightly.sh   # anahtar yokken ücretsiz mod
```
