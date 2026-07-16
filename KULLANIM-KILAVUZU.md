# KULLANIM KILAVUZU — GÜNLÜK OPERASYON (tek sayfa)
> Soru: "Bileşenler çalışıyor mu, burayı en verimli nasıl kullanırım?" — cevabın kalıcı hâli.
> Damga: 2026-07-16 · Kanıt: gecelik döngü test turu GEÇTİ (AUDIT_LOG: gecelik_dongu_TEST)

## 1. NE NEREDE ÇALIŞIR
| Bileşen | Cowork (claude.ai projesi) | Claude Code (bilgisayarında CLI) |
|---|---|---|
| Beceriler | ✅ Emülasyon: dokümanı okur, yordamı uygularım | ✅ Otomatik tetiklenir (`.claude/skills/`) |
| Ajanlar | ✅ Emülasyon: adıyla çağır, o rolü yüklerim | ✅ Gerçek alt-ajan (`.claude/agents/`) |
| Komutlar | ✅ Emülasyon: `/komut parametre` yaz, aynen uygularım | ✅ Gerçek slash komutu (`.claude/commands/`) |
| Ayarlar/Kancalar | ❌ (Claude Code'a özel) | ✅ settings.json + hooks (damga kancası dahil) |
| MCP'ler | ✅ Bağlı konektörler (Supermetrics, HubSpot, Shopify...) | ✅ .mcp.json |
| Döngüler | ✅ KANITLI — gecelik görev her gece 03:00 TSİ | ✅ Routines |
| Eklentiler | — (manifest, referans) | ✅ `/plugin marketplace add` |

## 2. GÜNLÜK ÇAĞRI KALIPLARI (Cowork'te kopyala-yapıştır)
| İş | Çağrı örneği |
|---|---|
| Response DGA | `/pitch-brifi — [müşteri], [sektör]` · `rakip-analisti: [rakip ajans/marka]` · `atif-analisti: [kampanya verisi]` · `/linkedin-yayinci [konu]` |
| VESTRA | İlk kez: `fiyat izleme kur: [rakip URL listesi]` → sonra `/haftalik-fiyat-raporu` |
| Movéa | Önce bir kez: `TON_REHBERI'ni dolduralım` → sonra `/icerik-takvimi bu hafta` · `marka-icerik-ajani: [tema]` |
| İBB Kültür AŞ | `/haftalik-tarama-raporu` · `etkinlik-tarayici: [kıyas kurum]` |
| Tahmin Uzmanı | `v-serisi-iyilestirici: [mevcut prompt]` · `/v-serisi-rapor` |

Kural: **Bileşeni ADIYLA çağır + parametre ver.** "Bana bir şeyler yaz" değil, "/pitch-brifi — X Bankası, finans" — tetikleme %80 burada.

## 3. CLAUDE CODE'DA GERÇEK OTOMASYON (bir kez, 5 dk)
```
git clone https://github.com/metinduraktr-44/adops-agents.git
cd adops-agents
mkdir -p .claude && cp -r components/agents components/commands components/skills .claude/
claude          # (kurulu değilse: npm install -g @anthropic-ai/claude-code)
```
Doğrulama: `/` yaz → pitch-brifi görünmeli; `/agents` → pitch-deck-uretici listelenmeli.
Not: kopyalama ≠ başlatma; bileşen ekledikten sonra Claude Code'u yeniden başlat (Discovery).

## 4. RİTİM — SENİN PAYINA DÜŞEN
- **Her sabah 2 dk:** Cowork'e "dün gece ne oldu?" yaz → AUDIT son satırı GEÇTİ mi + `uretim/` yeni dosya var mı raporlarım.
- **Haftalık üretim otomatik:** Pzt skill · Sal agent · Çar MCP · Per pilot deliverable · Cum konsolidasyon — gecelik döngü v2 uyguluyor.
- **Cuma:** Haftanın deliverable'ını GERÇEK işte kullan (pitch'e koy, rapora çevir, müşteriye gönder) → kanıt metriğini söyle, KARAR_LOGU'na işlerim. Darboğaz üretim değil, sahada kullanım (K-001, 90 günde ilk ödeme hedefi).

## 5. VERİM KURALLARI (Cilt 4 özeti)
1. Adıyla çağır + parametre ver — genel istek yerine bileşen adı.
2. DELTA iste: "sadece değişeni yaz" — tekrar üretim token yakar.
3. Aynı analizi iki kez isteme; "BILGI_TABANI'nda var mı, bak" de.
4. Kullanmadığın bileşeni söyle → arşivlerim (sadeleşme = hız).
5. Yeni bileşen ihtiyacında: "X için bileşen üret" — Cilt 3 birincil kaynağından, 5 güvenlik kuralıyla üretirim.
