# TEK SAYFA İŞ LİSTESİ — 2026-11-03 (Europe/Istanbul)

> Damga: **2026-11-03 15:05 TRT** (`Europe/Istanbul`, `2026-11-03T12:05:00Z`)  
> Repo: [`metinduraktr-44/claude-otonom-sistem`](https://github.com/metinduraktr-44/claude-otonom-sistem) · Kanıt: `gh pr list` canlı  
> Bu ajan: [bc-415e4b83…](https://cursor.com/agents/bc-415e4b83-e90f-56de-bfb9-b77d0ac33073) · Önceki rapor: [bc-c972701c…](https://cursor.com/agents/bc-c972701c-f335-58b4-9f81-cf25817a0b52)  
> FAZ6 **çiftlenmedi** (kardeş: `cursor/giga-security-faz6-6a77`). 🚩 900B/900M tek dosya **RED**. LLM: Gemini/OpenRouter secret yok → skeleton; Anthropic kredi 0.

## 1. Sinyal

| Alan | Canlı |
|------|--------|
| `main` | `0ec1a921` nightly/holding 2026-11-03 07:10Z |
| Açık PR | **7** — [#37](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37) bu rapor (draft) · [#36](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/36) çift draft · [#35](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35) MERGE · [#34](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34)/[#32](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/32)/[#31](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/31) CLOSE · [#33](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33) WAIT/MERGE leftover |
| Merged GIGA | **#19–#30** — #23/#26/#27 **MERGED** (draft kapatma değil) |
| Agency | Faz 5 · `CANVA:BRIEF-ONLY` · `CONTEXT/{BRAND,PRODUCT,VOICE}.md` TODO · INBOX boş |
| Security | 120/600 · `MODE=ASSESS-ONLY` · FAZ6 ayrı dal |
| LATOS | **633** title (`ROSTER/TITLE_INVENTORY.md`) · 3 kart (`CISO`, `hq-ceo`, `adops-ceo`) · 72 silinmiş restore **onaysız** |

---

## 2. METİN YAPACAKLAR

| # | Öncelik | Eylem | Yönlendirme URL | Kısa not |
|---|---------|--------|-----------------|----------|
| M1 | **P0** | `GEMINI_API_KEY` ekle (önce Cursor Secrets; yedek GitHub Actions) | [Cursor Cloud Agents / Secrets](https://cursor.com/dashboard?tab=cloud-agents) · [Google AI Studio — API key](https://aistudio.google.com/apikey) · [Repo Actions Secrets](https://github.com/metinduraktr-44/claude-otonom-sistem/settings/secrets/actions) | Env’de Gemini/OpenRouter yok → nightly/günlük **iskelet**; değeri chate yapıştırma, smoke: `python3 scripts/gemini_client.py smoke`. |
| M2 | P1 | OpenRouter yedek (Gemini yoksa) | [OpenRouter keys](https://openrouter.ai/keys) · aynı [Cursor Secrets](https://cursor.com/dashboard?tab=cloud-agents) | Öncelik Gemini → OpenRouter → Anthropic; Anthropic kredi 0, skeleton kaçınılmaz. |
| M3 | P1 | Canva MCP OAuth (opsiyonel) | [Canva MCP](https://mcp.canva.com/mcp) · Cursor **Settings → MCP → Authorize** · PKCE: [`tools/canva-client/README.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/tools/canva-client/README.md) | Varsayılan **BRIEF-ONLY**; OAuth olmadan tasarım mutate yok. |
| M4 | P1 | Marka kit bırak | [CONTEXT/INBOX](https://github.com/metinduraktr-44/claude-otonom-sistem/tree/main/CONTEXT/INBOX) · stub: [BRAND](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/CONTEXT/BRAND.md) · [PRODUCT](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/CONTEXT/PRODUCT.md) · [VOICE](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/CONTEXT/VOICE.md) | Kit yoksa AdOps CRE seed devam; ajan CONTEXT dolduramaz. |
| M5 | P2 | Cursor restart + `/devam` smoke | Bu ajan: [bc-415e4b83](https://cursor.com/agents/bc-415e4b83-e90f-56de-bfb9-b77d0ac33073) · [Cloud Agents](https://cursor.com/dashboard?tab=cloud-agents) | Skills/hooks yeni chat’te yüklenir; 900M paste **RED**. |
| M6 | P2 | Gemini kota / Cursor billing | [AI Studio](https://aistudio.google.com/apikey) · [Cursor dashboard](https://cursor.com/dashboard) | Kota 0 = dry-run iskelet; kredi sohbetine secret koyma. |
| M7 | P2 | GHA yeşil izle | [Actions](https://github.com/metinduraktr-44/claude-otonom-sistem/actions) · [Open PRs](https://github.com/metinduraktr-44/claude-otonom-sistem/pulls) | `katalog/` npm **kurma**; ürün = stdlib Python. |

---

## 3. METİN ONAYLAYACAKLAR

| # | PR / karar | URL | Kısa not | Önerilen karar |
|---|------------|-----|----------|----------------|
| A1 | #35 Claude Code güvenlik ingest | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35 | ASSESS-ONLY; validate **SUCCESS**; mergeable | **MERGE** |
| A2 | #34 draft (aynı ingest) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34 | #35 supersede | **CLOSE** |
| A3 | #37 bu iş listesi | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37 | URL+not + adam-saat; FAZ6 yok | **MERGE** (draft→ready bu tur) |
| A4 | #36 çift iş-listesi draft | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/36 | Aynı niyet, dal `cursor/is-listesi-rapor-8e8f` | **CLOSE** |
| A5 | #32 tek sayfa 2026-09-02 | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/32 | Eski merge raporu; bu dosya güncel | **CLOSE** |
| A6 | #31 Dependabot `katalog/` npm | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/31 | Vendored örnek; ürün dep değil | **CLOSE** (SKIP npm) |
| A7 | #33 `actions/setup-python` 5→7 | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33 | Tek dosya: `skill-ajans-dongu.yml` hâlâ `@v5`; diğer workflow `@v7` (#30 merged) | **MERGE** (küçük leftover) veya **WAIT** incele 5 dk |
| A8 | 72 `uretim/rol-kartlari` restore | [`LATOS/STATE.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/LATOS/STATE.md) | Otomatik restore **yok** | **WAIT** (insan evet/hayır) |
| A9 | `CANVA:ON` | `/canva-uret` + [mcp.canva.com/mcp](https://mcp.canva.com/mcp) | OAuth + marka kit sonrası | **WAIT** |
| A10 | Security `MODE=IMPLEMENT` | [`SECURITY/STATE.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/main/SECURITY/STATE.md) | FAZ6 SoA + ethics PASS şart; exploit **yok** | **WAIT** |

`gh pr create/edit` ajan için **403** — merge/close Metin UI’dan.

---

## 4. AJAN YAPACAKLAR

| # | Faz | İş | Bağımlılık | Durum |
|---|-----|-----|------------|--------|
| S0 | Rapor | Bu tek sayfa (URL+not+saat) | `gh pr list` | **bu PR** |
| S1 | Sec FAZ6 | NIST/ISO SoA iskelet, ASSESS-ONLY | Ethics/secret-redakte; **çiftleme yok** | Kardeş ajan `giga-security-faz6-6a77` |
| S2 | Sec FAZ4+ | Kontroller 021–100 × 6 (fazlı → 600) | S1; MODE=ASSESS | Bekler |
| S3 | Sec skill | 6 motor ~20k derinlik | S2 paralel | Kısmi 6 skill |
| S4 | LATOS FAZ4 | 10 title iş kartı pilot (`/is-karti`) | 633 envanter; restore A8 opsiyonel | 3/633 |
| S5 | LATOS FAZ2–3 | RESEARCH + `ORG/ORG_CHART` | Plan var | İçerik yok |
| S6 | Agency | S03–S08 brief + critic PASS | M4 kit yoksa seed | S01–S02 var |
| S7 | Agency CONTEXT | BRAND/PRODUCT/VOICE doldur | **M4 INBOX** | Stub TODO |
| S8 | Canva ops | İlk export (yalnızca CANVA:ON) | M3 + A9 | Kapalı |
| S9 | Holding | Nightly/daily iskelet → LLM dolu | **M1 secret** | Generation: off |

---

## 5. ONAYLANANLAR (merged / kilit)

| Kanıt | URL | Not |
|-------|-----|-----|
| Live terminal | [#19](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/19) | AUDIT parse hotfix |
| CILT12 MEGA | [#22](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/22) | 900k paste RED |
| Agency GIGA | [#23](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/23) [#24](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/24) | **MERGED** (draft close değil) · BRIEF-ONLY |
| Security GIGA | [#25](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/25) [#26](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/26) | **MERGED** · 120/600 defense-only |
| LATOS GIGA | [#27](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/27) [#28](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/28) | **MERGED** · 633 title |
| Hotfix + rapor | [#29](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/29) | MEGA marker |
| setup-python (çoğu) | [#30](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/30) | Leftover = #33 |
| Guardrail | `STATE.md` Security | ASSESS-ONLY · exploit yok · secret `${VAR}` |

---

## 6. ROADMAP — adam-saat (takvim gün/hafta yok)

M = Metin · S = Ajan. Aralık = belirsizlik.

| Faz | Çıktı | Adam-saat (Metin / Ajan) | Kapı |
|-----|--------|---------------------------|------|
| P0 onay | #35 MERGE; #34/#36/#32/#31 CLOSE; #33 leftover; #37 MERGE | **0.5–0.8 M** / 0 | GitHub UI (ajan 403) |
| P0 secret | Gemini (veya OpenRouter) + `gemini_client.py smoke` | **0.25–0.5 M** / **0.25 S** | Cursor Secrets; chate key yok |
| P0 restart | Skill keşif + `/devam` duman | **0.1 M** / 0 | Yeni Agent chat |
| Sec FAZ6 | SoA / COMPLIANCE iskelet | **0.25 M** okuma / **4–8 S** | ASSESS-ONLY; kardeş ajan |
| Sec MODE | `IMPLEMENT` kararı | **0.25 M** / 0 | Ethics PASS + A10 |
| Sec 021–100 | 480 kontrol fazlı (→600) | 0 / **40–80 S** | Tek oturumda bitmez |
| Sec skill | ~20k × 6 motor | 0 / **12–24 S** | P2 |
| LATOS FAZ4 | 10 kart pilot | 0 / **6–12 S** | `/is-karti` |
| LATOS restore | 72 rol-kart (onaylıysa) | **0.5 M** / **2–6 S** | A8 evet |
| LATOS FAZ2–3 | Research + org chart | 0 / **4–8 S** | Plan |
| Agency kit | INBOX marka | **0.5–2 M** / 0 | Dosya Metin |
| Agency CONTEXT | BRAND/PRODUCT/VOICE | 0 / **3–6 S** | M4 |
| Agency brief | S03–S08 + critic | 0 / **4–8 S** | Seed veya kit |
| Canva OAuth | MCP authorize | **0.5–1 M** / 0 | İsteğe bağlı |
| Canva ON | İlk export | **0.25 M** / **2–4 S** | M3+A9 |
| Rapor bu tur | URL+not yenileme | 0 / **0.5–1 S** | Bu PR |

**Toplam (bu ufuk):** Metin **~2.1–6.2 saat** (P0 ≈ 1 saat; kit+OAuth opsiyonel). Ajan **~78–157 saat** (büyük kısım 021–100 + skill; fazlı).

**Bu PR kapsamı:** yalnızca doküman. FAZ6 kontrol/SoA **yok**.

---

## 7. Hızlı linkler

| Ne | URL |
|----|-----|
| Repo | https://github.com/metinduraktr-44/claude-otonom-sistem |
| Open PRs | https://github.com/metinduraktr-44/claude-otonom-sistem/pulls |
| #35 MERGE | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35 |
| #37 bu rapor | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37 |
| #36 CLOSE çift | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/36 |
| Cursor Secrets | https://cursor.com/dashboard?tab=cloud-agents |
| Gemini key | https://aistudio.google.com/apikey |
| GHA Secrets | https://github.com/metinduraktr-44/claude-otonom-sistem/settings/secrets/actions |
| Canva MCP | https://mcp.canva.com/mcp |
| INBOX | https://github.com/metinduraktr-44/claude-otonom-sistem/tree/main/CONTEXT/INBOX |
| Bu ajan | https://cursor.com/agents/bc-415e4b83-e90f-56de-bfb9-b77d0ac33073 |

⏱️ Damga: 2026-11-03T12:05:00Z (15:05 Europe/Istanbul) · 🔍 Denetim: GEÇTİ (`gh`+dosya; kod/exploit yok) · 📚 Öğrenim: açık kuyruk +2 draft (#36/#37); #23/#26/#27 MERGED; Metin P0 = #35 + Gemini URL · 🔗 Önceki: evet (`bc-c972701c`, `uretim/TEK-SAYFA-IS-LISTESI.md` 14:45 TRT)
