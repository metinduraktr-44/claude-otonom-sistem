# /is-karti — Faz 4 İş Kartı Üretimi (skeleton→tam)

## Objective
Envanterdeki title için `JOB_CARDS/{slug}/CARD.md` üret veya genişlet.

## Requirements
- Faz 0–1: skeleton + INDEX yeterli
- Faz 4+: 2000+ char, 200+ başlık hedefi (fazlı)
- Paralel agent: title grubu izolasyonu `JOB_CARDS/{slug}/`
- QA olmadan "tamam" işaretleme

## Output
- İş kartı dosyası yolu
- Durum: skeleton | in-progress | qa-pending
