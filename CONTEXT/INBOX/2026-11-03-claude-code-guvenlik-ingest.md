# INBOX — Claude Code bilgileri ve güvenlik uyarıları (sanitized)

**ts_ingest:** 2026-11-03T09:56:32Z  
**Kaynak:** kullanıcı yüklemesi (Gemini sohbet dışa aktarımı, 2026-10-13). Ham DOCX/PDF git’e alınmadı.  
**MODE:** damıtma · savunma-only · secret yok  
**Eş:** `SECURITY_RESEARCH/2026-11-03-claude-code-social-engineering.md`

## Kaynak karşılaştırması

| | DOCX | PDF |
|--|------|-----|
| SHA256 (orijinal binary) | `7f2992e8…f08263b3` | `d69eb470…ab717c83` |
| Çıkarılan metin | ~1.32M karakter, 760 satır XML | 298 sayfa Chrome/Skia print, ~1.34M karakter |
| Sonuç | **Aynı sohbet, format-farklı kopya.** Jaccard kelime örtüşmesi ~0.77 (PDF sayfa başlığı/satır kırımı). İçerik sözleşmesi aynı: viral görsel teyidi + ardından 10/100 modüllük “hyper-agency” prompt şişirme. |

Binary özdeş değil. Kaynak tek: `gemini.google.com` sohbet başlığı “Claude Code Bilgileri ve Güvenlik Uyarıları”.

## Claude Code — doğrulanmış olgular (sinyal)

- Claude Code: Anthropic’in **resmi terminal** kodlama aracı. Resmi doküman: https://docs.anthropic.com  
- MCP: açık protokol; resmi org: https://github.com/modelcontextprotocol — Anthropic GitHub: https://github.com/anthropics  
- Topluluk hafıza araçları (ör. `thedotmack/claude-mem`) ekosistemde **var olabilir**; ekran görüntüsündeki “98.3K star” iddiası **manipülasyon** olarak işaretlenmiş. Yıldız sayısını GitHub’da doğrula; ekran görüntüsüne güvenme.

## Bu holding için aksiyon (Cursor, Agency/Security/LATOS dokunulmadı)

1. **900B / 900M karakter tek prompt YASAK** — K-017 / BILGI_TABANI emsali. Gemini sohbetinin büyük kısmı bu imkânsız isteğin 100-modül tekrarı; kopyalama-değil, reddet.
2. **MCP/skill listesini kör yükleme** — sohbette yüzlerce Cursor skill adı (`/create-secret`, `/twilio-*`, vb.) yığın halinde. Holding’de mevcut `.cursor/skills` + `katalog/` yeterli; “hepsini Claude Code’a yapıştır” yok.
3. **Untrusted ingest** — görsel/PDF/DOCX model bağlamına girer → prompt injection yüzeyi. `CONTEXT/INBOX` damıtma; ham export `uploads/` dışında kalır.
4. Hook hizası: `scripts/secret_scan.py`, `scripts/ethics_check.py`, `.cursor/hooks.json` (`afterFileEdit` + `beforeShellExecution` `curl|sh` failClosed).

## Sırlar

Taramada **gerçek secret yok** (sk-ant / ghp / AKIA / JWT / private key / Bearer: 0). Değer yazılmadı.

## Kullanıcı (Metin) — yalnızca şüphe varsa

Bilinmeyen “Claude Code Setup” eklentisi kurulduysa kaldır + Anthropic anahtarını döndür: https://console.anthropic.com  
GitHub PAT: https://github.com/settings/tokens  
Resmi Claude Code: https://docs.anthropic.com/en/docs/claude-code
