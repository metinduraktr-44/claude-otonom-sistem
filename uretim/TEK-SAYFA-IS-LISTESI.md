# TEK SAYFA İŞ LİSTESİ — 2026-11-16 (Europe/Istanbul)

> Damga: **2026-11-16 16:18 TRT** (`Europe/Istanbul`, `2026-11-16T13:18:00Z`)  
> Repo: [`metinduraktr-44/claude-otonom-sistem`](https://github.com/metinduraktr-44/claude-otonom-sistem) · Kanıt: `gh pr list` canlı  
> Bu ajan: [bc-41fa18ee…](https://cursor.com/agents/bc-41fa18ee-373c-5738-94c8-61b5b8b90c0e)  
> `main`: `79f8322a` holding-konsolide **2026-11-16T07:17:45Z**  
> FAZ6 **bu PR’da yok** (kardeş [#39](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39)).  
> 🚩 **900.000.000 karakter tek prompt fiziksel imkânsız / RED.** Hedef: `PROMPTS/` 4–12 KiB sözleşme + `P00n.md` fazlı. 900k+ tek dosya **yazılmadı**.  
> LLM: `GEMINI_API_KEY` / `OPENROUTER_API_KEY` **UNSET** → skeleton.  
> Merge: ajan `gh` write **403**. Onaylı merge = **Metin GitHub UI**. `gh pr merge` denemesi yok.

## 0. Sinyal

| Alan | Canlı (`gh` + dosya, 2026-11-16T13:17Z) |
|------|--------|
| Açık PR | **2** — #35 CONFLICTING · #39 CONFLICTING |
| #37 | **MERGED** (11-15 tur) |
| #41 | **MERGED** agency wave |
| #33 | **MERGED** (WAIT listesi kapandı) |
| CLOSE listesi | #34 #36 #38 #32 #31 **zaten CLOSED** — `set_pr_status` yok |
| Agency | Faz 5 · `CANVA:BRIEF-ONLY` |
| Security | Matris 120/600 · `MODE=ASSESS-ONLY` · FAZ6 yalnız #39 |
| LATOS | 633 title · JOB_CARDS **54** · skill INDEX **696** (687 pending / **9 partial** AN-CH+AN-MIX / 0 done) · 72 restore onaysız |

### Açık PR

| PR | Draft | mergeable | Öneri |
|----|-------|-----------|--------|
| [#39](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39) FAZ6 SoA | hayır | **CONFLICTING** | **MERGE** (conflict UI) — kopyalanmadı |
| [#35](https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35) CC güvenlik ingest | hayır | **CONFLICTING** | **MERGE** (conflict UI) |

---

## 1. METİN YAPACAKLAR

| # | Öncelik | Eylem | Yönlendirme URL | Kısa not |
|---|---------|--------|-----------------|----------|
| M1 | **P0** | GitHub UI merge/close kuyruğu | [Open PRs](https://github.com/metinduraktr-44/claude-otonom-sistem/pulls) | #35/#39 CONFLICTING MERGE. CLOSE listesi zaten kapalı. Bu PR (skill-loop) MERGE. |
| M2 | **P0** | `GEMINI_API_KEY` | [Cursor Secrets](https://cursor.com/dashboard?tab=cloud-agents) · [AI Studio](https://aistudio.google.com/apikey) | Key chate yok. `python3 scripts/gemini_client.py smoke`. |
| M3 | P1 | OpenRouter yedek | [OpenRouter keys](https://openrouter.ai/keys) | Gemini → OpenRouter → Anthropic. |
| M4 | P1 | Canva MCP OAuth (opsiyonel) | [Canva MCP](https://mcp.canva.com/mcp) | Default **BRIEF-ONLY**. |
| M5 | P1 | Marka kit | [INBOX](https://github.com/metinduraktr-44/claude-otonom-sistem/tree/main/CONTEXT/INBOX) | Ajan uyduramaz. |
| M6 | P2 | Restart + `/latos-devam` | [Bu ajan](https://cursor.com/agents/bc-41fa18ee-373c-5738-94c8-61b5b8b90c0e) | 900M paste **RED**. Skill-loop `--dry-run` ay SKIP. |
| M7 | P2 | Expert seed onay | [`EXPERTS/adops-anl-dashboards/top100_SEED.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/cursor/latos-skill-loop-1116-6a77/EXPERTS/adops-anl-dashboards/top100_SEED.md) | 1 changelog isim · `unverified`. |
| M8 | P2 | 72 rol-kart restore | [`LATOS/STATE.md`](https://github.com/metinduraktr-44/claude-otonom-sistem/blob/cursor/latos-skill-loop-1116-6a77/LATOS/STATE.md) | Otomatik restore yok. |
| M9 | P2 | FIDE satranç seed | [ratings.fide.com](https://ratings.fide.com/) | Snapshot; top-100 kopyalanmadı. |

---

## 2. ONAY

| # | PR / karar | URL | Kısa not | Önerilen karar |
|---|------------|-----|----------|----------------|
| A1 | Bu tur skill-loop PR | https://github.com/metinduraktr-44/claude-otonom-sistem/compare/main...cursor/latos-skill-loop-1116-6a77?expand=1 | INDEX 696 + AN-CH/AN-MIX; FAZ6 yok; `gh pr create` **403** | **MERGE** (UI Create PR) |
| A2 | #35 Claude Code ingest | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/35 | **CONFLICTING** | **MERGE** (conflict çöz) |
| A3 | #39 FAZ6 SoA | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39 | Kardeş; **CONFLICTING** | **MERGE** (conflict çöz) |
| A4 | #37 iş listesi 11-15 | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/37 | | **MERGED** |
| A5 | #33 setup-python | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/33 | | **MERGED** |
| A6 | #34 #36 #38 #32 #31 | pulls | CLOSE listesi | **CLOSED** (iş yok) |
| A7 | 72 restore | LATOS STATE | İnsan | **WAIT** |
| A8 | `CANVA:ON` | mcp.canva.com | OAuth+kit | **WAIT** |
| A9 | Security `IMPLEMENT` | SECURITY/STATE.md | Ethics | **WAIT** |
| A10 | Top-100 yayın | EXPERTS/* | `unverified` | **WAIT** |

---

## 3. AJAN İŞ

| # | Faz | İş | Durum |
|---|-----|-----|--------|
| S0 | Rapor | Tek sayfa tablolar 1–5 | bu tur |
| S6a | LATOS skill-loop | INDEX 696 satır · `scripts/skill_loop.py` · ARCHIVE skip | **yazıldı** |
| S6b | Domain dalga | AN-CH 6 + AN-MIX 3 RESEARCH URL+ts | **9 partial** |
| S4 | FAZ4 | `adops-anl-dashboards` kart | **54/633**; qa **580** eksik (Faz 4) |
| S5 | FAZ5 | expert seed 1 isim changelog | `unverified` |
| S6 | FAZ6 talent | satranç FIDE seed · taxonomy 100 | top-100 yok |
| S8 | FAZ8 | title/ekip/uygulama INDEX 122 + P001–P003 / T001–T003 / E001–E003 | 🚩 900M yok |
| S1 | Sec FAZ6 | SoA | **#39** — kopyalanmadı |
| S2 | Sec 021–100 | 480 kontrol | Bekler |
| S9 | Nightly | skill_loop dry-run eklendi | kırıcı değil |

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
| P0 onay | Bu PR MERGE; #35/#39 conflict MERGE | M | GitHub UI |
| P0 secret | Gemini | M | Cursor Secrets |
| Skill INDEX | 696 satır iskelet | S bitti | `skill_loop.py --dry-run` |
| Domain kuyruk | 687 pending skill | S fazlı | bir domain/tur |
| FAZ4 kart | ~580 title | S fazlı | qa_check |
| FAZ5 uzman | sourced + unverified | M onay | uydurma yasak |
| FAZ6 yetenek | 100 INDEX; top-N | M onay | FIDE seed var |
| FAZ8 prompt | 122×3 set gövde | S fazlı | 4–12 KiB; 🚩 900M RED |
| Sec 021–100 | 480 kontrol | S | #39 ayrı |
| Agency S03–S08 | brief | M kit | BRIEF-ONLY |

---

## 6. Sende / bende

| Kim | Ne | URL |
|-----|----|-----|
| **Sende (Metin)** | Bu dal Create PR + merge | https://github.com/metinduraktr-44/claude-otonom-sistem/compare/main...cursor/latos-skill-loop-1116-6a77?expand=1 |
| **Sende** | Gemini | https://cursor.com/dashboard?tab=cloud-agents |
| **Sende** | Expert / restore / CANVA:ON / IMPLEMENT | WAIT §2 |
| **Bende** | pending domain dalgaları · P004–P122 · 580 kart | `/latos-devam` · [ajan](https://cursor.com/agents/bc-41fa18ee-373c-5738-94c8-61b5b8b90c0e) |
| **Bende değil** | #39 conflict çözümü | https://github.com/metinduraktr-44/claude-otonom-sistem/pull/39 |

## 7. Test kanıtı (bu tur)

| Komut | Sonuç |
|-------|--------|
| `python3 scripts/validate.py` | **DENETIM: GECTI** |
| `python3 scripts/qa_check.py` | exit 0 · 580/633 kart yok (Faz 4) |
| `python3 scripts/skill_loop.py --dry-run` | 696 rows · 2. koşu **SKIP calendar** |
| ethics (yeni dosyalar) | **GECTI** (0 finding) |
| secret_scan (yeni dosyalar) | **GECTI** |
| Repo-wide ethics/secret | önceden KALDI (CILT14 vb.) — bu PR genişletmedi |

Healthy roadmap (sende/bende) = bu dosya + GitHub blob (PR merge sonrası `main`).

⏱️ Damga: 2026-11-16T16:18+03:00 · 🔍 Denetim: GEÇTİ (validate + scoped ethics/secret) · 📚 Öğrenim: 696 INDEX + ay damgası SKIP; 900M tek dosya yazılmadı · 🔗 Önceki: evet (#37 MERGED)
