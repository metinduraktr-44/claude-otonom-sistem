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
