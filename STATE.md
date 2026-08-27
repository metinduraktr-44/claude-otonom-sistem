# STATE — Otonom AI Creative Agency

> Tek kaynak: oturum durumu. Her `/devam` veya `/resume` öncesi oku, sonra güncelle.

## Faz
- **phase:** `0` (Bootstrap — ingestion tamamlandı)
- **last_command:** bootstrap
- **last_updated_utc:** 2026-08-27T00:30:00Z

## CANVA modu
- **default:** `BRIEF-ONLY` — tasarım üretimi yok; brief + spec + senaryo çıktısı
- **CANVA:ON:** Kullanıcı açıkça istediğinde veya `/canva-uret` komutu ile MCP üzerinden Canva API/MCP devreye girer
- **OAuth:** Henüz yapılandırılmadı → `tools/canva-client/README.md`

## Ingestion özeti (Faz 0)
- **holding:** 8 iştirak · 633 rol · 688 slash skill
- **CONTEXT:** `CONTEXT/CONTEXT_BRIEF.md` dolduruldu (holding seed)
- **MATRIX:** `MATRIX/CHANNEL_MATRIX.md` — Meta/TikTok/Google/YouTube/IAB
- **ORG:** `ORG/ORG_CHART.md` + `ORG/SKILLS_INVENTORY.md` — holding referanslı

## Aktif iş
- **brief_id:** —
- **scenario_id:** —
- **design_id:** —

## Sonraki adım
1. Cursor yeniden başlat (rules/skills/hooks yüklensin)
2. Yeni Agent chat → `/devam` veya `/baslat`
3. Aktif marka/kampanya seç → `/brief-uret`
4. (Opsiyonel) Canva OAuth PKCE kurulumu — CANVA:ON için
