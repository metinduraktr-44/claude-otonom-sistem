# ÜLKE / PAZAR İSKELETİ
> Üretim: 2026-08-04T08:38:41Z · 10 ülke · Nightly research döngüsü

| Kod | Ülke | Rol | Dil | Hukuk | Öncelik |
|---|---|---|---|---|---:|
| TR | Türkiye | hedef+pazar | tr | KVKK, Ticaret Kanunu, Reklam Kurulu | 1 |
| US | United States | pazar | en | CCPA/CPRA, FTC Ads, HIPAA (health touch) | 2 |
| DE | Germany | pazar | de | GDPR, UWG, TMG | 3 |
| UK | United Kingdom | pazar | en | UK GDPR, ASA CAP, PECR | 4 |
| NL | Netherlands | pazar | nl | GDPR, ACM | 5 |
| AE | United Arab Emirates | pazar | ar/en | PDPL, ADGM/DIFC | 6 |
| SA | Saudi Arabia | pazar | ar/en | PDPL, CITC | 7 |
| CA | Canada | pazar | en/fr | PIPEDA, CASL | 8 |
| AU | Australia | pazar | en | Privacy Act, ACL | 9 |
| FR | France | pazar | fr | GDPR, CNIL, ARPP | 10 |

## Nightly workflow (her ülke)
1. Zaman damgalı arşivi oku
2. Hukuk/dil/rekabet + top5 yeniden tara
3. `uretim/ulke-arsiv/{CODE}/YYYY-MM-DD.md` yaz
4. BILGI_TABANI + AUDIT_LOG

🚩 Cowork URL bekleme yok — repo döngüsü yeter.
