# AYLIK GÜNCELLEME TAKVİMİ — Etki / Yetenek / MCP Arşivi
> Oluşturma: 2026-11-01T06:07:41Z · Döngü: her ayın 1'i 06:00 UTC (`scripts/mcp_ajans_etki_uret.py --hepsi`)

## Rutin
1. MCP katalog + canlı sunucu farkı → `data/mcp_hiyerarsi.json`
2. Etki sahipleri: yeni makale/röportaj/proje taraması → `son_inceleme` güncelle
3. Özel yetenekler: kültür/sanat/spor sinyali → arşiv
4. Prompt index yenile (sözleşme değişmedikçe body hash stabil)
5. BILGI_TABANI + AUDIT_LOG damga

## 12 aylık takvim
| Ay | Odak | Çıktı |
|---|---|---|
| 2026-11 | AI/C-level etki yenileme | arşiv diff + AUDIT satırı |
| 2026-12 | Açık kaynak & araç liderleri | arşiv diff + AUDIT satırı |
| 2027-01 | Güvenlik & hizalama isimleri | arşiv diff + AUDIT satırı |
| 2027-02 | Yatırımcı / strateji sesleri | arşiv diff + AUDIT satırı |
| 2027-03 | Spor yetenekleri | arşiv diff + AUDIT satırı |
| 2027-04 | Müzik & yaratıcı ekonomi | arşiv diff + AUDIT satırı |
| 2027-05 | Sinema / tasarım | arşiv diff + AUDIT satırı |
| 2027-06 | Edebiyat / fikir | arşiv diff + AUDIT satırı |
| 2027-07 | MCP yeni bağlayıcılar | arşiv diff + AUDIT satırı |
| 2027-08 | Pilot birim gelir sinyali | arşiv diff + AUDIT satırı |
| 2027-09 | Yıl sonu ranking revizyonu | arşiv diff + AUDIT satırı |
| 2027-10 | Boş-slot araştırma kapatma | arşiv diff + AUDIT satırı |

## Otomasyon kancası
- Mevcut: `.github/workflows/aylik-kurul.yml` (ayın 1'i)
- Ekleme önerisi: aynı workflow'a `python3 scripts/mcp_ajans_etki_uret.py --hepsi --pilot` adımı
