# İŞ LİSTESI + ROADMAP (ADAM-SAAT)

> **Damga:** 2026-11-04 **14:45 Europe/Istanbul** (UTC 11:45)  
> **Dal:** `cursor/giga-devam-8e8f` · PR [#38](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38) (DRAFT)  
> **MODE:** Agency **BRIEF-ONLY** · Security **ASSESS-ONLY** · CANVA:OFF · merge yok · git restore yok  
> **Sayaç:** kontroller **600/600** · brief **24** · JOB_CARDS **23** (13 C-level + 10 Director)

Kurul: Baş Mimar + Denetçi + İş/Gelir. Varsayım: DEVAM = onaylı dilim; merge / restore / CANVA:ON / IMPLEMENT **hariç**.

---

## 1) BENDE — YAPACAKLARIM

| Aksiyon | URL | Kısa not |
|---------|-----|----------|
| Cursor Secrets: `GEMINI_API_KEY` + `OPENROUTER_API_KEY` | https://cursor.com/dashboard | Secret yoksa nightly LLM dry-run kapalı kalır; kaydı yapınca ajan canlı çağrıya geçer. |
| Gemini key üret/rotate | https://aistudio.google.com/apikey | Eski key sohbet ifşası riski; yeni key’i yalnızca Cursor Secrets’a koy, repo’ya yazma. |
| OpenRouter key | https://openrouter.ai/keys | Gemini düşerse PR #16 yolu OpenRouter’a iner; key yoksa fallback de ölür. |
| Anthropic Console (sahte eklenti) | https://console.anthropic.com | Yalnızca #34/#35 “token vaadi / sahte eklenti” iddiasını **doğrulamak** için bak; buradan alınan key’i plugin’e yapıştırma. |
| GitHub PAT gözden geçir | https://github.com/settings/tokens | Minimum scope; sızıntı tarama (secret_scan) değer yazmaz — sen rotate edersin. |
| Canva Developers (OAuth hazırlığı) | https://www.canva.com/developers/ | Şimdi BRIEF-ONLY; app oluşturmak CANVA:ON **değil** — ON dersen client id/secret buradan. |
| Marka kit bırak | repo `CONTEXT/INBOX/` (README: `CONTEXT/INBOX/README.md`) | INBOX boş → critic-copy **PASS imkânsız**; PDF/logo/brief koyunca S01–S08 özelleşir. |
| Cursor restart + slash smoke | yeni chat → `/devam` · `/sec-devam` · `/latos-devam` | Rules/skills yüklenir; Faz kilidi (BRIEF-ONLY / ASSESS-ONLY) smoke edilir. |
| Açık PR kuyruğu | https://github.com/metinduraktr-44/claude-otonom-sistem/pulls | Canlı liste; kapatılmış PR uydurma. #38 bu turun DEVAM PR’ı. |

**Metin operasyon bandı (M1–M4 + INBOX):** **0,8–2 sa** (+ marka kit 1–3 sa).

---

## 2) BENDE — ONAYLAYACAKLARIM

Canlı `gh pr list` (2026-11-04 14:45 +03). Agent bunları **yapmaz**.

| Kapı | URL | Not |
|------|-----|-----|
| **#38 DEVAM** (DRAFT) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38 | 600 kontrol + 24 brief + 23 kart + Faz 5 INDEX + QA REVISE. Review → Ready/merge **sen**; ajan merge etmez. |
| **#35 ingest** | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35 | Claude Code güvenlik uyarısı PDF/DOCX. #34 ile örtüşür; birini merge diğerini kapat. |
| **#34 draft** | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34 | Viral-uyarı ingest; sahte eklenti/token **RED**. Ready yap veya #35 lehine kapat. |
| **#36 rapor** (DRAFT) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/36 | Eski iş-listesi (03 Kas, 120/600). Bu dosya artık **#38 dalında** güncel; #36’yı kapat veya #38 lehine bırak. |
| **#33 dup?** | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33 | `actions/setup-python` 5→7. **#30 MERGED** (2026-09-01) — muhtemel duplicate; kapat. |
| **#37** (açık, bilgi) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37 | Tek sayfa iş listesi 03 Kas; #38 LIVE özeti daha yeni. |
| **#39** (açık, bilgi) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39 | FAZ6 ISO SoA + 10 CTRL — **#38 ile karıştırma / merge etme**. |
| **CANVA:ON** | `STATE.md` CANVA bloğu | Varsayılan BRIEF-ONLY. ON = tasarım/MCP; açık cümle şart. |
| **MODE=IMPLEMENT** | `STATE.md` / `SECURITY/STATE.md` | ASSESS-ONLY varsayılan. IMPLEMENT = GHA SHA pin + sertleştirme izni. |
| **72 restore** | `ROSTER/TITLE_INVENTORY.md` | `uretim/rol-kartlari/*` git restore **yasak** ta ki sen “restore” demeden. |

**Onay turu bandı:** **1–2 sa**.

---

## 3) SENDE — ONAYLI (DEVAM, ekstra onay yok)

**Bu tur (04 Kas 14:45 +03) bitti:**

| ID | Teslim | Not |
|----|--------|-----|
| S1 | `COMPLIANCE/INDEX.md` + NIST/ISO/CIS kartları | Faz 5 INDEX; 600 satır **yeniden yazılmadı** |
| S2 | `QA/QA_REPORT.md` | S01–S08 critic-copy **REVISE×8**; spec **GAP**; **PASS=0** |
| S3 | 10 Director `JOB_CARDS/` | CARD + ≤10 heading; kümülatif **23** |
| S4 | STATE / plans / AUDIT / BILGI | tek satır öğrenim |
| S5 | validate / secret_scan / ethics_check | damga aşağıda |
| S6 | Bu rapor + `OZET-TEK-SAYFA-LIVE.md` | Europe/Istanbul |

**Kalan onaylı dilim (hâlâ DEVAM):**

| ID | İş | Sa |
|----|-----|-----|
| A9 | Director/EVP +10 skeleton (yine ≤10 H) | 4–8 |
| A10 | COMPLIANCE CIS IG1 **kanıt sütunu** (PASS uydurma yok) | 3–6 |
| A11 | LATOS 72 silinmiş **katalog** (restore değil) | 2–4 |
| A12 | Agency: S03–S08 kanal-özel hook (marka yokken hâlâ REVISE) | 4–8 |
| A13 | Skill ~20k kısmi derinlik (6 skill) | 6–12 |

**Kalan onaylı bant:** **19–38 sa**. Merge/restore/CANVA/IMPLEMENT yok.

---

## 4) SENDE — SONRAKİ ADIMLAR (onay / bağımlılık)

| ID | İş | Blok | Sa |
|----|-----|------|-----|
| B3+ | ISO SoA 93 / #39 içeriği | **#39 review**; #38’e kopyalama | 8–16 |
| B4 | Skill 20k tam set | — | 16–32 |
| B5 | IR playbook ASSESS (Faz 6) | — | 6–12 |
| B6 | 72 rol git restore | **Metin restore** | 2–6 |
| B7 | 633 JOB_CARDS skeleton | A9 sonrası | 70–150 |
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
| **Security** | 5 INDEX | INDEX var · SoA yok | **~20%** Faz 5 | **8–16** (IG1/GV.RM; 93 SoA değil) |
| **Security** | 6–8 | IR/skill/QA | **~8%** | **30–60** |
| **LATOS** | 0–1 | 633 envanter · 72 restore 0 | keşif **~90%** / restore **0%** | doküman **2–4** |
| **LATOS** | 4 kart | **23/633** skeleton · 10/200 H | kart **3,6%** · başlık **≪1%** (230 / 126 600) | +10 kart **4–8** · 633 skeleton **70–150** · 200H×633 **400–800+** |
| **LATOS** | 8–9 | 122 prompt / 200 tahmin | **0%** | 20-title kesit **16–40**; 900M char **🚩 0 sa — imkânsız** |

### Toplam bant

| Sahip | Bu tur (yapıldı) | Kalan onaylı DEVAM | 3-hat derinlik (600 stub + 633 skeleton + agency Canva’sız) | Yapılmayacak |
|-------|------------------|--------------------|--------------------------------------------------------------|--------------|
| **Metin** | Secrets + PR bakışı **0,8–2 sa** | aynı + marka 1–3 | — | — |
| **Agent** | INDEX+QA+10 kart **~4–8 sa** eşdeğeri | **19–38 sa** | **~200–400 sa** | 633×200 dolu **400–800+**; 900M **imkânsız** |

---

## 6) Metin — tek satır sonraki aksiyon

**Cursor Secrets’a Gemini+OpenRouter koy → yeni chat `/devam` `/sec-devam` `/latos-devam` → [#38](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38) review; [#35](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35)/[#34](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34) triyaj; CANVA:ON / IMPLEMENT / 72 restore kapalı.**
