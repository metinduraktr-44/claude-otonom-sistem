# TEK SAYFA İŞ LİSTESİ — 2026-11-15 (Europe/Istanbul)

> Damga: **2026-11-15 13:05 TRT** (`Europe/Istanbul`, `2026-11-15T10:05:00Z`)  
> Repo: [`metinduraktr-44/claude-otonom-sistem`](https://github.com/metinduraktr-44/claude-otonom-sistem) · Kanıt: `gh pr list` canlı  
> Bu ajan: [bc-d8693b81…](https://cursor.com/agents/bc-d8693b81-e243-50e9-b06b-98ca49308b99) · Önceki rapor: [bc-ce8671ca…](https://cursor.com/agents/bc-ce8671ca-49c0-5253-87e5-d7b5218f6d3a)  
> FAZ6 **bu PR’da yok** (kardeş [#39](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39)).  
> 🚩 **900.000.000 karakter tek prompt fiziksel imkânsız / RED.** Hedef korunur: `PROMPTS/{TITLES,TEAMS,EXECUTION}/` 4–12 KiB sözleşme + `P001.md`… Fazlı. 900k+ tek dosya **yazılmadı**.  
> LLM: `GEMINI_API_KEY` / `OPENROUTER_API_KEY` **UNSET** → skeleton. `ANTHROPIC_API_KEY` env SET (değer yok).  
> Merge: ajan `gh` write **403**. Onaylı merge listesi aşağıda; **gerçek merge = Metin GitHub UI**.

## 1. Sinyal

| Alan | Canlı (`gh` + dosya, 2026-11-15T10:00Z) |
|------|--------|
| `main` | `ee498f1f` holding-konsolide **2026-11-15T07:09:09Z** |
| Açık PR | **9** — §3 |
| Bu PR | [#37](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37) OPEN · **draft=false** · title `docs: tek sayfa iş listesi 2026-11-15` · **MERGEABLE/CLEAN** |
| FAZ6 | [#39](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39) **CONFLICTING** · SoA **kopyalanmadı** |
| Mega draft | [#38](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38) DRAFT · CONFLICTING · 🚩 tek PR |
| Merged GIGA | **#19–#30** MERGED |
| Agency | Faz 5 · `CANVA:BRIEF-ONLY` · S01–S02 · S03–S08 yok |
| Security | Matris **120/600** · `MODE=ASSESS-ONLY` · FAZ6 yalnızca #39 |
| LATOS | **633** title · iş kartı **13** klasör / **12** envanter slug (`qa_check` **621** eksik) · yetenek INDEX **101** · hq-ceo **122 slot + P001–P003** · 72 restore **onaysız** |

### Açık PR gerçek durum

| PR | Draft | mergeable | Base ← head | Öneri |
|----|-------|-----------|-------------|-------|
| [#39](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39) FAZ6 SoA | hayır | CONFLICTING | `giga-security-faz6-6a77` | **MERGE** (conflict UI) |
| [#38](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38) mega DEVAM | **evet** | CONFLICTING | `giga-devam-8e8f` | **CLOSE** |
| [#37](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37) bu rapor + LATOS pilot | hayır | **MERGEABLE / CLEAN** | `tek-sayfa-is-listesi-6a77` | **MERGE** |
| [#36](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/36) iş-listesi çift | **evet** | MERGEABLE / CLEAN | `is-listesi-rapor-8e8f` | **CLOSE** |
| [#35](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35) CC güvenlik ingest | hayır | CONFLICTING | `claude-code-guvenlik-uyarilari-6a77` | **MERGE** (conflict UI) |
| [#34](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34) ingest draft | **evet** | CONFLICTING | `claude-code-security-ingest-8e8f` | **CLOSE** |
| [#33](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33) setup-python 5→7 | hayır | MERGEABLE / CLEAN | dependabot GHA | **MERGE** veya **WAIT** |
| [#32](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/32) tek sayfa 09-02 | hayır | MERGEABLE / CLEAN | `tek-sayfa-rapor-12ed` | **CLOSE** |
| [#31](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/31) katalog npm | hayır | MERGEABLE / CLEAN | dependabot yarn | **CLOSE** |

`gh pr create/edit/merge` ajan **403**. Close için `set_pr_status` kullanılmadı (kullanıcı CLOSE önerisi verdi; merge onayı açık — PR kapatılmadı).

---

## 2. METİN YAPACAKLAR

| # | Öncelik | Eylem | Yönlendirme URL | Kısa not |
|---|---------|--------|-----------------|----------|
| M1 | **P0** | `GEMINI_API_KEY` ekle | [Cursor Secrets](https://cursor.com/dashboard?tab=cloud-agents) · [AI Studio](https://aistudio.google.com/apikey) · [GHA Secrets](https://github.com/metinduraktr-44/claude-otonom-sistem/settings/secrets/actions) | 11-15 günlük hâlâ iskelet. Key’i chate yapıştırma. `python3 scripts/gemini_client.py smoke`. |
| M2 | P1 | OpenRouter yedek | [OpenRouter keys](https://openrouter.ai/keys) | Sıra Gemini → OpenRouter → Anthropic. |
| M3 | P1 | Canva MCP OAuth (opsiyonel) | [Canva MCP](https://mcp.canva.com/mcp) · [`tools/canva-client/README.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/tools/canva-client/README.md) | Default **BRIEF-ONLY**. |
| M4 | P1 | Marka kit | [INBOX](https://github.com/metinduraktr-44/claude-otonom-sistem/tree/main/CONTEXT/INBOX) · [BRAND](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/CONTEXT/BRAND.md) | Stub `_TODO`. Ajan uyduramaz. |
| M5 | P2 | Restart + `/latos-devam` | [Bu ajan](https://cursor.com/agents/bc-d8693b81-e243-50e9-b06b-98ca49308b99) | 900M paste **RED**. |
| M6 | P2 | Kota / billing | [Cursor dashboard](https://cursor.com/dashboard) | Kota 0 = dry-run. |
| M7 | P0 | GitHub UI merge/close | [Open PRs](https://github.com/metinduraktr-44/claude-otonom-sistem/pulls) | #37 CLEAN MERGE. #35/#39 conflict UI. #34 #36 #38 #32 #31 CLOSE. #33 MERGE/WAIT. `katalog/` npm yok. |
| M8 | P2 | Expert seed onay | [`EXPERTS/adops-ceo/top100_SEED.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/cursor/tek-sayfa-is-listesi-6a77/EXPERTS/adops-ceo/top100_SEED.md) | IAB URL’li `unverified`. Ranking yok. |
| M9 | P2 | 72 rol-kart restore kararı | [`LATOS/STATE.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/cursor/tek-sayfa-is-listesi-6a77/LATOS/STATE.md) | Otomatik restore yok. |

---

## 3. METİN ONAYLAYACAKLAR

| # | PR / karar | URL | Kısa not | Önerilen karar |
|---|------------|-----|----------|----------------|
| A1 | #37 iş listesi + LATOS pilot | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37 | CLEAN; FAZ6 yok; 10 kart + 101 yetenek + P001–P003 | **MERGE** |
| A2 | #35 Claude Code ingest | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35 | **CONFLICTING** | **MERGE** (conflict çöz) |
| A3 | #39 FAZ6 SoA | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39 | Kardeş; **CONFLICTING** | **MERGE** (conflict çöz) |
| A4 | #33 setup-python 5→7 | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33 | Leftover workflow pin | **MERGE** veya **WAIT** |
| A5 | #34 ingest draft | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34 | #35 supersede | **CLOSE** |
| A6 | #36 çift iş-listesi | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/36 | Draft CLEAN | **CLOSE** |
| A7 | #38 mega DEVAM | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38 | 🚩 CONFLICTING | **CLOSE** |
| A8 | #32 tek sayfa 09-02 | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/32 | Stale; bu dosya güncel | **CLOSE** |
| A9 | #31 katalog npm | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/31 | Vendored örnek | **CLOSE** |
| A10 | 72 restore | LATOS STATE | İnsan | **WAIT** |
| A11 | `CANVA:ON` | mcp.canva.com | OAuth+kit | **WAIT** |
| A12 | Security `IMPLEMENT` | SECURITY/STATE.md | Ethics PASS | **WAIT** |
| A13 | Top-100 yayın | EXPERTS/* | `unverified` | **WAIT** |

---

## 4. AJAN İŞ + ONAYLANANLAR (#19–#30)

### Ajan iş (bu tur)

| # | Faz | İş | Durum |
|---|-----|-----|--------|
| S0 | Rapor | Tek sayfa 5 tablo | **#37** |
| S4 | LATOS FAZ4 | 10 title skeleton (≥2k char) | **13 klasör / 12 slug**; qa **621/633** yok |
| S4b | LATOS FAZ5 | sourced expert stub | hq-ceo + adops-ceo `unverified` |
| S4c | LATOS FAZ6 | 101 yetenek INDEX + 2 talent stub | yazıldı |
| S4d | LATOS FAZ8 | 122 slot INDEX + P001–P003 | 🚩 900M yok |
| S4e | Loop | CALENDAR + ARCHIVE/2026-11/latos | GHA dokunulmadı |
| S1 | Sec FAZ6 | SoA | **#39** — burada yok |
| S2 | Sec 021–100 | 480 kontrol | Bekler; #38 **yapmaz** |
| S6 | Agency S03–S08 | brief | Bekler (M4) |
| S9 | Nightly LLM | iskelet→dolu | **M1** |

### Onaylananlar (merged)

| Kanıt | URL | Not |
|-------|-----|-----|
| Live terminal | [#19](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/19) | AUDIT parse |
| … | [#20](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/20) [#21](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/21) | MERGED |
| CILT12 MEGA | [#22](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/22) | 900k paste RED |
| Agency GIGA | [#23](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/23) [#24](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/24) | BRIEF-ONLY |
| Security GIGA | [#25](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/25) [#26](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/26) | 120/600 defense-only |
| LATOS GIGA | [#27](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/27) [#28](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/28) | 633 title |
| Hotfix | [#29](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/29) | MEGA marker |
| setup-python | [#30](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/30) | Leftover = #33 |

---

## 5. ROADMAP — adam-saat (takvim gün/hafta yok)

M = Metin · S = Ajan. Aralık = belirsizlik.

| Faz | Çıktı | Adam-saat (Metin / Ajan) | Kapı |
|-----|--------|---------------------------|------|
| P0 onay | #37+#35+#39 MERGE; CLOSE #34 #36 #38 #32 #31; #33 MERGE/WAIT | **0.6–1.0 M** / 0 | GitHub UI |
| P0 secret | Gemini + smoke | **0.25–0.5 M** / **0.25 S** | Cursor Secrets |
| P0 restart | `/latos-devam` duman | **0.1 M** / 0 | Yeni chat |
| LATOS FAZ4 kalan | 621 skeleton | 0 / **80–160 S** | paralel agent; tek oturum değil |
| LATOS FAZ5 | 633×100 sourced | **2–4 M onay** / **40–80 S** | unverified zorunlu |
| LATOS FAZ6 | 100 yetenek × top-N | **1 M** / **20–40 S** | INDEX 101 bitti |
| LATOS FAZ8 | 122×3 set | 0 / **30–60 S** | 4–12 KiB; 🚩 900M RED |
| Sec 021–100 | 480 kontrol | 0 / **40–80 S** | #38 kapat |
| Agency S03–S08 | brief | **0.5–2 M kit** / **4–8 S** | M4 |
| Canva ON | export | **0.5–1 M** / **2–4 S** | A11 |
| Bu tur | rapor + 10 kart + loop | 0 / **2–4 S** | #37 |

**Toplam ufuk:** Metin **~5–10 saat** (P0 ≈ 1.1; kit+OAuth+onay). Ajan **~220–440 saat** (620 kart + uzman/prompt; fazlı).

---

## 6. Sende bekleyen / bende bekleyen

| Kim | Ne | Yönlendirme |
|-----|----|-------------|
| **Sende (Metin)** | Merge/close kuyruğu | [PRs](https://github.com/metinduraktr-44/claude-otonom-sistem/pulls) — #37 MERGE · #35/#39 conflict MERGE · CLOSE #34 #36 #38 #32 #31 · #33 MERGE/WAIT |
| **Sende** | Gemini secret | [Secrets](https://cursor.com/dashboard?tab=cloud-agents) |
| **Sende** | Expert yayın / 72 restore / CANVA:ON / IMPLEMENT | WAIT kapıları §3 |
| **Bende (ajan)** | 621 JOB_CARDS · expert aylık döngü · P004–P122 · S03–S08 | Yeni chat `/latos-devam` · [bu ajan](https://cursor.com/agents/bc-d8693b81-e243-50e9-b06b-98ca49308b99) |
| **Bende** | #39 FAZ6 conflict çözümü **değil** (kardeş dal; kopyalanmaz) | [#39](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39) |

---

## 7. Hızlı linkler

| Ne | URL |
|----|-----|
| #37 | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37 |
| IAB State of Data 2025 | https://www.iab.com/wp-content/uploads/2025/03/IAB_State_of_Data_2025_March__V2.pdf |
| Bu ajan | https://cursor.com/agents/bc-d8693b81-e243-50e9-b06b-98ca49308b99 |

⏱️ Damga: 2026-11-15T10:05:00Z (13:05 Europe/Istanbul) · 🔍 Denetim: GEÇTİ (validate/qa/ethics/secret; kod/exploit yok) · 📚 Öğrenim: 633 title backlog 620; 900M RED; merge ajan 403 · 🔗 Önceki: evet (`bc-ce8671ca`)
