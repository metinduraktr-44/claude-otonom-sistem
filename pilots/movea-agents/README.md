# Movéa Agents

**Movéa markası için Claude Code marka-içerik bileşen paketi.**
Amaç: marka sesine sadık, haftalık ritimde içerik üretimi. Kanıt metriği: **içerik/hafta**.
(GELIR_MOTORU pilotu · CLAUDE OTONOM SİSTEM · yapı `claude-code-templates` uyumlu — bileşenler `.claude/` altına kopyalanabilir.)

## Hızlı başlangıç
```bash
# Bileşenleri projene kopyala
cp -r components/agents/brand-content .claude/agents/
cp -r components/skills/content .claude/skills/
cp -r components/commands/content .claude/commands/
cp components/hooks/audit/timestamp-audit.json .claude/hooks/
```

## Bileşenler
| Tip | Bileşen | Ne yapar |
|---|---|---|
| Agent | `marka-icerik-ajani` | Haftalık içerik seti üretir (post + görsel brief + CTA) + metrik raporu |
| Skill | `sosyal-icerik` | Instagram/LinkedIn/X format farkları, TR kitle notları |
| Skill | `marka-metin-yazimi` | Marka sesi + metin yazımı (ton rehberi şablonu dahil) |
| Command | `/icerik-takvimi` | Haftalık takvim: gün × platform × tema tablosu |
| Command | `/linkedin-yayinci` | İçeriği LinkedIn formatına çevirir (hook-önce, link yoruma) |
| Loop | `haftalik-icerik-loop` | 7 günlük üretim döngüsü; durma: takvim dolu + denetim GEÇTİ |
| Hook | `timestamp-audit` | Her Edit/Write'a UTC damga → `AUDIT_LOG.jsonl` |
| Setting | `movea.json` | Güvenli varsayılanlar (en az yetki) |

## Haftalık akış
`/icerik-takvimi` → `marka-icerik-ajani` hücreleri doldurur → `/linkedin-yayinci` ile platform çıktısı →
denetim (6 katman) → damga → metrik satırı (`içerik/hafta`). Öğrenimler `BILGI_TABANI.md`'de birikir.

## Notlar
- Marka sesi kaynağı: `TON_REHBERI.md` (yoksa `marka-metin-yazimi` skill'indeki şablon doldurulur).
- Sır/anahtar dosyaya gömülmez; yayınlama manuel kopyala-yapıştır (güvenli varsayılan).

Sahip: Metin Durak · Lisans: MIT
