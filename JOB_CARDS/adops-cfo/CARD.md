# CFO, AdOps Agency

> **status:** skeleton · **faz:** 1–4 pilot · **slug:** `adops-cfo`
> **ts:** 2026-11-15T09:57:00Z · **tz:** Europe/Istanbul 2026-11-15 12:57+03
> Tam hedef (Faz 4+): 2.000+ karakter + 200 başlık — bu kart **dürüst skeleton+pilot**; H021–H200 backlog.

> Git notu: `uretim/rol-kartlari/` history'de silinmiş olabilir — restore **insan onaylı**.

## Kimlik
- **Unvan:** CFO, AdOps Agency
- **Tier:** C-LEVEL
- **Reports to:** `adops-ceo`
- **Unit:** adops
- **Envanter:** `ROSTER/TITLE_INVENTORY.md` (633 title; hiçbir title atlanmaz)

## Misyon
Ajans marj, medya spend vs fee, CRE kapasite maliyeti.

## LLM agency yapısı (C-level → işçi)
```
Owner / Chairman (insan onay)
 └── Group / Holding C-suite (CEO·COO·CTO·CFO·CCO·CAIO)
      └── EVP / Director (alan sahibi)
           └── Manager / Lead (ajans orkestratör prompt)
                └── Analyst / Operator (P00x execution prompt)
                     └── Worker / Specialist (tek görev, token sınırı)
```
Bu title'ın katmanı: **C-LEVEL**. Alt title'lar envanterde durur; atlama yok, üretim fazlı.

## Sorumluluklar
- Kendi alan KPI + RACI.
- Nightly/daily çıktıyı okuyup DELTA yazmak (BILGI_TABANI zinciri).
- Secret: `${VAR}` / `<REDACTED>` — chat/commit yok.
- 🚩 Tek prompt 900.000.000 karakter **fiziksel imkânsız / RED**. Sözleşme 4–12 KiB + `P001.md`…

## RACI
| Alan | R | A | C | I |
|------|---|---|---|---|
| Alan operasyonu | adops-cfo | adops-ceo | hq-ceo | Birim CEO |
| Ethics/secret sapma | hq-cco | hq-ceo | CISO | Tüm ajanlar |
| Prompt bütçesi | hq-caio | hq-cfo | hq-cto | LATOS |

## KPI (placeholder — ölçüm Faz 7)
- validate.py GECTI
- qa_check missing-card delta (hedef: düşen backlog)
- Aylık expert döngüsü: ARCHIVE okundu mu?

## 7/24 + toplantı (iskelet)
- Günlük: standup digest (`OPERATIONS/247_WORKFLOWS.md`)
- Haftalık: OKR confidence
- Aylık: `CALENDAR/LATOS_RESEARCH_LOOP.md` — oku arşiv → web not → yaz `ARCHIVE/YYYY-MM/`

## Roadmap bağ
- `ROADMAP/adops-cfo.md` (hedef / faz kapısı / iş akışı listesi)
- Deadline: **faz kapısı**, takvim günü değil (ajan gün/hafta yazmaz)

## INDEX (H001–H020 dolu isim; H021–H200 placeholder)
| # | Başlık | Durum | Not |
|---|--------|-------|-----|
| H001 | Kimlik & mandate | skeleton | Rolün kimlik & mandate alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H002 | Raporlama hattı | skeleton | Rolün raporlama hattı alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H003 | RACI matrisi | skeleton | Rolün raci matrisi alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H004 | KPI seti | skeleton | Rolün kpi seti alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H005 | Escalation | skeleton | Rolün escalation alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H006 | LLM agency arayüzü | skeleton | Rolün llm agency arayüzü alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H007 | 7/24 workflow | skeleton | Rolün 7/24 workflow alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H008 | Toplantı ritmi | skeleton | Rolün toplantı ritmi alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H009 | Roadmap & deadline (fazlı) | skeleton | Rolün roadmap & deadline (fazlı) alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H010 | QA / doğrulama | skeleton | Rolün qa / doğrulama alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H011 | Secret hygiene | skeleton | Rolün secret hygiene alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H012 | Ethics guardrail | skeleton | Rolün ethics guardrail alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H013 | Envanter bağı | skeleton | Rolün envanter bağı alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H014 | Prompt sözleşmesi | skeleton | Rolün prompt sözleşmesi alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H015 | Arşiv & aylık döngü | skeleton | Rolün arşiv & aylık döngü alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H016 | Eğitim / competency | skeleton | Rolün eğitim / competency alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H017 | Kapasite & span | skeleton | Rolün kapasite & span alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H018 | Risk kaydı | skeleton | Rolün risk kaydı alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H019 | İnsan onay kapıları | skeleton | Rolün i̇nsan onay kapıları alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H020 | Sonraki DEVAM | skeleton | Rolün sonraki devam alanı: holding JSON + STATE.md. Açıklama fazlı; 200 başlık tek oturumda üretilmez. Yönlendirme: `/is-karti adops-cfo`. Eğitim: critic-spec + qa_check. |
| H021–H200 | (200 hedef) | backlog | `/latos-devam` |

## 🚩 Dürüstlük
633×100×122×900M tek oturumda **yapılmaz**. Bu kart envanter satırını JOB_CARDS'a bağlar.
