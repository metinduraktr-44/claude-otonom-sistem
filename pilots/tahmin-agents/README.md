# Tahmin Agents 🎯
**Tahmin/analitik dikeyi için Claude Code bileşen paketi — prompt v-serisi iyileştirme odaklı.**

Metin Durak'ın "Tahmin Uzmanı" ürününün motoru: mevcut tahmin prompt'larını (v1, v2, ...) okuyan,
zayıflıkları teşhis eden ve ölçülebilir kalite artışıyla bir sonraki versiyonu üreten ajan seti.
GELIR_MOTORU pilotu · Kanıt metriği: **v-serisi kalite artışı + kullanım sayısı**.

> Yapı `claude-code-templates` (aitmpl.com) ile uyumludur; bileşenler `.claude/` altına drop-in kopyalanır.

## ⚡ Kurulum
```bash
# Seçenek A — bileşenleri projene kopyala
cp -r components/agents/prompt-engineering .claude/agents/
cp components/hooks/audit/timestamp-audit.json .claude/hooks/

# Seçenek B — repoyu Claude Code / Cowork projesine bağla; CLAUDE.md orkestratörü devralır.
```

## 🧩 İçerik
| Tip | Bileşen | Ne yapar |
|---|---|---|
| Agent | `v-serisi-iyilestirici` | v-N prompt'u okur, zayıflık teşhis eder, v-N+1 üretir, öncesi/sonrası tablosu verir |
| Skill | `tahmin-kalite-olcumu` | Tahmin çıktısını 4 eksende puanlar: kalibrasyon, gerekçe, veri dayanağı, tutarlılık |
| Command | `/v-serisi-rapor` | Versiyonlar arası kalite trendi raporu (AUDIT_LOG + rubrik skorlarından) |
| Loop | `kalite-serisi-loop` | İyileştir→değerlendir döngüsü; N ardışık GEÇTİ olana kadar durmaz |
| Hook | `timestamp-audit` | Her Edit/Write'a UTC damga basar, AUDIT_LOG.jsonl'a satır ekler |
| Setting | `tahmin-uzmani` | Güvenli varsayılanlar: minimal izin, tehlikeli komutlar deny |
| MCP | `arxiv` | Tahmin/kalibrasyon metodolojisi literatür taraması (arXiv) |

## 🔍 Denetim protokolü
Her üretim 6 katmanlı kuyruktan geçer (structural / integrity-SHA256 / semantic / reference /
patterns / review) + gerçek `date -u` damgası → `AUDIT_LOG.jsonl`. Öğrenimler `BILGI_TABANI.md`'de
birikir; bir sonraki çalışma onları girdi alır (zincir).

## 💰 Gelir bağlantısı
Katman 1 (bu paket) → 3 bileşen GEÇTİ sonrası Katman 2 (`--create-agent` ile müşteriye kurulan
global ajan) → Katman 3 (kurulum + danışmanlık). Ayrıntı: proje `GELIR_MOTORU.md`.

Lisans: MIT · Sahip: Metin Durak
