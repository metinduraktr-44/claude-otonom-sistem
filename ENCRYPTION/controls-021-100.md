# Encryption Controls 021–100

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok


**MODE:** ASSESS-ONLY · **ts:** 2026-11-03T11:47:59Z · **count:** 80/100 (kümülatif 100/100 bu motor tranche hedefi 001–100)

Kolonlar: id, ad, açıklama, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi

### ENC-021 — TLS 1.2 taban teyidi
- **açıklama:** Outbound istemciler TLS1.2 altını kullanmaz.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-021 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-022 — TLS 1.3 tercih kaydı
- **açıklama:** Hedef sürüm 1.3; gap ASSESS.
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-022 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-023 — Sertifika doğrulama zorunlu
- **açıklama:** verify=False yasağı (tespit taraması).
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-023 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-024 — Özel CA envanteri
- **açıklama:** Kurumsal CA yoksa N/A.
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-024 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-025 — Sertifika süre izleme N/A
- **açıklama:** Ürün sertifikası yok; GitHub/API kendi zinciri.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-025 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-026 — HSTS N/A
- **açıklama:** Bizim kenar yok.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-026 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-027 — Cipher deny listesi (isim)
- **açıklama:** NULL/EXPORT/RC4 isim olarak yasak; PoC yok.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-027 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-028 — Zayıf hash yasak listesi
- **açıklama:** MD5/SHA1 imza kullanımı taraması.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-028 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-029 — HMAC vs encryption ayrımı
- **açıklama:** Bütünlük ve gizlilik kontrolleri karıştırılmaz.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-029 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-030 — AEAD tercih kaydı
- **açıklama:** Yeni tasarımda AEAD; mevcut kod stdlib.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-030 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-031 — Anahtar üretim noktası envanteri
- **açıklama:** Token üretim yerleri ASSESS.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-031 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-032 — stdlib secrets kullanımı
- **açıklama:** os.urandom/secrets tercih; zayıf PRNG tarama.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-032 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-033 — Anahtar saklama politikası
- **açıklama:** Diskte düz anahtar yok; ${VAR}|vault://.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-033 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-034 — Anahtar rotasyon referansı
- **açıklama:** SECRETS-DRYRUN + runbook işaretçisi.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-034 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-035 — Anahtar imha politikası
- **açıklama:** Sızıntıda rotate; değere chat'te yer yok.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-035 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-036 — KMS/HSM N/A veya hedef
- **açıklama:** Bulut KMS yoksa gap/N/A yazılı.
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-036 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-037 — GitHub Secrets şifreleme güveni
- **açıklama:** Platform şifrelemesine güven + kapsam daraltma.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-037 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-038 — Cursor Secrets ayrımı
- **açıklama:** LLM anahtarları sohbet geçmişine yapıştırılmaz.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-038 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-039 — Terraform sensitive bayrağı
- **açıklama:** variables.tf sensitive ASSESS.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-039 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-040 — Remote state encryption ASSESS
- **açıklama:** backend şifreleme notu.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-040 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-041 — At-rest markdown redaksiyon
- **açıklama:** Raporlarda <REDACTED> standardı.
- **NIST_CSF:** ID.SC-02
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-041 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-042 — Yedek şifreleme N/A
- **açıklama:** Ayrı yedek ürünü yok; git remote TLS.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-042 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-043 — Disk şifreleme N/A
- **açıklama:** Runner disk GitHub sorumluluğu.
- **NIST_CSF:** GV.RR-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-043 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-044 — DB TDE N/A
- **açıklama:** Veritabanı yok.
- **NIST_CSF:** ID.RA-05
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-044 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-045 — Obje depo SSE N/A
- **açıklama:** Bucket yok.
- **NIST_CSF:** ID.AM-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-045 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-046 — Log şifreleme-adjacent maske
- **açıklama:** secret_scan REPORTS.
- **NIST_CSF:** ID.RA-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-046 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-047 — E-posta şifreleme N/A
- **açıklama:** Ürün mail yok.
- **NIST_CSF:** GV.PO-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-047 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-048 — Dosya şifreleme aracı yok iddiası
- **açıklama:** age/gpg prod akışı yok; iddia edilmez.
- **NIST_CSF:** PR.AA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-048 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-049 — Field-level encryption N/A
- **açıklama:** Uygulama şeması yok.
- **NIST_CSF:** PR.DS-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-049 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-050 — Token binding N/A
- **açıklama:** OAuth Canva kapalı.
- **NIST_CSF:** PR.IR-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-050 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-051 — PQC FIPS 203 farkındalık yenileme
- **açıklama:** ML-KEM yol haritası pqc-roadmap.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-051 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-052 — PQC FIPS 204 farkındalık yenileme
- **açıklama:** ML-DSA imza farkındalığı.
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-052 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-053 — PQC FIPS 205 farkındalık yenileme
- **açıklama:** SLH-DSA farkındalığı.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-053 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-054 — HNDL risk kaydı
- **açıklama:** Harvest-now decrypt-later notu (savunma).
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-054 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-055 — Kripto çevikliği gereksinimi
- **açıklama:** Algoritma değişiminde tek nokta kırılmasın.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-055 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-056 — Protokol dondurma yasağı
- **açıklama:** Sabit eski TLS iddiası yok.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-056 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-057 — Karma imza stratejisi notu
- **açıklama:** Klasik+PQC hibrit gelecek notu.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-057 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-058 — Sertifika şeffaflığı N/A
- **açıklama:** Kendi CT izleme yok.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-058 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-059 — Code signing hedefi
- **açıklama:** Release imza ASSESS (TC paylaşır).
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-059 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-060 — Commit imza hedefi
- **açıklama:** SSH/GPG commit imza org politikası ASSESS.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-060 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-061 — Provenance imza
- **açıklama:** Build attestasyon imza hedefi.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-061 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-062 — SBOM imza
- **açıklama:** SBOM bütünlüğü hedefi.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-062 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-063 — LLM API transport integrity
- **açıklama:** HTTPS base_url teyidi.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-063 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-064 — Webhook imza doğrulama N/A
- **açıklama:** Inbound webhook yok.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-064 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-065 — JWT doğrulama N/A
- **açıklama:** Ürün JWT yok.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-065 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-066 — OIDC token audience ASSESS
- **açıklama:** GHA OIDC kullanılırsa audience daralt.
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-066 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-067 — PATs düz metin yasağı
- **açıklama:** PAT dosyası git'te yok.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-067 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-068 — API anahtarı prefix tarama
- **açıklama:** secret_scan LLM prefix gap kapatma hedefi.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-068 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-069 — QR/secret backup yasağı
- **açıklama:** 2FA yedek kodları repo dışı.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-069 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-070 — Ekran görüntüsü secret yasağı
- **açıklama:** PR screenshot'ta token yok.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-070 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-071 — Notebook secret yasağı
- **açıklama:** ipynb'te key yok.
- **NIST_CSF:** ID.SC-02
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-071 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-072 — Doküman gizli ek yasağı
- **açıklama:** PDF ingest redakte damıtma.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-072 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-073 — Sıkıştırma bombası farkındalığı
- **açıklama:** Büyük arşiv git'e alınmaz.
- **NIST_CSF:** GV.RR-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-073 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-074 — Homomorfik/kullanılmayan kripto yok
- **açıklama:** Pazarlama kripto iddiası yok.
- **NIST_CSF:** ID.RA-05
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-074 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-075 — Özel protokol yasağı
- **açıklama:** Kendi TLS'i yazma yasağı.
- **NIST_CSF:** ID.AM-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-075 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-076 — Rolling crypto DIY yasağı
- **açıklama:** Özel cipher yok.
- **NIST_CSF:** ID.RA-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-076 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-077 — Sabit IV/nonce tarama hedefi
- **açıklama:** Varsa tespit; PoC yok.
- **NIST_CSF:** GV.PO-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-077 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-078 — Padding oracle sınıfı farkındalık
- **açıklama:** Kendi CBC yok; N/A+eğitim.
- **NIST_CSF:** PR.AA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-078 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-079 — Yan kanal N/A
- **açıklama:** Donanım yok.
- **NIST_CSF:** PR.DS-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-079 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-080 — TRNG/HSM N/A
- **açıklama:** Donanım RNG yok.
- **NIST_CSF:** PR.IR-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-080 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-081 — Anahtar seremonisi N/A
- **açıklama:** Çok partili key yok.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-081 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-082 — Escrow politikası
- **açıklama:** İş sürekliliği için secret sahip yedek (insan).
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-082 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-083 — Kripto envanter yenileme
- **açıklama:** encryption-engine inventory stub.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-083 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-084 — Algoritma yaşlandırma listesi
- **açıklama:** Deprecated algo isimleri (savunma).
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-084 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-085 — FIPS modu iddiası yok
- **açıklama:** FIPS-validated iddia edilmez.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-085 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-086 — Common Criteria iddiası yok
- **açıklama:** CC sertifika yok.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-086 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-087 — Müşteri getirdi anahtar N/A
- **açıklama:** BYOK yok.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-087 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-088 — Çok bulut KEK N/A
- **açıklama:** Çoklu KMS yok.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-088 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-089 — Secret scanning exception kaydı
- **açıklama:** False-positive allowlist dar ve gerekçeli.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-089 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-090 — Vault placeholder standardı
- **açıklama:** vault:// op:// ${VAR} <REDACTED>.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-090 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-091 — Şifre politikası insan hesabı
- **açıklama:** Org GitHub parola/SSO ASSESS.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-091 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-092 — Passkey hedefi
- **açıklama:** Org passkey opsiyonu ASSESS.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-092 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-093 — Shared password yasağı
- **açıklama:** Paylaşılan admin şifresi yok.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-093 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-094 — Emergency break-glass kaydı
- **açıklama:** Acil erişim AUDIT'e yazılır.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-094 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-095 — Kriptografik teslimat şampiyonu
- **açıklama:** ORG crypto rol seed.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-095 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-096 — Eğitim: secret hygiene
- **açıklama:** skill secret-hygiene referansı.
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-096 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-097 — ENC kanıt yolu
- **açıklama:** Her kontrol doğrulama dosyası.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-097 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-098 — ENC istisna N/A listesi
- **açıklama:** Kapsam dışı şifreleme kontrolleri yazılı.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-098 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-099 — ENC peer review
- **açıklama:** Kripto iddiaları abartılmaz.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-099 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### ENC-100 — ENC review döngüsü 021–100
- **açıklama:** TASKS kapanış.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı ENC-100 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

