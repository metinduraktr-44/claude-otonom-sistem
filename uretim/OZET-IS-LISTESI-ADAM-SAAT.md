# İŞ LİSTESİ + ROADMAP (ADAM-SAAT)

> **Damga:** 2026-11-03 14:45 Europe/Istanbul (UTC 11:45)  
> **Kaynak:** `main` `0ec1a921` · açık PR gh · STATE / plans / TASKS / ROSTER / matrix  
> **Dal bu rapor:** `cursor/is-listesi-rapor-8e8f` (giga-devam’a dokunulmadı)  
> **MODE:** Agency BRIEF-ONLY · Security **ASSESS-ONLY** · CANVA:OFF  
> **Kırmızı çizgi:** 900M char / 633×200 başlık tek tur = **imkânsız**. Saatler aralık + % tamam.

Kurul: Baş Mimar + İş/Gelir + Denetçi. Varsayım: “DEVAM ET” = onaylı agent devam (PR merge / git-restore / CANVA:ON / IMPLEMENT **hariç**).

---

## 0) Snapshot (İstanbul)

| Madde | Değer | İstanbul |
|-------|--------|----------|
| Rapor anı | 2026-11-03T11:45:21Z | **14:45 +03** |
| main HEAD | `0ec1a921` holding-konsolide | 03 Kas 10:10 +03 |
| Son nightly | 2026-11-03T00:02:58Z | **03:02 +03** · Generation: off |
| daily-agency | 2026-11-03T06:17:21Z | **09:17 +03** · `SEC-OPS` iskelet |
| STATE Agency | 2026-08-27T13:01:29Z | 27 Ağu 16:01 +03 · Faz 5 seed |
| STATE Security | 2026-08-27T13:05:00Z | 27 Ağu 16:05 +03 · 120/600 |
| STATE LATOS | 2026-08-27T20:20:00Z | 27 Ağu 23:20 +03 · Faz 0–1 |
| LIVE özet | 2026-09-02T20:50:00Z | 02 Eyl **23:50 +03** · **bayat** (açık PR “yok” diyor — yanlış) |
| PR #34 | draft · 10:01Z | **13:01 +03** |
| PR #35 | open · 10:02Z | **13:02 +03** |
| `STATE_SECURITY.md` | yok | `SECURITY/STATE.md` + `STATE.md` |

**Envanter (ölçülen):** ROSTER 633 title · git-silinmiş **72** · JOB_CARDS **3** dizin (hq-ceo, adops-ceo, CISO; CISO H001–H005/200) · BRIEFS **6** (S01–S02 × 3 kanal) · INBOX **boş** · kontroller **120/600** (6 motor × 001–020) · COMPLIANCE iskelet boş.

**Açık PR:** [#35](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35) · [#34](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34) (draft, #35 ile örtüşür) · [#33](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33) (setup-python; **#30 merged** — muhtemel duplicate) · [#32](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/32) (Eyl merge raporu, bayat) · [#31](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/31) (dependabot npm katalog örneği).

---

## 1) BENDE (Metin) — YAPACAKLARIM

| # | Aksiyon | Neden | URL / komut | Sa |
|---|---------|-------|-------------|-----|
| M1 | **Cursor Secrets** | LLM dry-run kalkmaz; nightly generation off | [cursor.com/dashboard](https://cursor.com/dashboard) → Secrets: `GEMINI_API_KEY`, `OPENROUTER_API_KEY` | 0,2–0,4 |
| M2 | **Gemini rotate** | Eski key chat ifşa riski (önceki tur notu) | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) | 0,1–0,2 |
| M3 | **OpenRouter key** | Gemini fallback (PR #16 merged, runtime key yok) | [openrouter.ai/keys](https://openrouter.ai/keys) | 0,1–0,2 |
| M4 | **Cursor restart + 3 slash** | Rules/skills yükle; Faz kilidi smoke | Yeni chat → `/devam` · `/sec-devam` · `/latos-devam` | 0,2–0,4 |
| M5 | **Marka kit → INBOX** | Agency TBD; S03–S08 müşteri kilidi yok | repo `CONTEXT/INBOX/` (PDF/logo/brief) | 1–3 |
| M6 | **Canva OAuth** (opsiyonel) | Yalnızca CANVA:ON sonrası; şimdi BRIEF-ONLY | [canva.com/developers](https://www.canva.com/developers/) · `tools/canva-client/` · `CANVA_CLIENT_ID/SECRET` | 0,5–1,5 |

**Bu tur Metin operasyon (M1–M4 zorunlu, M5 değer kilidi):** **0,6–1,2 sa** (+ marka 1–3).

---

## 2) BENDE — ONAYLAYACAKLARIM

İnsan kapısı. Agent **DEVAM** ile bunları yapmaz.

| # | Kapı | Karar | URL | Sa |
|---|------|-------|-----|-----|
| O1 | **PR #35** güvenlik ingest (PDF/DOCX) | Review → merge veya kapat (#34 ile birleştir) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35 | 0,3–0,6 |
| O2 | **PR #34** (draft, aynı tema) | Ready + merge **veya** #35 lehine kapat | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34 | 0,2–0,4 |
| O3 | **PR #33** setup-python 5→7 | #30 zaten merged (1 Eyl). Duplicate ise **kapat** | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33 | 0,1 |
| O4 | **PR #32** tek sayfa rapor (2 Eyl) | Bayat; kapat veya bu raporla değiştir | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/32 | 0,1 |
| O5 | **PR #31** dependabot npm (katalog örnek app) | İsteğe bağlı; holding runtime değil | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/31 | 0,2–0,4 |
| O6 | **72 git-silinmiş rol** restore | `uretim/rol-kartlari/*.md` · otomatik restore **yasak** | Envanter: `ROSTER/TITLE_INVENTORY.md` | 0,2 onay + agent 2–6 |
| O7 | **CANVA:ON** | Varsayılan BRIEF-ONLY. Açılmazsa tasarım/export yok | `STATE.md` CANVA bloğu | 0,1 |
| O8 | **MODE=IMPLEMENT** vs ASSESS-ONLY | Security varsayılan ASSESS-ONLY. IMPLEMENT = kod/CI sertleştirme izni | `STATE.md` / `SECURITY/STATE.md` | 0,1 |
| O9 | Bu rapor PR | `cursor/is-listesi-rapor-8e8f` merge | (push sonrası PR) | 0,1 |

**Onay turu (O1–O5 + O6–O8 bayrak):** **1–2 sa**.

---

## 3) SENDE (agent) — ONAYLI (DEVAM; ekstra onay yok)

Kapsam: doküman / ASSESS / brief-seed / skeleton. **Merge, restore, CANVA, IMPLEMENT yok.**

| ID | İş | Track | Sa (kalan, bu dilim) |
|----|-----|-------|----------------------|
| A1 | Controls **021–040** × 6 motor + matrix satır (ASSESS stub, 001–020 kalitesi) | Security | 8–14 |
| A2 | GHA permissions + pin-gap **ASSESS notu** (kod pin’i yok) | Security | 2–4 |
| A3 | LATOS Faz 1 kapanış: 72 silinmiş **katalog** (restore değil) | LATOS | 2–4 |
| A4 | LATOS Faz 2: `RESEARCH/_ORG_BEST_PRACTICE.md` seed | LATOS | 3–6 |
| A5 | JOB_CARDS **10 title pilot** skeleton (CARD+INDEX; 200 başlık değil) | LATOS | 6–12 |
| A6 | Agency S03–S08 brief × 3 kanal — **AdOps CRE TBD** (marka yokken proxy) | Agency | 8–14 |
| A7 | critic-copy/spec **hafif PASS** S01–S02 mevcut 6 brief | Agency | 2–4 |
| A8 | `uretim/OZET-TEK-SAYFA-LIVE.md` yenile — **giga-devam çakışmazsa** | Docs | 0,5–1 |

**Onaylı dilim toplam:** **32–59 sa** agent.

Paralel kural: Security motor dizinleri izole; LATOS `JOB_CARDS/{slug}/`; Agency `BRIEFS/`. giga-devam aynı dosyaya yazarsa **çekil**.

---

## 4) SENDE — SONRAKİ ADIMLAR (onay veya bağımlılık)

| ID | İş | Blok | Sa (sonra) |
|----|-----|------|------------|
| B1 | Controls 041–100 × 6 (360 kontrol) | — ASSESS-ONLY yeter; IMPLEMENT değil | 24–48 |
| B2 | Controls 101–100 tamam → **600/600** | B1; kalite çubuğu düşmesin | +16–32 |
| B3 | COMPLIANCE pack NIST/CIS/ISO/SOC2 | Faz 5 kapısı | 8–16 |
| B4 | Skill ~20k derinlik (6 kısmi + 14) | Faz 7 | 16–32 |
| B5 | Detection/IR playbook ASSESS | Faz 6 | 6–12 |
| B6 | 72 rol **git restore** | **O6 Metin** | 2–6 |
| B7 | 633 JOB_CARDS skeleton (CARD.md only) | Pilot A5 sonrası | 80–160 |
| B8 | 200 başlık × kart (H001–H200) | B7; **büyük** — seçilmiş 20 title önce | 20 title: 40–80 · 633 title: **400–800+** |
| B9 | 122 prompt/title | Faz 8; 🚩 900M RED | 20 title: 16–32 |
| B10 | Canva PKCE + MCP smoke | **O7 CANVA:ON** + M6 | 8–16 |
| B11 | Faz 6–7 üretim pipeline (export/delivery) | B10 | 16–32 |
| B12 | LLM live (dry-run kalk) | **M1–M3 secrets** | 1–2 |
| B13 | MODE IMPLEMENT: pin GHA, permissions, scanner CI | **O8** | 8–16 |
| B14 | PR #34/#35 conflict çöz + main | **O1–O2** | 1–2 |

---

## 5) ROADMAP + ADAM-SAAT (kalan)

Tamam % = mevcut teslim / dürüst hedef (iskelet), **karakter bombası değil**.

| Track | Faz | Durum | % | Kalan sa | Not |
|-------|-----|-------|---|----------|-----|
| **Agency** | 0–5 seed | S01–S02 brief ✅ · S03–S08 ⏳ | ~35% pipeline | **12–22** (TBD marka) | Marka kit yok → özelleştirme kilit |
| **Agency** | 4 Canva | BRIEF-ONLY · OAuth skeleton | 10% Canva | **8–16** post-O7 | CANVA:ON insan |
| **Agency** | 6–7 prod | Archive + bulk export | 0% | **16–32** | B10’a bağlı |
| **Security** | 0–4 | 120/600 · 6 skill kısmi | **20%** kontrol | **8–14** (021–040) | Bu DEVAM dilimi |
| **Security** | 4 kalan | 480 kontrol | 20%→100% | **40–80** | Stub kalitesi; roman değil |
| **Security** | 5–8 | COMPLIANCE/IR/QA | ~5% | **30–60** | ASSESS |
| **LATOS** | 0–1 | 633 envanter ✅ · 72 restore ⏳ | ~90% keşif / 0% restore | **2–4** doküman | Restore = O6 |
| **LATOS** | 2–3 | Research + org | ~5% | **7–14** | A4 + org chart |
| **LATOS** | 4 kart | 3/633 dizin · 5/200 başlık (1 kart) | **0,5%** kart · **≪1%** başlık | Pilot **6–12** · 633 skeleton **80–160** · 200H×633 **400–800+** | 200H tam set **bu çeyrek hedefi değil** |
| **LATOS** | 8–9 | 122 prompt · 200 tahmin/gün | 0% | fazlı, 20-title kesit **16–40** | 900M char **🚩 RED** |
| **Ops** | nightly | validate+damga yeşil; gen off | — | **1–2** secrets sonrası | 03 Kas 03:02 +03 |
| **Docs/PR** | ingest | #34/#35 açık | — | Metin 0,5–1 | Agent merge etmez |

### Toplam (dürüst bant)

| Sahip | Bu DEVAM dilimi | Sonraki kapı (onaysız teknik) | Tam 3-hat “derinlik” (seçilmiş kesit + 600 kontrol stub + 633 skeleton) | Yapılmayacak |
|-------|-----------------|-------------------------------|------------------------------------------------------------------------|--------------|
| **Metin** | **2–5 sa** (M1–M4 + O1–O8) | +1–3 sa marka kit | aynı | — |
| **Agent** | **32–59 sa** (A1–A8) | **+90–170 sa** (B1–B5, B12 kısmi) | **~220–430 sa** (600 kontrol + 633 skeleton + agency Faz7 Canva’sız) | 633×200 başlık dolu ≈ **400–800+ sa daha**; 900M char **0 sa — imkânsız** |

**Önerilen kesit (değer/saat):** 10 JOB_CARDS + controls 021–040 + S03–S08 TBD brief = **32–59 sa**. 633×200’e **girme**.

---

## 6) Metin — tek satır sonraki aksiyon

**Cursor Secrets’a Gemini+OpenRouter koy → yeni chat `/devam` `/sec-devam` `/latos-devam` → [#35](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35) review; 72 restore / CANVA:ON / IMPLEMENT kapalı tut.**

---

## Denetçi

| Katman | Sonuç |
|--------|--------|
| Structural | 6 bölüm + saat tablosu + URL |
| Integrity | PR/HEAD gh+git; 120/600 matrix; 633/72 ROSTER; 3 JOB_CARDS |
| Semantic | adam-saat; takvim günü yok; 900M RED |
| Reference | STATE 27 Ağu; LIVE 2 Eyl bayat — bu rapor güncel |
| Patterns | ASSESS-ONLY · BRIEF-ONLY · restore insan |
| Review | GEÇTİ — giga-devam’a yazılmadı; LIVE header güncellenmedi (çakışma) |

⏱️ Damga: 2026-11-03 14:45 Europe/Istanbul · 🔍 Denetim: GEÇTİ · 📚 Öğrenim: Açık PR 5 (#35/#34 asıl; #33 muhtemel dup #30); agent onaylı dilim 32–59 sa, 633×200 ayrı bant · 🔗 Önceki: evet (LIVE 2 Eyl + STATE 27 Ağu)
