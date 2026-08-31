# ORG_CHART — Holding × Creative Agency

> Kaynak: `data/holding_istirak_org.json` · 8 iştirak · 633 rol · refresh 2026-08-27T12:56:59Z
> Duplicate yok — detay rol listesi JSON'da; bu dosya eşleme katmanı.

## Kurul (Group Board)

| Rol | Slug | Görev |
|-----|------|-------|
| Chairman / Sahip | owner | Nihai onay: sermaye, faz kapıları |
| Group CEO | group-ceo | Portföy stratejisi |
| Group COO | group-coo | Operasyon ritmi |
| Group CTO | group-cto | CI, doğrulama, MCP |
| Group CFO | group-cfo | API bütçesi |
| Group CCO | group-cco | 5 güvenlik kuralı + uyum |

## Creative Agency OS → Holding eşlemesi

Bu repo (`claude-otonom-sistem`) **Holding HQ / OS** katmanında çalışır. Kreatif üretim hattı **AdOps CRE** departmanına bağlanır; medya satırı **SOC**.

```
KURUL (6)
 └── Holding HQ / OS (71 rol) ← Creative Agency OS (.cursor/)
      ├── INF — Teknoloji & Altyapı (CI, MCP, hooks)
      ├── TAL — Yetenek & Ajan Kalitesi (skills, critics)
      └── PRD — Ürün & Premium Paket
 └── AdOps Agency (219 rol) ← Ana kreatif/medyan hattı
      ├── CRE — Kreatif Stüdyo & DCO ★
      │    ├── Concept & Copy
      │    ├── Video & Motion
      │    ├── DCO & Feeds
      │    └── Ad Format Lab
      ├── SOC — Ücretli Sosyal (Meta, TikTok, …)
      ├── STR — Strateji & Planlama
      ├── ANA — Analitik & Ölçümleme
      └── … (PRG, SEA, MOB, RET, SEO, CRO, CLS, NBD, PRT)
 └── Diğer iştirakler — marka-özel kreatif ihtiyaçları (referans JSON)
```

## Rol dağılımı

| İştirak | ID | Rol | Prompt hedef |
|---------|-----|-----:|-------------:|
| Holding HQ / OS | hq | 71 | 8662 |
| AdOps Agency | adops | 219 | 26718 |
| Performer Growth Hub | performer | 78 | 9516 |
| VizaTrack | vizatrack | 84 | 10248 |
| Holding Hukuk & Uyum | hukuk | 55 | 6710 |
| Tahmin Uzmanı | tahmin | 56 | 6832 |
| Movéa (M-AIOS) | movea | 35 | 4270 |
| Çiğköftem | cigkoftem | 35 | 4270 |
| **Toplam** | | **633** | **77226** |

## Creative Agency OS rolleri (Cursor katmanı)

| Rol | Sorumluluk | Skill/Command |
|-----|------------|---------------|
| Orkestratör | Faz yönetimi, STATE | `/baslat`, `/devam` |
| Brief Writer | Kampanya brief | `brief-writer`, `/brief-uret` |
| Scenario Lead | Kreatif senaryo | `creative-scenarios` |
| Spec Engineer | Kanal spec doğrulama | `spec-matrix`, `/spec-dogrula` |
| Canva Operator | Design ops (CANVA:ON only) | `canva-*` skills, `/canva-uret` |
| Expert Engine | Persona rotasyonu | `expert-engine`, `/uzman-guncelle` |
| QA Lead | critic-* subagents | `QA/QA_REPORT.md` |
| Archivist | Kampanya arşivi | `archive-loop`, `/arsivle` |

## Referanslar

- Detay org: `docs/HOLDING-ISTIRAK-ORG.md`
- Rol kartları: `uretim/rol-kartlari/` (48 pilot) — bio uydurma yok
- AdOps CRE EVP: `uretim/rol-kartlari/adops-evp-kreatif-stüdyo-dco.md`
- Ajans org JSON: `data/ajans_org.json`
- Experts digest: `EXPERTS/DIGEST.md`
