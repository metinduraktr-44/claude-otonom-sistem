# TRANSFER PAKETİ — Tahmin Uzmanı
> 2026-08-04T08:44:30Z · hedef repo: `a-agency-tahmin-uzman-` · segment: agency

## Nasıl uygula (hedef repoda)
1. Bu dosyayı oku
2. `python3 standardize_repo.py . <tip> <repo>` (HQ scripts kopyala)
3. Rol kartlarını `.claude/agents/` veya `docs/rol-kartlari/` altına taşı
4. BILGI_TABANI + AUDIT_LOG başlat

## Domain
Spor/finans/danışmanlık forecast

## C-roles
CEO, CSO, CDO

## Departmanlar
- **FCST** Forecasting: Sports Models, Finance Models, Scenario Lab
- **RES** Araştırma: Signal Desk, Source QA, Archive Loop
- **DEL** Teslimat: Client Briefs, Risk Flags, Retros

## EVP/C pilot (HQ uretim/rol-kartlari)

- `tahmin-ceo` — CEO, Tahmin Uzmanı — reports_to: owner
- `tahmin-cso` — CSO, Tahmin Uzmanı — reports_to: group-ceo
- `tahmin-cdo` — CDO, Tahmin Uzmanı — reports_to: group-ceo
- `tahmin-evp-forecasting` — EVP, Forecasting — reports_to: tahmin-ceo
- `tahmin-evp-araştırma` — EVP, Araştırma — reports_to: tahmin-ceo
- `tahmin-evp-teslimat` — EVP, Teslimat — reports_to: tahmin-ceo

## Top-5 seed
- Nate Silver — probabilistik forecast — https://www.natesilver.net
- Philip Tetlock — superforecasting — https://www.goodjudgment.com
- Annie Duke — karar bilimi — https://www.annieduke.com
- Nassim Taleb — risk/anti-fragile — https://www.fooledbyrandomness.com
- Gary Klein — naturalistic decision — https://www.gary-klein.com

## Workflows
- bireysel: eğitim, iş-listesi, todo, roadmap, toplantı, alt-üst-iletişim, yan-iletişim
- grupsal: dept-sync, standup, board, escalation, retro, okrs
- 7x24: follow-the-sun · 3 vardiya · nightly research archive

🚩 Bu bulutta hedef repoya push yetkisi yok; paket HQ’da hazır.
