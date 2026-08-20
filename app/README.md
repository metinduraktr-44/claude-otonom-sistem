# app/ — Holding Kontrol Uygulaması (iOS · Android · Web) — BLUEPRINT
> CILT10 §2 kontrol yüzeyi. LLM ajanları 7/24 arka planda çalışır; app onların panosudur.

## Durum
Bu klasör **blueprint + iskele plandır**. Çalışan RN/Supabase uygulaması, aşağıdaki secret'ler eklendikten sonra kurulur (🚩 secret'leri **kullanıcı** Secrets panelinden ekler; ajan hesap/anahtar açamaz — CILT10 §0).

## Teknoloji (repo deseniyle uyumlu)
| Katman | Seçim | Not |
|---|---|---|
| Web | React / Next.js | Lovable ile hızlı iskele (MEGA-PRONT §7.2) |
| Mobil | React Native / Expo | tek kod tabanı → App Store + Play |
| Backend/DB/Auth | Supabase (Postgres+auth+storage+edge) | RLS ile korumalı |
| Ödeme (ops.) | Stripe | premium/lisans kanalı |
| Kaynak-of-truth | `data/holding.json` + `.claude/org/org.json` | app bunları okur |

## Ana ekranlar (6)
1. **Holding panosu** — iştirak sağlığı, OKR skorları, 🚩 (kaynak: `docs/HOLDING-KONSOLIDE.md` + `docs/REPO-SAGLIK-MATRISI.md`).
2. **Org gezgini** — C→işçi ağaç; her ünvan kartı (`.claude/agents/{DEPT}/{dept}-lead.md`) + son standup.
3. **Görev/roadmap** — 7/24 canlı task; üst iş listesi → task → roadmap → rapor.
4. **Araştırma arşivi** — `arastirma/{ulke}/{istirak}/{unvan}/{YYYY-MM}-top5.md` + _INDEKS.
5. **Toplantı & iletişim** — standup satırları, tutanaklar, üst/yan/alt hatlar.
6. **Öğrenme** — `BILGI_TABANI.md` akışı, changelog takibi, sertifika ilerleme.

## Gerekli secret'ler (KULLANICI ekler — Secrets paneli)
`SUPABASE_URL` · `SUPABASE_ANON_KEY` · `SUPABASE_SERVICE_ROLE` · (ops.) `STRIPE_API_KEY` · `ANTHROPIC_API_KEY` (gecelik LLM) · dağıtım: `EXPO_TOKEN` / `APPLE_*` / `GOOGLE_PLAY_*`.

## Kurulum sırası (secret'ler eklendikten sonra)
1. Supabase şeması: `holding`, `units`, `org_titles`, `tasks`, `research_archive`, `meetings` tabloları (RLS).
2. Web iskele (Next.js) → 6 ekran; `data/holding.json` + `.claude/org/org.json` okur.
3. RN/Expo → aynı veri; App Store/Play dağıtımı.
4. Gecelik döngü (Scheduled/Routines) → araştırma arşivini + org kartlarını besler.
