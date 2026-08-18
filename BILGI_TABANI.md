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
## 2026-08-04T09:41:05Z — skill ajans envanteri
- skills=696; domains=50; titles=216; pilot_prompts=2440; ekipler=50
- 🚩 900B karakter RED; Claude Code MASTER üretilidi.

## 2026-08-04T09:41:04Z — MCP×etki×prompt motoru
- MCP=174; tech=141; cult=116; org_roles=104; prompts_index=12688
- 🚩 900M karakter/prompt reddedildi (K-017 emsali); 122×(4–12KiB) sözleşme.

## 2026-08-04T09:41:04Z — skill ajans envanteri
- skills=696; domains=50; titles=216; pilot_prompts=2440; ekipler=50
- 🚩 900B karakter RED; Claude Code MASTER üretilidi.

## 2026-08-04T09:41:03Z — MCP×etki×prompt motoru
- MCP=174; tech=141; cult=116; org_roles=104; prompts_index=12688
- 🚩 900M karakter/prompt reddedildi (K-017 emsali); 122×(4–12KiB) sözleşme.

## 2026-08-04T09:40:00Z — skill ajans envanteri
- skills=696; domains=50; titles=216; pilot_prompts=2440; ekipler=50
- 🚩 900B karakter RED; Claude Code MASTER üretilidi.

## 2026-08-04T09:40:00Z — MCP×etki×prompt motoru
- MCP=174; tech=141; cult=116; org_roles=104; prompts_index=12688
- 🚩 900M karakter/prompt reddedildi (K-017 emsali); 122×(4–12KiB) sözleşme.

## 2026-08-04T08:44:49Z — skill ajans envanteri
- skills=696; domains=50; titles=216; pilot_prompts=2440; ekipler=50
- 🚩 900B karakter RED; Claude Code MASTER üretilidi.

## 2026-08-04T08:44:48Z — MCP×etki×prompt motoru
- MCP=174; tech=141; cult=116; org_roles=104; prompts_index=12688
- 🚩 900M karakter/prompt reddedildi (K-017 emsali); 122×(4–12KiB) sözleşme.

## 2026-08-04T08:43:07Z — skill ajans envanteri
- skills=696; domains=50; titles=216; pilot_prompts=2440; ekipler=50
- 🚩 900B karakter RED; Claude Code MASTER üretilidi.

## 2026-08-04T08:43:07Z — MCP×etki×prompt motoru
- MCP=174; tech=141; cult=116; org_roles=104; prompts_index=12688
- 🚩 900M karakter/prompt reddedildi (K-017 emsali); 122×(4–12KiB) sözleşme.

## 2026-08-03T16:03:13Z — skill ajans envanteri
- skills=696; domains=50; titles=216; pilot_prompts=2440; ekipler=50
- 🚩 900B karakter RED; Claude Code MASTER üretilidi.

## 2026-08-03T15:49:56Z — MCP×etki×prompt motoru
- MCP=174; tech=141; cult=116; org_roles=104; prompts_index=12688
- 🚩 900M karakter/prompt reddedildi (K-017 emsali); 122×(4–12KiB) sözleşme.


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
- [2026-08-04T08:39:12Z] holding-istirak: 8 birim · 633 rol · 957 soru · 10 ülke · 48 rol kartı · SECRETS dry-run · CLAUDE-CODE MASTER V2 · 🚩900B RED
- [2026-08-04T08:44:48Z] MASTER-V2 UYGULANDI (Claude Code iptal): FAZ0-6 · kart=120 · 10 ülke arşiv · dry-run · IS_LISTESI · 7 transfer paket · adops push yetkisi yok → paket HQ
## 2026-08-04T01:17:34Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-04T08:44:35Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-04-SEC-AUD.md); K4 Cowork oturumu taslağı doldurur.
- [2026-08-04T08:50:51Z] title+500 soru (316500 indeks) · top100/domain (uydurma yok, pending slot) · 🚩900B RED · main merge conflict çözüldü · merge onaylı
- [2026-08-04T08:52:35Z] PR #13 MERGED squash · 500 soru/title · top100 · 🚩900B RED · kisi uydurma yok

- [2026-08-04T09:40:08Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-04-SEC-AUD.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-04T09:40:09Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-04T09:41:04Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-04-SEC-AUD.md); K4 Cowork oturumu taslağı doldurur.
### 2026-08-04T09:41:04Z — LIVE TERMINAL
- `scripts/live_dashboard.sh` + tmux `holding-live` (60s)
- Tüm metrikler terminalde; watch döngüsü aktif

- [2026-08-04T09:41:05Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-04-SEC-AUD.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-05T01:21:16Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-05T08:42:10Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-05-SEC-SUP.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-06T01:18:32Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-06T08:43:53Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-06-HRA-REC.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-07T01:59:44Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-07T07:22:06Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-07-HRA-PRF.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-08T00:42:39Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-08T06:59:30Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-08-HRA-LRN.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-09T00:44:58Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-09T07:02:14Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-09-LGL-LIC.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-10T00:47:04Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-10T07:48:41Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-10-LGL-PRV.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-11T00:46:47Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-11T07:14:03Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-11-INF-MCP.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-12T00:54:28Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-12T07:38:48Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-12-INF-SET.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-13T00:55:50Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-13T07:40:01Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-13-INF-HKS.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-14T00:55:33Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-14T07:37:46Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-14-INF-LOP.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-15T00:31:46Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-15T06:44:09Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-15-STR-INT.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-16T00:32:46Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-16T06:45:48Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-16-STR-CMP.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-17T00:31:35Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-17T07:02:42Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-17-STR-GRW.md); K4 Cowork oturumu taslağı doldurur.
## 2026-08-18T00:31:04Z — nightly run
- Ran read->distill->produce->validate->stamp. Generation: off.

- [2026-08-18T06:50:01Z] daily-agency: iskelet üretildi (uretim/gunluk/2026-08-18-ENG-PLT.md); K4 Cowork oturumu taslağı doldurur.