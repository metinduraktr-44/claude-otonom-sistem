# İŞ LİSTESI + ROADMAP (ADAM-SAAT)

> **Damga:** 2026-11-15 **12:48 Europe/Istanbul** (UTC 09:48)  
> **Dal:** `cursor/giga-devam-8e8f` · PR [#38](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38) (DRAFT)  
> **MODE:** Agency **BRIEF-ONLY** · Security **ASSESS-ONLY** · CANVA:OFF · merge yok · git restore yok  
> **Sayaç:** kontroller **600/600** · brief **24** · JOB_CARDS **43** (33 önceki + 10 Lead) · critic PASS **0** · 72 katalog restore **0**

Kurul: Baş Mimar + Denetçi + İş/Gelir. Varsayım: DEVAM = onaylı dilim; merge / restore / CANVA:ON / IMPLEMENT **hariç**.

---

## 1) BENDE — YAPACAKLARIM

| Aksiyon | URL | Kısa not |
|---------|-----|----------|
| Cursor Secrets: `GEMINI_API_KEY` + `OPENROUTER_API_KEY` | https://cursor.com/dashboard | Secret yoksa nightly LLM dry-run kapalı kalır; kaydı yapınca ajan canlı çağrıya geçer. |
| Gemini key üret/rotate | https://aistudio.google.com/apikey | Eski key sohbet ifşası riski; yeni key’i yalnızca Cursor Secrets’a koy, repo’ya yazma. |
| OpenRouter key | https://openrouter.ai/keys | Gemini düşerse OpenRouter fallback; key yoksa fallback de ölür. |
| Anthropic Console (sahte eklenti) | https://console.anthropic.com | Yalnızca #34/#35 “token vaadi / sahte eklenti” iddiasını **doğrulamak** için bak; buradan alınan key’i plugin’e yapıştırma. |
| GitHub PAT gözden geçir | https://github.com/settings/tokens | Minimum scope; sızıntı tarama (secret_scan) değer yazmaz — sen rotate edersin. |
| Canva Developers (OAuth hazırlığı) | https://www.canva.com/developers/ | Şimdi BRIEF-ONLY; app oluşturmak CANVA:ON **değil** — ON dersen client id/secret buradan. |
| Açık PR kuyruğu | https://github.com/metinduraktr-44/claude-otonom-sistem/pulls | Canlı liste; kapatılmış PR uydurma. #38 bu turun DEVAM PR’ı. |
| Marka kit bırak | repo `CONTEXT/INBOX/` | INBOX boş → critic-copy **PASS imkânsız**; PDF/logo/brief koyunca S01–S08 özelleşir. |
| Cursor restart + slash smoke | yeni chat → `/devam` · `/sec-devam` · `/latos-devam` | Rules/skills yüklenir; Faz kilidi (BRIEF-ONLY / ASSESS-ONLY) smoke edilir. |

**Metin operasyon bandı (M1–M4 + INBOX):** **0,8–2 sa** (+ marka kit 1–3 sa).

---

## 2) BENDE — ONAYLAYACAKLARIM

Canlı `gh pr list --state open` (2026-11-15 12:48 +03). Agent bunları **yapmaz**.

| Kapı | URL | Not |
|------|-----|-----|
| **#38 DEVAM** (DRAFT) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38 | Dilim-4: 43 JOB_CARDS + NIST-GV-RM stub + QA REVISE. Review → Ready/merge **sen**; ajan merge etmez. |
| **#39** (açık) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39 | FAZ6 ISO SoA + 10 CTRL — **#38 ile karıştırma / merge etme**. |
| **#37** (açık) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37 | Tek sayfa iş listesi 04 Kas; #38 LIVE özeti daha yeni. |
| **#36 rapor** (DRAFT) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/36 | Eski iş-listesi (03 Kas, 120/600). Güncel dosya **#38 dalında**; kapat veya #38 lehine bırak. |
| **#35 ingest** | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35 | Claude Code güvenlik uyarısı PDF/DOCX. #34 ile örtüşür; birini merge diğerini kapat. |
| **#34 draft** | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34 | Viral-uyarı ingest; sahte eklenti/token **RED**. Ready yap veya #35 lehine kapat. |
| **#33 dup?** | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33 | `actions/setup-python` 5→7. Muhtemel duplicate (eski #30 merged) — kapat. |
| **#32** (açık, bilgi) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/32 | Tek sayfa merge raporu 2026-09-02 — arşiv; merge şart değil. |
| **#31** (açık, bilgi) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/31 | Dependabot npm `katalog/` examples — ürün runtime değil; triyaj. |
| **CANVA:ON** | `STATE.md` CANVA bloğu | Varsayılan BRIEF-ONLY. ON = tasarım/MCP; açık cümle şart. |
| **MODE=IMPLEMENT** | `STATE.md` / `SECURITY/STATE.md` | ASSESS-ONLY varsayılan. IMPLEMENT = GHA SHA pin + sertleştirme izni. |
| **72 restore** | `ROSTER/GIT_DELETED_TITLES.md` | 72 slug kataloglandı; `uretim/rol-kartlari/*` git restore **yasak** ta ki sen “restore” demeden. |

**Onay turu bandı:** **1–2 sa**.

---

## 3) SENDE — ONAYLI (DEVAM, ekstra onay yok)

**Bu tur (15 Kas 12:48 +03) bitti:**

| ID | Teslim | Not |
|----|--------|-----|
| A14 | +10 Lead `JOB_CARDS/` (5 AdOps + 5 HQ) | CARD + ≤10 heading; kümülatif **43**; mevcut 33 slug yok |
| A15 | `COMPLIANCE/NIST-GV-RM.md` | GV.RM-01…07 + risk tablosu TBD; **PASS uydurma yok** |
| A12-light | `QA/QA_REPORT.md` | INBOX boş → **REVISE**; PASS=0 |
| R1 | `RESEARCH/2026-11-15_nist-csf-20-gv-rm.md` | NIST CSWP 29 URL+timestamp |
| S4 | STATE / plans / AUDIT / BILGI | tek satır öğrenim |
| S5 | validate / secret_scan / ethics_check | slice |
| S6 | Bu rapor + `OZET-TEK-SAYFA-LIVE.md` | Europe/Istanbul |

**Kalan onaylı dilim (hâlâ DEVAM):**

| ID | İş | Sa |
|----|-----|-----|
| A12 | Agency: S03–S08 kanal-özel hook (marka yokken hâlâ REVISE) | 4–8 |
| A13 | Skill ~20k kısmi derinlik (6 skill; light 3 dosya bitti) | 5–11 |
| A16 | Sonraki 10 JOB_CARDS (kalan Lead / diğer birimler) | 4–8 |
| A17 | ISO A.5 SoA 20 satır özet (ASSESS; #39 çakıştırma yok) | 2–4 |

**Kalan onaylı bant:** **15–31 sa**. Merge/restore/CANVA/IMPLEMENT yok.

---

## 4) SENDE — SONRAKİ ADIMLAR (onay / bağımlılık)

| İş | Bağımlılık | Sa (tahmini) |
|----|------------|--------------|
| critic-copy/spec **PASS** | Marka kit INBOX + (spec için) CANVA:ON + export | 6–12 |
| GHA SHA40 pin | MODE=IMPLEMENT onayı | 2–5 |
| 72 `uretim/rol-kartlari` restore | Metin “restore” + seçici liste | 3–8 |
| Canva OAuth live | CANVA:ON + developers app | 4–10 |
| 200 heading/title doldurma | Faz 4+ DEVAM dalgaları (633×) | 200–400+ |
| 122 prompt/title | Faz 8 + token bütçesi | 80–150 |
| IR playbook / Faz 6 | ASSESS; #39 ile merge çakıştırma yok | 4–8 |
| 🚩 900M char/prompt | **RED** — fiziksel imkânsız; fazlı alt dosya | — |

---

## 5) ROADMAP — adam-saat (güncel sayaç)

| Blok | Mevcut | Kalan iş | Adam-saat |
|------|--------|----------|-----------|
| JOB_CARDS skeleton | **43**/633 | 590 title × skeleton (≤10 heading) | **80–160** |
| JOB_CARDS 2000+/200 başlık | 0 tam | 633 × fazlı H001–H200 | **400–800+** |
| Security 600 kontrol | **600**/600 katalog | Uygulama kanıtı / IMPLEMENT | **20–40** (IMPLEMENT sonrası) |
| Compliance SoA | INDEX+IG1+GV.RM stub | ISO A.5 özet + SOC2 | **6–12** |
| Agency briefs | **24**/24 seed | S03–S08 kanal-özel + marka | **8–16** |
| Critic PASS | **0**/8 | Marka + (spec) pixel | **6–12** |
| Skill ~20k × 6 | light kısmi | derinlik dump değil | **15–30** |
| Prompt 122/title | 0 | Faz 8 | **80–150** |
| Forecast 200/gün/title | 0 | Faz 9 Cloud | **40–80** (otomasyon) |
| 🚩 900M char tek prompt | — | **RED** | 0 (yapılmaz) |

**Onaylı DEVAM kalan band (A12/A13/A16/A17):** **15–31 sa**.  
**Tüm roadmap (insan kapıları hariç iskelet):** kabaca **650–1300+ sa** — tek oturumda bitmez.

---

## 6) Metin — tek satır sonraki aksiyon

**Cursor Secrets’a Gemini+OpenRouter koy → yeni chat’te `/devam` smoke → marka kit’i `CONTEXT/INBOX/`’a bırak; #38’i review et (merge sen).**

---

⏱️ Damga: 2026-11-15T09:48:56Z (12:48 +03) · 🔍 Denetim: GEÇTİ (slice) · 📚 Öğrenim: MANAGER tier envanterde yok → Lead; GV.RM stub≠nicel iştah · 🔗 Önceki: evet
