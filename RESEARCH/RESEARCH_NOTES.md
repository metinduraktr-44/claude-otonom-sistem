# RESEARCH_NOTES — Pazar & Trend Notları

> Faz 1 · ts: 2026-08-27T12:56:59Z · Odak: AdOps CRE / SOC kreatif · Mod: BRIEF-ONLY

## Holding bağlamı

- 8 iştirak; kreatif üretim hattı **AdOps CRE** (Concept & Copy, Video & Motion, DCO & Feeds, Ad Format Lab)
- Medya satırı: **SOC** (Meta, TikTok) — spec doğrulama `MATRIX/CHANNEL_MATRIX.md`
- Skill/rol duplicate yok: 688 slash skill + 633 rol referans alınır

## Meta / Instagram (2026)

| Bulgu | Kaynak | ts_not |
|-------|--------|--------|
| Feed görsel default **4:5 (1080×1350)**; 1:1'e göre ~%31 daha fazla dikey alan | https://rule1.ai/articles/instagram-ad-sizes | 2026-08-27 |
| Stories/Reels unified **9:16 (1080×1920)**; safe zone üst ~14% / alt ~20–35% / yan ~6% | https://www.1clickreport.com/blog/meta-ads-creative-safe-zones-2026-guide | 2026-08-27 |
| Copy pratik limitleri: primary ~125 char · headline ~27 char (Ads Manager) | `MATRIX/CHANNEL_MATRIX.md` (repo seed) | 2026-08-27 |
| Advantage+ / Andromeda: hedeflemeden çok **konsept çeşitliliği** (≈10–15+ kavramsal farklı asset) performans kaldıracı | https://www.logicalposition.com/blog/the-2026-paid-social-playbook | 2026-08-27 |
| Advantage+ Creative kombinasyon havuzu; ince varyasyon ≠ konsept çeşitliliği | https://adlibrary.com/posts/meta-ads-creative-testing-automation | 2026-08-27 |

## TikTok

| Bulgu | Kaynak | ts_not |
|-------|--------|--------|
| In-Feed zorunlu dikey **9:16 1080×1920**; 1:1/16:9 letterbox ve zayıf performans | https://www.adsights.ai/resources/guides/tiktok-ad-creative-video-specs-guide | 2026-08-27 |
| Önerilen ad length **9–15s** (max 60s auction in-feed) | https://tikadtools.com/blog/tiktok-in-feed-ads/ | 2026-08-27 |
| Hook 0–3s kritik; native/UGC estetik TV spottan güçlü | aynı + industry consensus | 2026-08-27 |
| Master 9:16 → Meta 4:5/9:16 derive üretim hattı | https://conversion.studio/blog/tiktok-ad-specs | 2026-08-27 |

## AdOps CRE için operasyonel çıkarım

1. **Tek master:** 9:16 üret → 4:5 / 1:1 / 1.91:1 derive (`MATRIX/`)
2. **Konsept ≥ varyasyon:** Senaryo seti (01–08) kavramsal açı çeşitliliği sağlar
3. **Spec-first:** Safe zone brief'te zorunlu alan; CANVA:ON olmadan da BRIEF-ONLY teslim değerli
4. **SOC dual-path:** Meta + TikTok aynı big idea, farklı hook ritmi ve copy limiti

## Sonraki araştırma kuyruğu

- INBOX brand kit gelince: marka-özel rakip kreatif örnekleri
- Google PMax / YouTube Shorts derinleşme (Faz 4+ kanal genişletme)
- Hukuk: reklam politikası cross-check (`hukuk` iştirak) — claim review
