# CONTEXT_BRIEF — Ajans Bağlam Özeti

> Faz 0 refresh: 2026-08-27T12:56:59Z · Kaynak: holding JSON, slash katalog, AdOps CRE EVP kartı · Mod: CANVA:BRIEF-ONLY

## Holding & Ajans Kimliği

| Alan | Değer |
|------|-------|
| **Portföy** | metinduraktr-44 — 8 iştirak, 633 rol, 688 slash skill |
| **HQ repo** | `claude-otonom-sistem` (bu workspace) |
| **Ajans birimi** | AdOps Agency (`adops-agents`) — performans pazarlama & programatik |
| **Kreatif stüdyo** | AdOps CRE (Concept & Copy, Video & Motion, DCO & Feeds, Ad Format Lab) |
| **Orkestrasyon** | CLAUDE.md uzman kurulu + GIGA Creative Agency OS (`.cursor/`) |

### İştirak haritası (8 birim) — duplicate yok; kaynak `data/holding_istirak_org.json`

1. **Holding HQ / OS** — ortak standart, MCP/skill motoru (71 rol)
2. **AdOps Agency** — programatik, paid social, SEO, CRO, kreatif stüdyo (219 rol)
3. **Performer Growth Hub** — app growth UA/retention/monetization (78 rol)
4. **VizaTrack** — göç & relokasyon platformu (84 rol)
5. **Holding Hukuk & Uyum** — KVKK/GDPR, reklam politikası (55 rol)
6. **Tahmin Uzmanı** — spor/finans forecast (56 rol)
7. **Movéa (M-AIOS)** — premium medikal scrubs DTC (35 rol)
8. **Çiğköftem** — gıda markası web app (35 rol)

## Marka

| Alan | Değer |
|------|-------|
| **marka_adı** | TBD — aktif müşteri kit yok; varsayılan ürün yolu: **AdOps CRE** (holding içi) |
| **ürün_yolu** | AdOps CRE — performans kreatif üretim sistemi (brief→senaryo→spec→brief-only teslim) |
| **sektör** | Dijital ajans + performans kreatif / DCO |
| **ton** | Profesyonel, veri-odaklı, McKinsey Kıdemli Ortak — agresif sansasyon yok |
| **hedef_kitle** | B2B: performans pazarlama ekipleri, growth lead, CMO/ajans ortakları |

### Marka guardrail seed (AdOps CRE)

- Kanıtsız süperlatif, tıbbi/hukuki iddia yasak (brief izin vermedikçe)
- Rakip ismi karşılaştırması yasak
- TR birincil dil; EN varyant ayrı bölüm
- Safe zone: 9:16 ve 4:5 için kritik içerik merkez ~80%

## Kanal önceliği

- **birincil:** Meta (Feed 4:5, Stories/Reels 9:16), TikTok In-Feed 9:16
- **ikincil:** Google Display/PMax, YouTube 16:9 + Shorts 9:16, IAB standard units
- **spec kaynağı:** `MATRIX/CHANNEL_MATRIX.md` · `MATRIX/PRODUCTION_GRID.csv`

## Kısıtlar

| Kısıt | Değer |
|-------|-------|
| **dil** | TR (varsayılan) |
| **CANVA modu** | `BRIEF-ONLY` — `STATE.md` (CANVA:ON kapalı) |
| **prompt sözleşmesi** | 122 prompt/rol × 4–12 KiB; 🚩 900M/900B karakter RED |
| **skill envanteri** | `data/slash_skill_katalog.json` (688 skill, 9 domain) — referans, duplicate yok |
| **rol org** | `data/holding_istirak_org.json` (633 rol) |

## Aktif kampanya (seed — marka TBD)

| Alan | Değer |
|------|-------|
| **kampanya_adı** | AdOps CRE — Performans Kreatif Motoru (seed) |
| **kampanya_kodu** | `ADOPs-CRE-SEED-2026Q3` |
| **deadline** | TBD (müşteri kilidi sonrası) |
| **KPI** | TBD → varsayılan proxy: CTR, thumb-stop rate, CPA (müşteri funnel'ına göre) |
| **birincil senaryo seti** | `SCENARIOS/01` … `08` |

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

## Açık maddeler (müşteri girdisi gerekir)

- [ ] Aktif müşteri/marka seçimi ve brand kit yükleme (`CONTEXT/INBOX/`)
- [ ] Kampanya KPI ve deadline kilidi
- [ ] Canva OAuth PKCE — yalnızca CANVA:ON istendiğinde (`tools/canva-client/`)

---

## LATOS Bölümü

> **Güncelleme:** 2026-08-27T20:15:00Z · Faz 0–1 bootstrap

### Kaynaklar Tarandı
| Kaynak | Bulgu |
|--------|-------|
| `data/holding_istirak_org.json` | 633 rol, 8 istirak birimi |
| `uretim/rol-kartlari/` | EVP/C-level kartları (kısmi) |
| `data/slash_skill_katalog.json` | 688 skill, 30 title index |
| `ORG/ROLES/` | 11 Security rol (ayrı track) |
| Git deleted | ~72 `uretim/rol-kartlari/*.md` (kurtarılabilir, insan onaylı) |

### Track Ayrımı (additive)
- **Agency** — BRIEFS/, CANVA_OPS/
- **Security** — SECURITY_*, LAYERS/, 6×100 matris
- **LATOS** — ROSTER/, JOB_CARDS/, EXPERTS/, FORECASTS/

### Karakter Hedefleri (dürüst)
- Faz 0–1: skeleton + envanter (633 title)
- Tam iş kartı/prompt/tahmin hedefleri Faz 4–9, fazlı

## INBOX

Yeni girdiler: `CONTEXT/INBOX/` — marka kit, brief PDF, rakip örnekleri, önceki chat dökümleri
