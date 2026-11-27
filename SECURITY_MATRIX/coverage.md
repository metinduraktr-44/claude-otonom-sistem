# SECURITY_MATRIX — coverage notes (dürüst)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**ts_utc:** 2026-11-03T11:50:00Z · **MODE:** `ASSESS-ONLY`

## İki sayaç — karıştırma

| Kaynak | Ne sayar | Sayı (bu tur hedef) |
|--------|----------|---------------------|
| `SECURITY_MATRIX/matrix.md` | Kavramsal crosswalk satır (LAY/FW/ENC/CHG/TC/COND 001–020) | **120 / 600** |
| Katalog `CTRL-*.md` | Dosya kartı (FAZ3 seed 88 + SAMPLE) | **89** (2026-11-03 `giga_security_faz6_soa.py`) |
| SoA | ISO 27001:2022 Annex A | **93 satır** (uygulanır ≠ implemente) |

120 matris satırının hepsinde birebir `CTRL-*.md` **yok**. Katalog 001–015/012 ağırlıklı; FAZ6 `L-016/017`, `FW-013/014`, `ENC-013`, `CH-013/014`, `TC-013/014`, `CD-016` ekler.

`CTRL-ENC-013` (log DLP) ≠ matris satırı `ENC-013` (HNDL notu). ID şeması yakın; SoA katalog YAML `ISO27001` alanına bakar.

## FAZ6 ekleri
ISO gap dolgusu (kimlik, auth info, cloud, URL hijyen, DLP, kaynak erişimi, ortam ayrımı, vuln mgmt, güvenlik testi, yasal kapsam).

## Sonraki
- Katalog 021–100 × 6 (batch)
- Matris 021–100
- NIST/CIS/SOC2 pack (SoA değil, crosswalk genişletme)

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
