# LATOS aylık research loop

> **ts:** 2026-11-15T09:57:00Z · komut: `/latos-aylik-dongu`
> Nightly GHA **kırılmadan** bu ritüel dokümanda yaşar (`nightly-improve.yml` dokunulmadı).

## Her ay (zorunlu sıra)

1. **OKU** `ARCHIVE/YYYY-MM/latos/` (önceki ay yoksa: “yok” yaz)
2. **OKU** `EXPERTS/{title}/` + `EXPERTS_TALENT/{skill}/` mevcut seed
3. **ARA** web (IAB, FIDE, Wikipedia, Thinkers50) — uydurma kişi YASAK
4. **YAZ** `ARCHIVE/YYYY-MM/latos/DIGEST.md` (URL+ts)
5. **DELTA** yalnızca değişen satırlar → expert/talent dosyası
6. **DIGEST** `EXPERTS/LEARNINGS.md` 1 satır
7. **QA** `python3 scripts/citation_check.py` · `qa_check.py`

## Takvim

| Ay | Motor | Durum |
|----|-------|-------|
| 2026-11 | LATOS research loop + 10 JOB_CARDS pilot | **bu tur** |
| 2026-12 | hq-ceo / adops-ceo expert +5 kaynaklı satır | pending |
| 2026-01 | 10 ek title skeleton | pending |

## 7/24 bağ

Günlük tahmin (Faz 9) yok. Günlük: `OPERATIONS/247_WORKFLOWS.md` iskelet. LLM key yoksa skeleton.
