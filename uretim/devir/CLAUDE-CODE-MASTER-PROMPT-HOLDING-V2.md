# CLAUDE CODE MASTER PROMPT — HOLDING V2 (yapıştır)

> Üretim: 2026-08-14T04:03:10Z · Repo: claude-otonom-sistem · Dal: cursor/mcp-ajans-etki-arsivi-8e8f
> Cursor Cloud üretti → Claude Code'a **tek parça** yapıştır.

## 🚩 ZORUNLU RED
Her prompt ≥900.000.000 / ≥900.000.000.000 / ≥9e17 karakter **RED**.
**Uygula:** 122 prompt/title · 4–12 KiB · referans zinciri · dry-run.

## FAZ 0 — Senkron
```bash
cd "$(git rev-parse --show-toplevel)"
git fetch origin && git status -sb
python3 scripts/mcp_ajans_etki_uret.py --dogrula
python3 scripts/skill_ajans_uretim.py --dogrula
python3 scripts/holding_istirak_ajans_uret.py --dogrula
```

## FAZ 1 — Oku (zincir 🔗)
1. BILGI_TABANI.md (en yeni)
2. docs/HOLDING-ISTIRAK-ORG.md · data/holding_istirak_org.json
3. docs/OZ-DENETIM-SORU-BANKASI.md · data/soru_bankasi.json
4. docs/ULKE-PAZAR-ISKELETI.md · data/ulke_pazar_iskeleti.json
5. docs/SECRETS-DRYRUN-MATRISI.md · .env.example
6. docs/LLM-AI-AJANS-ETKI-MOTORU.md · docs/SKILL-AJANS-HIYERARSI.md
7. uretim/OZET-TEK-SAYFA.md · uretim/rol-kartlari/

## FAZ 2 — Doğrula
- iştirak ≥ 7 (şu an 8)
- rol ≥ 100 (şu an 633)
- soru bankası ≥ 501 (şu an 957)
- ülke ≥ 8 (şu an 10)
- hiçbir 900M+ karakter dosya yok

## FAZ 3 — Uygula (kredi-min)
1. `python3 scripts/holding_istirak_ajans_uret.py --hepsi`
2. İsteğe bağlı: `--pilot-limit N` ile daha fazla rol kartı
3. Credential yoksa dry-run matrisi doldur; hesap açma zorunlu değil
4. Ülke nightly: `uretim/ulke-arsiv/TR/` örnek not + zaman damgası
5. Cowork URL bekleme — repo döngüsü yeterli

## FAZ 4 — 5 güvenlik kuralı
Resmi kaynak · script tedbiri · güncellik yanılgısı yok · fork yasağı · marketplace öncelik

## FAZ 5 — Damga
BILGI_TABANI tek satır · AUDIT_LOG · commit/push · PR #13 güncelle

## FAZ 6 — Rapor
Türkçe kısa tablo: iştirak/rol/soru/ülke + 🚩 + sonraki 3 aksiyon

## Çıktı sözleşmesi
⏱️ Damga · 🔍 Denetim · 📚 Öğrenim · 🔗 Önceki

---
Metin: Bu prompt Cursor'dan. FAZ 0→6 uygula; 900B üretme; secrets commit etme.
