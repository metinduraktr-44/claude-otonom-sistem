# COMPLIANCE INDEX — NIST CSF 2.0 × ISO 27001:2022 × CIS Controls v8

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

> **MODE:** ASSESS-ONLY · **Faz:** 5 skeleton · **ts:** 2026-11-10T11:55:00Z  
> **Kapsam:** INDEX + çapraz harita. **900 sayfa SoA / 600 kontrol yeniden yazımı YOK.**  
> Satır kaynağı: `SECURITY_MATRIX/matrix-001-020.csv` + `matrix-021-100.csv` (**600** satır, 6 motor × 100).

## Durum (dürüst)

| Artefakt | Durum | Not |
|----------|-------|-----|
| 600 kontrol katalog | ASSESS stub | Faz 3–4; uygulama kanıtı yok |
| Matrix CSV çapraz sütun | var | NIST_CSF / 800-53 / ISO27001 / CIS / OWASP |
| Bu INDEX | **iskelet** | Fonksiyon→motor; kontrol-kontrol SoA değil |
| ISO SoA 93 kontrol | **yok** | PR #39 ayrı dal; bu PR merge etmez |
| SOC 2 TSC | **değil bu dilim** | `SOC2.md` işaretçi |
| CIS IG1 kanıt sütunu | **stub** | `CIS-IG1.md` — PASS yok |
| MODE=IMPLEMENT | kapalı | Pin/CI sertleştirme ayrı onay |

## 6 motor (katalog)

| Prefiks | Motor | n | CSF ağırlık (CSV token) |
|---------|-------|---|-------------------------|
| LAY | Katman / DiD | 100 | GV, ID.AM, PR.PS |
| FW | Ağ / egress / sınır | 100 | PR.IR, ID.SC |
| ENC | Kripto / at-rest | 100 | PR.DS |
| CHG | Değişiklik / tedarik | 100 | ID.SC, GV.PO |
| TC | Tooling / CI / ajan | 100 | PR.PS, PR.AA |
| COND | Koşullu / istisna | 100 | GV.OV, RS/RC |

**Toplam:** 600. Detay satır **yeniden üretilmez** — CSV’ye bak.

## NIST CSF 2.0 — fonksiyon INDEX

Kaynak: NIST CSF 2.0 (Feb 2024) Govern + 5 fonksiyon. Bu repo **kanıt değil**, harita.

| CSF 2.0 | Kategori (seçilmiş) | Motor | Örnek kontrol ID | Repo kanıt (ASSESS) |
|---------|---------------------|-------|------------------|---------------------|
| **GV** Govern | GV.OC / GV.PO / GV.RM / GV.RR / GV.OV | LAY, CHG, COND | LAY-003, LAY-016, LAY-020 | `STATE.md` MODE; plan Faz 5–8 |
| **ID** Identify | ID.AM / ID.RA / ID.SC | LAY, FW, CHG | LAY-001, FW-003, CHG-001* | `SECURITY_CONTEXT/inventory.md` |
| **PR** Protect | PR.AA / PR.DS / PR.PS / PR.IR | ENC, FW, TC | ENC-001, FW-001, TC-* | secret_scan, ethics_check, pin-gap notu |
| **DE** Detect | DE.CM | LAY, TC | LAY-011 | hooks + scanner exit |
| **RS** Respond | RS.MA / RS.MI | LAY, COND | LAY-015 | SecOps rol iskeleti; playbook Faz 6 |
| **RC** Recover | RC.RP | LAY, COND | LAY-024 | yedekleme katmanı **ASSESS** — restore yok |

\*CHG-001 CSV’de; INDEX satır örneği. Tam liste = CSV.

### CSF boşlukları (ASSESS — sahte PASS yok)

- GV.RM (risk appetite nicel) CSV’de **1** token — zayıf.
- DE.AE (analiz) ayrı satır seti **yok**.
- RS.CO / RS.AN iletişim-analiz playbook **Faz 6**.
- RC.CO iletişim; RC.IM iyileştirme **yok**.
- Tag-pin GHA (25) vs SHA40 (0) = PR.PS tedarik **açık**; uygulama IMPLEMENT kapısı.

## ISO/IEC 27001:2022 — Annex A tema INDEX

93 Annex A kontrolünün tam SoA’sı **bu dosyada yok**. Tema → motor.

| Tema | ISO | Motor | Örnek A. | Not |
|------|-----|-------|----------|-----|
| Örgütsel | A.5 | LAY, CHG, COND | A.5.1 politika, A.5.9 envanter, A.5.21 tedarik, A.5.24 IR | STATE + inventory |
| İnsan | A.6 | — | A.6.3 farkındalık | LATOS/JOB_CARDS iskelet; eğitim paketi yok |
| Fiziksel | A.7 | N/A beyan | — | Cloud-agent / GitHub; tesis yok |
| Teknolojik | A.8 | ENC, FW, TC | A.8.9 config, A.8.12 sızıntı, A.8.24 kripto, A.8.32 change | CSV ISO sütunu |

**SoA durumu:** her Annex A satırı için Applicable/Implemented/Kanıt **doldurulmadı**. PR #39 (`giga-security-faz6`) SoA stub ayrı — **çakıştırma/merge yok**.

## CIS Controls v8 — IG INDEX

| CIS | Başlık (kısa) | IG1 | Motor | Repo ASSESS |
|-----|---------------|-----|-------|-------------|
| 1 | Envanter | evet | LAY | inventory.md |
| 2 | Yazılım envanteri | kısmi | CHG, TC | katalog vendored; pin gap |
| 3 | Veri koruma | evet | ENC, LAY | sınıflandırma + secret_scan |
| 4 | Güvenli config | kısmi | TC, LAY | validate.py; GHA permissions ASSESS |
| 5 | Hesap | kısmi | LAY | kimlik katmanı stub |
| 6 | Erişim | kısmi | LAY, FW | token scope ASSESS |
| 7 | Sürekli zafiyet | zayıf | CHG | research currency; scanner CI yok |
| 8 | Denetim log | kısmi | LAY | AUDIT_LOG.jsonl (işlem; SIEM değil) |
| 9 | E-posta/web | N/A | FW | inventory N/A |
| 10 | Malware savunması | N/A/zayıf | — | endpoint yok; etik yasak listesi |
| 11 | Kurtarma | zayıf | LAY | yedekleme ASSESS |
| 12 | Ağ | kısmi | FW | egress allowlist doküman |
| 13 | Ağ izleme | zayıf | DE | Faz 6 |
| 14 | Farkındalık | zayıf | A.6 | — |
| 15 | Servis sağlayıcı | kısmi | CHG, FW | MCP varsayılan kapalı |
| 16 | Uygulama güvenliği | kısmi | TC | ethics/validate; SAST yok |
| 17 | IR | zayıf | LAY | rol var, playbook yok |
| 18 | Penetrasyon | **RED** | — | ASSESS-ONLY; saldırı prosedürü yok |

## Nasıl kullanılır

1. Kontrol satırı ara: CSV `id` (LAY-042 … COND-100).
2. Çerçeve hücresi **hedef etiketidir**, sertifika kanıtı değil.
3. Yeni kontrol **yazma**; haritayı düzeltmek için CSV hücresi + bu INDEX notu.
4. IMPLEMENT veya audit-pack = ayrı insan kapısı.

## Sonraki (Faz 5+; bu PR değil)

- [ ] GV.RM tek sayfa risk kabul tablosu (ASSESS)
- [x] CIS IG1 kanıt sütunu stub (`CIS-IG1.md` — PASS değil; SoA 56 yok)
- [ ] ISO A.5 SoA 20 satırlık **özet** (93 değil)
- [ ] SOC 2 CC1–CC9 işaretçi doldurma (`SOC2.md`)
