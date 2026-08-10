# TRANSFER PAKETİ — Holding Hukuk & Uyum
> 2026-08-04T08:44:30Z · hedef repo: `claude-otonom-sistem` · segment: shared-service

## Nasıl uygula (hedef repoda)
1. Bu dosyayı oku
2. `python3 standardize_repo.py . <tip> <repo>` (HQ scripts kopyala)
3. Rol kartlarını `.claude/agents/` veya `docs/rol-kartlari/` altına taşı
4. BILGI_TABANI + AUDIT_LOG başlat

## Domain
KVKK/GDPR, lisans, reklam politikası, sözleşme, ülke onayı

## C-roles
CLO, CCO, DPO

## Departmanlar
- **PRIV** Gizlilik: KVKK, GDPR, DPIA
- **LIC** Lisanslama: OSS License, Vendor Contracts, IP
- **ADP** Reklam Politikası: Platform Policy, Claim Review, Crisis
- **REG** Regülasyon: Ülke Onayı, Cross-border Transfer, Retention

## EVP/C pilot (HQ uretim/rol-kartlari)

- `hukuk-clo` — CLO, Holding Hukuk & Uyum — reports_to: group-ceo
- `hukuk-cco` — CCO, Holding Hukuk & Uyum — reports_to: group-ceo
- `hukuk-dpo` — DPO, Holding Hukuk & Uyum — reports_to: group-ceo
- `hukuk-evp-gizlilik` — EVP, Gizlilik — reports_to: hukuk-ceo
- `hukuk-evp-lisanslama` — EVP, Lisanslama — reports_to: hukuk-ceo
- `hukuk-evp-reklam-politikası` — EVP, Reklam Politikası — reports_to: hukuk-ceo
- `hukuk-evp-regülasyon` — EVP, Regülasyon — reports_to: hukuk-ceo

## Top-5 seed
- Daniel Solove — gizlilik hukuku — https://teachprivacy.com
- Woodrow Hartzog — privacy by design — https://www.woodrowhartzog.com
- Helen Nissenbaum — contextual integrity — https://nissenbaum.tech.cornell.edu
- EDPB (kurum) — GDPR otorite — https://edpb.europa.eu
- KVKK (kurum) — TR gizlilik — https://www.kvkk.gov.tr

## Workflows
- bireysel: eğitim, iş-listesi, todo, roadmap, toplantı, alt-üst-iletişim, yan-iletişim
- grupsal: dept-sync, standup, board, escalation, retro, okrs
- 7x24: follow-the-sun · 3 vardiya · nightly research archive

🚩 Bu bulutta hedef repoya push yetkisi yok; paket HQ’da hazır.
