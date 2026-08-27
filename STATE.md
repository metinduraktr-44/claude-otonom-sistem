# STATE — Otonom AI Creative Agency

> Tek kaynak: oturum durumu. Her `/devam` veya `/resume` öncesi oku, sonra güncelle.

## Faz
- **phase:** `0` (Bootstrap)
- **last_command:** —
- **last_updated_utc:** 2026-08-27T00:00:00Z

## CANVA modu
- **default:** `BRIEF-ONLY` — tasarım üretimi yok; brief + spec + senaryo çıktısı
- **CANVA:ON:** Kullanıcı açıkça istediğinde veya `canva-uret` komutu ile MCP üzerinden Canva API/MCP devreye girer
- **OAuth:** Henüz yapılandırılmadı → `tools/canva-client/README.md`

## Aktif iş
- **brief_id:** —
- **scenario_id:** —
- **design_id:** —

## Sonraki adım (Faz 0)
1. Cursor yeniden başlat (rules/skills yüklensin)
2. `/devam` veya `/baslat` ile CONTEXT_BRIEF doldur
3. Canva OAuth PKCE kurulumu (opsiyonel, CANVA:ON için)
