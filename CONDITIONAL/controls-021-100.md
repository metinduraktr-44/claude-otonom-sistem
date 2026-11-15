# Conditional Controls 021–100

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok


**MODE:** ASSESS-ONLY · **ts:** 2026-11-03T11:47:59Z · **count:** 80/100 (kümülatif 100/100 bu motor tranche hedefi 001–100)

Kolonlar: id, ad, açıklama, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi

### COND-021 — MODE=ASSESS-ONLY koşulu
- **açıklama:** STATE MODE satırı üretim davranışını kilitler.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-021 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-022 — CANVA:ON kapalı koşulu
- **açıklama:** Tasarım üretimi tetiklenmez.
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-022 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-023 — Secret yoksa dry-run
- **açıklama:** LLM client anahtarsız SKIP.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-023 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-024 — Ethics fail koşulu
- **açıklama:** CI/hook fail-closed.
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-024 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-025 — Secret scan fail koşulu
- **açıklama:** Merge engeli kültürü.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-025 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-026 — validate.py fail koşulu
- **açıklama:** Structural/semantic KALDI durur.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-026 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-027 — Fork PR koşulu
- **açıklama:** Secret'lar fork'a akmaz.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-027 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-028 — branch=main koruma koşulu
- **açıklama:** Doğrudan yazma yok.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-028 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-029 — paths: SECURITY_* koşulu
- **açıklama:** Security PR ekstra checklist.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-029 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-030 — paths: .github/workflows koşulu
- **açıklama:** Pin gap notu zorunlu ASSESS.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-030 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-031 — Actor allowlist koşulu
- **açıklama:** Bot vs insan ayrımı ASSESS.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-031 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-032 — Schedule vs workflow_dispatch
- **açıklama:** Manuel tetik yetkisi dar.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-032 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-033 — Environment yok koşulu
- **açıklama:** Korumasız prod iddiası yok.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-033 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-034 — Risk skoru kaba eşik
- **açıklama:** assessment_id ile izlenir.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-034 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-035 — P0 secret sızıntı koşulu
- **açıklama:** IR yolu; değer yayınlanmaz.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-035 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-036 — Untrusted ingest koşulu
- **açıklama:** DOCX/PDF → damıtma, ham yok.
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-036 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-037 — Viral token vaadi koşulu
- **açıklama:** RED; resmi URL listesi.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-037 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-038 — Sahte eklenti koşulu
- **açıklama:** Marketplace iddiası kanıt ister.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-038 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-039 — 900M prompt koşulu
- **açıklama:** K-017 RED.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-039 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-040 — Expert bio uydurma koşulu
- **açıklama:** Kaynak yoksa yazma.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-040 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-041 — Exploit talep koşulu
- **açıklama:** ethics escalate; üretim yok.
- **NIST_CSF:** ID.SC-02
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-041 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-042 — Kimlik avı kiti talep koşulu
- **açıklama:** reddet / yasak (savunma tarama kuralı).
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-042 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-043 — C2/malware dil koşulu
- **açıklama:** Offensive kelime fail (istisna: yasak listesi).
- **NIST_CSF:** GV.RR-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-043 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-044 — Kabuğa yönlendirmeli indirme tarif koşulu
- **açıklama:** Yasak; tespit (örnek komut yok).
- **NIST_CSF:** ID.RA-05
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-044 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-045 — rm -rf / koşulu
- **açıklama:** Yasak desen.
- **NIST_CSF:** ID.AM-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-045 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-046 — eval( koşulu
- **açıklama:** validate forbidden.
- **NIST_CSF:** ID.RA-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-046 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-047 — base64|sh koşulu
- **açıklama:** Yasak desen.
- **NIST_CSF:** GV.PO-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-047 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-048 — Yetki yükseltme saldırı tarifi koşulu
- **açıklama:** Yasak / reddet; yalnızca sertleştirme metni.
- **NIST_CSF:** PR.AA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-048 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-049 — Kimlik doldurma betiği talep koşulu
- **açıklama:** Yasak / reddet.
- **NIST_CSF:** PR.DS-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-049 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-050 — Kimlik doğrulama atlama yükü talep koşulu
- **açıklama:** Yasak / reddet.
- **NIST_CSF:** PR.IR-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-050 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-051 — Rate-limit aşım koşulu
- **açıklama:** LLM client backoff.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-051 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-052 — Quota yoksa skip
- **açıklama:** API 429 → dur, deneme yağmuru yok.
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-052 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-053 — Nightly pencere koşulu
- **açıklama:** cron çakışması ASSESS.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-053 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-054 — Disk/büyük dosya koşulu
- **açıklama:** Ham PDF git reddi.
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-054 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-055 — LFS beklenmedik koşulu
- **açıklama:** ASSESS.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-055 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-056 — Submodule ekleme koşulu
- **açıklama:** İnsan onayı.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-056 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-057 — Force push koşulu
- **açıklama:** Yasak main.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-057 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-058 — Skip-ci koşulu
- **açıklama:** Güvenlik PR'da geçersiz.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-058 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-059 — Dependabot minor vs major
- **açıklama:** Major insan kapısı.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-059 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-060 — Action tag vs SHA koşulu
- **açıklama:** Tag ise gap kaydı.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-060 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-061 — permissions: write koşulu
- **açıklama:** Gerekçe yoksa reddet hedefi.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-061 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-062 — id-token: write koşulu
- **açıklama:** OIDC gerekçesi.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-062 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-063 — pull_request_target koşulu
- **açıklama:** Kaçınma / ekstra review.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-063 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-064 — Self-hosted runner koşulu
- **açıklama:** Yok; eklenirse yüksek risk.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-064 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-065 — Privileged k8s koşulu
- **açıklama:** ASSESS gap.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-065 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-066 — Public secret koşulu
- **açıklama:** GitHub secret scanning uyarısı süreci.
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-066 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-067 — Chat'e yapıştırılan key koşulu
- **açıklama:** Rotate talimatı; değeri tekrar yazma.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-067 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-068 — MCP enable koşulu
- **açıklama:** example default OFF.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-068 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-069 — Canva OAuth koşulu
- **açıklama:** Yalnızca kullanıcı CANVA:ON.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-069 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-070 — Agency merge koşulu
- **açıklama:** Additive; kullanıcı merge demeden birleştirme.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-070 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-071 — LATOS restore koşulu
- **açıklama:** git rol-kartlari insan onayı.
- **NIST_CSF:** ID.SC-02
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-071 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-072 — Parallel agent silme koşulu
- **açıklama:** Yabancı track destroy yok.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-072 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-073 — PR #34 açık bırakma
- **açıklama:** Ingest PR merge edilmez (DEVAM≠merge).
- **NIST_CSF:** GV.RR-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-073 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-074 — GHA pin uygulama koşulu
- **açıklama:** ASSESS-ONLY: raporla, workflow'u bu turda değiştirme.
- **NIST_CSF:** ID.RA-05
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-074 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-075 — Compliance pack yok koşulu
- **açıklama:** Faz 5 bekler; sahte sertifika iddiası yok.
- **NIST_CSF:** ID.AM-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-075 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-076 — IR playbook yok koşulu
- **açıklama:** Faz 6; yine de P0 yolu yazılı.
- **NIST_CSF:** ID.RA-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-076 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-077 — Skill 20k eksik koşulu
- **açıklama:** Kısmi derinlik dürüst beyan.
- **NIST_CSF:** GV.PO-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-077 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-078 — Kontrol 600 eksik koşulu
- **açıklama:** İlerleme sayacı; tamamlandı iddiası yok.
- **NIST_CSF:** PR.AA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-078 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-079 — N/A kapsam koşulu
- **açıklama:** Yüzey yoksa N/A; uydurma kontrol yok.
- **NIST_CSF:** PR.DS-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-079 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-080 — Waivers süre koşulu
- **açıklama:** İstisna sonsuz değil.
- **NIST_CSF:** PR.IR-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-080 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-081 — UTC damga koşulu
- **açıklama:** Her faz başı/sonu.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-081 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-082 — AUDIT satırı koşulu
- **açıklama:** ts_start/ts_end zorunlu.
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-082 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-083 — BILGI_TABANI satırı koşulu
- **açıklama:** Öğrenim 1 satır+.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-083 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-084 — STATE güncelleme koşulu
- **açıklama:** Faz/sayaç senkron.
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-084 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-085 — Matrix CSV=katalog koşulu
- **açıklama:** Satır sayıları eşit.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-085 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-086 — Türkçe teslim koşulu
- **açıklama:** Kullanıcı dilinde özet.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-086 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-087 — Kanıt path koşulu
- **açıklama:** Doğrulama yöntemi dosya gösterir.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-087 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-088 — Resmi URL koşulu
- **açıklama:** docs.anthropic.com / modelcontextprotocol.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-088 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-089 — Star count şişirme koşulu
- **açıklama:** Sosyal kanıt iddiası reddi.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-089 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-090 — Bedava 1,6B token koşulu
- **açıklama:** SAHTE işaret.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-090 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-091 — OmniRoute iddia koşulu
- **açıklama:** RESEARCH notu; kurulum yok.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-091 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-092 — İç müşteri verisi koşulu
- **açıklama:** Pilot PII yok.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-092 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-093 — Medikal claim koşulu
- **açıklama:** Movéa tonu ayrı; kanıtsız tedavi yok (agency).
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-093 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-094 — Rakip adı koşulu
- **açıklama:** Brief'te rakip yok.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-094 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-095 — Süperlatif koşulu
- **açıklama:** Kanıtsız en iyi yok.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-095 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-096 — Marka TBD koşulu
- **açıklama:** AdOps CRE default ürün yolu.
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-096 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-097 — BRIEF-ONLY teslim koşulu
- **açıklama:** Görsel üretim yok.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-097 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-098 — critic-copy henüz PASS değil
- **açıklama:** Hafif QA; sahte PASS yok.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-098 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-099 — COND kanıt CSV
- **açıklama:** matrix-021-100.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-099 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### COND-100 — COND review döngüsü 021–100
- **açıklama:** TASKS kapanış.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı COND-100 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

