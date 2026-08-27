# Layers Controls 001–020

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok


**MODE:** ASSESS-ONLY · **ts:** 2026-08-27T12:54:55Z · **count:** 20/100

Kolonlar: id, ad, açıklama, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi

### LAY-001 — Defense-in-depth envanteri
- **açıklama:** Holding varlık ve katman envanteri güncel tutulur (inventory + attack-surface).
- **NIST_CSF:** ID.AM-01 GV.OC
- **800-53:** CM-8 PM-5
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-1
- **OWASP:** ASVS-5 architecture
- **doğrulama_yöntemi:** SECURITY_CONTEXT/inventory.md varlığı ve last_updated kontrolü
- **savunma_gerekçesi:** Kontrolsüz yüzey = kör nokta; envanter tüm katmanların temeli

### LAY-002 — Trust boundary dokümantasyonu
- **açıklama:** CI, içerik, LLM outbound, infra trust sınırları yazılıdır.
- **NIST_CSF:** ID.AM-03
- **800-53:** CA-3
- **ISO27001:** A.5.14
- **CIS:** CIS-12
- **OWASP:** ASVS-5 L1 trust
- **doğrulama_yöntemi:** attack-surface.md trust sınıfları gözden geçirme
- **savunma_gerekçesi:** Sınır yoksa least-privilege ve egress politikası uygulanamaz

### LAY-003 — MODE ASSESS-ONLY varsayılan
- **açıklama:** Security OS varsayılanı agresif değişiklik değil gap/doküman üretimidir.
- **NIST_CSF:** GV.PO-01
- **800-53:** PL-1
- **ISO27001:** A.5.1
- **CIS:** CIS-4
- **OWASP:** Policy
- **doğrulama_yöntemi:** STATE.md MODE satırı teyidi
- **savunma_gerekçesi:** Yanlışlıkla saldırgan/değiştirici otomasyon riskini keser

### LAY-004 — Guardrail banner zorunluluğu
- **açıklama:** Security artefaktlarında GUARDRAIL satırı bulunur.
- **NIST_CSF:** GV.PO-02
- **800-53:** PL-2
- **ISO27001:** A.5.1
- **CIS:** CIS-14
- **OWASP:** Policy
- **doğrulama_yöntemi:** rg GUARDRAIL SECURITY_* LAYERS ORG
- **savunma_gerekçesi:** Savunma-only kültürünü dosya düzeyinde hatırlatır

### LAY-005 — Secret olmayan log katmanı
- **açıklama:** AUDIT/REPORTS katmanına secret değeri yazılmaz.
- **NIST_CSF:** PR.DS-01 DE.CM
- **800-53:** AU-9 SI-12
- **ISO27001:** A.8.15 A.8.12
- **CIS:** CIS-3 CIS-8
- **OWASP:** A02/A09
- **doğrulama_yöntemi:** secret_scan.py REPORTS AUDIT_LOG
- **savunma_gerekçesi:** Bilgi ifşası katmanını kapatır

### LAY-006 — Kimlik katmanı — token scope
- **açıklama:** GITHUB_TOKEN ve benzeri kimlikler en az yetki ile sınırlıdır.
- **NIST_CSF:** PR.AA-01
- **800-53:** AC-3 AC-6
- **ISO27001:** A.5.15 A.8.2
- **CIS:** CIS-5 CIS-6
- **OWASP:** A07
- **doğrulama_yöntemi:** Workflow permissions: blokları inceleme
- **savunma_gerekçesi:** EoP ve lateral movement yüzeyini daraltır

### LAY-007 — Egress bilinçli katman
- **açıklama:** Outbound API çağrıları bilinen host’lara yönlenir (allowlist ASSESS).
- **NIST_CSF:** PR.IR-01
- **800-53:** SC-7
- **ISO27001:** A.8.20
- **CIS:** CIS-12
- **OWASP:** A10 SSRF sınıfı
- **doğrulama_yöntemi:** LLM client base URL envanteri
- **savunma_gerekçesi:** Veri sızıntısı ve SSRF sınıfı riski azaltır

### LAY-008 — CI workload sertleştirme katmanı
- **açıklama:** Workflow’lar pin + permissions + mask ile sertleştirilir.
- **NIST_CSF:** PR.PS-01
- **800-53:** CM-6 SA-12
- **ISO27001:** A.8.9 A.5.21
- **CIS:** CIS-4 CIS-16
- **OWASP:** A08
- **doğrulama_yöntemi:** supply-chain.md checklist
- **savunma_gerekçesi:** CI en ayrıcalıklı süreç; katmanlı kontrol şart

### LAY-009 — Uygulama/script doğrulama katmanı
- **açıklama:** Generator çıktıları validate + ethics_check’ten geçer.
- **NIST_CSF:** PR.DS-02
- **800-53:** SI-10
- **ISO27001:** A.8.28
- **CIS:** CIS-16
- **OWASP:** ASVS input
- **doğrulama_yöntemi:** validate.py + ethics_check çalıştır
- **savunma_gerekçesi:** Bozuk/zararlı içerik yayılımını keser

### LAY-010 — Veri sınıflandırma katmanı
- **açıklama:** Secret / internal / public etiketleri dokümante.
- **NIST_CSF:** ID.AM-05
- **800-53:** RA-2
- **ISO27001:** A.5.12
- **CIS:** CIS-3
- **OWASP:** ASVS data
- **doğrulama_yöntemi:** SECRETS-DRYRUN-MATRISI + inventory
- **savunma_gerekçesi:** Yanlış koruma seviyesini önler

### LAY-011 — Defense detection katmanı
- **açıklama:** Hooks secret/ethics taramayı failClosed uygular.
- **NIST_CSF:** DE.CM-01
- **800-53:** SI-4
- **ISO27001:** A.8.16
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** hooks config + scanner exit code
- **savunma_gerekçesi:** Erken tespit sonraki katmanlara yük bindirmez

### LAY-012 — Vendored katalog izolasyon katmanı
- **açıklama:** katalog/ runtime bağımlılık sayılmaz; install edilmez.
- **NIST_CSF:** ID.SC-02
- **800-53:** SA-12
- **ISO27001:** A.5.21
- **CIS:** CIS-15
- **OWASP:** Supply chain
- **doğrulama_yöntemi:** AGENTS.md stdlib-only + no npm katalog
- **savunma_gerekçesi:** Üçüncü parti şablon riskini çalışma zamanından ayırır

### LAY-013 — Observability güvenli katman
- **açıklama:** OTel/TF sensitive değişkenler örnek dışı commit edilmez.
- **NIST_CSF:** PR.DS-01
- **800-53:** SC-28
- **ISO27001:** A.8.11 A.8.24
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** tfvars gitignore ASSESS
- **savunma_gerekçesi:** Telemetri token sızıntısını önler

### LAY-014 — Değişiklik gözetim katmanı
- **açıklama:** Güvenlik dosyaları review/CHANGE protokolüne tabi.
- **NIST_CSF:** GV.PO ID.RA
- **800-53:** CM-3
- **ISO27001:** A.8.32
- **CIS:** CIS-4
- **OWASP:** ASVS change
- **doğrulama_yöntemi:** CODEOWNERS/PR ASSESS
- **savunma_gerekçesi:** Yetkisiz güvenlik politika değişimini engeller

### LAY-015 — Incident hazırlık katmanı
- **açıklama:** IR skill ve SecOps rolü tanımlı; playbook ASSESS stub.
- **NIST_CSF:** RS.MA-01
- **800-53:** IR-4
- **ISO27001:** A.5.24
- **CIS:** CIS-17
- **OWASP:** IR
- **doğrulama_yöntemi:** ORG/ROLES/SecOps-Lead.md varlığı
- **savunma_gerekçesi:** Tespit sonrası müdahale katmanı boş kalmaz

### LAY-016 — Compliance map katmanı
- **açıklama:** Kontroller CSF/800-53/ISO/CIS/OWASP ile eşlenir.
- **NIST_CSF:** GV.OC-03
- **800-53:** CA-2
- **ISO27001:** A.5.35
- **CIS:** CIS-4
- **OWASP:** ASVS-5
- **doğrulama_yöntemi:** SECURITY_MATRIX satırları
- **savunma_gerekçesi:** Denetim ve önceliklendirme için ortak dil

### LAY-017 — Expert/org katmanı
- **açıklama:** Roller ve uzman DIGEST savunma odaklı tutulur.
- **NIST_CSF:** GV.RR-01
- **800-53:** PM-2
- **ISO27001:** A.5.2
- **CIS:** CIS-14
- **OWASP:** Governance
- **doğrulama_yöntemi:** ORG/ROLES + EXPERTS DIGEST
- **savunma_gerekçesi:** Hesap verebilirlik ve yetkinlik sinyali

### LAY-018 — Research currency katmanı
- **açıklama:** Standart sürümleri SECURITY_RESEARCH ile izlenir.
- **NIST_CSF:** ID.RA-01
- **800-53:** RA-3
- **ISO27001:** A.5.7
- **CIS:** CIS-7
- **OWASP:** ASVS currency
- **doğrulama_yöntemi:** standards-currency.md damgası
- **savunma_gerekçesi:** Eski kontrol setiyle yanlış güvenceyi önler

### LAY-019 — MCP güvenlik katmanı
- **açıklama:** Security MCP varsayılan kapalı; Canva ayrı track.
- **NIST_CSF:** PR.AA-05
- **800-53:** AC-20
- **ISO27001:** A.5.23
- **CIS:** CIS-15
- **OWASP:** A07
- **doğrulama_yöntemi:** mcp.security.example.json varsayılan OFF
- **savunma_gerekçesi:** Token’lı MCP yüzeyini bilerek kapalı tutar

### LAY-020 — Arşiv/QA katmanı planı
- **açıklama:** QA ve ARCHIVE döngüsü planlı (Faz 8); şimdilik stub kabul.
- **NIST_CSF:** GV.OV-01
- **800-53:** CA-7
- **ISO27001:** A.5.35
- **CIS:** CIS-4
- **OWASP:** QA
- **doğrulama_yöntemi:** security-master-plan Faz 8 checkbox
- **savunma_gerekçesi:** Sürekli iyileştirme katmanı kaybolmaz
