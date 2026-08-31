# İŞ LİSTESİ — MEGA AJANS / SKILL-MCP / CLAUDE CODE
> Damga: 2026-08-25T14:47:16Z · Kaynak: kullanıcı slash-skill listesi + MEGA-PRONT + CILT1–12

## 🚩 Kırmızı bayraklar (iş listesine GİRMEZ — eşdeğer uygulanır)
- [x] 900B/900M karakter pront → RED → modüler paket
- [x] Uydurma top-100 kişi → RED → kaynaklı arşiv + aylık döngü
- [x] Credential'sız mutate → RED → dry-run

## FAZ A — Senkron & doğrula (kredi-min)
- [x] A1 `python3 scripts/validate.py` → DENETIM: GECTI
- [x] A2 `python3 scripts/daily_agency.py --dogrula`
- [x] A3 `python3 scripts/skill_ajans_uretim.py --dogrula`
- [ ] A4 `python3 scripts/mcp_ajans_etki_uret.py --dogrula`
- [ ] A5 `python3 scripts/install_free_mit_agents.py` → 32/32
- [ ] A6 `bash scripts/live_dashboard.sh` (veya tmux `holding-live`)

## FAZ B — Oku (zincir — atlama)
- [ ] B1 `BILGI_TABANI.md` son 20 satır
- [x] B2 `docs/MEGA-PRONT-MASTER.md`
- [ ] B3 `docs/UNVAN-HIYERARSISI.md`
- [x] B4 `docs/CILT11-ENTERPRISE-MCP-ROUTING.md` + `docs/CILT12-MCP-SKILL-ROUTING-DETAY.md`
- [ ] B5 `docs/SKILL-AJANS-HIYERARSI.md` + `docs/SKILL-ROADMAP-7x24.md`
- [ ] B6 `docs/AYLIK-GUNCELLEME-TAKVIMI.md`
- [x] B7 `uretim/devir/CLAUDE-CODE-YAPISTIR-MEGA.md` (yapıştırma kaynağı)

## FAZ C — Ünvan / ajans iskeleti
- [ ] C1 `python3 scripts/daily_agency.py --org-json`
- [ ] C2 L9→L1 ladder doğrula (`.claude/org/org.json`)
- [ ] C3 Holding: `python3 scripts/holding_report.py`
- [ ] C4 +100 özel yetenek: `data/ozel_yetenekler.json` (adet=116)

## FAZ D — Skill/MCP routing (696 skill)
- [ ] D1 Domain başına `uretim/skill-workflows/{DOMAIN}.md` gözden geçir (50 domain)
- [ ] D2 Credential gerektirenleri dry-run işaretle
- [ ] D3 MCP canlı vs katalog: `data/mcp_hiyerarsi.json`
- [ ] D4 GitHub platform ünvanları (INF-HKS, ENG-DEV) pront paketi
- [ ] D5 Lovable platform ünvanları (PRD-DSN + Supabase) pront paketi

## FAZ E — Top-100 & arşiv döngüsü (uydurma yok)
- [ ] E1 `data/title_top_kisiler.json` oku (`uydurma_yasak=true`)
- [ ] E2 Bu ay 1 departman ailesi için web kaynaklı künye (varsa)
- [ ] E3 `arastirma/` altına `{YYYY-MM}-top100.md` + kaynaklar.jsonl
- [ ] E4 Aylık takvim: `docs/AYLIK-GUNCELLEME-TAKVIMI.md` + `aylik-kurul.yml`

## FAZ F — Prompt paketleri (122 sözleşme — 4–12 KiB)
- [ ] F1 Pilot: `uretim/promptlar/SKILL-OPS/` mevcut materyalize
- [ ] F2 Ünvan başına: 00-kimlik + 10-gorev + 20-ekip + 30-uygulama + SURUM.md
- [ ] F3 Her ekleme SHA256 + AUDIT

## FAZ G — 7/24 workflows
- [ ] G1 nightly-improve.yml
- [ ] G2 daily-agency.yml
- [ ] G3 skill-ajans-dongu.yml
- [ ] G4 holding-konsolide / holding-istirak
- [ ] G5 Secrets: GEMINI_API_KEY (+ opsiyonel OPENROUTER) — Anthropic kredi 0 uyarısı

## FAZ H — Claude Code / Cursor / Lovable / GitHub
- [x] H1 Claude Code: `uretim/devir/CLAUDE-CODE-YAPISTIR-MEGA.md` yapıştır → FAZ 0–6
- [ ] H2 Cursor: `.cursorrules` + bu iş listesi
- [ ] H3 Lovable: PLAN→AGENT→VISUAL; tek bileşen kuralı
- [ ] H4 GitHub: PR odaklı küçük commit; validate CI yeşil

## FAZ I — Damga & rapor
- [ ] I1 AUDIT_LOG.jsonl
- [ ] I2 BILGI_TABANI.md tek satır
- [ ] I3 Kullanıcıya Türkçe kısa tablo (skill/domain/title + 🚩)

## Sayılar (kanıt)
| Metrik | Değer |
|---|---:|
| Skills | 696 |
| Domains | 50 |
| Titles | 216 |
| Prompt hedef (sözleşme) | 38552 |
| MCP toplam | 174 |
| Özel yetenek | 116 |
