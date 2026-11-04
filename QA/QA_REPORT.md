# QA_REPORT — critic-copy / critic-spec (S01–S08)

> **ts:** 2026-11-04T11:40:00Z · **mod:** CANVA:BRIEF-ONLY · **marka:** TBD · **INBOX:** boş  
> **Kural:** sahte PASS yok. Critic ajanları readonly; bu rapor dosya **değiştirmez**.

## Denetim özeti (6 katman)

| Katman | Sonuç | Not |
|--------|-------|-----|
| Structural | GEÇTİ | SCENARIOS/01–08 + BRIEFS 24 + MATRIX |
| Integrity | GEÇTİ | 8 senaryo × 3 brief; S04 INDEX Google satırı brief’te yok |
| Semantic | REVISE | Marka TBD; kanıt proxy; rakip/claim yok (iyi) ama müşteri kilidi yok |
| Reference | KISMI | Araştırma URL 2026-08-27; 2026-11-03 brief’leri yeni kaynak damgası yok |
| Patterns | GEÇTİ | BRIEF-ONLY; 900B yok; CANVA:ON kapalı |
| Review | **PASS DEĞİL** | critic-copy/spec tam koşum **yapılmadı**; aşağıda dürüst gap |

**Genel:** **REVISE** (hafif yapısal GEÇTİ ≠ critic PASS)

## Kontrol listesi

- [x] S01–S08 senaryo klasörleri (SCENARIO/COPY/VISUAL)
- [x] Brief 24 adet (S01–S02 2026-08-27 · S03–S08 2026-11-03)
- [ ] Marka kit `CONTEXT/INBOX/`
- [ ] critic-copy **PASS** (hiçbir Si PASS değil)
- [ ] critic-spec **PASS** (export yok)
- [ ] `spec_validate.py` pixel koşumu (Pillow export sonrası)
- [ ] S03–S08 kanal-özel copy (aynı headline 3 kanala kopyalanmış)

---

## critic-copy (S01–S08)

Şablon çıktı: `VERDICT | ISSUES | SUGGESTIONS` — ajan koşumu yok; **statik denetim**.

| ID | Brief/copy | VERDICT | Dürüst gap |
|----|------------|---------|------------|
| S01 | Master-first | **REVISE** | TikTok headline `—`; marka yok; CTA “CRE pipeline” müşteri dili değil |
| S02 | Safe zone | **REVISE** | “Spec PASS zorunlu” headline **yanlış vaat** — pixel yokken spec PASS yok |
| S03 | Konsept çeşit | **REVISE** | Meta 4:5 / 9:16 / TikTok **aynı headline** “Konsept > varyasyon”; dual-path yok |
| S04 | DCO/feed | **REVISE** | INDEX öncelik Google 1.91:1; brief set yalnızca Meta+TikTok. Feed/SKU kanıtı yok |
| S05 | SOC dual | **REVISE** | Dual-path iddia; üç kanal metni klon. TikTok hook senaryoda var, brief’te zayıf |
| S06 | Brief-to-spec | **REVISE** | Ürün vaadi doğru (BRIEF-ONLY); fatura/teslim SLA yok; marka TBD |
| S07 | Multi-brand | **REVISE** | 8 iştirak iddiası holding JSON’a bağlı; iştirak ton paleti brief’te yok |
| S08 | Format lab | **REVISE** | Kill/graduate metrik tanımı yok; test dalgası grid satırı var, sonuç tablosu yok |

**Ortak ISSUES**
1. `CONTEXT/INBOX` boş → ton/marka uyumu **ölçülemez** (PASS imkânsız).
2. S03–S08: kanal kopyası = find-replace; critic-copy “platform ritmi” fail.
3. Claim risk düşük (rakip adı yok) — bu **PASS sayılmaz**, sadece kırmızı yok.
4. Karakter limiti: headline’lar ~27 altında (iyi); primary text otomatik sayım **yok**.

**SUGGESTIONS (sonraki tur, marka kit sonrası)**
- Kanal başına 1 distinct hook (S05 zorunlu).
- S02 headline’ı “Spec kapısı / export sonrası” olarak düzelt (sahte PASS vaadi kalksın).
- S04: ya Google brief ekle ya INDEX önceliğini Meta/TikTok’a çek.
- S01 TikTok headline doldur veya “UI CTA only” diye işaretle.

**Hiçbir Si: PASS / FAIL (yasal). Hepsi REVISE.**

---

## critic-spec (S01–S08)

| Kanal (brief) | Expected (`CHANNEL_MATRIX`) | Actual export | status |
|---------------|-----------------------------|---------------|--------|
| Meta 4:5 | 1080×1350 · 4:5 · ≤30 MB | **yok** (BRIEF-ONLY) | **GAP** |
| Meta 9:16 | 1080×1920 · 9:16 · safe zone | **yok** | **GAP** |
| TikTok 9:16 | 1080×1920 · 9–15s öneri | **yok** (video yok) | **GAP** |
| Google 1.91:1 (S04 INDEX) | 1200×628 | brief **yok** | **GAP** |
| `spec_validate.py` | Pillow + PRODUCTION_GRID | export yok → log üretmez/boş | **GAP** |

**VERDICT (spec):** **FAIL-as-in-not-run** değil — **N/A / GAP**. CANVA:ON + pixel olmadan critic-spec **PASS yazılmaz**.

**FIXES (insan kapısı)**
1. Marka kit → INBOX.
2. Kullanıcı `CANVA:ON` derse OAuth + `/canva-uret`.
3. Export sonrası `python3 scripts/spec_validate.py`.
4. O zamana kadar teslim = senaryo+brief+matrix (faturalanabilir doküman), **tasarım değil**.

---

## Sayaç

| Madde | Adet | Critic |
|-------|------|--------|
| Senaryo | 8 | COPY bank var; critic koşumu yok |
| Brief | 24 | REVISE × 8 (kanal klonu) |
| PASS | **0** | bilinçli |
| Pixel | 0 | BRIEF-ONLY |

**Bulgu 1:** Önceki QA (2026-08-27) “hafif GEÇTİ” idi; S03–S08 eklenince critic borcu **büyüdü**, kapanmadı.  
**Bulgu 2:** Security/LATOS bu raporda yok — ayrı STATE.
