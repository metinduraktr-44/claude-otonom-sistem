# HOLDING KONSOLİDE RAPOR — metinduraktr-44 Portföyü
> Üretim: 2026-07-22T09:28:34Z · Kaynak: data/holding.json · Mod: CANLI (API)

## Kurul
| Rol | Görev |
|---|---|
| Chairman / Sahip | Nihai onay: sermaye, faz kapıları, birim aç/kapa |
| Group CEO | Portföy stratejisi, birimler arası tahsis |
| Group COO | Operasyon ritmi (gözetim, standup, kurul) |
| Group CTO | Ortak teknik standart (CI, doğrulama, MCP, güvenlik) |
| Group CFO | API bütçesi + birim gelir konsolidasyonu |
| Group CCO | 5 güvenlik kuralı + lisans/uyum tüm repolarda |

## İş Birimleri
| Birim | Repo | Segment | Alan | Gelir | Son commit | Açık issue |
|---|---|---|---|---|---|---|
| Holding HQ / OS | claude-otonom-sistem | os | Ortak standart, gözetim, jeneratörler | — | 2026-07-22 | 3 |
| AdOps Agency | adops-agents | agency | Performans pazarlama & programatik | ✓ | 2026-07-22 | 603 |
| Tahmin Uzmanı | a-agency-tahmin-uzman- | agency | Spor/finans/danışmanlık forecast | ✓ | — | — |
| Performer | performer-growth-hub | agency | Uygulama büyüme / app growth | ✓ | — | — |
| Movéa (M-AIOS) | or-na.com | brand | Premium medikal scrubs DTC | ✓ | — | — |
| VizaTrack | VizaTrack | product | Göç & relokasyon platformu | ✓ | — | — |
| Çiğköftem | cigkoftem-web-app | brand | Gıda markası web app | ✓ | — | — |

## Segment Dağılımı
- **os**: Holding HQ / OS
- **agency**: AdOps Agency, Tahmin Uzmanı, Performer
- **brand**: Movéa (M-AIOS), Çiğköftem
- **product**: VizaTrack

## Ortak Hizmetler
- Güvenlik & Kalite: 5 kural + 6-katman doğrulama (CILT1/CILT8)
- Standardizasyon Motoru: scripts/standardize_repo.py
- Rol-Model Kütüphanesi: adops-agents/data/rol_modelleri.json (79 isim)
- Soru Bankası: adops-agents/docs/OZ-DENETIM-SORU-BANKASI.md (501)
- Gelir Modeli: 5 kanal (sponsorluk/placement/referral/premium/inbound)

## Ritim
- Günlük: birim standup + HQ gözetim · Haftalık: Group liderlik sync · Aylık: Holding kurulu (OKR + faz kapısı + sermaye tahsisi)

## Günün Holding Öz-Denetimi
- [ ] Her birimin son commit'i 48 saatten taze mi (ölü birim var mı)?
- [ ] Gelir motoru birimlerinde (AdOps/Tahmin/Performer) bu hafta ilerleme var mı?
- [ ] Marka birimleri (Movéa/VizaTrack/Çiğköftem) community-health standardında mı?
- [ ] Çapraz-sinerji fırsatı: AdOps bir markaya iç-müşteri hizmeti verebilir mi?
- [ ] Sermaye/gelir taahhüdü sahip onayından geçti mi (CILT1)?
