# CİLT 3 — GITHUB EKOSİSTEM HARİTASI + DOĞRULAMA
> Kaynak: docs/CLAUDE-OTONOM-SISTEM-MASTER.md BÖLÜM C · Gecelik döngünün FAZ 1 kaynak haritası budur.

# BÖLÜM C — GITHUB EKOSİSTEM HARİTASI + DOĞRULAMA
### En yüksek yıldızlı depolar (kategori bazlı) + GitHub-dışı doğrulama kaynakları + akademik güvenlik verisi
---
## 0. METODOLOJİ & KRİTİK UYARILAR (önce oku)
**Nasıl arattım:** "awesome-claude-code" ağ geçitleri, her kategori için ayrı sorgu (hooks, MCP, agents, skills, loops, plugins), resmi Anthropic depoları, ve büyük "hepsi-bir-arada" rakip depolar (wshobson, ECC, ruflo). Her rakam en az bir kaynaktan doğrudan GitHub sayfası/API'sinden alındı.

🚩 **Uyarı 1 — Yıldız sayıları burada son derece oynak.** Bu ekosistemde bazı depolar aylar içinde 10 kata kadar büyüdü (ör. ECC: Ocak'ta 31.9k → Temmuz'da 211.9k). Aşağıdaki rakamlar **bulduğum en güncel referans noktası**; sen okurken muhtemelen değişmiş olacak. **Kesin karar öncesi mutlaka github.com/[kullanıcı]/[repo] adresine gidip güncel sayıyı gör.**

🚩 **Uyarı 2 — Fork/mirror riski.** Aynı açıklamayla birebir kopyalanmış onlarca "fork" gördüm (ör. `ruvnet/ruflo`'nun kodflow, gegaowp, jcolano, erfwn81, INTGworld altında birebir aynı metinle kopyaları). Bu normal (açık kaynak), ama **her zaman orijinal/kanonik organizasyondan klonla**, rastgele bir fork'tan değil — bir fork sessizce zararlı kod eklenmiş olabilir. `everything-claude-code`'un kendi README'si bile bunu açıkça yazıyor: *"Official sources only... Third-party re-uploads and unofficial mirrors are not maintained or reviewed by the project and may contain malware."*

🚩 **Uyarı 3 — Resmi (Anthropic) vs topluluk ayrımı.** Aşağıda **[RESMİ]** etiketli olanlar `anthropics/` veya `modelcontextprotocol/` organizasyonu altında, Anthropic tarafından yönetiliyor/onaylanıyor. Diğerleri bağımsız geliştiricilerin ürünü — kaliteli olabilir ama Anthropic garantisi yok.

---
## 0.1 UYARILARI MİNİMİZE ETME — GitHub-DIŞI DOĞRULAMA KAYNAKLARI
**Önce şeffaflık:** GitHub API'sini (`api.github.com`) ve npm registry'yi (`registry.npmjs.org`) doğrudan sorgulayıp gerçek zamanlı indirme/yıldız verisi çekme bu ortamda ağ katmanında engellenebiliyor. Aşağıdaki **GitHub'ın kendisinden bağımsız** kaynaklarla aynı sonuç (daha güçlü şekilde) alınır — çünkü bunlar zaten "yıldız sayısına güvenme" probleminin akademik/endüstriyel çözümü olarak var:

| Kaynak | Ne yapıyor | GitHub'dan bağımsız mı? |
|---|---|---|
| **OpenSSF Scorecard** (`scorecard.dev`, `securityscorecards.dev`) | Yıldıza hiç bakmadan 19+ otomatik güvenlik kontrolü (imzalı release, fuzzing, CI testleri, bakım aktifliği) → 0-10 puan. Google BigQuery'de herkese açık veri seti. CISA bile öneriyor. | ✅ Evet — Linux Foundation/OpenSSF'e ait |
| **deps.dev** (Google Open Source Insights) | Bağımlılık + güvenlik açığı (OSV) + Scorecard verisini tek yerde birleştiriyor | ✅ Evet — Google projesi |
| **OSV.dev** (Open Source Vulnerabilities) | Bilinen zafiyet veritabanı — bir depo/paket gerçekten taranmış mı, açık var mı | ✅ Evet — bağımsız vakıf |
| **StarScout** (CMU akademik araştırma, arXiv 2412.13459) | "Lockstep" (toplu-zamanlı sahte yıldız) ve "low-activity" (boş hesap) imzalarını GHArchive'in tamamında tespit eden metodoloji | ✅ Evet — akademik, GHArchive veri seti |
| **fakestarchecker.com / GitProbe / starforensic.com** | Repo URL'si yapıştır → hesap yaşı dağılımı + yıldız hızı + stargazer aktivitesi analiziyle 0-100 güven skoru | ✅ Evet — 3.parti, anlık |
| **star-history.com** | Zaman içinde yıldız grafiği — organik büyüme yumuşak eğri, sahte kampanya dik/ani sıçrama | ⚠️ Kısmen |
| **npmjs.com / pypi.org indirme sayısı** | Yıldız ile indirme sayısı orantısız mı? (10 bin yıldız + 50 indirme = kırmızı bayrak) | ✅ Evet — farklı platform |

**Claude Code'a özel EN GÜÇLÜ yöntem — Anthropic'in kendi taraması:** `anthropics/claude-plugins-community` reposu, "geçti" onayı almış 3.parti pluginleri barındırıyor — yani **Anthropic senin yerine güvenlik taraması yapmış**:
```
/plugin marketplace add anthropics/claude-plugins-community
```
Bu tek komut, "fork/mirror riski" ve "yıldız güvenilmez" uyarılarını **sıfıra indirir** — artık GitHub yıldızına değil, Anthropic'in onayına bakıyorsun.

### KATEGORİ BAZLI "EN GÜVENLİ SEÇİM" (uyarıları minimize eden)
| Kategori | En Güvenli Seçim | Neden uyarı minimize oluyor |
|---|---|---|
| **Skills** | `anthropics/skills` **[RESMİ]** | Anthropic kontrolünde; **agentskills.io açık standardı** — 40+ bağımsız şirket (Cursor, Copilot, Codex, Gemini CLI) aynı formatı benimsedi |
| **Agents** | `wshobson/agents` | 5 farklı harness'e (Codex, Cursor, OpenCode, Copilot, Gemini) resmi dağıtım; kademeli organik büyüme |
| **Commands** | `anthropics/claude-plugins-official` içindeki 28 komut **[RESMİ]** | Doğrudan Anthropic marketplace'i, `/plugin install` ile |
| **Settings** | `code.claude.com/docs/en/hooks-guide` (resmi doküman) | Repo değil, doğrudan Anthropic dokümantasyonu — sıfır fork/yıldız riski |
| **Hooks** | `disler/claude-code-hooks-mastery` | Birbirinden bağımsız 5+ "best-of" listesinde aynı repo (çapraz-kaynak konsensüsü) |
| **MCPs** | `modelcontextprotocol/servers` **[RESMİ]** | "Managed by Anthropic, built with community" + OpenSSF Scorecard'a tabi |
| **Loops** | `ruvnet/ruflo` | 12+ ay kesintisiz gerçek commit geçmişi — taklit etmesi pahalı sinyal |
| **Plugins** | `anthropics/claude-plugins-community` **[RESMİ, önceden taranmış]** | Anthropic: "otomatik doğrulama ve güvenlik taramasından geçti" |

**Özet:** Mümkün olan her yerde **resmi Anthropic kaynağını** kullan (Skills/Commands/MCPs/Plugins/Settings); mümkün olmayan yerlerde (Agents/Hooks/Loops) **tek yıldız sayısına değil, çapraz-kaynak konsensüsüne ve uzun/kesintisiz commit geçmişine** bak.

### GERÇEK AKADEMİK VERİ — GitHub'ın tamamen dışında (arXiv 2601.10338)
*"Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale"* (Ocak 2026) — GitHub yıldızına hiç bakmayan, iki farklı skill marketplace'ini (`skills.rest`, `skillsmp.com`) tarayan güvenlik araştırması:
- **42.447 skill** toplanmış, **31.132'si** SkillScan (statik analiz + LLM sınıflandırma, %86.7 kesinlik/%82.5 duyarlılık) ile analiz edilmiş
- **Sonuç: %26.1'i en az bir zafiyet içeriyor** — 4 kategoride 14 desen: prompt injection, veri sızıntısı (%13.3), yetki yükseltme (%11.8), tedarik zinciri riski
- **%5.2'si yüksek-şiddetli / kötü niyet şüphesi**
- **Kritik bulgu:** Çalıştırılabilir script içeren skill'ler, sadece talimat içerenlere göre **2.12 kat daha riskli** (OR=2.12, p<0.001)
- **Yıldız/güncellik yanılgısı:** *"Dün güncellenen bir skill, aylardır dokunulmamış birinden daha güvenli değil"* — aktiflik/güncellik tek başına güvenlik sinyali DEĞİL

**Pratik anlamı:** (1) Çalıştırılabilir script'i olmayan, sadece markdown-talimat bileşenleri tercih et — risk 2 kattan fazla düşer. (2) "Son güncelleme dün" bilgisine güvenme. (3) "Resmi Anthropic kaynağı öncelik" stratejisi akademik olarak da destekleniyor.

🚩 **Dürüstlük notu:** OpenSSF Scorecard'ın adaylara verdiği tam sayısal puanlar anlık üretiliyor; `scorecard.dev` → arama kutusuna `github.com/[kullanıcı]/[repo]` yaz → anlık puan.

---
## 1. "TOP YAZILIM EKİPLERİ"
| # | Kişi/Ekip | Ana Depo | Ne inşa ettiler |
|---|---|---|---|
| 1 | **Anthropic (resmi)** | `anthropics/skills`, `anthropics/claude-plugins-official/community`, `modelcontextprotocol/servers` | Skills standardı (agentskills.io), resmi plugin marketplace, MCP referans sunucuları |
| 2 | **Daniel Avila** (davila7) | `claude-code-templates` | 8 bileşen tipi kataloğu + CLI (bu sistemin katalog/ kaynağı) |
| 3 | **Jesse Vincent / Prime Radiant** (obra) | `superpowers` | TDD-zorunlu metodoloji: brainstorm→spec→plan→TDD→subagent→review |
| 4 | **Seth Hobson** (wshobson) | `agents` | Multi-harness plugin marketplace |
| 5 | **Affaan Mustafa** (affaan-m) | `everything-claude-code` (ECC) | Anthropic hackathon galibi; en hızlı büyüyen kapsamlı sistem |
| 6 | **Reuven Cohen / rUv** (ruvnet) | `ruflo` (eski adı claude-flow) | Hive-mind swarm orkestrasyonu, SPARC metodolojisi — Loops lideri |

## 2. GENEL / KAPSAMLI DEPOLAR
| Depo | ≈Yıldız | Neyi kapsıyor |
|---|---|---|
| `davila7/claude-code-templates` | ~29k | 8 tip, CLI kurulum (katalog/ altında tam kopyası mevcut) |
| `wshobson/agents` | ~31.3k | 203 agent, 175 skill, 109 command, 94 plugin — 5 harness |
| `affaan-m/everything-claude-code` | ~82k→212k | 60+ agent, 200-1300+ skill, 400+ command, hook, rule, 14 MCP config |
| `hesreallyhim/awesome-claude-code` | ~50k | Kürasyonlu keşif dizini |
| `rohitg00/awesome-claude-code-toolkit` | — | 135 agent, 35 skill, 42 command, 176+ plugin, 20 hook |

## 3-10. KATEGORİ DEPOLARI (özet tablo)
| Kategori | Birincil [RESMİ varsa] | İkincil/Topluluk |
|---|---|---|
| Skills | `anthropics/skills` (~161k) | `obra/superpowers` (~150-255k), `mattpocock/skills` (~101k+), `K-Dense-AI/claude-scientific-skills`, `alirezarezvani/claude-skills` (192-232+ profesyonel — pazarlama/PM dahil) |
| Agents | `wshobson/agents` (~31.3k) | `VoltAgent/awesome-claude-code-subagents`, `davepoon/claude-code-subagents-collection`, `0xfurai/claude-code-subagents`, `vijaythecoder/awesome-claude-agents` |
| Commands | `anthropics/claude-plugins-official` (28 komut) | wshobson (109), ECC (400+), rohitg00 (42) |
| Settings | `code.claude.com/docs` (resmi doküman) | rohitg00 rules (15), ECC rules/, `disler/claude-code-hooks-mastery` settings örnekleri |
| Hooks | `disler/claude-code-hooks-mastery` (13/13 event) | `karanb192/claude-code-hooks` (298★, 10 hook), `ithiria894/awesome-claude-code-hooks`, `dwarvesf/claude-guardrails` |
| MCPs | `modelcontextprotocol/servers` [RESMİ] (~88.4k) | `punkpeye/awesome-mcp-servers` (~90.7k), `wong2/awesome-mcp-servers`, `abordage/awesome-mcp` (günlük otomatik) |
| Loops | `ruvnet/ruflo` (~59-64k; npm: claude-flow) | `gastown` (~17k), `ralph-orchestrator` (~3k) |
| Plugins | `anthropics/claude-plugins-official` (~32.1k, 255+ plugin) + `claude-plugins-community` [RESMİ taranmış] | wshobson (94 plugin), karanb192 |

## 11. RİSK MİNİMİZASYONU — 3 KONTROL (2 dakika)
```
1) https://scorecard.dev/viewer/?uri=github.com/[kullanıcı]/[repo]
   → Branch-Protection, Signed-Releases, Maintained puanları (10/10'a yakın = iyi)
2) npmjs.com/package/[paket-adı] → "Provenance" sekmesi
   → Yeşil onay = kod-paket kriptografik eşleşmesi
3) Repo sayfasında "fork" ibaresi VARSA orijinal değildir → kanonik isme git
```
**Anti-kurcalama kanıtı:** `claude-plugins-community` → her plugin belirli bir commit SHA'sına pinlenir (sessizce değiştirilemez). davila7 → 4 doğrulayıcı (Structural/Integrity-SHA256/Semantic/Reference) + NVIDIA SkillSpector her PR'da otomatik.

## 12. 2 OTURUMLUK İNCELEME PLANI (gecelik döngüye bağlı)
**Oturum 1 — Skills + Agents + Commands:** `anthropics/skills` anatomi karşılaştırma · `wshobson/agents` model-tier routing · `obra/superpowers` TDD akışı (Tahmin Uzmanı'na uygulanabilirlik)
**Oturum 2 — Settings + Hooks + MCPs + Loops + Plugins:** `disler/claude-code-hooks-mastery` 13 event vs adops-agents · `modelcontextprotocol/servers` referans desen · `ruvnet/ruflo` Learning Loop → BILGI_TABANI iyileştirmesi
Her oturum sonunda: bulgu → BILGI_TABANI.md, damga → AUDIT_LOG.jsonl.
