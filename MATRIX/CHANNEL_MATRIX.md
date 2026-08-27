# Kanal × Format Matrisi — 2026 Spec Özeti

> Kaynak: Meta Unified Safe Zones (Mar 2026), TikTok Ads, Google Ads, YouTube, IAB standard units.
> Doğrulama: `python3 scripts/spec_validate.py` · Skill: `spec-matrix`

## Meta (Facebook + Instagram)

| Placement | Size (px) | Ratio | Safe zone / notes |
|-----------|-----------|-------|-------------------|
| Stories & Reels (unified) | 1080×1920 | 9:16 | Top 14%, bottom 20–35%, sides 6% — kritik içerik merkez ~80% |
| Feed image (recommended) | 1080×1350 | 4:5 | +31% screen vs 1:1; default image format 2026 |
| Feed image (alt) | 1440×1800 | 4:5 | High-res variant |
| Feed video | 1080×1920 | 9:16 | Full-screen vertical |
| Carousel card | 1080×1080 | 1:1 | Legacy; hâlâ desteklenir |
| Link / horizontal | 1200×628 | 1.91:1 | Right column, link preview |
| In-stream video | 1920×1080 | 16:9 | Horizontal video |

**Copy limits:** Primary text ~125 char · Headline ~27 char · Image max 30 MB · Video max 4 GB

## TikTok

| Placement | Size (px) | Ratio | Notes |
|-----------|-----------|-------|-------|
| In-Feed Ad | 1080×1920 | 9:16 | Zorunlu vertical |
| Video length | — | — | Max 60s ad; öneri 9–15s |
| Format | — | — | MP4/MOV H.264 + AAC |
| Max file | — | — | ~287.6 MB (mobile) |

**Safe zone:** Top/bottom UI overlap — CTA ve logo merkez bölgede

## Google Ads (Display / PMax / Demand Gen)

| Asset | Size (px) | Ratio | Notes |
|-------|-----------|-------|-------|
| Horizontal | 1200×628 | 1.91:1 | Responsive display primary |
| Square | 1200×1200 | 1:1 | Cross-placement |
| Logo square | 1200×1200 | 1:1 | Min 128×128 |
| Landscape logo | 1200×300 | 4:1 | Optional |

**Video (YouTube / Video campaigns):** 16:9 1920×1080 · 9:16 Shorts 1080×1920

## YouTube

| Format | Size (px) | Ratio | Max duration |
|--------|-----------|-------|--------------|
| Standard video | 1920×1080 | 16:9 | Kampanya hedefine göre |
| Shorts | 1080×1920 | 9:16 | 3 min (organic); ads vary |
| Thumbnail | 1280×720 | 16:9 | JPG/PNG |

## IAB Standard Display

| Unit | Size (px) | Device | Max weight |
|------|-----------|--------|------------|
| Medium Rectangle | 300×250 | Desktop/Mobile | 150 KB |
| Large Rectangle | 336×280 | Desktop/Mobile | 150 KB |
| Leaderboard | 728×90 | Desktop | 150 KB |
| Wide Skyscraper | 160×600 | Desktop | 150 KB |
| Half Page | 300×600 | Desktop | 150 KB |
| Mobile Banner | 320×50 | Mobile | 150 KB |
| Large Mobile Banner | 320×100 | Mobile | 150 KB |
| Billboard | 970×250 | Desktop | 150 KB |

## LinkedIn / X (özet)

| Platform | Feed | Ratio |
|----------|------|-------|
| LinkedIn single image | 1200×627 | 1.91:1 |
| LinkedIn carousel | 1080×1080 | 1:1 |
| X image | 1200×675 | 16:9 |

## Master creative stratejisi (2026)

1. **Master:** 9:16 (1080×1920) — Stories/Reels/TikTok/Shorts
2. **Derive:** 4:5 Feed, 1:1 carousel, 1.91:1 link
3. **Validate:** Her export → `spec-dogrula` + `CANVA_OPS/VALIDATION.log`
4. **Registry:** `CANVA_OPS/DESIGN_REGISTRY.csv`

## Changelog
- 2026-08-27: Bootstrap seed (Faz 0)
- TODO Faz 5: platform API changelog sync
