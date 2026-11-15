# Change Controls 021–100

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok


**MODE:** ASSESS-ONLY · **ts:** 2026-11-03T11:47:59Z · **count:** 80/100 (kümülatif 100/100 bu motor tranche hedefi 001–100)

Kolonlar: id, ad, açıklama, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi

### CHG-021 — PR şablon güvenlik maddesi ASSESS
- **açıklama:** PR checklist'te secret/ethics kutusu hedefi.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-021 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-022 — Zorunlu review sayısı ASSESS
- **açıklama:** Branch protection required reviews.
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-022 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-023 — CODEOWNERS güvenlik yolları yenileme
- **açıklama:** SECURITY_*, scripts/scanners sahipliği.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-023 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-024 — Admin bypass izleme
- **açıklama:** Koruma bypass audit (org ayarı ASSESS).
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-024 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-025 — Force-push yasağı ana dal
- **açıklama:** main force-push kapalı hedef.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-025 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-026 — Doğrudan commit yasağı main
- **açıklama:** PR-only kültür.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-026 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-027 — Signed commit hedefi (change)
- **açıklama:** İmza politikası org ASSESS.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-027 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-028 — STATUS check zorunluluğu
- **açıklama:** validate/ethics/secret_scan hedef kapısı.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-028 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-029 — Draft PR merceği
- **açıklama:** Draft, secret taramasından muaf değil.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-029 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-030 — Fork PR maintainer edit ASSESS
- **açıklama:** Fork katkı ağı izolasyonu.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-030 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-031 — Label high-risk değişim
- **açıklama:** workflows/** high-risk etiketi.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-031 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-032 — Workflow değişikliği ikinci onay
- **açıklama:** GHA dosyası extra review.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-032 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-033 — Hook kural değişikliği denetimi
- **açıklama:** ethics/secret kuralı PR ile gelir.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-033 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-034 — Scanner false-positive süreci
- **açıklama:** Kural gevşetme gerekçeli PR.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-034 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-035 — Bağımlılık bump ayrı PR
- **açıklama:** Dependabot tek konu.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-035 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-036 — Major bump insan kapısı
- **açıklama:** actions major sürüm + pin gap notu.
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-036 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-037 — Terraform plan review
- **açıklama:** infra plan artefaktı ASSESS.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-037 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-038 — State lock farkındalığı
- **açıklama:** tf lock N/A/gap.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-038 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-039 — Doküman-only yolu
- **açıklama:** MODE ASSESS-ONLY doküman PR'ları.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-039 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-040 — Kod değişimi MODE notu
- **açıklama:** Agresif pin uygulaması bu turda yok.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-040 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-041 — Rollback / git revert prosedürü
- **açıklama:** Kötü merge revert runbook stub.
- **NIST_CSF:** ID.SC-02
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-041 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-042 — Tag immutable hedefi
- **açıklama:** Tag hareket ettirme yasağı.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-042 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-043 — Release notes güvenlik satırı
- **açıklama:** Bilinen gap'ler release notunda abartılmaz.
- **NIST_CSF:** GV.RR-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-043 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-044 — Hotfix dar kapsam
- **açıklama:** Acil PR yalnızca ilgili dosya.
- **NIST_CSF:** ID.RA-05
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-044 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-045 — Feature flag N/A
- **açıklama:** Ürün flag yok; MODE bayrağı STATE'de.
- **NIST_CSF:** ID.AM-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-045 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-046 — Migration N/A
- **açıklama:** DB migration yok.
- **NIST_CSF:** ID.RA-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-046 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-047 — Schema change N/A
- **açıklama:** Ürün şeması yok.
- **NIST_CSF:** GV.PO-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-047 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-048 — API breaking change N/A
- **açıklama:** Ürün API yok.
- **NIST_CSF:** PR.AA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-048 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-049 — Skill sürümleme
- **açıklama:** Skill references DELTA yazımı.
- **NIST_CSF:** PR.DS-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-049 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-050 — Prompt dump yasağı değişim
- **açıklama:** 900M/900B prompt PR reddi.
- **NIST_CSF:** PR.IR-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-050 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-051 — Expert bio uydurma yasağı
- **açıklama:** EXPERTS yalnızca kaynak+ts.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-051 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-052 — Agency brief değişim ritmi
- **açıklama:** Brief PR critic-copy hedefi.
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-052 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-053 — LATOS kart batch limiti
- **açıklama:** 10 skeleton; 200 başlık uydurma yok.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-053 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-054 — Paralel track silme yasağı
- **açıklama:** Diğer OS dosyaları silinmez.
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-054 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-055 — Merge kullanıcı onayı
- **açıklama:** DEVAM ≠ merge.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-055 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-056 — Upstream-sync review
- **açıklama:** vendor delta insan incelemesi.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-056 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-057 — Submodule yasağı/ASSESS
- **açıklama:** Git submodule yok teyidi.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-057 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-058 — LFS politika
- **açıklama:** Büyük binary PR reddi.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-058 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-059 — Generated dosya disiplini
- **açıklama:** _generated rastgele commit yok.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-059 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-060 — Lockfile yoksa açıklama
- **açıklama:** Python stdlib; npm lock kökte yok.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-060 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-061 — Lisans uyumu değişim
- **açıklama:** Vendored MIT atıf korunur.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-061 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-062 — Gizli dosya .gitignore
- **açıklama:** Secret aday yolları ignore.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-062 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-063 — Pre-commit yerel opsiyon
- **açıklama:** Hook'lar Cursor/GHA; local opsiyonel.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-063 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-064 — CI skip yasağı
- **açıklama:** skip-ci kültürü güvenlik PR'da yok.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-064 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-065 — Schedule workflow değişimi
- **açıklama:** cron değişikliği kapasite ASSESS.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-065 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-066 — Environment protection kuralı
- **açıklama:** prod environment yoksa N/A.
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-066 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-067 — OIDC role değişimi
- **açıklama:** Bulut rolü yok/N/A.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-067 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-068 — Secret listesine ekleme süreci
- **açıklama:** Yeni secret adı SECRETS matrisine yazılır (değer yok).
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-068 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-069 — Secret silme süreci
- **açıklama:** Kullanılmayan secret rotate+remove.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-069 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-070 — Erişim kaybı offboarding
- **açıklama:** Collaborator çıkışı ASSESS.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-070 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-071 — Yeni collaborator onayı
- **açıklama:** En az yetki + süre.
- **NIST_CSF:** ID.SC-02
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-071 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-072 — Bot hesabı değişimi
- **açıklama:** Automation user envanteri.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-072 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-073 — App installation değişimi
- **açıklama:** GitHub App kapsam ASSESS.
- **NIST_CSF:** GV.RR-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-073 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-074 — Marketplace publish N/A
- **açıklama:** Bizim action publish yok.
- **NIST_CSF:** ID.RA-05
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-074 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-075 — Pages publish N/A
- **açıklama:** GitHub Pages yok/teyit.
- **NIST_CSF:** ID.AM-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-075 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-076 — Wiki değişim N/A
- **açıklama:** Wiki kullanılmıyorsa kapat hedefi.
- **NIST_CSF:** ID.RA-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-076 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-077 — Issue template güvenlik
- **açıklama:** Issue'ya secret yapıştırma uyarısı.
- **NIST_CSF:** GV.PO-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-077 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-078 — Discussion secret yasağı
- **açıklama:** Forum/sohbet redaksiyon.
- **NIST_CSF:** PR.AA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-078 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-079 — PR screenshot redaksiyon
- **açıklama:** UI'da token yok.
- **NIST_CSF:** PR.DS-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-079 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-080 — Commit mesajı secret yasağı
- **açıklama:** Mesajda key yok.
- **NIST_CSF:** PR.IR-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-080 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-081 — Rebase vs merge politikası
- **açıklama:** main'e squash/merge org standardı ASSESS.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-081 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-082 — Cherry-pick güvenlik fix
- **açıklama:** Fix ileri taşınır; exploit yayılmaz.
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-082 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-083 — Backport N/A
- **açıklama:** Tek ana hat.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-083 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-084 — Versiyon numarası VERSIONS.md
- **açıklama:** Anlamlı sürüm notu.
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-084 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-085 — CHANGELOG güvenlik maddesi
- **açıklama:** Kullanıcıya zararlı adım yazılmaz.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-085 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-086 — Deprecation duyurusu
- **açıklama:** Kontrol N/A geçişi yazılı.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-086 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-087 — Acil erişim değişimi kaydı
- **açıklama:** break-glass AUDIT.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-087 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-088 — CAB/hafif onay ritmi
- **açıklama:** Aylık kurul güvenlik maddesi.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-088 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-089 — Aylık expert refresh değişimi
- **açıklama:** Liste PR ile.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-089 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-090 — Standards currency refresh
- **açıklama:** SECURITY_RESEARCH damgası.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-090 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-091 — Threat landscape refresh
- **açıklama:** Yeni sınıf (sosyal mühendislik ingest) eklenir.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-091 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-092 — Skill depth DELTA
- **açıklama:** 20k hedefe küçük ekler.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-092 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-093 — Matrix CSV eş zamanlı güncelleme
- **açıklama:** Kontrol dosyası ve CSV aynı PR.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-093 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-094 — Sahipsiz dosya yasağı
- **açıklama:** Yeni kontrol klasörü motor adına bağlı.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-094 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-095 — Dosya adı istikrarı
- **açıklama:** controls-021-100.md kalıcı yol.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-095 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-096 — Büyük PR bölme kuralı
- **açıklama:** Track'ler karışmaz (MCP arşiv ayrı).
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-096 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-097 — Test kırılırsa merge yok
- **açıklama:** validate KALDI ise dur.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-097 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-098 — Ethics KALDI merge yok
- **açıklama:** offensive desen temizlenir.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-098 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-099 — Secret hit merge yok
- **açıklama:** değer yok; konum düzeltilir.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-099 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### CHG-100 — CHG review döngüsü 021–100
- **açıklama:** TASKS kapanış.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı CHG-100 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

