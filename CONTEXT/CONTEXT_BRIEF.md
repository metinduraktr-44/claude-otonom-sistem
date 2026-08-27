# CONTEXT_BRIEF — Ajans Bağlam Özeti

> Faz 0 ingestion: 2026-08-27T00:30:00Z · Kaynak: CLAUDE.md, data/*, uretim/*, docs/HOLDING-ISTIRAK-ORG.md

## Holding & Ajans Kimliği

| Alan | Değer |
|------|-------|
| **Portföy** | metinduraktr-44 — 8 iştirak, 633 rol, 688 slash skill |
| **HQ repo** | `claude-otonom-sistem` (bu workspace) |
| **Ajans birimi** | AdOps Agency (`adops-agents`) — performans pazarlama & programatik |
| **Kreatif stüdyo** | AdOps CRE (Concept & Copy, Video & Motion, DCO & Feeds, Ad Format Lab) |
| **Orkestrasyon** | CLAUDE.md uzman kurulu + GIGA Creative Agency OS (`.cursor/`) |

### İştirak haritası (8 birim)

1. **Holding HQ / OS** — ortak standart, MCP/skill motoru (71 rol)
2. **AdOps Agency** — programatik, paid social, SEO, CRO, kreatif stüdyo (219 rol)
3. **Performer Growth Hub** — app growth UA/retention/monetization (78 rol)
4. **VizaTrack** — göç & relokasyon platformu (84 rol)
5. **Holding Hukuk & Uyum** — KVKK/GDPR, reklam politikası (55 rol)
6. **Tahmin Uzmanı** — spor/finans forecast (56 rol)
7. **Movéa (M-AIOS)** — premium medikal scrubs DTC (35 rol)
8. **Çiğköftem** — gıda markası web app (35 rol)

## Marka (holding düzeyi — kampanya bazında güncellenecek)

- **marka_adı:** Holding portföyü / aktif müşteri TBD (AdOps veya iştirak markası)
- **sektör:** Dijital ajans + çoklu dikey (e-ticaret, app growth, gıda, medikal, B2B)
- **ton:** Profesyonel, veri-odaklı, McKinsey Kıdemli Ortak — agresif sansasyon yok
- **hedef_kitle:** B2B müşteriler (performans pazarlama) + iştirak marka tüketicileri

### Marka guardrail seed (AdOps CRE)

- Kanıtsız süperlatif, tıbbi/hukuki iddia yasak (brief izin vermedikçe)
- Rakip ismi karşılaştırması yasak
- TR birincil dil; EN varyant ayrı bölüm
- Safe zone: 9:16 ve 4:5 için kritik içerik merkez %80

## Kanal önceliği

- **birincil:** Meta (Feed 4:5, Stories/Reels 9:16), TikTok In-Feed 9:16
- **ikincil:** Google Display/PMax, YouTube 16:9 + Shorts 9:16, IAB standard units
- **spec kaynağı:** `MATRIX/CHANNEL_MATRIX.md` · `MATRIX/PRODUCTION_GRID.csv`

## Kısıtlar

| Kısıt | Değer |
|-------|-------|
| **dil** | TR (varsayılan) |
| **CANVA modu** | `BRIEF-ONLY` — `STATE.md` |
| **prompt sözleşmesi** | 122 prompt/rol × 4–12 KiB; 🚩 900M/900B karakter RED |
| **skill envanteri** | `data/slash_skill_katalog.json` (688 skill, 9 domain) |
| **rol org** | `data/holding_istirak_org.json` (633 rol) |

## Aktif kampanya

- **kampanya_adı:** TODO — kullanıcı `/brief-uret` ile seed
- **deadline:** TODO
- **KPI:** TODO (ör. CPA, ROAS, CTR, view-through)

## Referanslar (mevcut repo)

| Kaynak | Yol |
|--------|-----|
| Holding org | `data/holding_istirak_org.json`, `docs/HOLDING-ISTIRAK-ORG.md` |
| Slash skill katalog | `data/slash_skill_katalog.json` |
| Rol kartları (pilot 48) | `uretim/rol-kartlari/` |
| AdOps kreatif EVP | `uretim/rol-kartlari/adops-evp-kreatif-stüdyo-dco.md` |
| Soru bankası | `data/soru_bankasi.json` (957 soru) |
| Ülke/pazar | `data/ulke_pazar_iskeleti.json` (10 ülke) |
| Önceki kampanyalar | `ARCHIVE/` (henüz boş) |

## Inbox

Yeni girdiler: `CONTEXT/INBOX/` — marka kit, brief PDF, rakip örnekleri buraya bırakılır; Faz 1'de işlenir.

## TODO (Faz 1+)

- [ ] Aktif müşteri/marka seçimi ve brand kit yükleme
- [ ] Kampanya KPI ve deadline tanımı
- [ ] Canva OAuth PKCE (`tools/canva-client/`) — CANVA:ON için
- [ ] İlk brief → scenario → spec-dogrula döngüsü
