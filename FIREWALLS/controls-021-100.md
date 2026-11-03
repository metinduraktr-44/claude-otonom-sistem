# Firewalls Controls 021–100

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok


**MODE:** ASSESS-ONLY · **ts:** 2026-11-03T11:47:59Z · **count:** 80/100 (kümülatif 100/100 bu motor tranche hedefi 001–100)

Kolonlar: id, ad, açıklama, NIST_CSF, 800-53, ISO27001, CIS, OWASP, doğrulama_yöntemi, savunma_gerekçesi

### FW-021 — Egress host envanteri yenileme
- **açıklama:** Outbound host listesi LLM/API/docs için güncellenir.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-021 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-022 — Egress varsayılan deny hedefi
- **açıklama:** Runner ağında allowlist hedef mimarisi (uygulanmadı, ASSESS).
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-022 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-023 — DNS çözümleme sınırı ASSESS
- **açıklama:** Bağımlılık domain'leri allowlist taslağı.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-023 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-024 — DoH/özel DNS N/A
- **açıklama:** Kurumsal DNS yoksa N/A beyanı.
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-024 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-025 — Webhook inbound yok teyidi
- **açıklama:** Uygulama webhook dinleyicisi inventory ile yok.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-025 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-026 — GitHub webhook secret hijyeni
- **açıklama:** Varsa secret GitHub'da; sohbette yok.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-026 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-027 — IPv6/IPv4 kapsam notu
- **açıklama:** Ağ politikası dual-stack farkındalığı.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-027 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-028 — Proxy/orta kutu yasağı
- **açıklama:** Geliştirme MITM sertifikası yok beyanı.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-028 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-029 — CORS N/A beyanı
- **açıklama:** Tarayıcı app yoksa CORS kontrolü N/A.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-029 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-030 — WAF N/A beyanı
- **açıklama:** Kenar WAF yok; kapsam doküman deposu.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-030 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-031 — SSH inbound yok
- **açıklama:** Sunucu SSH yüzeyi inventory N/A.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-031 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-032 — RDP/WinRM yok
- **açıklama:** Windows yönetim yüzeyi N/A.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-032 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-033 — Veritabanı portu yok
- **açıklama:** Postgres/MySQL listen yok beyanı.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-033 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-034 — Redis/cache portu yok
- **açıklama:** Açık cache yüzeyi N/A.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-034 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-035 — Admin panel yok
- **açıklama:** Web admin UI inventory N/A.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-035 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-036 — Debug port yasağı tarama
- **açıklama:** listen/bind desenleri ASSESS (saldırı değil, tespit).
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-036 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-037 — Localhost-only varsayım yok
- **açıklama:** Dokümanda 'sadece local' iddiası kanıt ister.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-037 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-038 — Container publish port ASSESS
- **açıklama:** K8s workflow portları gözden geçirme.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-038 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-039 — Load balancer N/A
- **açıklama:** LB yok beyanı.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-039 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-040 — CDN kenar N/A
- **açıklama:** Ürün CDN'i yok; docs GitHub Pages değil.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-040 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-041 — Git remote allowlist
- **açıklama:** origin = holding kanonik remote.
- **NIST_CSF:** ID.SC-02
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-041 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-042 — Fork network izolasyonu
- **açıklama:** pull_request vs pull_request_target ASSESS.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-042 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-043 — Dependabot ağ kapsamı
- **açıklama:** Dependabot PR'ları secret'sız koşar.
- **NIST_CSF:** GV.RR-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-043 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-044 — Marketplace action kaynağı
- **açıklama:** actions/* ve güvenilen org önceliği.
- **NIST_CSF:** ID.RA-05
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-044 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-045 — Third-party action egress
- **açıklama:** Bilinmeyen action'ın outbound'u risk notu.
- **NIST_CSF:** ID.AM-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-045 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-046 — npm registry N/A/sınır
- **açıklama:** Katalog örnekleri izole; root npm yok.
- **NIST_CSF:** ID.RA-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-046 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-047 — PyPI indirme CI sınırı
- **açıklama:** CI'da pip yoksa N/A; varsa pin ASSESS.
- **NIST_CSF:** GV.PO-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-047 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-048 — Container registry N/A
- **açıklama:** Image push yok beyanı.
- **NIST_CSF:** PR.AA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-048 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-049 — Paket proxy yoksa pin
- **açıklama:** Tag @vN = pin gap (bkz. ASSESSMENTS).
- **NIST_CSF:** PR.DS-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-049 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-050 — TLS kesme yasağı
- **açıklama:** Kurumsal TLS intercept yok beyanı.
- **NIST_CSF:** PR.IR-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-050 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-051 — Email gateway N/A
- **açıklama:** MX/SMTP ürün yüzeyi yok.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-051 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-052 — SMS/voice gateway N/A
- **açıklama:** Twilio prod yok beyanı (docs MCP ayrı).
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-052 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-053 — Slack inbound webhook N/A
- **açıklama:** Chatops webhook yok.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-053 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-054 — MCP network enable kapısı
- **açıklama:** MCP açmadan önce host allowlist.
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-054 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-055 — Browser extension N/A
- **açıklama:** Kurumsal eklenti yüzeyi yok.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-055 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-056 — Mobile MDM N/A
- **açıklama:** Cihaz filosu bu repo kapsamında değil.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-056 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-057 — VPN konsantrator N/A
- **açıklama:** Kurumsal VPN bu track'te yok.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-057 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-058 — Office firewall N/A
- **açıklama:** Fiziksel ofis FW envanter dışı.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-058 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-059 — Cloud SG/NACL ASSESS
- **açıklama:** Terraform ağ kaynakları varsa review.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-059 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-060 — Public bucket yasağı
- **açıklama:** Nesne deposu public ACL yok hedefi.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-060 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-061 — OTel exporter hedef kontrolü
- **açıklama:** collector.yaml endpoint allowlist.
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-061 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-062 — Log shipping hedefi
- **açıklama:** Dış SIEM yoksa local REPORTS.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-062 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-063 — Time-sync bağımlılığı
- **açıklama:** Zaman damgası UTC; NTP N/A (GitHub runner).
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-063 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-064 — NTP amplifikasyon N/A
- **açıklama:** Kendi NTP sunucusu yok.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-064 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-065 — Rate limit outbound
- **açıklama:** LLM client retry/backoff ASSESS.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-065 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-066 — DoS sınıfı farkındalık
- **açıklama:** Schedule cron yığılması gözden geçirme.
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-066 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-067 — Nightly pencere çakışması
- **açıklama:** Çoklu workflow aynı anda token kapsamı.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-067 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-068 — Git LFS/büyük dosya sınırı
- **açıklama:** Ham 298 sayfa PDF git'e alınmaz.
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-068 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-069 — Harici kısa URL yasağı
- **açıklama:** Bit.ly vb. doküman kaynağı olamaz.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-069 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-070 — Untrusted binary indirme yasağı
- **açıklama:** Uzaktan betiği kabuğa yönlendirme yasak (tespit kuralı; örnek komut yok).
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-070 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-071 — Shell pipe deny listesi
- **açıklama:** ethics_check curl_pipe_bash kuralı.
- **NIST_CSF:** ID.SC-02
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-071 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-072 — sudo/root runner yasağı
- **açıklama:** GHA root alışkanlığı ASSESS.
- **NIST_CSF:** PR.DS-02
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-072 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-073 — Docker socket mount yasağı
- **açıklama:** Dind yok beyanı.
- **NIST_CSF:** GV.RR-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-073 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-074 — Privileged container yasağı
- **açıklama:** K8s privileged ASSESS (workflow).
- **NIST_CSF:** ID.RA-05
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-074 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-075 — HostNetwork yasağı
- **açıklama:** Pod hostNetwork ASSESS.
- **NIST_CSF:** ID.AM-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-075 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-076 — NodePort public yasağı
- **açıklama:** K8s NodePort ASSESS.
- **NIST_CSF:** ID.RA-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-076 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-077 — Ingress default deny
- **açıklama:** Ingress kaynağı varsa review.
- **NIST_CSF:** GV.PO-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-077 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-078 — NetworkPolicy hedefi
- **açıklama:** K8s NetPol yoksa gap notu.
- **NIST_CSF:** PR.AA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-078 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-079 — Service mesh N/A
- **açıklama:** Istio yok beyanı.
- **NIST_CSF:** PR.DS-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-079 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-080 — East-west görünürlük N/A
- **açıklama:** Mikroservis yok.
- **NIST_CSF:** PR.IR-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-080 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-081 — ICMP/management N/A
- **açıklama:** Sunucu yok.
- **NIST_CSF:** PR.PS-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-081 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-082 — BGP/peering N/A
- **açıklama:** Ağ operasyonu yok.
- **NIST_CSF:** DE.CM-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-082 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-083 — DDoS üretici hizmet N/A
- **açıklama:** Kenar koruma yok; kapsam doküman.
- **NIST_CSF:** RS.MA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-083 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-084 — Geo-IP blok N/A
- **açıklama:** Uygulama kenarı yok.
- **NIST_CSF:** RC.RP-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-084 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-085 — Bot yönetimi N/A
- **açıklama:** WAF/bot yok.
- **NIST_CSF:** GV.OV-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-085 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-086 — API gateway N/A
- **açıklama:** Ürün API yok.
- **NIST_CSF:** ID.SC-02
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-086 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-087 — GraphQL yüzey N/A
- **açıklama:** API yok.
- **NIST_CSF:** PR.DS-02
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-087 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-088 — WebSocket yüzey N/A
- **açıklama:** Canlı soket yok.
- **NIST_CSF:** GV.RR-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-088 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-089 — mTLS servis N/A
- **açıklama:** Servis mTLS yok; TLS outbound var.
- **NIST_CSF:** ID.RA-05
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-089 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-090 — Sertifika pin istemci ASSESS
- **açıklama:** Python requests verify varsayılanı.
- **NIST_CSF:** ID.AM-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-090 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-091 — Insecure skip verify taraması
- **açıklama:** rg verify=False scripts (tespit).
- **NIST_CSF:** ID.RA-01
- **800-53:** AC-3 SI-4
- **ISO27001:** A.5.9 A.8.9
- **CIS:** CIS-3
- **OWASP:** A02
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-091 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-092 — Karışık içerik N/A
- **açıklama:** Web app yok.
- **NIST_CSF:** GV.PO-01
- **800-53:** SC-7 SA-12
- **ISO27001:** A.5.15 A.8.12
- **CIS:** CIS-4
- **OWASP:** A04
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-092 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-093 — Deep link/intent N/A
- **açıklama:** Mobil yok.
- **NIST_CSF:** PR.AA-01
- **800-53:** SC-28 IR-4
- **ISO27001:** A.5.21 A.8.20
- **CIS:** CIS-5
- **OWASP:** A07
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-093 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-094 — Air-gap hedefi yok
- **açıklama:** Repo GitHub bağlı; air-gap iddiası yok.
- **NIST_CSF:** PR.DS-01
- **800-53:** SI-4 CA-2
- **ISO27001:** A.8.9 A.8.24
- **CIS:** CIS-6
- **OWASP:** A08
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-094 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-095 — Split-horizon DNS N/A
- **açıklama:** Kurumsal DNS yok.
- **NIST_CSF:** PR.IR-01
- **800-53:** SA-12 PL-2
- **ISO27001:** A.8.12 A.8.32
- **CIS:** CIS-8
- **OWASP:** A09
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-095 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-096 — Guest Wi-Fi N/A
- **açıklama:** Fiziksel kapsam dışı.
- **NIST_CSF:** PR.PS-01
- **800-53:** IR-4 AU-9
- **ISO27001:** A.8.20 A.5.24
- **CIS:** CIS-12
- **OWASP:** A10
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-096 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-097 — Printer/IoT N/A
- **açıklama:** Kapsam dışı.
- **NIST_CSF:** DE.CM-01
- **800-53:** CA-2 CM-8
- **ISO27001:** A.8.24 A.5.1
- **CIS:** CIS-14
- **OWASP:** ASVS-V1
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-097 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-098 — Lab ağ ayrımı
- **açıklama:** ASSESS-ONLY lab ile prod karışmaz (prod=git).
- **NIST_CSF:** RS.MA-01
- **800-53:** PL-2 AC-3
- **ISO27001:** A.8.32 A.5.9
- **CIS:** CIS-15
- **OWASP:** ASVS-V2
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-098 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-099 — Firewall kural review ritmi
- **açıklama:** FW-021–100 TASKS döngüsüne bağlı.
- **NIST_CSF:** RC.RP-01
- **800-53:** AU-9 SC-7
- **ISO27001:** A.5.24 A.5.15
- **CIS:** CIS-16
- **OWASP:** Policy
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-099 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

### FW-100 — FW tranche kapanış kontrolü
- **açıklama:** Bu batch CSV satır sayısı 80.
- **NIST_CSF:** GV.OV-01
- **800-53:** CM-8 SC-28
- **ISO27001:** A.5.1 A.5.21
- **CIS:** CIS-1
- **OWASP:** A01
- **doğrulama_yöntemi:** ASSESS: katalog satırı FW-100 + ilgili path/rg; değer yok
- **savunma_gerekçesi:** Savunma yüzeyi daraltma / tespit / uyum kanıtı; saldırı tarifi yok

