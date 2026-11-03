# COMPLIANCE

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**MODE:** `ASSESS-ONLY` · Sertifika iddiası yok.

| Dosya | İçerik |
|-------|--------|
| `ISO27001-2022-pack.md` | Paket özeti (`/compliance-paket`) |
| `ISO27001-2022-SOA.md` | Annex A 93 SoA iskeleti → mevcut `CTRL-*` |
| `gap-evidence.md` | GAP + N/A gerekçeleri |

Üretici: `python3 scripts/giga_security_faz6_soa.py` (idempotent).

NIST/CIS/SOC2 ayrı pack: backlog. Crosswalk kolonları: `SECURITY_MATRIX/matrix.md`.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
