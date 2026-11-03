# Transparent Code Controls 021–100

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok


**MODE:** ASSESS-ONLY · **ts:** 2026-11-03T11:47:59Z · **count:** 80/100 (kümülatif 100/100 bu motor tranche hedefi 001–100)

Kolonlar: id, ad, açıklama, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi

### TC-021 — SBOM format seçimi
- **açıklama:** CycloneDX veya SPDX hedefi yazılı.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-021 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-022 — SBOM kapsamı CI grafı
- **açıklama:** Workflow uses: listesi SBOM adayı.
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-022 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-023 — SBOM saklama yolu
- **açıklama:** Artefakt path planı (henüz üretme zorunlu değil).
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-023 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-024 — SBOM tüketici dokümanı
- **açıklama:** Doğrulama nasıl yapılır stub.
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-024 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-025 — Action SHA pin oranı ölçümü
- **açıklama:** rg uses @v vs @sha ASSESSMENTS.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-025 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-026 — Pin gap öncelik listesi
- **açıklama:** checkout/setup-python önce.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-026 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-027 — Immutable action tag yokluğu
- **açıklama:** Tag hareket riski notu.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-027 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-028 — 3. parti action allowlist taslağı
- **açıklama:** İsim listesi; exploit yok.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-028 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-029 — Action versiyon major sıçrama
- **açıklama:** v4→v5 review notu.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-029 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-030 — Dependabot Actions açık
- **açıklama:** dependabot.yml ASSESS.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-030 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-031 — Dependabot npm grup PR'ları
- **açıklama:** Katalog örnekleri izole risk.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-031 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-032 — SLSA seviye hedefi
- **açıklama:** supply-chain.md tablo.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-032 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-033 — Provenance build SHA bağlama
- **açıklama:** Run URL politikası.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-033 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-034 — Attestation depolama
- **açıklama:** gh attestation hedefi.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-034 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-035 — Immutable GitHub releases
- **açıklama:** Checklist ASSESS.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-035 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-036 — Release artefact checksum
- **açıklama:** SHA256 notu (doğrulama).
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-036 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-037 — Reproducible workflow hedefi
- **açıklama:** Aynı SHA aynı graf.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-037 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-038 — Vendored katalog SBOM opsiyonel
- **açıklama:** katalog politika.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-038 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-039 — Python stdlib beyanı
- **açıklama:** Root runtime pin'i stdlib.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-039 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-040 — Hash pin scriptleri
- **açıklama:** scanner script bütünlüğü git.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-040 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-041 — zizmor/actionlint hedefi
- **açıklama:** Tooling backlog (kurulum yok bu tur).
- **NIST_CSF:** ID.SC-02
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-041 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-042 — Scorecard ölçüm planı
- **açıklama:** OpenSSF Scorecard ASSESS backlog.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-042 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-043 — OSV tarama hedefi
- **açıklama:** Bağımlılık OSV (kapsam dar).
- **NIST_CSF:** GV.RR-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-043 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-044 — deps.dev farkındalık
- **açıklama:** Cilt 3 doğrulama araçları.
- **NIST_CSF:** ID.RA-05
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-044 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-045 — Socket.dev farkındalık
- **açıklama:** Supply-chain sinyal.
- **NIST_CSF:** ID.AM-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-045 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-046 — npm provenance farkındalık
- **açıklama:** Katalog paketleri için.
- **NIST_CSF:** ID.RA-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-046 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-047 — Fork PR secret sızdırmazlık
- **açıklama:** workflow design ASSESS.
- **NIST_CSF:** GV.PO-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-047 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-048 — pull_request_target kaçınma
- **açıklama:** Yanlış tetikleyici taraması.
- **NIST_CSF:** PR.AA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-048 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-049 — script injection farkındalığı
- **açıklama:** GHA context interpolasyon ASSESS.
- **NIST_CSF:** PR.DS-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-049 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-050 — Untrusted checkout güvenliği
- **açıklama:** Fork checkout sonra privileged yok.
- **NIST_CSF:** PR.IR-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-050 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-051 — Cache poison farkındalığı
- **açıklama:** cache key kapsamı.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-051 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-052 — Artifact download güveni
- **açıklama:** Başka job artefaktı imza/SHA.
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-052 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-053 — Composite action şeffaflığı
- **açıklama:** uses local path review.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-053 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-054 — Reusable workflow pin
- **açıklama:** caller pin SHA hedefi.
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-054 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-055 — Self-hosted runner yok teyidi
- **açıklama:** inventory.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-055 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-056 — Runner label hijyeni
- **açıklama:** Self-hosted yok.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-056 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-057 — Image base yok beyanı
- **açıklama:** Dockerfile prod yok.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-057 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-058 — Dockerfile örnek izolasyonu
- **açıklama:** katalog örnekleri çalıştırılmaz.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-058 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-059 — IaC module kaynak pin
- **açıklama:** Terraform module kaynak ASSESS.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-059 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-060 — Provider version constraint
- **açıklama:** terraform required_providers.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-060 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-061 — Lockfile terraform ASSESS
- **açıklama:** .terraform.lock.hcl var mı.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-061 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-062 — Helm/K8s manifest imza N/A
- **açıklama:** Prod cluster yok.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-062 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-063 — Cosign/keyless hedef notu
- **açıklama:** Gelecek; iddia yok.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-063 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-064 — Sigstore farkındalık
- **açıklama:** Doğrulama eğitimi.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-064 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-065 — In-toto farkındalık
- **açıklama:** SLSA komşu.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-065 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-066 — Git commit tree bütünlüğü
- **açıklama:** force-push yasağı ile paylaşır.
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-066 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-067 — Signed tags hedefi
- **açıklama:** annotated+signed.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-067 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-068 — GPG anahtar envanteri
- **açıklama:** İmza anahtarları org ASSESS.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-068 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-069 — SSH signing hedefi
- **açıklama:** Git SSH imza opsiyonu.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-069 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-070 — Merge commit doğrulanabilirliği
- **açıklama:** GitHub verified badge ASSESS.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-070 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-071 — Subresource integrity N/A
- **açıklama:** Web CDN yok.
- **NIST_CSF:** ID.SC-02
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-071 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-072 — Lockfile npm katalog
- **açıklama:** örnek todo-app izole.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-072 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-073 — Pip hash-checking N/A
- **açıklama:** pip yok/root.
- **NIST_CSF:** GV.RR-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-073 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-074 — Go sum N/A
- **açıklama:** Go prod yok.
- **NIST_CSF:** ID.RA-05
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-074 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-075 — Rust audit N/A
- **açıklama:** Rust prod yok.
- **NIST_CSF:** ID.AM-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-075 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-076 — Binary blob yasağı
- **açıklama:** Üçüncü parti binary commit yok.
- **NIST_CSF:** ID.RA-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-076 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-077 — Prebuilt tool checksum
- **açıklama:** İndirilen CLI SHA256 zorunlu hedef.
- **NIST_CSF:** GV.PO-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-077 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-078 — Uzaktan kurulum yönlendirme yasağı
- **açıklama:** Tespit kuralı; kurulum tarifi yok.
- **NIST_CSF:** PR.AA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-078 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-079 — Unpinned gist yasağı
- **açıklama:** Workflow gist uses yok.
- **NIST_CSF:** PR.DS-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-079 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-080 — Container digest pin N/A
- **açıklama:** Image yok.
- **NIST_CSF:** PR.IR-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-080 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-081 — Workflow permissions least
- **açıklama:** permissions: blokları ASSESS.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-081 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-082 — GITHUB_TOKEN write daraltma
- **açıklama:** contents: read varsayılan hedef.
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-082 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-083 — id-token izin bilinçli
- **açıklama:** OIDC yalnızca gerektiğinde.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-083 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-084 — packages: write N/A
- **açıklama:** Paket publish yok.
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-084 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-085 — attestations izin hedefi
- **açıklama:** Gelecek kapı.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-085 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-086 — concurrency group
- **açıklama:** Eski run iptal politikası ASSESS.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-086 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-087 — Cancel-in-progress bilinç
- **açıklama:** Yarım artefakt riski.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-087 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-088 — Matrix explosion sınırı
- **açıklama:** CI maliyet + yüzey.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-088 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-089 — Third-party badge tıklama riski
- **açıklama:** README rozet URL allowlist kültürü.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-089 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-090 — GitHub App diff review
- **açıklama:** Yeni app izinleri.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-090 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-091 — Marketplace install yasağı ajan
- **açıklama:** Sahte 'Claude Code Setup' eklenti RED.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-091 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-092 — Untrusted skill ingest
- **açıklama:** Viral PDF damıtılır, çalıştırılmaz.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-092 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-093 — Model ağırlığı yok
- **açıklama:** Repo model binaries taşımaz.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-093 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-094 — LFS pointer hijyeni
- **açıklama:** Beklenmeyen LFS ASSESS.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-094 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-095 — Large JSON secret tarama
- **açıklama:** MANIFEST gürültüsü false-positive politikası.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-095 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-096 — CycloneDX CLI yok iddiası
- **açıklama:** Henüz kurulmadı; hedef ayrı.
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-096 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-097 — Transparency log hedef notu
- **açıklama:** Rekor/CT benzeri gelecek.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-097 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-098 — Consumer verify runbook
- **açıklama:** docs stub plan.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-098 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-099 — TC kanıt CSV satırı
- **açıklama:** matrix-021-100.csv.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-099 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### TC-100 — TC review döngüsü 021–100
- **açıklama:** TASKS kapanış.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı TC-100 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

