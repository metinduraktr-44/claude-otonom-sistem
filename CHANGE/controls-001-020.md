# Change Controls 001–020

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok


**MODE:** ASSESS-ONLY · **ts:** 2026-08-27T12:54:55Z · **count:** 20/100

Kolonlar: id, ad, açıklama, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi

### CHG-001 — Change advisory gate ASSESS
- **açıklama:** Güvenlik politikası değişikliği PR + gerekçe.
- **NIST_CSF:** GV.PO-01
- **800-53:** CM-3
- **ISO27001:** A.8.32
- **CIS:** CIS-4
- **OWASP:** ASVS change
- **doğrulama_yöntemi:** PR şablon / checklist
- **savunma_gerekçesi:** Yetkisiz politika kayması engeli

### CHG-002 — Branch protection ASSESS
- **açıklama:** main korumalı; force-push kapalı hedef.
- **NIST_CSF:** PR.PS-01
- **800-53:** CM-5
- **ISO27001:** A.8.4 A.8.32
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** gh branch protection ASSESS
- **savunma_gerekçesi:** Doğrudan main yazımını keser

### CHG-003 — CODEOWNERS güvenlik yolları
- **açıklama:** SECURITY_* ve .cursor/rules security sahipliği.
- **NIST_CSF:** GV.RR
- **800-53:** CM-5
- **ISO27001:** A.8.4
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** CODEOWNERS ASSESS
- **savunma_gerekçesi:** Gözden geçirmeden merge engeli

### CHG-004 — Kontrol üretim batch limiti
- **açıklama:** /kontrol-uret aşırı dump yok; fazlı.
- **NIST_CSF:** GV.OV
- **800-53:** CM-3
- **ISO27001:** A.5.1
- **CIS:** CIS-4
- **OWASP:** Process
- **doğrulama_yöntemi:** plan batch limiti
- **savunma_gerekçesi:** Kalite ve denetlenebilirlik

### CHG-005 — Agency/security branch ayrımı
- **açıklama:** Creative agency ayrı branch; additive merge.
- **NIST_CSF:** GV.OC
- **800-53:** CM-3
- **ISO27001:** A.5.1
- **CIS:** CIS-4
- **OWASP:** Process
- **doğrulama_yöntemi:** STATE.md notu
- **savunma_gerekçesi:** Çakışan GIGA track birleşiminde kayıp yok

### CHG-006 — Workflow değişikliği ek review
- **açıklama:** GHA yaml değişiklikleri güvenlik checklist.
- **NIST_CSF:** PR.PS
- **800-53:** CM-3 SA-12
- **ISO27001:** A.8.32 A.5.21
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** PR label/checklist
- **savunma_gerekçesi:** CI tedarik zinciri değişim kontrolü

### CHG-007 — Scanner kural değişikliği denetimi
- **açıklama:** secret_scan/ethics pattern PR ile.
- **NIST_CSF:** DE.CM
- **800-53:** SI-4 CM-3
- **ISO27001:** A.8.16
- **CIS:** CIS-8
- **OWASP:** Detection
- **doğrulama_yöntemi:** scripts PR
- **savunma_gerekçesi:** False-negative/positive yönetimi

### CHG-008 — Rollback planı ASSESS
- **açıklama:** Kötü kontrol/policy için geri alma yolu.
- **NIST_CSF:** RC.RP
- **800-53:** CM-3 CP-10
- **ISO27001:** A.5.29
- **CIS:** CIS-4
- **OWASP:** IR
- **doğrulama_yöntemi:** git revert prosedürü
- **savunma_gerekçesi:** Hatalı değişiklikte hızlı toparlanma

### CHG-009 — Semantic version / tag disiplini
- **açıklama:** Release tag mutability ASSESS; immutable hedef.
- **NIST_CSF:** PR.DS-06
- **800-53:** CM-3 SI-7
- **ISO27001:** A.8.9
- **CIS:** CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** immutable releases dokümanı
- **savunma_gerekçesi:** Tag repoint sınıfı risk

### CHG-010 — Doküman-only vs kod değişimi ayrımı
- **açıklama:** ASSESS-ONLY’de kod değişimi gerekçeli.
- **NIST_CSF:** GV.PO
- **800-53:** CM-4
- **ISO27001:** A.5.1
- **CIS:** CIS-4
- **OWASP:** Policy
- **doğrulama_yöntemi:** STATE MODE
- **savunma_gerekçesi:** Kapsam taşmasını önler

### CHG-011 — Secret içeren PR reddi
- **açıklama:** secret_scan fail → merge engeli.
- **NIST_CSF:** PR.DS
- **800-53:** SI-10
- **ISO27001:** A.8.28
- **CIS:** CIS-16
- **OWASP:** A02
- **doğrulama_yöntemi:** hooks failClosed
- **savunma_gerekçesi:** Secret commit’i durdurur

### CHG-012 — Ethics fail merge engeli
- **açıklama:** Offensive içerik pattern → fail.
- **NIST_CSF:** GV.PO
- **800-53:** SI-10
- **ISO27001:** A.5.1
- **CIS:** CIS-14
- **OWASP:** Policy
- **doğrulama_yöntemi:** ethics_check
- **savunma_gerekçesi:** Savunma-only bozulmasını önler

### CHG-013 — Upstream sync review
- **açıklama:** katalog upstream-sync diff review zorunlu.
- **NIST_CSF:** ID.SC
- **800-53:** SA-12 CM-3
- **ISO27001:** A.5.21
- **CIS:** CIS-15
- **OWASP:** A08
- **doğrulama_yöntemi:** upstream-sync.yml ASSESS
- **savunma_gerekçesi:** Vendored zararlı değişim yakalama

### CHG-014 — Infra terraform plan review
- **açıklama:** TF plan insan gözü; auto-apply yok varsayılan.
- **NIST_CSF:** PR.PS
- **800-53:** CM-3
- **ISO27001:** A.8.32
- **CIS:** CIS-4
- **OWASP:** Cloud
- **doğrulama_yöntemi:** workflow terraform ASSESS
- **savunma_gerekçesi:** Altyapı drift/sızıntı engeli

### CHG-015 — Skill depth değişim kaydı
- **açıklama:** Skill references güncellemesi AUDIT satırı.
- **NIST_CSF:** GV.OV
- **800-53:** CM-3
- **ISO27001:** A.8.32
- **CIS:** CIS-4
- **OWASP:** Process
- **doğrulama_yöntemi:** AUDIT_LOG
- **savunma_gerekçesi:** İzlenebilirlik

### CHG-016 — Expert list refresh aylık
- **açıklama:** top100 seed doğrulama TODO.
- **NIST_CSF:** GV.RR
- **800-53:** PM-2
- **ISO27001:** A.5.2
- **CIS:** CIS-14
- **OWASP:** Governance
- **doğrulama_yöntemi:** EXPERTS TODO
- **savunma_gerekçesi:** Eski/yanlış referans engeli

### CHG-017 — Standards currency refresh
- **açıklama:** standards-currency damga yenileme.
- **NIST_CSF:** ID.RA
- **800-53:** RA-3
- **ISO27001:** A.5.7
- **CIS:** CIS-7
- **OWASP:** Compliance
- **doğrulama_yöntemi:** SECURITY_RESEARCH
- **savunma_gerekçesi:** Map güncelliği

### CHG-018 — Emergency change yolu
- **açıklama:** Acil yama: kısa yoldan PR + sonradan ADR.
- **NIST_CSF:** RS.MI
- **800-53:** CM-3 IR-4
- **ISO27001:** A.5.24
- **CIS:** CIS-17
- **OWASP:** IR
- **doğrulama_yöntemi:** playbook stub
- **savunma_gerekçesi:** Krizde kontrolsüzlüğü sınırlar

### CHG-019 — Deprecation süreci
- **açıklama:** Eski kontrol/skill işaretle, silme yerine deprecate.
- **NIST_CSF:** GV.OC
- **800-53:** CM-3
- **ISO27001:** A.8.32
- **CIS:** CIS-4
- **OWASP:** Process
- **doğrulama_yöntemi:** TODO/Status alanı
- **savunma_gerekçesi:** Sessiz kontrol kaybı olmaz

### CHG-020 — CHG review döngüsü
- **açıklama:** CHG-001–020 periyodik.
- **NIST_CSF:** GV.OV
- **800-53:** CA-2
- **ISO27001:** A.5.35
- **CIS:** CIS-4
- **OWASP:** QA
- **doğrulama_yöntemi:** TASKS
- **savunma_gerekçesi:** Change protokolü canlı kalır
