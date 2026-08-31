# Conditional Controls 001–020

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok


**MODE:** ASSESS-ONLY · **ts:** 2026-08-27T12:54:55Z · **count:** 20/100

Kolonlar: id, ad, açıklama, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi

### COND-001 — Risk-based access koşulu
- **açıklama:** Yüksek risk değişiklikte ek onay.
- **NIST_CSF:** PR.AA-01
- **800-53:** AC-2 AC-3
- **ISO27001:** A.5.15
- **CIS:** CIS-6
- **OWASP:** A07
- **doğrulama_yöntemi:** PR label high-risk
- **savunma_gerekçesi:** ZTA: bağlam olmadan geniş yetki yok

### COND-002 — MODE koşulu
- **açıklama:** ASSESS-ONLY dışına çıkış açık karar + damga.
- **NIST_CSF:** GV.PO
- **800-53:** PL-1
- **ISO27001:** A.5.1
- **CIS:** CIS-4
- **OWASP:** Policy
- **doğrulama_yöntemi:** STATE.md
- **savunma_gerekçesi:** Yanlış modda tehlikeli otomasyon yok

### COND-003 — Secret varlığı koşulu
- **açıklama:** Key yoksa dry-run; gerçek çağrı engeli.
- **NIST_CSF:** PR.AA PR.DS
- **800-53:** IA-5
- **ISO27001:** A.8.5
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** client dry-run davranışı
- **savunma_gerekçesi:** Kazara ücretli/gizli çağrı yok

### COND-004 — Fork PR koşulu
- **açıklama:** Fork’tan secret’lı job çalışmaz.
- **NIST_CSF:** PR.AA
- **800-53:** AC-3
- **ISO27001:** A.8.3
- **CIS:** CIS-6
- **OWASP:** A07
- **doğrulama_yöntemi:** workflow if koşulları ASSESS
- **savunma_gerekçesi:** Koşullu erişim

### COND-005 — Branch koşulu
- **açıklama:** main’e doğrudan push yok.
- **NIST_CSF:** PR.PS
- **800-53:** CM-5
- **ISO27001:** A.8.4
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** branch protection
- **savunma_gerekçesi:** Yazım koşulu

### COND-006 — Zaman koşulu — nightly pencere
- **açıklama:** Zamanlanmış işler tanımlı UTC pencerede.
- **NIST_CSF:** PR.IR
- **800-53:** CP-2
- **ISO27001:** A.5.29
- **CIS:** CIS-11
- **OWASP:** Ops
- **doğrulama_yöntemi:** schedule crontab ASSESS
- **savunma_gerekçesi:** Anormal tetik tespiti

### COND-007 — Environment protection ASSESS
- **açıklama:** Prod-like secrets environment approval.
- **NIST_CSF:** PR.AA
- **800-53:** AC-3
- **ISO27001:** A.5.15
- **CIS:** CIS-6
- **OWASP:** A07
- **doğrulama_yöntemi:** GHA environments ASSESS
- **savunma_gerekçesi:** İnsan kapısı

### COND-008 — Path filter koşulu
- **açıklama:** Sadece ilgili path değişince kritik job.
- **NIST_CSF:** PR.PS
- **800-53:** CM-3
- **ISO27001:** A.8.32
- **CIS:** CIS-4
- **OWASP:** Ops
- **doğrulama_yöntemi:** paths filters
- **savunma_gerekçesi:** Gereksiz ayrıcalıklı koşu azaltır

### COND-009 — Actor allowlist koşulu
- **açıklama:** Belirli actor/team kritik workflow.
- **NIST_CSF:** PR.AA
- **800-53:** AC-2
- **ISO27001:** A.5.15
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** GITHUB_ACTOR koşulları ASSESS
- **savunma_gerekçesi:** Yetkisiz tetik

### COND-010 — Ethics fail koşulu
- **açıklama:** ethics_check fail → pipeline kır.
- **NIST_CSF:** GV.PO
- **800-53:** SI-10
- **ISO27001:** A.5.1
- **CIS:** CIS-14
- **OWASP:** Policy
- **doğrulama_yöntemi:** CI step
- **savunma_gerekçesi:** Savunma-only koşulu

### COND-011 — Secret scan fail koşulu
- **açıklama:** Bulgu → failClosed.
- **NIST_CSF:** PR.DS
- **800-53:** SI-10
- **ISO27001:** A.8.28
- **CIS:** CIS-16
- **OWASP:** A02
- **doğrulama_yöntemi:** hooks/CI
- **savunma_gerekçesi:** Secret sızıntı koşulu

### COND-012 — Risk skoru eşiği (kaba)
- **açıklama:** P0 açıkken yeni özellik merge kısıtı ASSESS.
- **NIST_CSF:** ID.RA GV.RM
- **800-53:** RA-3
- **ISO27001:** A.5.3
- **CIS:** CIS-4
- **OWASP:** Risk
- **doğrulama_yöntemi:** STATE assessment_id
- **savunma_gerekçesi:** Risk-based governance

### COND-013 — Compliance pack koşulu
- **açıklama:** İlgili kontrol map’siz merge uyarısı.
- **NIST_CSF:** GV.OC
- **800-53:** CA-2
- **ISO27001:** A.5.35
- **CIS:** CIS-4
- **OWASP:** Compliance
- **doğrulama_yöntemi:** matrix TBD satır sayısı
- **savunma_gerekçesi:** Kanıtsız kontrol engeli

### COND-014 — PQC migration koşulu
- **açıklama:** Kripto değişimi crypto-agility checklist ile.
- **NIST_CSF:** PR.DS
- **800-53:** SC-13
- **ISO27001:** A.8.24
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ENC checklist
- **savunma_gerekçesi:** Algo değişiminde regresyon engeli

### COND-015 — MCP enable koşulu
- **açıklama:** Security MCP yalnız gerekçe + secret vault ile.
- **NIST_CSF:** PR.AA
- **800-53:** AC-20
- **ISO27001:** A.5.23
- **CIS:** CIS-15
- **OWASP:** A07
- **doğrulama_yöntemi:** example default OFF
- **savunma_gerekçesi:** Koşullu üçüncü parti bağ

### COND-016 — Canva ayrımı koşulu
- **açıklama:** Canva MCP security track’te açılmaz.
- **NIST_CSF:** GV.OC
- **800-53:** CM-3
- **ISO27001:** A.5.1
- **CIS:** CIS-4
- **OWASP:** Process
- **doğrulama_yöntemi:** AGENTS.md
- **savunma_gerekçesi:** Track çakışması yok

### COND-017 — Rate limit koşulu
- **açıklama:** API client retry/rate ASSESS.
- **NIST_CSF:** PR.IR
- **800-53:** SC-5
- **ISO27001:** A.8.6
- **CIS:** CIS-11
- **OWASP:** DoS sınıfı
- **doğrulama_yöntemi:** client code ASSESS
- **savunma_gerekçesi:** Kötüye kullanım/DoS azaltır

### COND-018 — Data classification koşulu
- **açıklama:** Public olmayan içerik LLM’e gitmeden redakte.
- **NIST_CSF:** PR.DS
- **800-53:** SI-12
- **ISO27001:** A.8.12
- **CIS:** CIS-3
- **OWASP:** A02 LLM
- **doğrulama_yöntemi:** prompt hygiene
- **savunma_gerekçesi:** Prompt sızıntı engeli

### COND-019 — Emergency override kayıt koşulu
- **açıklama:** Override varsa AUDIT zorunlu.
- **NIST_CSF:** GV.PO RS.MI
- **800-53:** AU-2 IR-4
- **ISO27001:** A.5.24
- **CIS:** CIS-17
- **OWASP:** IR
- **doğrulama_yöntemi:** AUDIT_LOG
- **savunma_gerekçesi:** İstisnanın izi

### COND-020 — COND review döngüsü
- **açıklama:** COND-001–020 periyodik.
- **NIST_CSF:** GV.OV
- **800-53:** CA-2
- **ISO27001:** A.5.35
- **CIS:** CIS-4
- **OWASP:** QA
- **doğrulama_yöntemi:** TASKS
- **savunma_gerekçesi:** Koşullu politikalar güncel
