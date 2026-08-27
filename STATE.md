# STATE — Holding + Security OS

> Tek kaynak: oturum durumu. Her `/sec-devam` veya agency `/devam` öncesi ilgili bölümü oku, sonra güncelle.

## Holding (mevcut)
- **runtime:** Python 3 stdlib + Bash + GHA
- **validate:** `python3 scripts/validate.py`

---

## Security OS

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

### Faz
- **phase:** `0` (Bootstrap + ingestion)
- **MODE:** `ASSESS-ONLY` (varsayılan — gap/doküman; agresif kod değişikliği yok)
- **last_command:** `sec-baslat` / bootstrap
- **last_updated_utc:** 2026-08-27T12:37:54Z

### Guardrails
- defense-only · secret-redakte · exploit-yok · tehlikeli shell yok
- Faz başı/sonu damgası zorunlu

### Ingestion özeti (Faz 0)
- **inventory:** `SECURITY_CONTEXT/inventory.md`
- **attack-surface:** `SECURITY_CONTEXT/attack-surface.md` (savunma perspektifi)
- **secrets found:** konum+tip only — değer yok (bkz. inventory)
- **holding çapraz:** `docs/SECRETS-DRYRUN-MATRISI.md`, `infra/`, workflows

### Aktif iş
- **assessment_id:** —
- **control_batch:** —
- **compliance_pack:** —

### Sonraki adım
1. Cursor yeniden başlat (rules/skills/hooks keşfi)
2. Hybrid: skill yüklenmezse inline Bölüm 7–11 / skill SKILL.md
3. Yeni Agent chat → `/sec-devam` (Faz 1 Research)
4. Canva MCP dokunulmadı — security MCP örnek (`mcp.security.example.json`) varsayılan kapalı

### Creative Agency notu
Agency GIGA track ayrı branch’te yaşar. Merge sırasında `STATE.md` agency bölümü additive birleşsin; Security OS bölümü silinmesin.
