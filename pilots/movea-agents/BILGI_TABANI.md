# BİLGİ TABANI — movea-agents (birikimli öğrenme)
Sistem öğrenmesi burada birikir. Her haftalık döngü yeni satır ekler; bir sonraki hafta bunu girdi alır.

## 2026-07-16 — Seed
- Repo kuruldu. Dikey: Movéa marka içerik (GELIR_MOTORU pilotu; kanıt metriği: içerik/hafta).
- Yapı adops-agents iskeletinden uyarlandı; kaynak desenler: content-marketer, social-content,
  copywriting, publisher-linkedin/x, nightly-changelog-loop (davila7/claude-code-templates).
- Denetim: 6 katman (structural / integrity-SHA256 / semantic / reference / patterns / review).
- Tasarım kararı: yayınlama manuel kopyala-yapıştır (API anahtarı yok) — güvenli varsayılan;
  marka sesi tek kaynağı TON_REHBERI.md, yoksa şablon doldurulur ve varsayımlar işaretlenir.
- İlk iş: TON_REHBERI.md'yi Metin ile doldur → sonra /icerik-takvimi → ilk döngü.
