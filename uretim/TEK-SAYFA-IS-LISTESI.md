# TEK SAYFA İŞ LİSTESI — 2026-11-27 (Europe/Istanbul)

> Damga: **2026-11-27 13:35 TRT** (`Europe/Istanbul`, `2026-11-27T10:35:00Z`)  
> Repo: [`metinduraktr-44/claude-otonom-sistem`](https://github.com/metinduraktr-44/claude-otonom-sistem) · Kanıt: `gh pr list` canlı  
> Bu ajan: [bc-7e6dbf1f…](https://cursor.com/agents/bc-7e6dbf1f-19fe-52d5-a086-3a54a823428a)  
> `main`: `eacab21b` holding-konsolide **2026-11-27T07:11:18Z**  
> Dal: `cursor/latos-skill-loop-1127-6a77` (from `origin/main`; #43 INDEX cherry-pick + AN-PH dalga)  
> FAZ6 SoA **additive kopya** (`COMPLIANCE/ISO27001-2022-SOA.md`); kardeş [#39](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39) hâlâ CONFLICTING.  
> 🚩 **900.000.000 karakter tek prompt fiziksel imkânsız / RED.** Hedef: `PROMPTS/` 4–12 KiB sözleşme + `P00n.md` fazlı. 900k+ tek dosya **yazılmadı**.  
> LLM: `GEMINI_API_KEY` / `OPENROUTER_API_KEY` **UNSET** → skeleton.  
> Merge: ajan `gh` write **403**. Onaylı merge = **Metin GitHub UI**. `gh pr merge` / `gh pr create` denemesi yok.

## 0. Sinyal

| Alan | Canlı (`gh` + dosya, 2026-11-27T10:24Z) |
|------|--------|
| Açık PR | **3** — #44 MERGEABLE (draft) · #43 CONFLICTING · #39 CONFLICTING |
| #37 | **MERGED** 2026-11-15T09:59:04Z |
| #41 | **MERGED** 2026-11-15T13:45:29Z |
| #33 | **MERGED** 2026-11-15T09:59:00Z |
| #40 | **MERGED** dependabot katalog |
| CLOSE listesi | #42 #35 **CLOSED 2026-11-27T10:21:22Z** · #34 #36 #38 #32 #31 CLOSED |
| Agency | Faz 5 · `CANVA:BRIEF-ONLY` |
| Security | Matris 120/600 · `MODE=ASSESS-ONLY` · FAZ6 SoA bu dalda kopya; #39 rebase Metin |
| LATOS | 633 title · JOB_CARDS **55** · skill INDEX **696** (675 pending / **21 partial** = 9 AN-CH+AN-MIX + **12 AN-PH** / 0 done) · 72 restore onaysız |

### Açık PR

| PR | Draft | mergeable | Öneri |
|----|-------|-----------|--------|
| [#44](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/44) skills-wave-2 | evet | **MERGEABLE** | **WAIT** (draft; kart dalgası ayrı) |
| [#43](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/43) skill-loop 11-16 | hayır | **CONFLICTING** | **CLOSE** — INDEX bu dalda (`1127`) |
| [#39](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39) FAZ6 SoA | hayır | **CONFLICTING** | **MERGE** (conflict UI) veya 1127 kopyası |

---

## 1. METİN YAPACAKLAR

| # | Öncelik | Eylem | Yönlendirme URL | Kısa not |
|---|---------|--------|-----------------|----------|
| M1 | **P0** | Bu dal Create PR + MERGE | [compare 1127](https://github.com/metinduraktr-44/claude-otonom-sistem/compare/main...cursor/latos-skill-loop-1127-6a77?expand=1) | Title: `docs(latos): skill döngüsü dalga 2026-11-27`. Ajan `gh pr create` 403. |
| M2 | **P0** | #43 kapat veya not düş | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/43 | INDEX 696 superseded by 1127. |
| M3 | **P0** | #39 conflict MERGE | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39 | SoA kopyası 1127’de; yine de UI. #35/#42 **CLOSED**. |
| M4 | **P0** | `GEMINI_API_KEY` | [Cursor Secrets](https://cursor.com/dashboard?tab=cloud-agents) · [AI Studio](https://aistudio.google.com/apikey) | Key chate yok. `python3 scripts/gemini_client.py smoke`. |
| M5 | P1 | OpenRouter yedek | [OpenRouter keys](https://openrouter.ai/keys) | Gemini → OpenRouter → Anthropic. |
| M6 | P1 | Canva MCP OAuth (opsiyonel) | [Canva MCP](https://mcp.canva.com/mcp) | Default **BRIEF-ONLY**. |
| M7 | P1 | Marka kit | [INBOX](https://github.com/metinduraktr-44/claude-otonom-sistem/tree/main/CONTEXT/INBOX) | Ajan uyduramaz. |
| M8 | P2 | Restart + `/latos-devam` | [Bu ajan](https://cursor.com/agents/bc-7e6dbf1f-19fe-52d5-a086-3a54a823428a) | 900M paste **RED**. skill_loop ay SKIP. |
| M9 | P2 | Expert seed onay | [`EXPERTS/adops-anl-ga4-tagging/top100_SEED.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/cursor/latos-skill-loop-1127-6a77/EXPERTS/adops-anl-ga4-tagging/top100_SEED.md) | Org URL · kişi yok · `unverified`. |
| M10 | P2 | 72 rol-kart restore | [`LATOS/STATE.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/cursor/latos-skill-loop-1127-6a77/LATOS/STATE.md) | Otomatik restore yok. |

---

## 2. ONAY

| # | PR / karar | URL | Kısa not | Önerilen karar |
|---|------------|-----|----------|----------------|
| A1 | Bu tur skill-loop 1127 | compare URL §6 | INDEX 696 + AN-PH 12; FAZ6 kopya | **MERGE** |
| A2 | #43 11-16 INDEX | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/43 | **CONFLICTING** · superseded | **CLOSE** |
| A3 | #35 Claude Code ingest | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35 | 2026-11-27T10:21:22Z | **CLOSED** |
| A4 | #39 FAZ6 SoA | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39 | **CONFLICTING**; dosyalar 1127’de | **MERGE** veya 1127 yeter |
| A5 | #42 skills wave | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/42 | superseded by #44 | **CLOSED** |
| A5b | #44 skills-wave-2 | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/44 | draft MERGEABLE | **WAIT** |
| A6 | #37 iş listesi 11-15 | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37 | | **MERGED** |
| A7 | #41 agency wave | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/41 | | **MERGED** |
| A8 | #33 setup-python | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33 | | **MERGED** |
| A9 | #34 #36 #38 #32 #31 | pulls | CLOSE listesi | **CLOSED** (iş yok) |
| A10 | 72 restore | LATOS STATE | İnsan | **WAIT** |
| A11 | `CANVA:ON` | mcp.canva.com | OAuth+kit | **WAIT** |
| A12 | Security `IMPLEMENT` | SECURITY/STATE.md | Ethics | **WAIT** |
| A13 | Top-100 yayın | EXPERTS/* | `unverified` | **WAIT** |

---

## 3. AJAN İŞ

| # | Faz | İş | Durum |
|---|-----|-----|--------|
| S0 | Rapor | Tek sayfa tablolar 1–5 | bu tur |
| S6a | LATOS skill-loop | INDEX 696 · `skill_loop.py` · Kasım **SKIP** | **koştu** |
| S6b | Domain dalga | AN-PH 12 RESEARCH URL+ts | **12 partial** (63 AN-PH pending) |
| S4 | FAZ4 | `adops-anl-ga4-tagging` kart | **55/633**; qa eksik Faz 4 |
| S5 | FAZ5 | expert seed org-URL | `unverified` · kişi yok |
| S6 | FAZ6 talent | product-analytics stub | top-100 yok |
| S6s | Sec FAZ6 | SoA + CTRL 013+ additive kopya | **kopyalandı** (#39 conflict duruyor) |
| S8 | FAZ8 | title/ekip/uygulama INDEX 122 + P/T/E 001–003 | 🚩 900M yok |
| S2 | Sec 021–100 | 480 kontrol | Bekler |
| S9 | Nightly | skill_loop dry-run | kırıcı değil |
| S10 | Ay döngüsü | Kasım ARCHIVE delta · Aralık stub | **yazıldı** |

---

## 4. ONAYLANAN

| Kanıt | URL | Not |
|-------|-----|-----|
| Live terminal | [#19](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/19) | MERGED |
| Slash-skill / CILT12 | [#21](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/21) [#22](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/22) | 900k paste RED |
| Agency GIGA | [#23](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/23) [#24](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/24) | BRIEF-ONLY |
| Security GIGA | [#25](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/25) [#26](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/26) | 120/600 |
| LATOS GIGA | [#27](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/27) [#28](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/28) | 633 title |
| Hotfix / setup-python | [#29](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/29) [#30](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/30) [#33](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33) | leftover kapandı |
| Tek sayfa 11-15 | [#37](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37) | **MERGED** |
| Agency wave | [#41](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/41) | **MERGED** 15 Kas |
| Dependabot katalog | [#40](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/40) | MERGED — `katalog/` npm ürün değil |

---

## 5. ROADMAP (adam-saat / gün / hafta yok)

M = Metin kapısı · S = ajan dalga. Ölçek: **P0 / fazlı backlog** — sayısal saat yok.

| Faz | Çıktı | Kim | Kapı |
|-----|--------|-----|------|
| P0 onay | 1127 MERGE; #43 CLOSE; #39 conflict; #44 draft ayrı | M | GitHub UI |
| P0 secret | Gemini | M | Cursor Secrets |
| Skill INDEX | 696 satır iskelet | S bitti | `skill_loop.py --dry-run` |
| Domain kuyruk | 675 pending skill | S fazlı | 8–15 skill/tur |
| FAZ4 kart | ~578 title | S fazlı | qa_check |
| FAZ5 uzman | sourced + unverified | M onay | uydurma yasak |
| FAZ6 yetenek | 100 INDEX; top-N | M onay | FIDE + PH stub |
| FAZ8 prompt | 122×3 set gövde | S fazlı | 4–12 KiB; 🚩 900M RED |
| Sec 021–100 | 480 kontrol | S | ASSESS-ONLY |
| Agency S03–S08 | brief | M kit | BRIEF-ONLY |

---

## 6. Sende / bende

| Kim | Ne | URL |
|-----|----|-----|
| **Sende (Metin)** | Bu dal Create PR + merge | https://github.com/metinduraktr-44/claude-otonom-sistem/compare/main...cursor/latos-skill-loop-1127-6a77?expand=1 |
| **Sende** | #43 CLOSE | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/43 |
| **Sende** | Gemini | https://cursor.com/dashboard?tab=cloud-agents |
| **Sende** | Expert / restore / CANVA:ON / IMPLEMENT | WAIT §2 |
| **Bende** | pending domain dalgaları · P004–P122 · 578 kart | `/latos-devam` · [ajan](https://cursor.com/agents/bc-7e6dbf1f-19fe-52d5-a086-3a54a823428a) |
| **Bende değil** | GitHub merge (403) | UI |

## 7. Test kanıtı (bu tur)

| Komut | Sonuç |
|-------|--------|
| `python3 scripts/validate.py` | **DENETIM: GECTI** (119 dosya) |
| `python3 scripts/qa_check.py` | exit 0 · **579/633** kart yok (Faz 4; bu tur +1 → 55 kart) |
| `python3 scripts/skill_loop.py --dry-run` | 696 rows · **SKIP calendar 2026-11** · pending 675 / partial 21 / done 0 |
| ethics (yeni dilim) | **GECTI** (0 finding) |
| secret_scan (yeni dilim) | **GECTI** |
| Repo-wide ethics/secret | önceden KALDI (CILT14 vb.) — bu PR genişletmedi |

Healthy roadmap (sende/bende) = bu dosya + GitHub blob (PR merge sonrası `main`).

⏱️ Damga: 2026-11-27T13:35+03:00 · 🔍 Denetim: GEÇTİ (validate + scoped ethics/secret) · 📚 Öğrenim: Kasım SKIP + AN-PH 12 partial; 900M tek dosya yazılmadı · 🔗 Önceki: evet (#43 CONFLICTING; #35/#42 CLOSED 11-27; #37/#41 MERGED)
