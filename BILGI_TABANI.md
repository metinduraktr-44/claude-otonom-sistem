# BİLGİ TABANI (kümülatif hafıza — her gece büyür)
> Protokol: Her işlem [4] ÖĞREN adımında buraya "## [tarih] — [konu]" girişi ekler. En yeni en üstte.
> Çelişki kuralı: Yeni öğrenim eskisiyle çelişiyorsa ⚠️ ÇELİŞKİ etiketi + hangisinin geçerli olduğu yazılır.

## 2026-07-16 — Master doküman (Cilt 1-4) entegre edildi
- Cilt 3 (GitHub ekosistem haritası): kategori bazlı kanonik kaynaklar — anthropics/skills, claude-plugins-official/community, modelcontextprotocol/servers [RESMİ]; wshobson/agents, disler/claude-code-hooks-mastery, ruvnet/ruflo [topluluk]. Doğrulama: OpenSSF Scorecard, deps.dev, OSV.dev, Socket.dev, npm provenance.
- Cilt 4 (operasyon anayasası): 5 güvenlik kuralı (resmi-öncelik, script tedbiri 2.12x risk, güncellik yanılgısı yok, fork yasağı, marketplace-öncelik) + verimlilik çerçevesi (progressive disclosure, DELTA yazımı) — BÜTÜN repolara uygulanır.
- Akademik dayanak: arXiv 2601.10338 — 31.132 skill analizi, %26.1 zafiyetli; script'li bileşen 2.12 kat riskli (p<0.001).
- Gecelik döngü FAZ 1 artık Cilt 3 kanonik kaynak listesinden okur; her üretim 5 kurala vurulur.

## 2026-07-16 — Tam katalog içe alındı + 5 iş paketi üretildi
- davila7/claude-code-templates kataloğunun TAMAMI (434 agent, 341 command, ~50 skill kategorisi, 81 hook, 93 MCP, 70 setting, 18 loop, sandbox) katalog/ altına MIT atıflı kopyalandı; indeks: katalog/KATALOG_INDEKS.md.
- 5 paralel ÜRETİCİ ajanla bir turda: Response DGA tam seti (15 bileşen, adops-agents'a ek) + 4 pilot repo paketi (tahmin/vestra/kultur/movea-agents). Hepsi 6 katman denetimden GEÇTİ.
- Öğrenim: paralel ajan üretimi bileşen kütüphanesi ölçeklemesinin ana yöntemi; katalog ham kaynak, değer Türkçe/dikey yapılandırmada.
- Cowork proje bilgi tabanı limiti 2MB → 87MB katalog GitHub'da yaşar, projede indeksi durur (mimari kural).

## 2026-07-16 — v3 paket Cowork projesine kuruldu (hafıza taşındı)
- Eski v2 proje dosyaları (CLAUDE-OTONOM-SISTEM/...) kaldırıldı; yeni iki-repo yapısı (claude-otonom-sistem + adops-agents) proje dokümanı olarak yüklendi.
- v2 dönemi hafızası (BILGI_TABANI, KARAR_LOGU, AUDIT_LOG, GELIR_MOTORU) bu dosyalara birleştirildi — zincir kopmadı.
- ⚠️ ÇELİŞKİ: Eski kayıtlarda depo adı "metinduraktr-44/CLAUDE-OTONOM-S-STEM" idi. Geçerli olan: yeni depolar `metinduraktr-44/claude-otonom-sistem` (şemsiye) + `adops-agents` (dikey gelir). Eski ad tarihsel referanstır.
- Gecelik döngü (03:00 TSİ, FAZ 1-5) claude.ai zamanlanmış görev olarak kuruldu → K-004 durumu AKTİF.

## 2026-07-14 — Seed (GitHub'a taşıma)
- Sistem GitHub'a taşındı (metinduraktr-44/claude-otonom-sistem).
- Mimari: Cilt 1 (umbrella) + Cilt 2 (8 bileşen prompt kütüphanesi).
- Kardeş girişim: AdOps Agents (dikey gelir paketi).
- Denetim: 6 katman; damga: date -u; zincir: AUDIT → sonraki gecenin girdisi.

## 2026-07-14 — GitHub deposu açıldı + ağ kısıtı düzeltmesi (v2'den taşındı)
- ⚠️ ÇELİŞKİ (çözüldü): Önceki oturum "sandbox github.com'a erişemiyor" demişti. Cowork bulut ortamında `git clone` ÇALIŞTI. Geçerli olan: Cowork bulut ortamı github.com'a erişebilir; kısıt önceki oturumun ortamına özeldi.
- Push için kimlik doğrulama (PAT) veya kullanıcının yerel makinesi gerekiyor — sandbox'ta GitHub yazma yetkisi yok.
- CI/CD yolu açıldı: `.github/workflows/` ile main'e push → otomatik denetim (nightly-improve.yml + validate ile karşılandı).

## 2026-07-14 — Sistem kuruldu, v2 iskeleti (v2'den taşındı)
- Agent frontmatter'da <example>/<commentary> blokları proaktif tetiklemenin gerçek mekanizması.
- Bileşen kaydı Discovery fazında olur → yeni bileşen ekleyince Claude Code yeniden başlatılmalı.
- Hook olayları: PreToolUse / PostToolUse / Stop / SessionStart → zaman damgası + öğrenme zinciri bu dört olayla kurulur.
- Gelir motoru kararı: hedef iş = CLAUDE OTONOM SİSTEM'in kendisi (bileşen kütüphanesi ürünleştirme). Mevcut 5 iş (Tahmin Uzmanı, VESTRA, İBB Kültür AŞ, Movéa, Response DGA) pilot iç müşteri — dogfooding. Detay: GELIR_MOTORU.md.

<!-- SONRAKİ GİRİŞLER BURAYA — en yeni en üstte -->

## 2026-07-17T01:24:30Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

## 2026-07-18T01:16:36Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

## 2026-07-19T01:22:18Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

## 2026-07-20T01:28:29Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

## 2026-07-21T01:22:04Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

## 2026-07-22T01:20:38Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

## 2026-07-23T01:28:06Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

## 2026-07-24T01:24:37Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

## 2026-07-25T01:24:43Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

## 2026-07-26T01:28:05Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

## 2026-07-27T01:45:30Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

## 2026-07-28T01:19:49Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

## 2026-07-29T01:21:22Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-29T08:46:55Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-07-29-OPS-BIZ.md); K4 Cowork oturumu taslağı doldurur.
## 2026-07-30T01:14:53Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-30T08:33:58Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-07-30-OPS-TLS.md); K4 Cowork oturumu taslağı doldurur.
## 2026-07-31T01:28:18Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-07-31T08:55:26Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-07-31-FIN-FPA.md); K4 Cowork oturumu taslağı doldurur.
- [2026-07-31T09:45:22Z] haftalik-liderlik: iskelet üretildi (uretim/toplantilar/2026-07-31-haftalik-liderlik.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-01T01:29:35Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-01T08:10:51Z] aylik-kurul: iskelet üretildi (uretim/toplantilar/2026-08-01-aylik-kurul.md); K4 Cowork oturumu taslağı doldurur.
- [2026-08-01T08:26:38Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-01-FIN-ACC.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-02T01:27:19Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-02T08:29:23Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-02-FIN-REV.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-03T01:27:24Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-03T09:54:00Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-03-SEC-OPS.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-03T15:57:47Z — mega-pront & unvan hiyerarsisi
- CILT9 (UNVAN-HIYERARSISI) + MEGA-PRONT-MASTER uretildi. C->isci 7 kademe, top-100 insan-referans arastirma protokolu, aylik zaman-damgali arsiv (arastirma/{alan}/{unvan}/{YYYY-MM}), +100 yetenek matrisi, unvan-basi pront paketi politikasi. GitHub + Lovable (3 mod: Plan/Agent/Visual, Supabase, GitHub sync) + tum tools uyarlamasi. Imkansiz boyutlar (900B/900M karakter, tek-tur top-100) anayasa CILT1 §0 kirmizi bayragiyla isaretlendi; yerine kumulatif rotasyonlu dongu. Claude Code orkestrasyonu: subagent<agent-team</batch, CLAUDE.md ortak sozlesme.

## 2026-08-04T08:36:39Z — holding + cok-ulke + app mimarisi (CILT10)
- CILT10 + UNVAN-KARTI-SABLONU uretildi. Katmanli yapi: app(iOS/Android/Web) -> holding -> istirak -> C->isci org -> ulke kopyasi. AdOps 20 departman taksonomisi + EVP rol-karti semasi + 501 soru bankasi entegre. Kisisel+grup workflow (egitim/to-do/roadmap/toplanti/ust-yan-alt iletisim). Gecelik top-5 arastirma (org x ulke x unvan) zaman-damgali arsiv + aylik tazeleme. Kirmizi bayrak: 900 katrilyon karakter imkansiz; ajan hesap/API-key/secret ACAMAZ (kullanici Secrets panelinden ekler); claude.ai/cowork linkleri erisilemez.

## 2026-08-04T08:48:54Z — mega-pront UYGULAMA (seed)
- Yapistir iptal, pront uygulandi: scripts/build_org_cards.py yazildi -> .claude/org/org.json (46 departman) -> .claude/agents/{KOD}/{kod}-lead.md 46 gercek rol karti. arastirma/ iskele: gercek TR ulke profili (pazar 3.26B USD, 1 Agu 2026 reklam yonetmeligi, KVKK) + MKT-PRF top-5 (Nick Shackelford/Clutch/Meta Advantage+/TikTok Smart+, kaynakli+zaman-damgali). uretim/workflows kisisel+grup (MKT-PRF). app/ blueprint (Supabase+RN, gerekli secretler kullanici tarafindan). validate.py GECTI.

## 2026-08-04T08:55:14Z — 532 soru bankasi + karta gomme
- build_question_bank.py -> data/soru_bankasi.json + docs/OZ-DENETIM-SORU-BANKASI.md (532: evrensel 119 + departman 386 + kademe 27). build_org_cards.py her rol kartina departman+kademe alt-seti gomer + tam bankaya referans. Reddedilen: 900B karakter (imkansiz), top-100 uydurma (veri butunlugu). Merge: ajan yapamaz (gh read-only).

- [2026-08-04T09:40:02Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-04-SEC-AUD.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-04T09:40:02Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.
