# Kültür Agents 🎭
**Kültür-etkinlik kurumları için Claude Code bileşen paketi.**
İstanbul/TR sahne odağı — konser salonları, festivaller, kültür merkezleri, biletleme.

Pilot müşteri: **İBB Kültür AŞ**. Kanıt metriği: **haftalık tarama teslimi** (etkinlik/kıyas-kurum tarama raporu, her Cuma).

> Yapı `claude-code-templates` (aitmpl.com) ile uyumludur. Bileşenleri projenin `.claude/` klasörüne kopyala, çalışır.

## ⚡ Hızlı başlangıç
```bash
cp -r components/agents/culture-events .claude/agents/
cp -r components/skills/research/etkinlik-tarama .claude/skills/
cp components/commands/reporting/haftalik-tarama-raporu.md .claude/commands/
```

## 🧩 İçerik
| Tip | Bileşen | Ne yapar |
|---|---|---|
| Agent | `etkinlik-tarayici` | Benzer kurumların program/bilet/format hamlelerini tarar; fırsat-tehdit çıkarır (ANA PİLOT) |
| Agent | `kitle-trend-analisti` | Kültür tüketim trendleri: genç kitle, format, fiyatlama |
| Skill | `etkinlik-tarama` | Haftalık tarama yordamı: kaynak listesi, sinyal çıkarma, kıyas tablosu |
| Command | `/haftalik-tarama-raporu` | Haftalık teslim formatı: 5 sinyal + kıyas tablosu + 3 öneri |
| Loop | `haftalik-tarama-loop` | 7 günlük döngü: tara → damıt → raporla → damgala |
| Hook | `timestamp-audit` | Her düzenlemeye UTC damga → `AUDIT_LOG.jsonl` |
| Setting | `kultur-as` | Kamu kurumu için güvenli varsayılanlar (en az yetki) |

## 🔍 Denetim & damga
Her üretim CLAUDE.md'deki DENETİM KUYRUĞU'ndan geçer; her işlem `AUDIT_LOG.jsonl`'a
damgalanır, öğrenimler `BILGI_TABANI.md`'de birikir (model değişmez, bilgi tabanı büyür).

## Lisans
MIT · Yazar: Metin Durak
