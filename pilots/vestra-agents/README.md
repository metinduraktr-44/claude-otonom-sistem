# Vestra Agents 🛒
**VESTRA e-ticaret markası için Claude Code bileşen paketi: rakip fiyat izleme, kampanya istihbaratı, haftalık rapor otomasyonu.**

> GELIR_MOTORU pilotu (K-001). Kanıt metriği: **haftalık izleme raporu otomasyonu**.
> Yapı `claude-code-templates` (aitmpl.com) ile uyumludur — bileşenler `.claude/` altına kopyalanınca çalışır.

## ⚡ Kurulum
```bash
# Seçenek A — projeye kopyala
cp -r components/agents/ecommerce .claude/agents/
cp -r components/skills .claude/skills/
cp components/hooks/audit/timestamp-audit.json .claude/hooks/

# Seçenek B — projeyi bu repoya bağla; Claude bileşenleri kendisi yükler.
```

## 🧩 İçerik
| Tip | Bileşen | Ne yapar |
|---|---|---|
| Agent | `rakip-fiyat-izleyici` | Rakip listesini okur; fiyat/stok/kampanya değişimini çıkarır; aksiyon önerir |
| Skill | `fiyat-izleme` | Kaynak listesi yönetimi, değişim tespiti, eşik uyarıları |
| Skill | `kampanya-analizi` | Rakip kampanya/indirim desenlerini çözer, cevap stratejisi kurar |
| Command | `/haftalik-fiyat-raporu` | Haftalık değişim tablosu + aksiyon listesi |
| Loop | `haftalik-izleme-loop` | 7 günlük döngü: izle → analiz → rapor → logla |
| Hook | `timestamp-audit` | Her düzenlemeye UTC damga → `AUDIT_LOG.jsonl` |
| MCP | `brightdata` | Rakip sayfa taraması için bağlayıcı şablonu |
| Setting | `vestra.json` | Güvenli varsayılanlar (en az yetki) |

## 🔁 Haftalık ritim
Loop her 7 günde bir koşar: rakip kaynakları tara → değişimleri damıt →
`/haftalik-fiyat-raporu` üret → aksiyonları `AUDIT_LOG.jsonl`'a yaz →
öğrenimi `BILGI_TABANI.md`'ye ekle. Rapor teslim edilmeden döngü kapanmaz.

## ⚖️ Hukuk & etik
Veri toplama yalnızca kamuya açık sayfalardan, `robots.txt` ve site kullanım
koşullarına uyarak yapılır; kişisel veri toplanmaz (KVKK).

## 🇹🇷 Sahip
Metin Durak · VESTRA · Lisans: MIT
