# TEK SAYFA İŞ LİSTESİ — 2026-11-04 (Europe/Istanbul)

> Damga: **2026-11-04 14:40 TRT** (`Europe/Istanbul`, `2026-11-04T11:40:00Z`)  
> Repo: [`metinduraktr-44/claude-otonom-sistem`](https://github.com/metinduraktr-44/claude-otonom-sistem) · Kanıt: `gh pr list` canlı  
> Bu ajan: [bc-05fbb414…](https://cursor.com/agents/bc-05fbb414-736b-554d-81d7-afcf4a22ca9d) · Önceki rapor: [bc-415e4b83…](https://cursor.com/agents/bc-415e4b83-e90f-56de-bfb9-b77d0ac33073)  
> FAZ6 **bu PR’da yok** (kardeş [#39](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39) · `cursor/giga-security-faz6-6a77`). 🚩 900B/900M tek dosya **RED**.  
> LLM: `GEMINI_API_KEY` / `OPENROUTER_API_KEY` **UNSET** → skeleton. `ANTHROPIC_API_KEY` env SET (değer raporlanmaz); bakiye bu turda sorgulanmadı — önceki tur kredi **0**.

## 1. Sinyal

| Alan | Canlı (`gh` + dosya, 2026-11-04T11:34Z) |
|------|--------|
| `main` | `cc8b6b79` holding-konsolide 2026-11-04 07:10Z (nightly/daily 11-04 koştu) |
| Açık PR | **9** — tablo §3; draft: #34 #36 #38 |
| Bu PR | [#37](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37) OPEN · **draft=false** · base=`main` · validate **SUCCESS** (2026-11-04 push) · **MERGEABLE/CLEAN** (`origin/main` merge bu tur) |
| FAZ6 | [#39](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39) OPEN · draft=false · **CONFLICTING** · SoA/CTRL **çiftlenmedi** |
| Mega draft | [#38](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38) DRAFT · CONFLICTING · 600 kontrol/S03–S08/LATOS 13 — 🚩 tek PR |
| Merged GIGA | **#19–#30** MERGED |
| Agency | Faz 5 · `CANVA:BRIEF-ONLY` · S01–S02 brief var · S03–S08 yok · `CONTEXT/{BRAND,PRODUCT,VOICE}.md` TODO |
| Security | Matris **120/600** · `MODE=ASSESS-ONLY` · FAZ6 içerik yalnızca #39 |
| LATOS | **633** title (`ROSTER/TITLE_INVENTORY.md`) · iş kartı **3/633** (`CISO`, `hq-ceo`, `adops-ceo`) · 72 silinmiş restore **onaysız** |

### Açık PR gerçek durum

| PR | Draft | mergeable | Base ← head | Öneri |
|----|-------|-----------|-------------|-------|
| [#39](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39) FAZ6 SoA | hayır | CONFLICTING | main ← `giga-security-faz6-6a77` | **MERGE** (conflict UI) |
| [#38](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38) mega DEVAM | **evet** | CONFLICTING | main ← `giga-devam-8e8f` | **CLOSE** |
| [#37](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37) bu rapor | hayır | **MERGEABLE** | main ← `tek-sayfa-is-listesi-6a77` | **MERGE** |
| [#36](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/36) iş-listesi çift | **evet** | MERGEABLE | main ← `is-listesi-rapor-8e8f` | **CLOSE** |
| [#35](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35) CC güvenlik ingest | hayır | CONFLICTING | main ← `claude-code-guvenlik-uyarilari-6a77` | **MERGE** (conflict UI) |
| [#34](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34) ingest draft | **evet** | CONFLICTING | main ← `claude-code-security-ingest-8e8f` | **CLOSE** |
| [#33](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33) setup-python 5→7 | hayır | MERGEABLE | main ← dependabot GHA | **MERGE** veya **WAIT** |
| [#32](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/32) tek sayfa 09-02 | hayır | MERGEABLE | main ← `tek-sayfa-rapor-12ed` | **CLOSE** |
| [#31](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/31) katalog npm | hayır | MERGEABLE | main ← dependabot yarn | **CLOSE** |

`gh pr create/edit/merge` ajan **403**. Merge/close = Metin GitHub UI.

---

## 2. METİN YAPACAKLAR

| # | Öncelik | Eylem | Yönlendirme URL | Kısa not |
|---|---------|--------|-----------------|----------|
| M1 | **P0** | `GEMINI_API_KEY` ekle (Cursor Secrets; yedek GHA) | [Cursor Cloud Agents / Secrets](https://cursor.com/dashboard?tab=cloud-agents) · [Google AI Studio — API key](https://aistudio.google.com/apikey) · [Repo Actions Secrets](https://github.com/metinduraktr-44/claude-otonom-sistem/settings/secrets/actions) | Env’de Gemini/OpenRouter **yok** → nightly/günlük **iskelet**. Değeri chate yapıştırma. Smoke: `python3 scripts/gemini_client.py smoke`. |
| M2 | P1 | OpenRouter yedek | [OpenRouter keys](https://openrouter.ai/keys) · [Cursor Secrets](https://cursor.com/dashboard?tab=cloud-agents) | Sıra Gemini → OpenRouter → Anthropic. Anthropic env var var; kredi 0 ise skeleton kalır. |
| M3 | P1 | Canva MCP OAuth (opsiyonel) | [Canva MCP](https://mcp.canva.com/mcp) · Cursor **Settings → MCP → Authorize** · PKCE: [`tools/canva-client/README.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/tools/canva-client/README.md) | Varsayılan **BRIEF-ONLY**. OAuth yok → tasarım mutate yok. |
| M4 | P1 | Marka kit bırak | [CONTEXT/INBOX](https://github.com/metinduraktr-44/claude-otonom-sistem/tree/main/CONTEXT/INBOX) · [BRAND](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/CONTEXT/BRAND.md) · [PRODUCT](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/CONTEXT/PRODUCT.md) · [VOICE](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/CONTEXT/VOICE.md) | Stub `_TODO`. Kit yoksa AdOps CRE seed. Ajan INBOX’ı uyduramaz. |
| M5 | P2 | Cursor restart + `/devam` smoke | Bu ajan: [bc-05fbb414](https://cursor.com/agents/bc-05fbb414-736b-554d-81d7-afcf4a22ca9d) · [Cloud Agents](https://cursor.com/dashboard?tab=cloud-agents) | Skills/hooks yeni chat’te. 900M paste **RED**. |
| M6 | P2 | Gemini kota / Cursor billing | [AI Studio](https://aistudio.google.com/apikey) · [Cursor dashboard](https://cursor.com/dashboard) | Kota 0 = dry-run. Secret sohbete koyma. |
| M7 | P2 | GHA yeşil + conflict UI | [Actions](https://github.com/metinduraktr-44/claude-otonom-sistem/actions) · [Open PRs](https://github.com/metinduraktr-44/claude-otonom-sistem/pulls) | `katalog/` **npm kurma**. #35/#39 CONFLICTING — merge ekranında çöz. |

---

## 3. METİN ONAYLAYACAKLAR

| # | PR / karar | URL | Kısa not | Önerilen karar |
|---|------------|-----|----------|----------------|
| A1 | #35 Claude Code güvenlik ingest | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35 | ASSESS-ONLY; **CONFLICTING** vs 11-04 `main` | **MERGE** (conflict çöz) |
| A2 | #34 draft (aynı ingest) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34 | #35 supersede | **CLOSE** |
| A3 | #37 bu iş listesi | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37 | URL+not + adam-saat; FAZ6 yok; draft=false | **MERGE** |
| A4 | #36 çift iş-listesi draft | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/36 | Dal `is-listesi-rapor-8e8f`; MERGEABLE | **CLOSE** |
| A5 | #39 FAZ6 ISO SoA | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39 | Kardeş PR; SoA iskelet; **CONFLICTING**; bu dosyaya kopyalanmadı | **MERGE** (conflict çöz) |
| A6 | #38 mega DEVAM draft | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38 | 600 kontrol + brief + LATOS tek PR · 🚩 · CONFLICTING | **CLOSE** |
| A7 | #32 tek sayfa 2026-09-02 | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/32 | Stale; bu dosya güncel | **CLOSE** |
| A8 | #31 Dependabot `katalog/` npm | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/31 | Vendored örnek; ürün dep değil | **CLOSE** (SKIP npm) |
| A9 | #33 `actions/setup-python` 5→7 | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33 | Leftover: `skill-ajans-dongu.yml` hâlâ `@v5`; diğerleri `@v7` (#30) | **MERGE** veya **WAIT** (5 dk) |
| A10 | 72 `uretim/rol-kartlari` restore | [`LATOS/STATE.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/LATOS/STATE.md) | Otomatik restore yok | **WAIT** |
| A11 | `CANVA:ON` | `/canva-uret` + [mcp.canva.com/mcp](https://mcp.canva.com/mcp) | OAuth + kit sonrası | **WAIT** |
| A12 | Security `MODE=IMPLEMENT` | [`SECURITY/STATE.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/SECURITY/STATE.md) | #39 ethics PASS şart; exploit yok | **WAIT** |

---

## 4. AJAN YAPACAKLAR + ONAYLANANLAR

### Ajan iş

| # | Faz | İş | Bağımlılık | Durum |
|---|-----|-----|------------|--------|
| S0 | Rapor | Tek sayfa yenile (URL+not+saat) | `gh pr list` | **bu PR #37** |
| S1 | Sec FAZ6 | ISO SoA iskelet, ASSESS-ONLY | Ethics/secret-redakte | **#39** — burada yok |
| S2 | Sec FAZ4+ | Kontroller 021–100 × 6 (→600) | S1; MODE=ASSESS | Bekler; #38 **yapmaz** |
| S3 | Sec skill | 6 motor ~20k derinlik | S2 paralel | Kısmi 6 skill |
| S4 | LATOS FAZ4 | 10 title iş kartı (`/is-karti`) | 633 envanter; A10 opsiyonel | **3/633** |
| S5 | LATOS FAZ2–3 | RESEARCH + `ORG/ORG_CHART` | Plan | İçerik yok |
| S6 | Agency | S03–S08 brief + critic PASS | M4 kit yoksa seed | S01–S02 var |
| S7 | Agency CONTEXT | BRAND/PRODUCT/VOICE doldur | **M4 INBOX** | Stub TODO |
| S8 | Canva ops | İlk export (yalnızca CANVA:ON) | M3 + A11 | Kapalı |
| S9 | Holding | Nightly/daily iskelet → LLM dolu | **M1 secret** | 11-04 hâlâ Generation: off |

### Onaylananlar (merged / kilit)

| Kanıt | URL | Not |
|-------|-----|-----|
| Live terminal | [#19](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/19) | AUDIT parse hotfix |
| CILT12 MEGA | [#22](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/22) | 900k paste RED |
| Agency GIGA | [#23](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/23) [#24](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/24) | **MERGED** · BRIEF-ONLY |
| Security GIGA | [#25](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/25) [#26](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/26) | **MERGED** · 120/600 defense-only |
| LATOS GIGA | [#27](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/27) [#28](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/28) | **MERGED** · 633 title |
| Hotfix + rapor | [#29](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/29) | MEGA marker |
| setup-python (çoğu) | [#30](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/30) | Leftover = #33 |
| Guardrail | `STATE.md` Security | ASSESS-ONLY · exploit yok · secret `${VAR}` |

---

## 5. ROADMAP — adam-saat (takvim gün/hafta yok)

M = Metin · S = Ajan. Aralık = belirsizlik.

| Faz | Çıktı | Adam-saat (Metin / Ajan) | Kapı |
|-----|--------|---------------------------|------|
| P0 onay | #35+#37+#39 MERGE; #34/#36/#38/#32/#31 CLOSE; #33 leftover | **0.6–1.0 M** / 0 | GitHub UI; #35/#39 conflict |
| P0 secret | Gemini (veya OpenRouter) + `gemini_client.py smoke` | **0.25–0.5 M** / **0.25 S** | Cursor Secrets; chate key yok |
| P0 restart | Skill keşif + `/devam` duman | **0.1 M** / 0 | Yeni Agent chat |
| Sec FAZ6 | SoA okuma / COMPLIANCE | **0.25 M** / **0 S bu dal** | İş #39’da |
| Sec MODE | `IMPLEMENT` kararı | **0.25 M** / 0 | Ethics PASS + A12 |
| Sec 021–100 | 480 kontrol fazlı (→600) | 0 / **40–80 S** | Tek oturumda bitmez; #38 kapat |
| Sec skill | ~20k × 6 motor | 0 / **12–24 S** | P2 |
| LATOS FAZ4 | 10 kart pilot | 0 / **6–12 S** | `/is-karti` · şimdi 3/633 |
| LATOS restore | 72 rol-kart (onaylıysa) | **0.5 M** / **2–6 S** | A10 evet |
| LATOS FAZ2–3 | Research + org chart | 0 / **4–8 S** | Plan |
| Agency kit | INBOX marka | **0.5–2 M** / 0 | Dosya Metin |
| Agency CONTEXT | BRAND/PRODUCT/VOICE | 0 / **3–6 S** | M4 |
| Agency brief | S03–S08 + critic | 0 / **4–8 S** | Seed veya kit |
| Canva OAuth | MCP authorize | **0.5–1 M** / 0 | İsteğe bağlı |
| Canva ON | İlk export | **0.25 M** / **2–4 S** | M3+A11 |
| Rapor bu tur | URL+not yenileme + main merge | 0 / **0.5–1 S** | Bu PR |

**Toplam (bu ufuk):** Metin **~2.2–6.6 saat** (P0 ≈ 1.1 saat; kit+OAuth opsiyonel). Ajan **~74–149 saat** (büyük kısım 021–100 + skill; fazlı). FAZ6 ajan-saati #39’da sayılır, burada 0.

**Bu PR kapsamı:** doküman + append-only log + `main` merge. FAZ6 SoA/CTRL **yok**.

---

## 6. Hızlı linkler

| Ne | URL |
|----|-----|
| Repo | https://github.com/metinduraktr-44/claude-otonom-sistem |
| Open PRs | https://github.com/metinduraktr-44/claude-otonom-sistem/pulls |
| #37 bu rapor | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37 |
| #39 FAZ6 MERGE | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39 |
| #35 MERGE | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35 |
| #38 CLOSE mega | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/38 |
| #36 CLOSE çift | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/36 |
| Cursor Secrets | https://cursor.com/dashboard?tab=cloud-agents |
| Gemini key | https://aistudio.google.com/apikey |
| GHA Secrets | https://github.com/metinduraktr-44/claude-otonom-sistem/settings/secrets/actions |
| Canva MCP | https://mcp.canva.com/mcp |
| INBOX | https://github.com/metinduraktr-44/claude-otonom-sistem/tree/main/CONTEXT/INBOX |
| Bu ajan | https://cursor.com/agents/bc-05fbb414-736b-554d-81d7-afcf4a22ca9d |

⏱️ Damga: 2026-11-04T11:40:00Z (14:40 Europe/Istanbul) · 🔍 Denetim: GEÇTİ (`gh pr list` + dosya; kod/exploit yok) · 📚 Öğrenim: açık kuyruk **9 PR** (+#38 CLOSE mega, +#39 FAZ6 MERGE); #37 **MERGEABLE/CLEAN**; Gemini hâlâ yok · 🔗 Önceki: evet (`bc-415e4b83`, `uretim/TEK-SAYFA-IS-LISTESI.md` 15:05 TRT 2026-11-03)
