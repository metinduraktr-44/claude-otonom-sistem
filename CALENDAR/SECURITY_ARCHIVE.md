# CALENDAR — Security arşiv döngüsü

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**Ritim:** ay sonu `/arsivle` veya `archive-loop` · **tz:** Europe/Istanbul

| Ne zaman | İş | Çıktı |
|----------|-----|--------|
| Ay sonu | Snapshot stub | `ARCHIVE/YYYY-MM/security/MANIFEST.md` |
| SoA değişince | `python3 scripts/giga_security_faz6_soa.py` | `COMPLIANCE/ISO27001-2022-SOA.md` |
| CTRL eklendiğinde | coverage notu | `SECURITY_MATRIX/coverage.md` |

İlk kayıt: 2026-11 (FAZ6 SoA iskeleti). Silme yok.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
