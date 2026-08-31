# Firewalls Controls 001–020

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok


**MODE:** ASSESS-ONLY · **ts:** 2026-08-27T12:54:55Z · **count:** 20/100

Kolonlar: id, ad, açıklama, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi

### FW-001 — Egress allowlist politikası ASSESS
- **açıklama:** Outbound ağ hedefleri için allowlist taslağı.
- **NIST_CSF:** PR.IR-01
- **800-53:** SC-7
- **ISO27001:** A.8.20
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** LLM/API host listesi dokümanı
- **savunma_gerekçesi:** Sınırsız egress veri sızdırır

### FW-002 — Runner internet varsayılan reddi (hedef)
- **açıklama:** Mümkünse harden-runner ile gereksiz egress kesilir — ASSESS.
- **NIST_CSF:** PR.IR-02
- **800-53:** SC-7
- **ISO27001:** A.8.22
- **CIS:** CIS-12
- **OWASP:** Network
- **doğrulama_yöntemi:** Workflow egress ASSESS notu
- **savunma_gerekçesi:** CI runner’lar yüksek ayrıcalıklı

### FW-003 — Webhook/inbound yüzey yok teyidi
- **açıklama:** Holding’de app inbound listener yok; yeni ekleme gate.
- **NIST_CSF:** ID.AM-02
- **800-53:** CM-8
- **ISO27001:** A.8.9
- **CIS:** CIS-1
- **OWASP:** ASVS
- **doğrulama_yöntemi:** inventory: uygulama sunucusu yok
- **savunma_gerekçesi:** Attack surface büyütmeyi engeller

### FW-004 — DNS/dependency domain allowlist ASSESS
- **açıklama:** Paket/Action kaynak domainleri bilinen registry.
- **NIST_CSF:** ID.SC-03
- **800-53:** SA-12
- **ISO27001:** A.5.21
- **CIS:** CIS-15
- **OWASP:** A08
- **doğrulama_yöntemi:** Action market kaynakları listesi
- **savunma_gerekçesi:** Typosquat sınıfı riski azaltır

### FW-005 — Secret store ağ sınırı
- **açıklama:** Secrets yalnızca GHA secrets / vault; chat’e kopyalanmaz.
- **NIST_CSF:** PR.DS-01
- **800-53:** SC-7 SC-28
- **ISO27001:** A.8.5
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** SECRETS matrisi
- **savunma_gerekçesi:** Secret’ın yanlış kanaldan çıkışını keser

### FW-006 — Terraform provider endpoint bilinçli
- **açıklama:** Provider/API endpoint’leri dokümante; shadow endpoint yok.
- **NIST_CSF:** PR.IR-01
- **800-53:** SC-7
- **ISO27001:** A.5.23
- **CIS:** CIS-12
- **OWASP:** Cloud
- **doğrulama_yöntemi:** terraform providers ASSESS
- **savunma_gerekçesi:** Yanlış backend’e state/token gitmesini önler

### FW-007 — OTel exporter hedef kontrolü
- **açıklama:** Collector exporter endpoint allowlist.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-8
- **ISO27001:** A.8.20
- **CIS:** CIS-12
- **OWASP:** A09
- **doğrulama_yöntemi:** opentelemetry-collector.yaml gözden geçirme
- **savunma_gerekçesi:** Telemetry hijack/sızıntı riski

### FW-008 — PR fork network izolasyonu
- **açıklama:** Fork PR’larda secret’lı job’lar kısıtlı.
- **NIST_CSF:** PR.AA-05
- **800-53:** AC-3
- **ISO27001:** A.8.3
- **CIS:** CIS-6
- **OWASP:** A07
- **doğrulama_yöntemi:** workflow pull_request vs target ASSESS
- **savunma_gerekçesi:** Fork’tan secret exfil sınıfını keser

### FW-009 — Doküman içi URL allowlist kültürü
- **açıklama:** Research’te yalnızca güvenilir standart/vendor URL.
- **NIST_CSF:** GV.PO
- **800-53:** SI-3
- **ISO27001:** A.5.7
- **CIS:** CIS-14
- **OWASP:** Content
- **doğrulama_yöntemi:** SECURITY_RESEARCH kaynak listesi
- **savunma_gerekçesi:** Zararlı talimat enjeksiyonunu azaltır

### FW-010 — Shell dangerous pattern deny
- **açıklama:** Tehlikeli shell kalıplarını (curl-pipe-shell, rm-rf-root) ethics_check ile tespit edip engelle (yasak).
- **NIST_CSF:** PR.PS-02
- **800-53:** CM-7
- **ISO27001:** A.8.7
- **CIS:** CIS-4
- **OWASP:** Policy
- **doğrulama_yöntemi:** ethics_check.py block patterns
- **savunma_gerekçesi:** Tehlikeli otomasyon komutlarını keser

### FW-011 — MCP network varsayılan kapalı
- **açıklama:** Security MCP örneği aktif edilmeden bağlanmaz.
- **NIST_CSF:** PR.AA
- **800-53:** AC-20
- **ISO27001:** A.5.23
- **CIS:** CIS-15
- **OWASP:** A07
- **doğrulama_yöntemi:** example json kapalı
- **savunma_gerekçesi:** Ek token kanalı açılmaz

### FW-012 — Log outbound redaksiyon
- **açıklama:** Dışa giden hata raporlarında secret mask.
- **NIST_CSF:** PR.DS DE.CM
- **800-53:** AU-9
- **ISO27001:** A.8.12
- **CIS:** CIS-3 CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** holding_report dry-run
- **savunma_gerekçesi:** Log ile secret kaçışını önler

### FW-013 — Nightly job rate bilinci
- **açıklama:** Zamanlanmış işler kota/çakışma ASSESS.
- **NIST_CSF:** PR.IR
- **800-53:** CP-2
- **ISO27001:** A.5.29
- **CIS:** CIS-11
- **OWASP:** DoS sınıfı
- **doğrulama_yöntemi:** workflow schedule gözden geçirme
- **savunma_gerekçesi:** Kaynak tüketimi / kilit riski

### FW-014 — Git remote allowlist
- **açıklama:** Push yalnızca bilinen origin.
- **NIST_CSF:** PR.AA
- **800-53:** AC-3
- **ISO27001:** A.5.14
- **CIS:** CIS-6
- **OWASP:** A07
- **doğrulama_yöntemi:** git remote -v ASSESS
- **savunma_gerekçesi:** Yanlış remote’a kod/secret itmeyi önler

### FW-015 — Dependency proxy yoksa pin
- **açıklama:** Proxy yok → doğrudan pin/SBOM ile telafi.
- **NIST_CSF:** ID.SC
- **800-53:** SA-12
- **ISO27001:** A.5.21
- **CIS:** CIS-15
- **OWASP:** A08
- **doğrulama_yöntemi:** supply-chain.md
- **savunma_gerekçesi:** Tedarik bütünlüğü

### FW-016 — Browser/extension N/A beyanı
- **açıklama:** Holding runtime tarayıcıya bağlı değil; kapsam dışı işaretli.
- **NIST_CSF:** ID.AM
- **800-53:** CM-8
- **ISO27001:** A.5.9
- **CIS:** CIS-1
- **OWASP:** Scope
- **doğrulama_yöntemi:** inventory N/A
- **savunma_gerekçesi:** Yanlış kontrol yükünü önler

### FW-017 — Email gateway N/A beyanı
- **açıklama:** E-posta güvenlik kontrolü kapsam dışı (holding otomasyon).
- **NIST_CSF:** ID.AM
- **800-53:** CM-8
- **ISO27001:** A.5.9
- **CIS:** CIS-1
- **OWASP:** Scope
- **doğrulama_yöntemi:** inventory
- **savunma_gerekçesi:** Kapsam netliği

### FW-018 — Admin interface yok
- **açıklama:** Yönetim UI yok; CLI/CI tek yüzey.
- **NIST_CSF:** PR.AA
- **800-53:** AC-6
- **ISO27001:** A.8.2
- **CIS:** CIS-6
- **OWASP:** A07
- **doğrulama_yöntemi:** inventory
- **savunma_gerekçesi:** Ek admin yüzey açılmaz

### FW-019 — Temporary debug port yasağı
- **açıklama:** Debug listen/port dokümante edilmez ve eklenmez.
- **NIST_CSF:** PR.IR
- **800-53:** CM-7
- **ISO27001:** A.8.9
- **CIS:** CIS-4
- **OWASP:** ASVS
- **doğrulama_yöntemi:** kodda listen/bind araması ASSESS
- **savunma_gerekçesi:** Gizli dinleyici yüzeyi engeli

### FW-020 — Firewall kontrol review döngüsü
- **açıklama:** FW-001–020 üç aylık ASSESS review.
- **NIST_CSF:** GV.OV
- **800-53:** CA-2
- **ISO27001:** A.5.35
- **CIS:** CIS-4
- **OWASP:** QA
- **doğrulama_yöntemi:** TASKS/SECURITY_MASTER
- **savunma_gerekçesi:** Kontrol çürümesini önler
