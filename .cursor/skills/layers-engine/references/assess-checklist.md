# LAY ASSESS checklist (kısa)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**ts:** 2026-11-10T11:55:00Z · DiD katmanları · exploit yok

| Katman | Repo bakışı | ASSESS boşluk |
|--------|-------------|----------------|
| Network | `FIREWALLS/` + inventory egress | canlı diyagram yok |
| Identity | `ORG/ROLES/` + COND | IdP/MFA kanıtı repo-dışı |
| App | `scripts/validate.py` `ethics_check.py` | SAST yok |
| Data | `secret_scan.py` ENC katalog | DLP yok |
| Detect | hooks + AUDIT_LOG | SIEM yok (Faz 6) |
| Recover | git remote | restore testi yok; 72 title restore insan |

Yeni LAY-xxx **yazma**. Katalog 600/600. Kanıt: `COMPLIANCE/CIS-IG1.md`.
