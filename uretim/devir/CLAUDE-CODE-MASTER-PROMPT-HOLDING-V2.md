# HOLDING V2 MASTER — UYGULAMA PROTOKOLÜ (Cursor ajan çalıştırır)

> Üretim/uygulama: 2026-08-04T08:44:30Z · Repo: claude-otonom-sistem · Dal: cursor/mcp-ajans-etki-arsivi-8e8f
> **Claude Code'a yapıştırma İPTAL.** Aynı protokolü Cursor Cloud ajanı uygular ve push eder.

## 🚩 ZORUNLU RED
≥900.000.000 / ≥900.000.000.000 / ≥9e17 karakter prompt **RED**.
**Uygula:** 122 prompt/title · 4–12 KiB · referans zinciri · dry-run.

## FAZ DURUMU (2026-08-04T08:44:30Z)
| Faz | Durum |
|---|---|
| 0 Senkron/doğrula | GEÇTİ (mcp+skill+holding) |
| 1 Zincir oku | GEÇTİ |
| 2 Eşik kontrol | GEÇTİ (8/633/957/10; 900M+=0) |
| 3 Uygula | GEÇTİ (kart=120, 10 ülke arşiv, dry-run, IS_LISTESI, transfer paket) |
| 4 5 güvenlik kuralı | GEÇTİ (secret commit yok; resmi kaynak öncelik) |
| 5 Damga+push+PR | BU KOŞUM |
| 6 Rapor | BU KOŞUM |

## Komutlar (yeniden koşum)
```bash
python3 scripts/mcp_ajans_etki_uret.py --dogrula
python3 scripts/skill_ajans_uretim.py --dogrula
python3 scripts/holding_istirak_ajans_uret.py --hepsi --pilot-limit 120
python3 scripts/holding_istirak_ajans_uret.py --dogrula
```

## Artefaktlar
- `IS_LISTESI.md` · `uretim/OZET-TEK-SAYFA.md`
- `uretim/rol-kartlari/` (120) · `uretim/ulke-arsiv/*/YYYY-MM-DD.md`
- `uretim/dry-run/` · `uretim/devir/istirak/*-TRANSFER.md`
- `docs/SECRETS-DRYRUN-MATRISI.md`

## Cross-repo
`adops-agents` ve diğer iştiraklere bu entegrasyonun **push yetkisi yok**.
Transfer paketleri HQ’da; yazma yetkisi gelince uygula.

## Çıktı sözleşmesi
⏱️ Damga · 🔍 Denetim · 📚 Öğrenim · 🔗 Önceki
