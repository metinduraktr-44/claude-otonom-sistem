# TEK SAYFA İŞ LİSTESİ — 2026-11-03 (Europe/Istanbul)

> Damga: **2026-11-03 14:45 TRT** (`2026-11-03T11:45:00Z`) · Repo: `metinduraktr-44/claude-otonom-sistem` · Kanıt: `gh pr list` canlı · Ajan: https://cursor.com/agents/bc-c972701c-f335-58b4-9f81-cf25817a0b52  
> FAZ6 uygulama **bu PR’da yok** (kardeş ajan: `cursor/giga-security-faz6-6a77`). 🚩 900B/900M tek dosya yok.

## 1. Özet

| Sinyal | Durum (canlı) |
|--------|----------------|
| main | nightly/holding OK (`0ec1a921` 07:10Z) |
| Açık PR | **5** — #35 hazır · #34 draft (çift) · #33 GA leftover · #32 eski rapor · #31 katalog skip |
| Merged GIGA | **#19–#30** (Canva #24 · Security #25/#26 · LATOS #27/#28 · hotfix #29) |
| Agency | Faz 5 · `CANVA:BRIEF-ONLY` · marka TBD · INBOX boş |
| Security | 120/600 ASSESS · MODE=`ASSESS-ONLY` · `COMPLIANCE/` iskelet · FAZ6 ayrı dal |
| LATOS | 633 title · 3 kart (CISO, hq-ceo, adops-ceo) · 72 silinmiş restore **onaysız** |

## 2. Metin — yapacaklarım

| # | İş | Yönlendirme | URL |
|---|-----|--------------|-----|
| M1 | `GEMINI_API_KEY` (öncelik) → yoksa OpenRouter → Anthropic | Cursor Secrets / Cloud Agents. Değeri chate yapıştırma. | [Cursor Secrets](https://cursor.com/dashboard?tab=cloud-agents) · [AI Studio](https://aistudio.google.com/apikey) |
| M2 | Canva MCP OAuth (opsiyonel; BRIEF-ONLY yeter) | Settings → MCP → Authorize. PKCE: `tools/canva-client/README.md` | `https://mcp.canva.com/mcp` |
| M3 | Cursor restart / yeni Agent | Skills+hooks yükle; `/devam` smoke | Bu ajan: [bc-c972701c…](https://cursor.com/agents/bc-c972701c-f335-58b4-9f81-cf25817a0b52) |
| M4 | Marka kit → `CONTEXT/INBOX/` | `BRAND/PRODUCT/VOICE.md` hâlâ TODO. Kit yoksa AdOps CRE seed devam. | [INBOX](https://github.com/metinduraktr-44/claude-otonom-sistem/tree/main/CONTEXT/INBOX) |
| M5 | Billing / kota (Gemini) | Kota bitince dry-run iskelet | Google AI Studio + Cursor billing |

## 3. Metin — onaylayacaklarım

| # | Karar | Öneri | URL |
|---|--------|--------|-----|
| A1 | #35 Claude Code güvenlik ingest | **MERGE** (validate SUCCESS, ASSESS-ONLY) | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35 |
| A2 | #34 draft (aynı ingest) | **CLOSE** — #35 supersede | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34 |
| A3 | #32 tek sayfa 2026-09-02 | **CLOSE** — bu rapor güncel | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/32 |
| A4 | #31 Dependabot `katalog/` npm | **SKIP/CLOSE** — vendored; ürün dep değil | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/31 |
| A5 | #33 `actions/setup-python` 5→7 | **İNCELE** — çoğu workflow zaten `@v7`; `skill-ajans-dongu.yml` hâlâ `@v5` | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33 |
| A6 | 72 `uretim/rol-kartlari` restore | İnsan onayı olmadan restore **yok** | `LATOS/STATE.md` |
| A7 | `CANVA:ON` | OAuth + marka kit sonrası. Şimdi BRIEF-ONLY. | `/canva-uret` |
| A8 | Security `MODE=IMPLEMENT` | FAZ6 SoA + ethics PASS sonrası. Şimdi ASSESS-ONLY. | `SECURITY/STATE.md` |

## 4. Ajan — onaylı / yapılan

| Track | Kanıt | Not |
|-------|-------|-----|
| Live terminal | [#19](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/19) MERGED | AUDIT parse hotfix |
| CILT12 MEGA | [#22](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/22) | 900k paste RED |
| Agency GIGA | [#23](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/23) [#24](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/24) | BRIEF-ONLY continuum |
| Security GIGA | [#25](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/25) [#26](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/26) | 120/600 · defense-only |
| LATOS GIGA | [#27](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/27) [#28](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/28) | 633 title |
| Hotfix + rapor | [#29](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/29) [#30](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/30) | MEGA marker · setup-python |
| #35 ingest | **OPEN** — henüz main’de değil | Merge Metin |

## 5. Ajan — ileri adımlar

| P | İş | Kim | Durum |
|---|-----|-----|--------|
| **P0** | Security **FAZ6 COMPLIANCE** (NIST/ISO SoA iskelet, ASSESS-ONLY) | Sistem | Kardeş ajan üretiyor — **çiftleme yok** |
| **P0** | #35 merge sonrası CILT14 pointer main’de | Metin merge + Sistem rebase | Bekler A1 |
| **P1** | LATOS FAZ4 — 10 kart pilot (`/is-karti`) | Sistem | 3/633 mevcut |
| **P1** | Canva CONTEXT `BRAND/PRODUCT/VOICE` | Sistem (INBOX sonrası) | Stub TODO |
| **P2** | Kontroller 021–100 (batch) → 600 fazlı | Sistem | 40–80h kümülatif |
| **P2** | LATOS FAZ2 RESEARCH + org chart | Sistem | Plan var, içerik yok |

## 6. Roadmap + adam-saat (M = Metin · S = Sistem)

Aralık = belirsizlik; takvim haftası değil.

| İş | Adam-saat (M/S) | Bağımlılık |
|----|-----------------|------------|
| Açık PR tarama (#35 merge, #34/#32/#31 close, #33 incele) | **0.5h M** | — |
| Gemini secret + smoke (`gemini_client.py smoke`) | **0.25h M** + 0.25h S | M1 |
| Cursor restart / skill keşif | **0.1h M** | — |
| Canva MCP OAuth | **0.5–1h M** | İsteğe bağlı |
| Marka kit INBOX bırakma | **0.5–2h M** | Dosya hazırlığı |
| FAZ6 SoA / COMPLIANCE paket | **4–8h S** | ASSESS-ONLY; kardeş ajan |
| `MODE=IMPLEMENT` kararı | **0.25h M** | FAZ6 + ethics |
| LATOS 10 kart pilot | **6–12h S** | Restore kararı A6 opsiyonel |
| 72 rol-kart restore (onaylıysa) | **2–6h S** + **0.5h M** onay | A6 |
| Canva CONTEXT doldurma | **3–6h S** | M4 kit |
| `CANVA:ON` ilk export | **2–4h S** + **0.25h M** | M2+A7 |
| 600 kontrol tam (fazlı 021–100×6) | **40–80h S** | P2; tek oturumda bitmez |
| Skill ~20k derinlik (6 motor) | **12–24h S** | P2 |

**Bu tur (rapor):** ~0.5–1h S envanter. FAZ6 içerik **hariç**.

## 7. Bekleyen URL’ler

| Ne | URL |
|----|-----|
| Repo | https://github.com/metinduraktr-44/claude-otonom-sistem |
| Open PRs | https://github.com/metinduraktr-44/claude-otonom-sistem/pulls |
| #35 MERGE | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35 |
| #34 CLOSE | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/34 |
| #33 incele | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33 |
| #32 CLOSE | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/32 |
| #31 SKIP | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/31 |
| Bu ajan | https://cursor.com/agents/bc-c972701c-f335-58b4-9f81-cf25817a0b52 |
| Secrets | https://cursor.com/dashboard?tab=cloud-agents |
| Canva MCP | https://mcp.canva.com/mcp |
| Gemini key | https://aistudio.google.com/apikey |
| Docs | `STATE.md` · `SECURITY/STATE.md` · `LATOS/STATE.md` · `docs/IS-LISTESI-GIGA-*.md` · `SECURITY_MATRIX/matrix.md` |

⏱️ Damga: 2026-11-03T11:45:00Z · 🔍 Denetim: GEÇTİ (envanter `gh`+dosya; kod yok) · 📚 Öğrenim: #23/#26/#27 artık MERGED; açık iş = #35 + FAZ6 ayrı dal + Metin sırları · 🔗 Önceki: evet (`uretim/TEK-SAYFA-RAPOR-MERGE-DURUM.md` 2026-08-31)
