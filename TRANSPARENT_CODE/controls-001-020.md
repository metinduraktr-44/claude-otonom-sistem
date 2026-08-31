# Transparent Code Controls 001–020

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok


**MODE:** ASSESS-ONLY · **ts:** 2026-08-27T12:54:55Z · **count:** 20/100

Kolonlar: id, ad, açıklama, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi

### TC-001 — SBOM üretim gereksinimi
- **açıklama:** CI/action grafı için SBOM (CycloneDX/SPDX) hedefi.
- **NIST_CSF:** ID.SC-02
- **800-53:** SA-12
- **ISO27001:** A.5.21
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** SBOM planı transparent-code references
- **savunma_gerekçesi:** Bileşen şeffaflığı

### TC-002 — Action SHA pin zorunluluğu ASSESS
- **açıklama:** uses satırları 40-char SHA.
- **NIST_CSF:** ID.SC-03
- **800-53:** SA-12 SI-7
- **ISO27001:** A.5.21
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** rg uses workflows pin oranı
- **savunma_gerekçesi:** Tag repoint sınıfı savunma

### TC-003 — Dependabot Actions güncellemesi
- **açıklama:** github-actions ekosistemi açık.
- **NIST_CSF:** ID.SC
- **800-53:** RA-5 SA-12
- **ISO27001:** A.8.8
- **CIS:** CIS-7
- **OWASP:** A08
- **doğrulama_yöntemi:** dependabot.yml ASSESS
- **savunma_gerekçesi:** Pin’leri güvenli günceller

### TC-004 — SLSA provenance hedef seviyesi
- **açıklama:** L1→L2 roadmap belgelenir.
- **NIST_CSF:** ID.SC PR.DS
- **800-53:** SA-12
- **ISO27001:** A.5.21
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** supply-chain.md SLSA tablo
- **savunma_gerekçesi:** İnşa bütünlüğü

### TC-005 — Immutable releases ASSESS
- **açıklama:** Org/repo immutable release hedefi.
- **NIST_CSF:** PR.DS-06
- **800-53:** SI-7
- **ISO27001:** A.8.26
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** GitHub docs checklist
- **savunma_gerekçesi:** Release asset/tag kilidi

### TC-006 — Release attestation ASSESS
- **açıklama:** Sigstore/GitHub attestation doğrulama planı.
- **NIST_CSF:** PR.DS-06
- **800-53:** SI-7
- **ISO27001:** A.8.26
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** gh attestation ASSESS
- **savunma_gerekçesi:** Tüketici doğrulaması

### TC-007 — Action allowlist
- **açıklama:** Yeni Action ekleme gerekçeli allowlist.
- **NIST_CSF:** ID.SC-03
- **800-53:** SA-12
- **ISO27001:** A.5.19
- **CIS:** CIS-15
- **OWASP:** A08
- **doğrulama_yöntemi:** allowlist doküman stub
- **savunma_gerekçesi:** Gölge bağımlılık engeli

### TC-008 — Workflow SBOM artefakt saklama
- **açıklama:** SBOM REPORTS veya release’de.
- **NIST_CSF:** ID.SC
- **800-53:** AU-7
- **ISO27001:** A.5.21
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** path planı
- **savunma_gerekçesi:** Denetim kanıtı

### TC-009 — Katalog ayrı SBOM (opsiyonel)
- **açıklama:** Vendored ağaç ayrı izlenir.
- **NIST_CSF:** ID.SC
- **800-53:** SA-12
- **ISO27001:** A.5.21
- **CIS:** CIS-15
- **OWASP:** A08
- **doğrulama_yöntemi:** katalog politika
- **savunma_gerekçesi:** Karışıklığı önler

### TC-010 — Scorecard ASSESS
- **açıklama:** OpenSSF Scorecard çalıştırma planı.
- **NIST_CSF:** ID.RA
- **800-53:** RA-5
- **ISO27001:** A.8.8
- **CIS:** CIS-7
- **OWASP:** A08
- **doğrulama_yöntemi:** TASKS backlog
- **savunma_gerekçesi:** Dış sinyal ile gap

### TC-011 — zizmor/actionlint ASSESS
- **açıklama:** Workflow dangerous pattern taraması.
- **NIST_CSF:** DE.CM
- **800-53:** SI-4
- **ISO27001:** A.8.16
- **CIS:** CIS-8
- **OWASP:** A08
- **doğrulama_yöntemi:** tooling backlog
- **savunma_gerekçesi:** CI misconfig tespiti

### TC-012 — Provenance commit SHA bağlama
- **açıklama:** Artefakt↔commit izlenebilir.
- **NIST_CSF:** PR.DS-06
- **800-53:** SI-7
- **ISO27001:** A.8.26
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** GHA run URL politikası
- **savunma_gerekçesi:** İnkâr edilemezlik

### TC-013 — Fork PR secret izolasyonu (TC)
- **açıklama:** Supply-chain + IAM kesişimi.
- **NIST_CSF:** PR.AA ID.SC
- **800-53:** AC-3 SA-12
- **ISO27001:** A.8.3
- **CIS:** CIS-6
- **OWASP:** A07
- **doğrulama_yöntemi:** workflow design ASSESS
- **savunma_gerekçesi:** PR üzerinden exfil keser

### TC-014 — Lockfile bilinci
- **açıklama:** Root lock yok (stdlib); yeni dep eklenirse lock zorunlu.
- **NIST_CSF:** ID.SC
- **800-53:** SA-10
- **ISO27001:** A.8.28
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** AGENTS.md + PR gate
- **savunma_gerekçesi:** Reproduce edilebilirlik

### TC-015 — Image/base yok beyanı
- **açıklama:** Container image yüzeyi yok; eklenirse pin+SBOM.
- **NIST_CSF:** ID.AM
- **800-53:** CM-8
- **ISO27001:** A.5.9
- **CIS:** CIS-1
- **OWASP:** Scope
- **doğrulama_yöntemi:** inventory
- **savunma_gerekçesi:** Yeni yüzey kontrolü

### TC-016 — Third-party action CVE sınıfı izleme
- **açıklama:** Action compromise sınıfı research’te.
- **NIST_CSF:** ID.RA
- **800-53:** RA-5
- **ISO27001:** A.8.8
- **CIS:** CIS-7
- **OWASP:** A08
- **doğrulama_yöntemi:** threat-landscape.md
- **savunma_gerekçesi:** Erken uyarı

### TC-017 — Build script bütünlüğü
- **açıklama:** scripts/ değişimleri review + scan.
- **NIST_CSF:** PR.PS
- **800-53:** CM-3 SI-7
- **ISO27001:** A.8.28
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** PR + scanners
- **savunma_gerekçesi:** Generator güvenliği

### TC-018 — Transparency log hedefi
- **açıklama:** İleride rekor/sigstore transparency ASSESS.
- **NIST_CSF:** PR.DS
- **800-53:** SI-7
- **ISO27001:** A.8.26
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** roadmap notu
- **savunma_gerekçesi:** Uzun vadeli doğrulanabilirlik

### TC-019 — Consumer verify dokümanı
- **açıklama:** Tüketicinin attestation doğrulama adımları (değer yok).
- **NIST_CSF:** PR.DS-06
- **800-53:** SI-7
- **ISO27001:** A.8.26
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** docs stub plan
- **savunma_gerekçesi:** Dış güven

### TC-020 — TC review döngüsü
- **açıklama:** TC-001–020 periyodik.
- **NIST_CSF:** GV.OV
- **800-53:** CA-2
- **ISO27001:** A.5.35
- **CIS:** CIS-4
- **OWASP:** QA
- **doğrulama_yöntemi:** TASKS
- **savunma_gerekçesi:** Supply-chain kontrolleri güncel
