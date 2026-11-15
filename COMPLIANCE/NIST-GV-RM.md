# NIST CSF 2.0 — GV.RM Risk Management (ASSESS stub)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

> **MODE:** ASSESS-ONLY · **ts:** 2026-11-15T09:50:00Z · **Faz 5+**  
> **Kaynak:** NIST CSF 2.0 Govern → **GV.RM** (Risk Management Strategy) — CSWP 29 (2024-02-26).  
> Bu dosya **nicel risk kabul stub**’tır. Hücre `PASS` **yazılmaz**. Sertifika / audit iddiası yok.  
> **600 kontrol yeniden yazımı YOK.**

Çapraz: [INDEX.md](INDEX.md) · [NIST-CSF-2.0.md](NIST-CSF-2.0.md) · `SECURITY_MATRIX/` · `STATE.md` MODE

## Durum (dürüst)

| Soru | Cevap |
|------|--------|
| Risk appetite nicel (para/SLA) | **yok** — tablo iskelet; değerler `TBD` |
| Risk kabul imza / SoA | **yok** |
| Sahte PASS | **yasak** |
| MODE=IMPLEMENT | kapalı — pin/CI sertleştirme ayrı kapı |
| INDEX’teki GV.RM boşluğu | bu stub **kapatır iskeleti**, kanıt üretmez |

## GV.RM alt kategoriler (NIST etiket → repo)

| Alt | NIST niyet (kısa) | Repo bağ | kanıt_durum | boşluk |
|-----|-------------------|----------|-------------|--------|
| GV.RM-01 | Risk yönetim hedefleri belirlenir | `STATE.md` MODE=ASSESS-ONLY; GUARDRAIL | ASSESS | Nicel hedef (RTO/RPO/€) yok |
| GV.RM-02 | Risk iştahı / tolerans ifade edilir | Bu tablo (TBD satırlar) | ASSESS | Sayısal eşik yok |
| GV.RM-03 | ERM süreçlerine siber risk dahil | AUDIT_LOG + OZET; CISO JOB_CARD skeleton | ASSESS | ERM entegrasyon ritüeli yok |
| GV.RM-04 | Risk yanıt seçenekleri yönü | ASSESS vs IMPLEMENT / CANVA kapıları | ASSESS | Formal response matrix yok |
| GV.RM-05 | Risk iletişim hatları (tedarik dahil) | MCP kapalı varsayılan; GHA notu | ASSESS | Tedarikçi risk kanalı zayıf |
| GV.RM-06 | Standart risk hesap/öncelik yöntemi | Bu tablo iskeleti | ASSESS | Skor metodu TBD — uydurma skor yok |
| GV.RM-07 | Pozitif risk / fırsat | BRIEF-ONLY faturalanabilir doküman yolu | ASSESS | Fırsat kaydı ayrı değil |

*Kaynak damgası:* NIST CSWP 29 (CSF 2.0, 2024-02-26) — https://nvlpubs.nist.gov/nistpubs/cswp/nist.cswp.29.pdf · erişim 2026-11-15T09:50:00Z. Alt ID’ler resmi Core; lisanslı spreadsheet kopyası değil.

## Risk kabul tablosu (iskelet — değer uydurma yok)

| Risk ID | Varlık / yüzey | Etki (TBD) | Olasılık (TBD) | İştah | Tedavi (ASSESS) | Sahip |
|---------|----------------|------------|----------------|-------|-----------------|-------|
| R-001 | Secret sızıntısı (chat/log) | TBD | TBD | Düşük kabul | `secret_scan.py`; `${VAR}` | hq-lead-validation-security |
| R-002 | GHA pin eksik (tag≠SHA40) | TBD | TBD | **IMPLEMENT kapısı** | Gap notu; uygulama yok | hq-lead-ci-cd-actions |
| R-003 | Offensive içerik üretimi | TBD | TBD | Sıfır kabul | `ethics_check.py` + GUARDRAIL | CISO / ethics |
| R-004 | Marka/claim hatası (Agency) | TBD | TBD | INBOX kilidi | critic REVISE; CANVA:OFF | hq-lead-quality-bar |
| R-005 | 72 rol git restore hatası | TBD | TBD | İnsan onayı | katalog; restore=NO | LATOS / Metin |

**Kural:** Etki/olasılık hücreleri `TBD` kalır ta ki Metin nicel iştah verir. Uydurma skor = sahte uygunluk.

## MODE bağları

| Kapı | GV.RM etkisi |
|------|----------------|
| ASSESS-ONLY (varsayılan) | Gap + stub; risk tablosu doldurulmaz sahte skorla |
| MODE=IMPLEMENT | Pin/CI sertleştirme **izin** — bu dosyada otomatik açılmaz |
| CANVA:ON | Agency tasarım riski ayrı; Security GV.RM’yi genişletmez |
| 72 restore | İnsan kapısı; otomatik tedavi yok |

## Sonraki (onaylı DEVAM — hâlâ PASS değil)

- [ ] Metin: risk iştahı (nicel) → `CONTEXT/INBOX/` veya bu tabloyu doldur
- [ ] ISO A.5 SoA özet (93 değil; 20 satır) — #39 ile çakıştırma yok
- [ ] SOC 2 CC işaretçi (`SOC2.md`)
- [ ] IR playbook ASSESS (Faz 6)

⏱️ Damga: 2026-11-15T09:50:00Z · Denetim: ASSESS stub · Öğrenim: GV.RM stub ≠ risk kabul imzası
