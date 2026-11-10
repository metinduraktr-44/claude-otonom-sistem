# İŞ LİSTESI + ROADMAP (ADAM-SAAT)

> **Damga:** 2026-11-10 **14:55 Europe/Istanbul** (UTC 11:55)  
> **Dal:** `cursor/giga-devam-8e8f` · PR [#38](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38) (DRAFT)  
> **MODE:** Agency **BRIEF-ONLY** · Security **ASSESS-ONLY** · CANVA:OFF · merge yok · git restore yok  
> **Sayaç:** kontroller **600/600** · brief **24** · JOB_CARDS **33** (23 önceki + 10 EVP) · critic PASS **0** · 72 katalog restore **0**

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

Canlı `gh pr list --state open` (2026-11-10 14:55 +03). Agent bunları **yapmaz**.

| Kapı | URL | Not |
|------|-----|-----|
| **#38 DEVAM** (DRAFT) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38 | Dilim-3: 33 JOB_CARDS + CIS-IG1 stub + 72 katalog. Review → Ready/merge **sen**; ajan merge etmez. |
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

**Bu tur (10 Kas 14:55 +03) bitti:**

| ID | Teslim | Not |
|----|--------|-----|
| A9 | +10 AdOps EVP `JOB_CARDS/` | CARD + ≤10 heading; kümülatif **33**; mevcut 23 slug yok |
| A10 | `COMPLIANCE/CIS-IG1.md` | kanıt_yolu sütunu; **PASS uydurma yok**; 56-safeguard SoA yok |
| A11 | `ROSTER/GIT_DELETED_TITLES.md` | n=72 envanter eşleşmesi; restore **0** |
| A13-light | 3 skill `references/` | secret-hygiene / compliance-mapper / layers-engine; 20k yok |
| S4 | STATE / plans / AUDIT / BILGI | tek satır öğrenim |
| S5 | validate / secret_scan / ethics_check | slice |
| S6 | Bu rapor + `OZET-TEK-SAYFA-LIVE.md` | Europe/Istanbul |

**Kalan onaylı dilim (hâlâ DEVAM):**

| ID | İş | Sa |
|----|-----|-----|
| A12 | Agency: S03–S08 kanal-özel hook (marka yokken hâlâ REVISE) | 4–8 |
| A13 | Skill ~20k kısmi derinlik (6 skill; light 3 dosya bitti) | 5–11 |
| A14 | Sonraki 10 JOB_CARDS (Director-3 / kalan EVP) | 4–8 |
| A15 | GV.RM tek sayfa risk kabul (ASSESS) | 2–4 |

**Kalan onaylı bant:** **15–31 sa**. Merge/restore/CANVA/IMPLEMENT yok.

---

## 4) SENDE — SONRAKİ ADIMLAR (onay / bağımlılık)

| ID | İş | Blok | Sa |
|----|-----|------|-----|
| B3+ | ISO SoA 93 / #39 içeriği | **#39 review**; #38’e kopyalama | 8–16 |
| B4 | Skill 20k tam set | — | 16–32 |
| B5 | IR playbook ASSESS (Faz 6) | — | 6–12 |
| B6 | 72 rol git restore | **Metin restore** | 2–6 |
| B7 | 633 JOB_CARDS skeleton | A14 sonrası | 66–142 |
| B8 | 200 başlık × kart | seçilmiş 20 title önce | 20 title: 40–80 · 633: **400–800+** |
| B10 | Canva PKCE + MCP | **CANVA:ON** + Developers | 8–16 |
| B12 | LLM live | **Cursor Secrets** | 1–2 |
| B13 | GHA SHA pin | **IMPLEMENT** | 8–16 |
| B14 | #34/#35/#36/#37/#39 triyaj | Metin | 1–3 |

---

## 5) ROADMAP + ADAM-SAAT (yeni sayaçlar)

Tamam % = teslim / dürüst hedef (iskelet). Karakter bombası değil. Saat = aralık.

| Track | Faz | Durum | % | Kalan sa |
|-------|-----|-------|---|----------|
| **Agency** | 0–5 seed | 24/24 brief · critic PASS **0/8** | **~48%** pipeline (brief var, PASS yok) | **10–20** (marka kit sonrası critic) |
| **Agency** | Canva | BRIEF-ONLY | **10%** | **8–16** post-CANVA:ON |
| **Agency** | 6–7 prod | export yok | **0%** | **16–32** |
| **Security** | 0–4 katalog | **600/600** stub | **100%** katalog · **≠** uygulanmış kontrol | kalite/kanıt **12–24** |
| **Security** | 5 INDEX+IG1 | INDEX + CIS-IG1 stub · SoA yok | **~28%** Faz 5 | **6–14** (GV.RM; 93 SoA değil) |
| **Security** | 6–8 | IR/skill/QA | **~8%** | **30–60** |
| **LATOS** | 0–1 | 633 envanter · 72 katalog · restore 0 | keşif **~95%** / restore **0%** | restore **2–6** (onaylı) |
| **LATOS** | 4 kart | **33/633** skeleton · 10/200 H | kart **5,2%** · başlık **≪1%** (330 / 126 600) | +10 kart **4–8** · 633 skeleton **66–142** · 200H×633 **400–800+** |
| **LATOS** | 8–9 | 122 prompt / 200 tahmin | **0%** | 20-title kesit **16–40**; 900M char **🚩 0 sa — imkânsız** |

### Toplam bant

| Sahip | Bu tur (yapıldı) | Kalan onaylı DEVAM | 3-hat derinlik (600 stub + 633 skeleton + agency Canva’sız) | Yapılmayacak |
|-------|------------------|--------------------|--------------------------------------------------------------|--------------|
| **Metin** | Secrets + PR bakışı **0,8–2 sa** | aynı + marka 1–3 | — | — |
| **Agent** | 10 EVP + IG1 + 72 katalog **~4–8 sa** eşdeğeri | **15–31 sa** | **~200–400 sa** | 633×200 dolu **400–800+**; 900M **imkânsız** |

---

## 6) Metin — tek satır sonraki aksiyon

**Cursor Secrets’a Gemini+OpenRouter koy → yeni chat `/devam` `/sec-devam` `/latos-devam` → [#38](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38) review; [#35](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35)/[#34](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34) triyaj; CANVA:ON / IMPLEMENT / 72 restore kapalı.**
