# Encryption Controls 001–020

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok


**MODE:** ASSESS-ONLY · **ts:** 2026-08-27T12:54:55Z · **count:** 20/100

Kolonlar: id, ad, açıklama, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi

### ENC-001 — TLS minimum sürüm politikası
- **açıklama:** Outbound TLS ≥1.2; hedef 1.3.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-8
- **ISO27001:** A.8.24
- **CIS:** CIS-3
- **OWASP:** A02 ASVS crypto
- **doğrulama_yöntemi:** Python/OS TLS varsayılanı + doküman politikası
- **savunma_gerekçesi:** Pasif dinlemeye karşı iletim koruması

### ENC-002 — Certificate verification zorunlu
- **açıklama:** ssl verify kapatma yasak; kodda av.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-8
- **ISO27001:** A.8.24
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** rg verify=False scripts
- **savunma_gerekçesi:** MITM sınıfı riske karşı

### ENC-003 — Secret at-rest politikası
- **açıklama:** Secrets disk/repo’da plaintext yasak; Actions secrets / vault.
- **NIST_CSF:** PR.DS-01
- **800-53:** SC-28
- **ISO27001:** A.8.11
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** secret_scan + .gitignore
- **savunma_gerekçesi:** At-rest ifşa engeli

### ENC-004 — Sensitive Terraform değişkenleri
- **açıklama:** Token tipleri sensitive=true; değer example’da yok.
- **NIST_CSF:** PR.DS-01
- **800-53:** SC-28
- **ISO27001:** A.8.11
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** variables.tf sensitive bayrakları
- **savunma_gerekçesi:** State/tfvars sızıntı riski

### ENC-005 — Remote state encryption ASSESS
- **açıklama:** TF state backend şifreleme hedefi belgelenir.
- **NIST_CSF:** PR.DS-01
- **800-53:** SC-28
- **ISO27001:** A.8.24
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** backend config ASSESS
- **savunma_gerekçesi:** State içinde secret tipi korunur

### ENC-006 — Key rotation prosedür referansı
- **açıklama:** Rotate adımları değer içermeden yazılı.
- **NIST_CSF:** PR.AA-03
- **800-53:** IA-5 SC-12
- **ISO27001:** A.8.24
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** SECRETS-DRYRUN + runbook
- **savunma_gerekçesi:** Çalıntı anahtar ömrünü kısaltır

### ENC-007 — Crypto envanteri
- **açıklama:** Kullanılan protokol/kütüphane listesi.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-13
- **ISO27001:** A.5.9
- **CIS:** CIS-1
- **OWASP:** ASVS
- **doğrulama_yöntemi:** encryption-engine inventory stub
- **savunma_gerekçesi:** Bilinen zayıf algo avı için temel

### ENC-008 — Zayıf algoritma yasak listesi (isim)
- **açıklama:** MD5/SHA1 bütünlük, RC4 vs. isim düzeyinde yasak.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-13
- **ISO27001:** A.8.24
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** kod/algo envanter taraması
- **savunma_gerekçesi:** Klasik zayıf kripto kullanımını önler

### ENC-009 — PQC FIPS 203 farkındalık
- **açıklama:** ML-KEM standardı roadmap’te.
- **NIST_CSF:** ID.RA PR.DS
- **800-53:** SC-12 SC-13
- **ISO27001:** A.8.24
- **CIS:** CIS-3
- **OWASP:** ASVS crypto
- **doğrulama_yöntemi:** pqc-roadmap.md
- **savunma_gerekçesi:** Kuantum-era key exchange hazırlığı

### ENC-010 — PQC FIPS 204 farkındalık
- **açıklama:** ML-DSA imza standardı roadmap’te.
- **NIST_CSF:** PR.DS
- **800-53:** SC-13
- **ISO27001:** A.8.24
- **CIS:** CIS-3
- **OWASP:** A08 signing
- **doğrulama_yöntemi:** pqc-roadmap.md
- **savunma_gerekçesi:** Uzun vadeli imza çevikliği

### ENC-011 — PQC FIPS 205 farkındalık
- **açıklama:** SLH-DSA hash-based alternatif belgelenir.
- **NIST_CSF:** PR.DS
- **800-53:** SC-13
- **ISO27001:** A.8.24
- **CIS:** CIS-3
- **OWASP:** A08
- **doğrulama_yöntemi:** pqc-roadmap.md
- **savunma_gerekçesi:** Algoritma çeşitliliği

### ENC-012 — Crypto-agility gereksinimi
- **açıklama:** Algo değişiminde tek nokta kırılganlık planı.
- **NIST_CSF:** ID.RA-05
- **800-53:** SC-13
- **ISO27001:** A.8.24
- **CIS:** CIS-4
- **OWASP:** ASVS
- **doğrulama_yöntemi:** crypto-agility skill
- **savunma_gerekçesi:** PQC/klasik geçiş maliyeti düşer

### ENC-013 — HNDL risk notu
- **açıklama:** Uzun ömürlü gizli veri yok varsayımı + token TTL.
- **NIST_CSF:** ID.RA-01
- **800-53:** RA-3
- **ISO27001:** A.5.7
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** threat-landscape + pqc-roadmap
- **savunma_gerekçesi:** Harvest-now riskini yönetir

### ENC-014 — GitHub Secrets şifreleme güveni
- **açıklama:** Org/repo secrets kullan; plaintext env commit yok.
- **NIST_CSF:** PR.DS-01
- **800-53:** SC-28
- **ISO27001:** A.8.11
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** workflow secrets kullanımları
- **savunma_gerekçesi:** CI gizli malzeme koruması

### ENC-015 — Log mask encryption-adjacent
- **açıklama:** CI log mask + redaksiyon.
- **NIST_CSF:** PR.DS DE.CM
- **800-53:** AU-9
- **ISO27001:** A.8.12
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** secret_scan REPORTS
- **savunma_gerekçesi:** Şifreli kanal sonrası log sızıntısı engeli

### ENC-016 — Commit imza ASVS hedefi
- **açıklama:** İsteğe bağlı signed commits / release attestation.
- **NIST_CSF:** PR.DS-06
- **800-53:** SI-7
- **ISO27001:** A.8.26
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** git config / immutable releases ASSESS
- **savunma_gerekçesi:** Bütünlük ve inkâr edilemezlik

### ENC-017 — Transport integrity LLM API
- **açıklama:** HTTPS only API base URL.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-8
- **ISO27001:** A.8.24
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** client base_url https teyidi
- **savunma_gerekçesi:** API key ve prompt koruması

### ENC-018 — Randomness/stdlib bilinç
- **açıklama:** Güvenlik için secrets/token üretimi varsa CSPRNG; holding’de minimal.
- **NIST_CSF:** PR.DS
- **800-53:** SC-12
- **ISO27001:** A.8.24
- **CIS:** CIS-3
- **OWASP:** ASVS
- **doğrulama_yöntemi:** token üretim noktaları ASSESS
- **savunma_gerekçesi:** Tahmin edilebilir secret engeli

### ENC-019 — Vault placeholder standardı
- **açıklama:** Doküman vault:///<REDACTED> veya ${VAR}.
- **NIST_CSF:** PR.DS-01
- **800-53:** IA-5
- **ISO27001:** A.5.15
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** rg vault:// veya ${VAR} SECURITY
- **savunma_gerekçesi:** Yanlışlıkla gerçek secret basmayı önler

### ENC-020 — ENC review döngüsü
- **açıklama:** ENC-001–020 periyodik ASSESS.
- **NIST_CSF:** GV.OV
- **800-53:** CA-2
- **ISO27001:** A.5.35
- **CIS:** CIS-4
- **OWASP:** QA
- **doğrulama_yöntemi:** TASKS
- **savunma_gerekçesi:** Kripto politikası güncel kalır
