# CIS Controls v8 — IG1 kanıt sütunu (ASSESS stub)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

> **MODE:** ASSESS-ONLY · **ts:** 2026-11-10T11:55:00Z · **Faz 5+**  
> **Kaynak:** CIS Controls v8 / v8.1 IG1 (temel hijyen) — **lisanslı CIS spreadsheet kopyası yok.**  
> Bu dosya **kanıt indeksi stub**’tır. Hücre `PASS` **yazılmaz**. Sertifika / audit iddiası yok.

Çapraz: [INDEX.md](INDEX.md) · [CIS-Controls.md](CIS-Controls.md) · `SECURITY_MATRIX/matrix-001-020.csv` + `matrix-021-100.csv`

## Durum (dürüst)

| Soru | Cevap |
|------|--------|
| IG1 tam SoA (56 safeguard) | **yok** — kontrol-seviyesi + kanıt yolu stub |
| Sahte PASS | **yasak** |
| MODE=IMPLEMENT | kapalı — pin/CI sertleştirme yok |
| CIS 18 pentest | **RED** — saldırı prosedürü / PoC yok |
| 600 kontrol yeniden yazımı | **yok** |

## Sütun sözlüğü

| Sütun | Anlam |
|-------|--------|
| IG1 | CIS IG1 kapsamı (evet / kısmi / zayıf / N/A / RED) |
| kanıt_yolu | Repoda bakılacak dosya/script — varlık ≠ uygunluk |
| kanıt_durum | her zaman `ASSESS` veya `N/A` veya `RED` — **PASS yok** |
| boşluk | ne eksik |

## CIS 1–18 × IG1 kanıt

| CIS | Başlık | IG1 | kanıt_yolu | kanıt_durum | boşluk |
|-----|--------|-----|------------|-------------|--------|
| 1 | Enterprise Asset Inventory | evet | `SECURITY_CONTEXT/inventory.md` | ASSESS | Donanım/cloud asset CMDB yok |
| 2 | Software Inventory | kısmi | `katalog/` izole; stdlib Python | ASSESS | SBOM üretim CI yok; pin gap |
| 3 | Data Protection | evet | `scripts/secret_scan.py`; `docs/SECRETS-DRYRUN-MATRISI.md` | ASSESS | Sınıflandırma politikası kısa; DLP yok |
| 4 | Secure Configuration | kısmi | `scripts/validate.py`; `.github/workflows/` | ASSESS | GHA SHA40 pin **0**; IMPLEMENT kapısı |
| 5 | Account Management | kısmi | `ORG/ROLES/`; GHA identities notu | ASSESS | IdP envanteri yok |
| 6 | Access Control Lists | kısmi | token scope ASSESS; COND kontroller | ASSESS | MFA kanıtı repo-dışı |
| 7 | Continuous Vulnerability | zayıf | `SECURITY_RESEARCH/` currency | ASSESS | Dependabot PR açık; scanner CI yok |
| 8 | Audit Log Management | kısmi | `AUDIT_LOG.jsonl`; `REPORTS/` | ASSESS | SIEM/retention SLA yok |
| 9 | Email & Web Browser | N/A | `SECURITY_CONTEXT/inventory.md` (N/A) | N/A | Holding OS e-posta/endpoint değil |
| 10 | Malware Defenses | N/A/zayıf | ethics yasak listesi | ASSESS | Endpoint AV bu runtime’da yok |
| 11 | Data Recovery | zayıf | git remote; LAY yedekleme satırı | ASSESS | Restore testi yok; 72 rol restore ayrı kapı |
| 12 | Network Infrastructure | kısmi | FW motor; egress allowlist doküman | ASSESS | Canlı ağ diyagramı yok |
| 13 | Network Monitoring | zayıf | DE.CM notu INDEX | ASSESS | Faz 6; central alerting yok |
| 14 | Security Awareness | zayıf | GUARDRAIL rules; EXPERTS seed | ASSESS | Eğitim kaydı/quiz yok |
| 15 | Service Provider Management | kısmi | MCP varsayılan kapalı; Actions | ASSESS | Tedarikçi SoA yok |
| 16 | Application Software Security | kısmi | `scripts/ethics_check.py`; validate | ASSESS | SAST/DAST yok; pentest RED |
| 17 | Incident Response | zayıf | SecOps rol iskeleti; IR skill | ASSESS | Playbook Faz 6; #39 ile çakıştırma yok |
| 18 | Penetration Testing | **RED** | — | **RED** | ASSESS-ONLY; exploit/PoC **üretilmez** |

## Safeguard SoA (bilinçli boş)

IG1’in ~56 safeguard satırı **doldurulmadı**. Neden: lisanslı CIS ID tablosu repo’da yok; uydurma ID = sahte uygunluk.

Sonraki (onaylı DEVAM, hâlâ PASS değil):

- [ ] Lisanslı CIS v8.1 IG1 ID listesini `CONTEXT/INBOX/`’a bırak → satır satır `kanıt_yolu`
- [ ] GV.RM nicel risk kabul tablosu (ayrı)
- [ ] ISO A.5 SoA 20 satır özet — **#39 kopyalama yok**

## Nasıl okunur

1. `kanıt_yolu` dosyayı aç; scanner çıktısına bak.
2. `ASSESS` = gap notu geçerli; kapatma IMPLEMENT veya ayrı hardening PR.
3. `RED` = bu OS kasıtlı olarak üretmez (CIS 18).
4. Bu tabloyu “CIS IG1 uyumlu” diye alıntılama.
