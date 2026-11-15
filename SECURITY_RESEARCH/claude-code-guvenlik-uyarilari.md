# Claude Code — güvenlik uyarıları (damıtılmış)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

> **MODE:** `ASSESS-ONLY` · **Damga (Europe/Istanbul):** 2026-11-03T12:56:08+0300 · **UTC:** 2026-11-03T09:56:08Z  
> **Kaynak:** kullanıcı yüklemesi *Claude Code Bilgileri ve Güvenlik Uyarıları* (PDF+DOCX, aynı Gemini export).  
> **Üretim damgası (PDF metadata):** 2026-10-13T10:18:45Z · Skia/PDF · sohbet URL’si `https://gemini.google.com/app/7699f6b4f6bf8620` (özel oturum; kanonik spec değil).  
> **Tercih edilen metin:** DOCX XML extract (1 317 825 karakter, 760 paragraf) ≈ PDF `pypdf` (298 sayfa, 1 334 588 karakter). İçerik eşdeğer; mega-prompt gövdesi **repoya kopyalanmadı**.

## Sinyal (uygula)

Sosyal medya görseli Claude Code / MCP vaatleriyle **yanıltıcı**. Aşağıdaki kurallar Holding Security OS + CILT4 “resmi-öncelik” ile hizalıdır.

| # | Kırmızı bayrak | Operasyon kuralı |
|---|----------------|------------------|
| 1 | **OmniRoute “ayda ~1,6 milyar token bedava”** | Gerçek dışı. Ücretsiz/katmanlı servis bu ölçekte token vermez. Token budget = faturalı kota + `${VAR}` anahtar. |
| 2 | **“Claude Code Setup = Anthropic resmi eklenti”** | Yalan. Anthropic’in bu isimde resmi eklentisi yok. Kurulum: [Claude Code docs](https://docs.anthropic.com). |
| 3 | **Sahte GitHub yıldızı (ör. 98.3K)** | `thedotmack/claude-mem` topluluk deposu; yıldız sayısı montaj olabilir. Star count’a güvenme; Scorecard / commit tarih / LICENSE bak. |
| 4 | **DM / sosyal medya → script veya eklenti kur** | Yükleme = API anahtarı ve repo sızıntısı riski. Pipe-to-shell ve belirsiz `npx`/`pip` **yasak**. |
| 5 | **MCP “hepsini kur” paste** | Resmi katalog: [modelcontextprotocol](https://github.com/modelcontextprotocol) + [anthropics](https://github.com/anthropics). Marketplace dışı MCP varsayılan **OFF**. |
| 6 | **900k+ karakter / +100 sayfa tek paste** | 🚩 Fiziksel token sınırı. Bu sohbette kullanıcı açıkça 900.000 karakter, 10+ sayfa, 100 modül tek-prompt istedi. Karşı: fazlı `SKILL.md` + `references/` + `/sec-devam`. |
| 7 | **Topluluk hafıza/proxy “resmi Claude” diye** | `claude-mem` vb. **unverified** üçüncü taraf. Holding’de bellek = `BILGI_TABANI.md` + `AUDIT_LOG.jsonl` + `.agency` iddiası yok. |
| 8 | **Anahtar sohbete/ekrana yapıştırma** | Extract’te canlı `sk-ant-` / PAT / `AKIA` **yok**. Yine de: yalnızca `${ANTHROPIC_API_KEY}` / `vault://` / `<REDACTED>`. |

## Resmi yönlendirme (allowlist)

1. Claude Code: `https://docs.anthropic.com`  
2. MCP sunucuları: `https://github.com/modelcontextprotocol`  
3. Anthropic GitHub: `https://github.com/anthropics`  
4. Holding: `docs/CILT4-COWORK-MASTER-TALIMATI.md` (5 kural: resmi-öncelik, script tedbiri, güncellik yanılgısı yok, fork yasağı, marketplace-öncelik) · `SECURITY.md`

## Bilinçli olarak **yazılmayanlar**

- 100-modül / “ULTIMATE MASTER SYSTEM PROMPT” gövdeleri (900B emsali + reverse-engineer başlıklı şişirme) — **YASAK / yazılmaz**.  
- Exploit PoC / phishing kiti / credential stuffing script / bypass payload — **YASAK** (savunma listesi; üretim yok).  
- Gerçek secret değer — **YASAK**.

## Hook eşlemesi

| Kontrol | Dosya |
|---------|--------|
| Sosyal mühendislik + pipe-to-shell | `scripts/ethics_check.py` (`curl`/`wget` → shell) |
| Anthropic key biçimi | `scripts/secret_scan.py` (`sk-ant-apiNN-…`) |
| Politika satırı | `.cursor/rules/05-ethics-guardrail.mdc` |
| Metin özet | `docs/CLAUDE-CODE-GUVENLIK-OZET.md` |

## Kullanıcı aksiyonu (Metin)

1. Claude Code’u yalnızca resmi docs’tan kur; “Claude Code Setup” eklentisini kurma.  
2. DM’den gelen zip/script/`npx` çalıştırma.  
3. Canva/LATOS track’e bu mega-prompt’u yapıştırma.  
4. Secret tarama: `python3 scripts/secret_scan.py` · etik: `python3 scripts/ethics_check.py`.
