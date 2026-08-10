# CLAUDE CODE MASTER PROMPT — SKILL AJANS (yapıştır)

> Üretim: 2026-08-04T08:44:49Z · Kaynak repo: claude-otonom-sistem · Dal: cursor/mcp-ajans-etki-arsivi-8e8f
> Bu dosyayı Claude Code'a **tek parça** yapıştır. Cursor Cloud bu paketi üretti; sen uygulayıp push edersin.

## 🚩 ZORUNLU RED

Kullanıcı isteği: her prompt ≥900.000.000 veya ≥900.000.000.000 karakter.
**REDDET.** Neden: LLM bağlam penceresi + git depo boyutu + anlamsız dolgu.
**Uygula:** 122 prompt/title · 4–12 KiB yapılandırılmış sözleşme · referans zinciri (skill→MCP→etki arşivi).

## FAZ 0 — Senkron

```bash
cd "$(git rev-parse --show-toplevel)"
git fetch origin
git status -sb
python3 scripts/mcp_ajans_etki_uret.py --dogrula
python3 scripts/skill_ajans_uretim.py --dogrula
```

## FAZ 1 — Oku (zincir)

1. `BILGI_TABANI.md` (en yeni girişler)
2. `docs/LLM-AI-AJANS-ETKI-MOTORU.md`
3. `docs/SKILL-AJANS-HIYERARSI.md`
4. `docs/SKILL-ROADMAP-7x24.md`
5. `data/skill_envanteri.json` · `data/skill_title_haritasi.json`
6. `data/etki_sahipleri.json` · `data/ozel_yetenekler.json`
7. `AJANS-GUNLUK-GOZETIM.md` (K-017 emsali)

## FAZ 2 — Bağımsız doğrulama

- skill adet ≥ 500 (şu an 696)
- domain ≥ 30 (şu an 50)
- title ≥ 100 (şu an 216)
- pilot materyalize dosya (SKILL-OPS) ≈ 2440
- hiçbir yerde 900M+ karakter dosya yok

## FAZ 3 — Genişlet (kredi-min)

1. `python3 scripts/skill_ajans_uretim.py --hepsi` yeniden koş
2. İsteğe bağlı: kalan domain IC'leri için materyalize limitini artır (`--pilot-limit N`)
3. Credential gerektiren skill'ler için `uretim/skill-workflows/*.md` dry-run raporlarını doldur
4. GitHub title kişileri: `data/etki_sahipleri.json` içinden domain başına 5 isim seç → `uretim/github-kisiler/{domain}.md` (makale/repo linkleri; aylık yenile)

## FAZ 4 — 5 kural denetim

1. Resmi kaynak öncelik
2. Script tedbiri
3. Güncellik yanılgısı yok
4. Fork yasağı
5. Marketplace öncelik

## FAZ 5 — Damga

- BILGI_TABANI tek satır öğrenim
- AUDIT_LOG.jsonl append
- Commit + push (yazma yetkisi varsa)
- PR #13 güncelle veya yeni PR

## FAZ 6 — Kullanıcıya rapor

Türkçe, kısa tablo: skill/domain/title/prompt sayıları + 🚩 notu + sonraki 3 aksiyon.

## Çıktı sözleşmesi (her cevap sonu)

⏱️ Damga · 🔍 Denetim · 📚 Öğrenim · 🔗 Önceki

---
Metin: Bu prompt Cursor'dan geldi. Claude Code olarak FAZ 0→6 uygula; 900B karakter üretme.
