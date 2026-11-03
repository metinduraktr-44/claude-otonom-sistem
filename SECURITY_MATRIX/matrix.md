# SECURITY_MATRIX — Crosswalk (tranche 001–100 × 6)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**MODE:** ASSESS-ONLY · **ts:** 2026-11-03T11:47:59Z · **rows:** 600 / 600 (001–100 × 6)

| ID | Ad | NIST_CSF | 800-53 | ISO27001 | CIS | OWASP | Doğrulama | Status |
|----|----|----------|--------|----------|-----|-------|-----------|--------|

| LAY-001 | Defense-in-depth envanteri | ID.AM-01 GV.OC | CM-8 PM-5 | A.5.9 A.8.9 | CIS-1 | ASVS-5 architecture | SECURITY_CONTEXT/inventory.md varlığı ve last_updated kontro | ASSESS |
| LAY-002 | Trust boundary dokümantasyonu | ID.AM-03 | CA-3 | A.5.14 | CIS-12 | ASVS-5 L1 trust | attack-surface.md trust sınıfları gözden geçirme | ASSESS |
| LAY-003 | MODE ASSESS-ONLY varsayılan | GV.PO-01 | PL-1 | A.5.1 | CIS-4 | Policy | STATE.md MODE satırı teyidi | ASSESS |
| LAY-004 | Guardrail banner zorunluluğu | GV.PO-02 | PL-2 | A.5.1 | CIS-14 | Policy | rg GUARDRAIL SECURITY_* LAYERS ORG | ASSESS |
| LAY-005 | Secret olmayan log katmanı | PR.DS-01 DE.CM | AU-9 SI-12 | A.8.15 A.8.12 | CIS-3 CIS-8 | A02/A09 | secret_scan.py REPORTS AUDIT_LOG | ASSESS |
| LAY-006 | Kimlik katmanı — token scope | PR.AA-01 | AC-3 AC-6 | A.5.15 A.8.2 | CIS-5 CIS-6 | A07 | Workflow permissions: blokları inceleme | ASSESS |
| LAY-007 | Egress bilinçli katman | PR.IR-01 | SC-7 | A.8.20 | CIS-12 | A10 SSRF sınıfı | LLM client base URL envanteri | ASSESS |
| LAY-008 | CI workload sertleştirme katmanı | PR.PS-01 | CM-6 SA-12 | A.8.9 A.5.21 | CIS-4 CIS-16 | A08 | supply-chain.md checklist | ASSESS |
| LAY-009 | Uygulama/script doğrulama katmanı | PR.DS-02 | SI-10 | A.8.28 | CIS-16 | ASVS input | validate.py + ethics_check çalıştır | ASSESS |
| LAY-010 | Veri sınıflandırma katmanı | ID.AM-05 | RA-2 | A.5.12 | CIS-3 | ASVS data | SECRETS-DRYRUN-MATRISI + inventory | ASSESS |
| LAY-011 | Defense detection katmanı | DE.CM-01 | SI-4 | A.8.16 | CIS-8 | A09 | hooks config + scanner exit code | ASSESS |
| LAY-012 | Vendored katalog izolasyon katmanı | ID.SC-02 | SA-12 | A.5.21 | CIS-15 | Supply chain | AGENTS.md stdlib-only + no npm katalog | ASSESS |
| LAY-013 | Observability güvenli katman | PR.DS-01 | SC-28 | A.8.11 A.8.24 | CIS-3 | A02 | tfvars gitignore ASSESS | ASSESS |
| LAY-014 | Değişiklik gözetim katmanı | GV.PO ID.RA | CM-3 | A.8.32 | CIS-4 | ASVS change | CODEOWNERS/PR ASSESS | ASSESS |
| LAY-015 | Incident hazırlık katmanı | RS.MA-01 | IR-4 | A.5.24 | CIS-17 | IR | ORG/ROLES/SecOps-Lead.md varlığı | ASSESS |
| LAY-016 | Compliance map katmanı | GV.OC-03 | CA-2 | A.5.35 | CIS-4 | ASVS-5 | SECURITY_MATRIX satırları | ASSESS |
| LAY-017 | Expert/org katmanı | GV.RR-01 | PM-2 | A.5.2 | CIS-14 | Governance | ORG/ROLES + EXPERTS DIGEST | ASSESS |
| LAY-018 | Research currency katmanı | ID.RA-01 | RA-3 | A.5.7 | CIS-7 | ASVS currency | standards-currency.md damgası | ASSESS |
| LAY-019 | MCP güvenlik katmanı | PR.AA-05 | AC-20 | A.5.23 | CIS-15 | A07 | mcp.security.example.json varsayılan OFF | ASSESS |
| LAY-020 | Arşiv/QA katmanı planı | GV.OV-01 | CA-7 | A.5.35 | CIS-4 | QA | security-master-plan Faz 8 checkbox | ASSESS |
| FW-001 | Egress allowlist politikası ASSESS | PR.IR-01 | SC-7 | A.8.20 | CIS-12 | A10 | LLM/API host listesi dokümanı | ASSESS |
| FW-002 | Runner internet varsayılan reddi (hedef) | PR.IR-02 | SC-7 | A.8.22 | CIS-12 | Network | Workflow egress ASSESS notu | ASSESS |
| FW-003 | Webhook/inbound yüzey yok teyidi | ID.AM-02 | CM-8 | A.8.9 | CIS-1 | ASVS | inventory: uygulama sunucusu yok | ASSESS |
| FW-004 | DNS/dependency domain allowlist ASSESS | ID.SC-03 | SA-12 | A.5.21 | CIS-15 | A08 | Action market kaynakları listesi | ASSESS |
| FW-005 | Secret store ağ sınırı | PR.DS-01 | SC-7 SC-28 | A.8.5 | CIS-3 | A02 | SECRETS matrisi | ASSESS |
| FW-006 | Terraform provider endpoint bilinçli | PR.IR-01 | SC-7 | A.5.23 | CIS-12 | Cloud | terraform providers ASSESS | ASSESS |
| FW-007 | OTel exporter hedef kontrolü | PR.DS-02 | SC-8 | A.8.20 | CIS-12 | A09 | opentelemetry-collector.yaml gözden geçirme | ASSESS |
| FW-008 | PR fork network izolasyonu | PR.AA-05 | AC-3 | A.8.3 | CIS-6 | A07 | workflow pull_request vs target ASSESS | ASSESS |
| FW-009 | Doküman içi URL allowlist kültürü | GV.PO | SI-3 | A.5.7 | CIS-14 | Content | SECURITY_RESEARCH kaynak listesi | ASSESS |
| FW-010 | Shell dangerous pattern deny | PR.PS-02 | CM-7 | A.8.7 | CIS-4 | Policy | ethics_check.py block patterns | ASSESS |
| FW-011 | MCP network varsayılan kapalı | PR.AA | AC-20 | A.5.23 | CIS-15 | A07 | example json kapalı | ASSESS |
| FW-012 | Log outbound redaksiyon | PR.DS DE.CM | AU-9 | A.8.12 | CIS-3 CIS-8 | A09 | holding_report dry-run | ASSESS |
| FW-013 | Nightly job rate bilinci | PR.IR | CP-2 | A.5.29 | CIS-11 | DoS sınıfı | workflow schedule gözden geçirme | ASSESS |
| FW-014 | Git remote allowlist | PR.AA | AC-3 | A.5.14 | CIS-6 | A07 | git remote -v ASSESS | ASSESS |
| FW-015 | Dependency proxy yoksa pin | ID.SC | SA-12 | A.5.21 | CIS-15 | A08 | supply-chain.md | ASSESS |
| FW-016 | Browser/extension N/A beyanı | ID.AM | CM-8 | A.5.9 | CIS-1 | Scope | inventory N/A | ASSESS |
| FW-017 | Email gateway N/A beyanı | ID.AM | CM-8 | A.5.9 | CIS-1 | Scope | inventory | ASSESS |
| FW-018 | Admin interface yok | PR.AA | AC-6 | A.8.2 | CIS-6 | A07 | inventory | ASSESS |
| FW-019 | Temporary debug port yasağı | PR.IR | CM-7 | A.8.9 | CIS-4 | ASVS | kodda listen/bind araması ASSESS | ASSESS |
| FW-020 | Firewall kontrol review döngüsü | GV.OV | CA-2 | A.5.35 | CIS-4 | QA | TASKS/SECURITY_MASTER | ASSESS |
| ENC-001 | TLS minimum sürüm politikası | PR.DS-02 | SC-8 | A.8.24 | CIS-3 | A02 ASVS crypto | Python/OS TLS varsayılanı + doküman politikası | ASSESS |
| ENC-002 | Certificate verification zorunlu | PR.DS-02 | SC-8 | A.8.24 | CIS-3 | A02 | rg verify=False scripts | ASSESS |
| ENC-003 | Secret at-rest politikası | PR.DS-01 | SC-28 | A.8.11 | CIS-3 | A02 | secret_scan + .gitignore | ASSESS |
| ENC-004 | Sensitive Terraform değişkenleri | PR.DS-01 | SC-28 | A.8.11 | CIS-3 | A02 | variables.tf sensitive bayrakları | ASSESS |
| ENC-005 | Remote state encryption ASSESS | PR.DS-01 | SC-28 | A.8.24 | CIS-3 | A02 | backend config ASSESS | ASSESS |
| ENC-006 | Key rotation prosedür referansı | PR.AA-03 | IA-5 SC-12 | A.8.24 | CIS-5 | A07 | SECRETS-DRYRUN + runbook | ASSESS |
| ENC-007 | Crypto envanteri | ID.AM-01 | CM-8 SC-13 | A.5.9 | CIS-1 | ASVS | encryption-engine inventory stub | ASSESS |
| ENC-008 | Zayıf algoritma yasak listesi (isim) | PR.DS-02 | SC-13 | A.8.24 | CIS-3 | A02 | kod/algo envanter taraması | ASSESS |
| ENC-009 | PQC FIPS 203 farkındalık | ID.RA PR.DS | SC-12 SC-13 | A.8.24 | CIS-3 | ASVS crypto | pqc-roadmap.md | ASSESS |
| ENC-010 | PQC FIPS 204 farkındalık | PR.DS | SC-13 | A.8.24 | CIS-3 | A08 signing | pqc-roadmap.md | ASSESS |
| ENC-011 | PQC FIPS 205 farkındalık | PR.DS | SC-13 | A.8.24 | CIS-3 | A08 | pqc-roadmap.md | ASSESS |
| ENC-012 | Crypto-agility gereksinimi | ID.RA-05 | SC-13 | A.8.24 | CIS-4 | ASVS | crypto-agility skill | ASSESS |
| ENC-013 | HNDL risk notu | ID.RA-01 | RA-3 | A.5.7 | CIS-3 | A02 | threat-landscape + pqc-roadmap | ASSESS |
| ENC-014 | GitHub Secrets şifreleme güveni | PR.DS-01 | SC-28 | A.8.11 | CIS-3 | A02 | workflow secrets kullanımları | ASSESS |
| ENC-015 | Log mask encryption-adjacent | PR.DS DE.CM | AU-9 | A.8.12 | CIS-8 | A09 | secret_scan REPORTS | ASSESS |
| ENC-016 | Commit imza ASVS hedefi | PR.DS-06 | SI-7 | A.8.26 | CIS-16 | A08 | git config / immutable releases ASSESS | ASSESS |
| ENC-017 | Transport integrity LLM API | PR.DS-02 | SC-8 | A.8.24 | CIS-3 | A02 | client base_url https teyidi | ASSESS |
| ENC-018 | Randomness/stdlib bilinç | PR.DS | SC-12 | A.8.24 | CIS-3 | ASVS | token üretim noktaları ASSESS | ASSESS |
| ENC-019 | Vault placeholder standardı | PR.DS-01 | IA-5 | A.5.15 | CIS-3 | A02 | rg vault:// veya ${VAR} SECURITY | ASSESS |
| ENC-020 | ENC review döngüsü | GV.OV | CA-2 | A.5.35 | CIS-4 | QA | TASKS | ASSESS |
| CHG-001 | Change advisory gate ASSESS | GV.PO-01 | CM-3 | A.8.32 | CIS-4 | ASVS change | PR şablon / checklist | ASSESS |
| CHG-002 | Branch protection ASSESS | PR.PS-01 | CM-5 | A.8.4 A.8.32 | CIS-16 | A08 | gh branch protection ASSESS | ASSESS |
| CHG-003 | CODEOWNERS güvenlik yolları | GV.RR | CM-5 | A.8.4 | CIS-16 | A08 | CODEOWNERS ASSESS | ASSESS |
| CHG-004 | Kontrol üretim batch limiti | GV.OV | CM-3 | A.5.1 | CIS-4 | Process | plan batch limiti | ASSESS |
| CHG-005 | Agency/security branch ayrımı | GV.OC | CM-3 | A.5.1 | CIS-4 | Process | STATE.md notu | ASSESS |
| CHG-006 | Workflow değişikliği ek review | PR.PS | CM-3 SA-12 | A.8.32 A.5.21 | CIS-16 | A08 | PR label/checklist | ASSESS |
| CHG-007 | Scanner kural değişikliği denetimi | DE.CM | SI-4 CM-3 | A.8.16 | CIS-8 | Detection | scripts PR | ASSESS |
| CHG-008 | Rollback planı ASSESS | RC.RP | CM-3 CP-10 | A.5.29 | CIS-4 | IR | git revert prosedürü | ASSESS |
| CHG-009 | Semantic version / tag disiplini | PR.DS-06 | CM-3 SI-7 | A.8.9 | CIS-16 | A08 | immutable releases dokümanı | ASSESS |
| CHG-010 | Doküman-only vs kod değişimi ayrımı | GV.PO | CM-4 | A.5.1 | CIS-4 | Policy | STATE MODE | ASSESS |
| CHG-011 | Secret içeren PR reddi | PR.DS | SI-10 | A.8.28 | CIS-16 | A02 | hooks failClosed | ASSESS |
| CHG-012 | Ethics fail merge engeli | GV.PO | SI-10 | A.5.1 | CIS-14 | Policy | ethics_check | ASSESS |
| CHG-013 | Upstream sync review | ID.SC | SA-12 CM-3 | A.5.21 | CIS-15 | A08 | upstream-sync.yml ASSESS | ASSESS |
| CHG-014 | Infra terraform plan review | PR.PS | CM-3 | A.8.32 | CIS-4 | Cloud | workflow terraform ASSESS | ASSESS |
| CHG-015 | Skill depth değişim kaydı | GV.OV | CM-3 | A.8.32 | CIS-4 | Process | AUDIT_LOG | ASSESS |
| CHG-016 | Expert list refresh aylık | GV.RR | PM-2 | A.5.2 | CIS-14 | Governance | EXPERTS TODO | ASSESS |
| CHG-017 | Standards currency refresh | ID.RA | RA-3 | A.5.7 | CIS-7 | Compliance | SECURITY_RESEARCH | ASSESS |
| CHG-018 | Emergency change yolu | RS.MI | CM-3 IR-4 | A.5.24 | CIS-17 | IR | playbook stub | ASSESS |
| CHG-019 | Deprecation süreci | GV.OC | CM-3 | A.8.32 | CIS-4 | Process | TODO/Status alanı | ASSESS |
| CHG-020 | CHG review döngüsü | GV.OV | CA-2 | A.5.35 | CIS-4 | QA | TASKS | ASSESS |
| TC-001 | SBOM üretim gereksinimi | ID.SC-02 | SA-12 | A.5.21 | CIS-16 | A08 | SBOM planı transparent-code references | ASSESS |
| TC-002 | Action SHA pin zorunluluğu ASSESS | ID.SC-03 | SA-12 SI-7 | A.5.21 | CIS-16 | A08 | rg uses workflows pin oranı | ASSESS |
| TC-003 | Dependabot Actions güncellemesi | ID.SC | RA-5 SA-12 | A.8.8 | CIS-7 | A08 | dependabot.yml ASSESS | ASSESS |
| TC-004 | SLSA provenance hedef seviyesi | ID.SC PR.DS | SA-12 | A.5.21 | CIS-16 | A08 | supply-chain.md SLSA tablo | ASSESS |
| TC-005 | Immutable releases ASSESS | PR.DS-06 | SI-7 | A.8.26 | CIS-16 | A08 | GitHub docs checklist | ASSESS |
| TC-006 | Release attestation ASSESS | PR.DS-06 | SI-7 | A.8.26 | CIS-16 | A08 | gh attestation ASSESS | ASSESS |
| TC-007 | Action allowlist | ID.SC-03 | SA-12 | A.5.19 | CIS-15 | A08 | allowlist doküman stub | ASSESS |
| TC-008 | Workflow SBOM artefakt saklama | ID.SC | AU-7 | A.5.21 | CIS-16 | A08 | path planı | ASSESS |
| TC-009 | Katalog ayrı SBOM (opsiyonel) | ID.SC | SA-12 | A.5.21 | CIS-15 | A08 | katalog politika | ASSESS |
| TC-010 | Scorecard ASSESS | ID.RA | RA-5 | A.8.8 | CIS-7 | A08 | TASKS backlog | ASSESS |
| TC-011 | zizmor/actionlint ASSESS | DE.CM | SI-4 | A.8.16 | CIS-8 | A08 | tooling backlog | ASSESS |
| TC-012 | Provenance commit SHA bağlama | PR.DS-06 | SI-7 | A.8.26 | CIS-16 | A08 | GHA run URL politikası | ASSESS |
| TC-013 | Fork PR secret izolasyonu (TC) | PR.AA ID.SC | AC-3 SA-12 | A.8.3 | CIS-6 | A07 | workflow design ASSESS | ASSESS |
| TC-014 | Lockfile bilinci | ID.SC | SA-10 | A.8.28 | CIS-16 | A08 | AGENTS.md + PR gate | ASSESS |
| TC-015 | Image/base yok beyanı | ID.AM | CM-8 | A.5.9 | CIS-1 | Scope | inventory | ASSESS |
| TC-016 | Third-party action CVE sınıfı izleme | ID.RA | RA-5 | A.8.8 | CIS-7 | A08 | threat-landscape.md | ASSESS |
| TC-017 | Build script bütünlüğü | PR.PS | CM-3 SI-7 | A.8.28 | CIS-16 | A08 | PR + scanners | ASSESS |
| TC-018 | Transparency log hedefi | PR.DS | SI-7 | A.8.26 | CIS-16 | A08 | roadmap notu | ASSESS |
| TC-019 | Consumer verify dokümanı | PR.DS-06 | SI-7 | A.8.26 | CIS-16 | A08 | docs stub plan | ASSESS |
| TC-020 | TC review döngüsü | GV.OV | CA-2 | A.5.35 | CIS-4 | QA | TASKS | ASSESS |
| COND-001 | Risk-based access koşulu | PR.AA-01 | AC-2 AC-3 | A.5.15 | CIS-6 | A07 | PR label high-risk | ASSESS |
| COND-002 | MODE koşulu | GV.PO | PL-1 | A.5.1 | CIS-4 | Policy | STATE.md | ASSESS |
| COND-003 | Secret varlığı koşulu | PR.AA PR.DS | IA-5 | A.8.5 | CIS-5 | A07 | client dry-run davranışı | ASSESS |
| COND-004 | Fork PR koşulu | PR.AA | AC-3 | A.8.3 | CIS-6 | A07 | workflow if koşulları ASSESS | ASSESS |
| COND-005 | Branch koşulu | PR.PS | CM-5 | A.8.4 | CIS-16 | A08 | branch protection | ASSESS |
| COND-006 | Zaman koşulu — nightly pencere | PR.IR | CP-2 | A.5.29 | CIS-11 | Ops | schedule crontab ASSESS | ASSESS |
| COND-007 | Environment protection ASSESS | PR.AA | AC-3 | A.5.15 | CIS-6 | A07 | GHA environments ASSESS | ASSESS |
| COND-008 | Path filter koşulu | PR.PS | CM-3 | A.8.32 | CIS-4 | Ops | paths filters | ASSESS |
| COND-009 | Actor allowlist koşulu | PR.AA | AC-2 | A.5.15 | CIS-5 | A07 | GITHUB_ACTOR koşulları ASSESS | ASSESS |
| COND-010 | Ethics fail koşulu | GV.PO | SI-10 | A.5.1 | CIS-14 | Policy | CI step | ASSESS |
| COND-011 | Secret scan fail koşulu | PR.DS | SI-10 | A.8.28 | CIS-16 | A02 | hooks/CI | ASSESS |
| COND-012 | Risk skoru eşiği (kaba) | ID.RA GV.RM | RA-3 | A.5.3 | CIS-4 | Risk | STATE assessment_id | ASSESS |
| COND-013 | Compliance pack koşulu | GV.OC | CA-2 | A.5.35 | CIS-4 | Compliance | matrix TBD satır sayısı | ASSESS |
| COND-014 | PQC migration koşulu | PR.DS | SC-13 | A.8.24 | CIS-3 | A02 | ENC checklist | ASSESS |
| COND-015 | MCP enable koşulu | PR.AA | AC-20 | A.5.23 | CIS-15 | A07 | example default OFF | ASSESS |
| COND-016 | Canva ayrımı koşulu | GV.OC | CM-3 | A.5.1 | CIS-4 | Process | AGENTS.md | ASSESS |
| COND-017 | Rate limit koşulu | PR.IR | SC-5 | A.8.6 | CIS-11 | DoS sınıfı | client code ASSESS | ASSESS |
| COND-018 | Data classification koşulu | PR.DS | SI-12 | A.8.12 | CIS-3 | A02 LLM | prompt hygiene | ASSESS |
| COND-019 | Emergency override kayıt koşulu | GV.PO RS.MI | AU-2 IR-4 | A.5.24 | CIS-17 | IR | AUDIT_LOG | ASSESS |
| COND-020 | COND review döngüsü | GV.OV | CA-2 | A.5.35 | CIS-4 | QA | TASKS | ASSESS |

CSV: `matrix-001-020.csv` + `matrix-021-100.csv`

## Tranche 021–100

| LAY-021 | Katman envanteri diff ritmi | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı LAY-021 + ilgili path/rg; değer yok | ASSESS |
| LAY-022 | Sınır sınıfı gözden geçirme | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı LAY-022 + ilgili path/rg; değer yok | ASSESS |
| LAY-023 | Least-privilege katman haritası | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı LAY-023 + ilgili path/rg; değer yok | ASSESS |
| LAY-024 | Ayrıcalık ayrımı (SoD) katmanı | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı LAY-024 + ilgili path/rg; değer yok | ASSESS |
| LAY-025 | Kimlik sağlayıcı envanteri | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı LAY-025 + ilgili path/rg; değer yok | ASSESS |
| LAY-026 | Servis hesabı katmanı | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı LAY-026 + ilgili path/rg; değer yok | ASSESS |
| LAY-027 | MFA politikası katmanı | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı LAY-027 + ilgili path/rg; değer yok | ASSESS |
| LAY-028 | Session ömrü politikası | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı LAY-028 + ilgili path/rg; değer yok | ASSESS |
| LAY-029 | Rol şablonları katmanı | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı LAY-029 + ilgili path/rg; değer yok | ASSESS |
| LAY-030 | Misafir/contractor erişim katmanı | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı LAY-030 + ilgili path/rg; değer yok | ASSESS |
| LAY-031 | Veri sınıflandırma yenileme | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı LAY-031 + ilgili path/rg; değer yok | ASSESS |
| LAY-032 | PII yok beyanı teyidi | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı LAY-032 + ilgili path/rg; değer yok | ASSESS |
| LAY-033 | Log saklama katmanı | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı LAY-033 + ilgili path/rg; değer yok | ASSESS |
| LAY-034 | Log bütünlüğü katmanı | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı LAY-034 + ilgili path/rg; değer yok | ASSESS |
| LAY-035 | Hata mesajı sızıntı katmanı | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı LAY-035 + ilgili path/rg; değer yok | ASSESS |
| LAY-036 | Yedekleme katmanı ASSESS | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı LAY-036 + ilgili path/rg; değer yok | ASSESS |
| LAY-037 | Arşiv sınıflandırma | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı LAY-037 + ilgili path/rg; değer yok | ASSESS |
| LAY-038 | Çöp kutusu/silinen sır | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı LAY-038 + ilgili path/rg; değer yok | ASSESS |
| LAY-039 | Çapraz iştirak veri sınırı | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı LAY-039 + ilgili path/rg; değer yok | ASSESS |
| LAY-040 | Doküman sınıflandırma banner | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı LAY-040 + ilgili path/rg; değer yok | ASSESS |
| LAY-041 | CI izolasyon katmanı | ID.SC-02 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı LAY-041 + ilgili path/rg; değer yok | ASSESS |
| LAY-042 | Build determinism katmanı | PR.DS-02 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı LAY-042 + ilgili path/rg; değer yok | ASSESS |
| LAY-043 | Bağımlılık katmanı envanteri | GV.RR-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı LAY-043 + ilgili path/rg; değer yok | ASSESS |
| LAY-044 | Katalog izolasyonu | ID.RA-05 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı LAY-044 + ilgili path/rg; değer yok | ASSESS |
| LAY-045 | Hook katmanı fail-closed | ID.AM-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı LAY-045 + ilgili path/rg; değer yok | ASSESS |
| LAY-046 | Lint/validate katmanı | ID.RA-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı LAY-046 + ilgili path/rg; değer yok | ASSESS |
| LAY-047 | Test katmanı güvenlik | GV.PO-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı LAY-047 + ilgili path/rg; değer yok | ASSESS |
| LAY-048 | Artifact saklama katmanı | PR.AA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı LAY-048 + ilgili path/rg; değer yok | ASSESS |
| LAY-049 | Cache zehirlenmesi farkındalığı | PR.DS-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı LAY-049 + ilgili path/rg; değer yok | ASSESS |
| LAY-050 | Runner imaj katmanı | PR.IR-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı LAY-050 + ilgili path/rg; değer yok | ASSESS |
| LAY-051 | LLM outbound katmanı | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı LAY-051 + ilgili path/rg; değer yok | ASSESS |
| LAY-052 | Prompt hygiene katmanı | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı LAY-052 + ilgili path/rg; değer yok | ASSESS |
| LAY-053 | MCP varsayılan kapalı katman | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı LAY-053 + ilgili path/rg; değer yok | ASSESS |
| LAY-054 | Tool-call denetim katmanı | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı LAY-054 + ilgili path/rg; değer yok | ASSESS |
| LAY-055 | Model çıktı süzgeç katmanı | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı LAY-055 + ilgili path/rg; değer yok | ASSESS |
| LAY-056 | Canva ayrım katmanı | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı LAY-056 + ilgili path/rg; değer yok | ASSESS |
| LAY-057 | Agency/security branch katmanı | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı LAY-057 + ilgili path/rg; değer yok | ASSESS |
| LAY-058 | Plugin/skill yükleme katmanı | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı LAY-058 + ilgili path/rg; değer yok | ASSESS |
| LAY-059 | Untrusted ingest katmanı | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı LAY-059 + ilgili path/rg; değer yok | ASSESS |
| LAY-060 | Token vaadi reddi katmanı | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı LAY-060 + ilgili path/rg; değer yok | ASSESS |
| LAY-061 | Infra kod katmanı | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı LAY-061 + ilgili path/rg; değer yok | ASSESS |
| LAY-062 | State dosyası gizliliği | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı LAY-062 + ilgili path/rg; değer yok | ASSESS |
| LAY-063 | Observability exporter katmanı | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı LAY-063 + ilgili path/rg; değer yok | ASSESS |
| LAY-064 | Metrik PII yasağı | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı LAY-064 + ilgili path/rg; değer yok | ASSESS |
| LAY-065 | Alert yorulması katmanı | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı LAY-065 + ilgili path/rg; değer yok | ASSESS |
| LAY-066 | Sağlık uçları N/A beyanı | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı LAY-066 + ilgili path/rg; değer yok | ASSESS |
| LAY-067 | Container runtime N/A | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı LAY-067 + ilgili path/rg; değer yok | ASSESS |
| LAY-068 | K8s workflow sınırlı kapsam | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı LAY-068 + ilgili path/rg; değer yok | ASSESS |
| LAY-069 | Secret store katmanı | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı LAY-069 + ilgili path/rg; değer yok | ASSESS |
| LAY-070 | Env dosyası katmanı | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı LAY-070 + ilgili path/rg; değer yok | ASSESS |
| LAY-071 | IR hazırlık katmanı | ID.SC-02 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı LAY-071 + ilgili path/rg; değer yok | ASSESS |
| LAY-072 | Olay sınıflandırma katmanı | PR.DS-02 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı LAY-072 + ilgili path/rg; değer yok | ASSESS |
| LAY-073 | İletişim katmanı IR | GV.RR-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı LAY-073 + ilgili path/rg; değer yok | ASSESS |
| LAY-074 | Adli saklama katmanı | ID.RA-05 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı LAY-074 + ilgili path/rg; değer yok | ASSESS |
| LAY-075 | İş sürekliliği katmanı | ID.AM-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı LAY-075 + ilgili path/rg; değer yok | ASSESS |
| LAY-076 | Yedek imza katmanı | ID.RA-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı LAY-076 + ilgili path/rg; değer yok | ASSESS |
| LAY-077 | Masaüstü egzersizi planı | GV.PO-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı LAY-077 + ilgili path/rg; değer yok | ASSESS |
| LAY-078 | Tedarikçi kesinti katmanı | PR.AA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı LAY-078 + ilgili path/rg; değer yok | ASSESS |
| LAY-079 | İnsan yedekleme katmanı | PR.DS-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı LAY-079 + ilgili path/rg; değer yok | ASSESS |
| LAY-080 | Eğitim katmanı | PR.IR-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı LAY-080 + ilgili path/rg; değer yok | ASSESS |
| LAY-081 | Uyum haritası katmanı | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı LAY-081 + ilgili path/rg; değer yok | ASSESS |
| LAY-082 | Kanıt deposu katmanı | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı LAY-082 + ilgili path/rg; değer yok | ASSESS |
| LAY-083 | Sahiplik katmanı | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı LAY-083 + ilgili path/rg; değer yok | ASSESS |
| LAY-084 | Ölçüm katmanı | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı LAY-084 + ilgili path/rg; değer yok | ASSESS |
| LAY-085 | Gap kaydı katmanı | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı LAY-085 + ilgili path/rg; değer yok | ASSESS |
| LAY-086 | İstisna kaydı katmanı | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı LAY-086 + ilgili path/rg; değer yok | ASSESS |
| LAY-087 | Politika sürüm katmanı | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı LAY-087 + ilgili path/rg; değer yok | ASSESS |
| LAY-088 | Dış denetim hazırlık | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı LAY-088 + ilgili path/rg; değer yok | ASSESS |
| LAY-089 | Yasal saklama katmanı | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı LAY-089 + ilgili path/rg; değer yok | ASSESS |
| LAY-090 | Etik kurul katmanı | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı LAY-090 + ilgili path/rg; değer yok | ASSESS |
| LAY-091 | Kontrol dil tutarlılığı | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı LAY-091 + ilgili path/rg; değer yok | ASSESS |
| LAY-092 | Yinelenen kontrol tespiti | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı LAY-092 + ilgili path/rg; değer yok | ASSESS |
| LAY-093 | Ölü kontrol temizliği | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı LAY-093 + ilgili path/rg; değer yok | ASSESS |
| LAY-094 | Batch limit katmanı | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı LAY-094 + ilgili path/rg; değer yok | ASSESS |
| LAY-095 | Peer review katmanı | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı LAY-095 + ilgili path/rg; değer yok | ASSESS |
| LAY-096 | Otomasyon vs insan kapısı | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı LAY-096 + ilgili path/rg; değer yok | ASSESS |
| LAY-097 | Metrik doğruluğu | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı LAY-097 + ilgili path/rg; değer yok | ASSESS |
| LAY-098 | Arşiv damgası | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı LAY-098 + ilgili path/rg; değer yok | ASSESS |
| LAY-099 | Okunabilirlik katmanı | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı LAY-099 + ilgili path/rg; değer yok | ASSESS |
| LAY-100 | LAY review döngüsü 021–100 | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı LAY-100 + ilgili path/rg; değer yok | ASSESS |
| FW-021 | Egress host envanteri yenileme | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı FW-021 + ilgili path/rg; değer yok | ASSESS |
| FW-022 | Egress varsayılan deny hedefi | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı FW-022 + ilgili path/rg; değer yok | ASSESS |
| FW-023 | DNS çözümleme sınırı ASSESS | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı FW-023 + ilgili path/rg; değer yok | ASSESS |
| FW-024 | DoH/özel DNS N/A | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı FW-024 + ilgili path/rg; değer yok | ASSESS |
| FW-025 | Webhook inbound yok teyidi | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı FW-025 + ilgili path/rg; değer yok | ASSESS |
| FW-026 | GitHub webhook secret hijyeni | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı FW-026 + ilgili path/rg; değer yok | ASSESS |
| FW-027 | IPv6/IPv4 kapsam notu | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı FW-027 + ilgili path/rg; değer yok | ASSESS |
| FW-028 | Proxy/orta kutu yasağı | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı FW-028 + ilgili path/rg; değer yok | ASSESS |
| FW-029 | CORS N/A beyanı | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı FW-029 + ilgili path/rg; değer yok | ASSESS |
| FW-030 | WAF N/A beyanı | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı FW-030 + ilgili path/rg; değer yok | ASSESS |
| FW-031 | SSH inbound yok | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı FW-031 + ilgili path/rg; değer yok | ASSESS |
| FW-032 | RDP/WinRM yok | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı FW-032 + ilgili path/rg; değer yok | ASSESS |
| FW-033 | Veritabanı portu yok | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı FW-033 + ilgili path/rg; değer yok | ASSESS |
| FW-034 | Redis/cache portu yok | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı FW-034 + ilgili path/rg; değer yok | ASSESS |
| FW-035 | Admin panel yok | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı FW-035 + ilgili path/rg; değer yok | ASSESS |
| FW-036 | Debug port yasağı tarama | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı FW-036 + ilgili path/rg; değer yok | ASSESS |
| FW-037 | Localhost-only varsayım yok | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı FW-037 + ilgili path/rg; değer yok | ASSESS |
| FW-038 | Container publish port ASSESS | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı FW-038 + ilgili path/rg; değer yok | ASSESS |
| FW-039 | Load balancer N/A | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı FW-039 + ilgili path/rg; değer yok | ASSESS |
| FW-040 | CDN kenar N/A | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı FW-040 + ilgili path/rg; değer yok | ASSESS |
| FW-041 | Git remote allowlist | ID.SC-02 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı FW-041 + ilgili path/rg; değer yok | ASSESS |
| FW-042 | Fork network izolasyonu | PR.DS-02 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı FW-042 + ilgili path/rg; değer yok | ASSESS |
| FW-043 | Dependabot ağ kapsamı | GV.RR-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı FW-043 + ilgili path/rg; değer yok | ASSESS |
| FW-044 | Marketplace action kaynağı | ID.RA-05 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı FW-044 + ilgili path/rg; değer yok | ASSESS |
| FW-045 | Third-party action egress | ID.AM-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı FW-045 + ilgili path/rg; değer yok | ASSESS |
| FW-046 | npm registry N/A/sınır | ID.RA-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı FW-046 + ilgili path/rg; değer yok | ASSESS |
| FW-047 | PyPI indirme CI sınırı | GV.PO-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı FW-047 + ilgili path/rg; değer yok | ASSESS |
| FW-048 | Container registry N/A | PR.AA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı FW-048 + ilgili path/rg; değer yok | ASSESS |
| FW-049 | Paket proxy yoksa pin | PR.DS-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı FW-049 + ilgili path/rg; değer yok | ASSESS |
| FW-050 | TLS kesme yasağı | PR.IR-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı FW-050 + ilgili path/rg; değer yok | ASSESS |
| FW-051 | Email gateway N/A | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı FW-051 + ilgili path/rg; değer yok | ASSESS |
| FW-052 | SMS/voice gateway N/A | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı FW-052 + ilgili path/rg; değer yok | ASSESS |
| FW-053 | Slack inbound webhook N/A | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı FW-053 + ilgili path/rg; değer yok | ASSESS |
| FW-054 | MCP network enable kapısı | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı FW-054 + ilgili path/rg; değer yok | ASSESS |
| FW-055 | Browser extension N/A | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı FW-055 + ilgili path/rg; değer yok | ASSESS |
| FW-056 | Mobile MDM N/A | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı FW-056 + ilgili path/rg; değer yok | ASSESS |
| FW-057 | VPN konsantrator N/A | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı FW-057 + ilgili path/rg; değer yok | ASSESS |
| FW-058 | Office firewall N/A | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı FW-058 + ilgili path/rg; değer yok | ASSESS |
| FW-059 | Cloud SG/NACL ASSESS | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı FW-059 + ilgili path/rg; değer yok | ASSESS |
| FW-060 | Public bucket yasağı | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı FW-060 + ilgili path/rg; değer yok | ASSESS |
| FW-061 | OTel exporter hedef kontrolü | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı FW-061 + ilgili path/rg; değer yok | ASSESS |
| FW-062 | Log shipping hedefi | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı FW-062 + ilgili path/rg; değer yok | ASSESS |
| FW-063 | Time-sync bağımlılığı | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı FW-063 + ilgili path/rg; değer yok | ASSESS |
| FW-064 | NTP amplifikasyon N/A | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı FW-064 + ilgili path/rg; değer yok | ASSESS |
| FW-065 | Rate limit outbound | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı FW-065 + ilgili path/rg; değer yok | ASSESS |
| FW-066 | DoS sınıfı farkındalık | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı FW-066 + ilgili path/rg; değer yok | ASSESS |
| FW-067 | Nightly pencere çakışması | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı FW-067 + ilgili path/rg; değer yok | ASSESS |
| FW-068 | Git LFS/büyük dosya sınırı | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı FW-068 + ilgili path/rg; değer yok | ASSESS |
| FW-069 | Harici kısa URL yasağı | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı FW-069 + ilgili path/rg; değer yok | ASSESS |
| FW-070 | Untrusted binary indirme yasağı | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı FW-070 + ilgili path/rg; değer yok | ASSESS |
| FW-071 | Shell pipe deny listesi | ID.SC-02 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı FW-071 + ilgili path/rg; değer yok | ASSESS |
| FW-072 | sudo/root runner yasağı | PR.DS-02 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı FW-072 + ilgili path/rg; değer yok | ASSESS |
| FW-073 | Docker socket mount yasağı | GV.RR-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı FW-073 + ilgili path/rg; değer yok | ASSESS |
| FW-074 | Privileged container yasağı | ID.RA-05 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı FW-074 + ilgili path/rg; değer yok | ASSESS |
| FW-075 | HostNetwork yasağı | ID.AM-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı FW-075 + ilgili path/rg; değer yok | ASSESS |
| FW-076 | NodePort public yasağı | ID.RA-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı FW-076 + ilgili path/rg; değer yok | ASSESS |
| FW-077 | Ingress default deny | GV.PO-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı FW-077 + ilgili path/rg; değer yok | ASSESS |
| FW-078 | NetworkPolicy hedefi | PR.AA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı FW-078 + ilgili path/rg; değer yok | ASSESS |
| FW-079 | Service mesh N/A | PR.DS-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı FW-079 + ilgili path/rg; değer yok | ASSESS |
| FW-080 | East-west görünürlük N/A | PR.IR-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı FW-080 + ilgili path/rg; değer yok | ASSESS |
| FW-081 | ICMP/management N/A | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı FW-081 + ilgili path/rg; değer yok | ASSESS |
| FW-082 | BGP/peering N/A | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı FW-082 + ilgili path/rg; değer yok | ASSESS |
| FW-083 | DDoS üretici hizmet N/A | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı FW-083 + ilgili path/rg; değer yok | ASSESS |
| FW-084 | Geo-IP blok N/A | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı FW-084 + ilgili path/rg; değer yok | ASSESS |
| FW-085 | Bot yönetimi N/A | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı FW-085 + ilgili path/rg; değer yok | ASSESS |
| FW-086 | API gateway N/A | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı FW-086 + ilgili path/rg; değer yok | ASSESS |
| FW-087 | GraphQL yüzey N/A | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı FW-087 + ilgili path/rg; değer yok | ASSESS |
| FW-088 | WebSocket yüzey N/A | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı FW-088 + ilgili path/rg; değer yok | ASSESS |
| FW-089 | mTLS servis N/A | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı FW-089 + ilgili path/rg; değer yok | ASSESS |
| FW-090 | Sertifika pin istemci ASSESS | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı FW-090 + ilgili path/rg; değer yok | ASSESS |
| FW-091 | Insecure skip verify taraması | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı FW-091 + ilgili path/rg; değer yok | ASSESS |
| FW-092 | Karışık içerik N/A | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı FW-092 + ilgili path/rg; değer yok | ASSESS |
| FW-093 | Deep link/intent N/A | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı FW-093 + ilgili path/rg; değer yok | ASSESS |
| FW-094 | Air-gap hedefi yok | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı FW-094 + ilgili path/rg; değer yok | ASSESS |
| FW-095 | Split-horizon DNS N/A | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı FW-095 + ilgili path/rg; değer yok | ASSESS |
| FW-096 | Guest Wi-Fi N/A | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı FW-096 + ilgili path/rg; değer yok | ASSESS |
| FW-097 | Printer/IoT N/A | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı FW-097 + ilgili path/rg; değer yok | ASSESS |
| FW-098 | Lab ağ ayrımı | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı FW-098 + ilgili path/rg; değer yok | ASSESS |
| FW-099 | Firewall kural review ritmi | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı FW-099 + ilgili path/rg; değer yok | ASSESS |
| FW-100 | FW tranche kapanış kontrolü | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı FW-100 + ilgili path/rg; değer yok | ASSESS |
| ENC-021 | TLS 1.2 taban teyidi | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı ENC-021 + ilgili path/rg; değer yok | ASSESS |
| ENC-022 | TLS 1.3 tercih kaydı | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı ENC-022 + ilgili path/rg; değer yok | ASSESS |
| ENC-023 | Sertifika doğrulama zorunlu | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı ENC-023 + ilgili path/rg; değer yok | ASSESS |
| ENC-024 | Özel CA envanteri | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı ENC-024 + ilgili path/rg; değer yok | ASSESS |
| ENC-025 | Sertifika süre izleme N/A | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı ENC-025 + ilgili path/rg; değer yok | ASSESS |
| ENC-026 | HSTS N/A | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı ENC-026 + ilgili path/rg; değer yok | ASSESS |
| ENC-027 | Cipher deny listesi (isim) | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı ENC-027 + ilgili path/rg; değer yok | ASSESS |
| ENC-028 | Zayıf hash yasak listesi | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı ENC-028 + ilgili path/rg; değer yok | ASSESS |
| ENC-029 | HMAC vs encryption ayrımı | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı ENC-029 + ilgili path/rg; değer yok | ASSESS |
| ENC-030 | AEAD tercih kaydı | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı ENC-030 + ilgili path/rg; değer yok | ASSESS |
| ENC-031 | Anahtar üretim noktası envanteri | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı ENC-031 + ilgili path/rg; değer yok | ASSESS |
| ENC-032 | stdlib secrets kullanımı | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı ENC-032 + ilgili path/rg; değer yok | ASSESS |
| ENC-033 | Anahtar saklama politikası | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı ENC-033 + ilgili path/rg; değer yok | ASSESS |
| ENC-034 | Anahtar rotasyon referansı | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı ENC-034 + ilgili path/rg; değer yok | ASSESS |
| ENC-035 | Anahtar imha politikası | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı ENC-035 + ilgili path/rg; değer yok | ASSESS |
| ENC-036 | KMS/HSM N/A veya hedef | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı ENC-036 + ilgili path/rg; değer yok | ASSESS |
| ENC-037 | GitHub Secrets şifreleme güveni | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı ENC-037 + ilgili path/rg; değer yok | ASSESS |
| ENC-038 | Cursor Secrets ayrımı | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı ENC-038 + ilgili path/rg; değer yok | ASSESS |
| ENC-039 | Terraform sensitive bayrağı | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı ENC-039 + ilgili path/rg; değer yok | ASSESS |
| ENC-040 | Remote state encryption ASSESS | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı ENC-040 + ilgili path/rg; değer yok | ASSESS |
| ENC-041 | At-rest markdown redaksiyon | ID.SC-02 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı ENC-041 + ilgili path/rg; değer yok | ASSESS |
| ENC-042 | Yedek şifreleme N/A | PR.DS-02 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı ENC-042 + ilgili path/rg; değer yok | ASSESS |
| ENC-043 | Disk şifreleme N/A | GV.RR-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı ENC-043 + ilgili path/rg; değer yok | ASSESS |
| ENC-044 | DB TDE N/A | ID.RA-05 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı ENC-044 + ilgili path/rg; değer yok | ASSESS |
| ENC-045 | Obje depo SSE N/A | ID.AM-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı ENC-045 + ilgili path/rg; değer yok | ASSESS |
| ENC-046 | Log şifreleme-adjacent maske | ID.RA-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı ENC-046 + ilgili path/rg; değer yok | ASSESS |
| ENC-047 | E-posta şifreleme N/A | GV.PO-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı ENC-047 + ilgili path/rg; değer yok | ASSESS |
| ENC-048 | Dosya şifreleme aracı yok iddiası | PR.AA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı ENC-048 + ilgili path/rg; değer yok | ASSESS |
| ENC-049 | Field-level encryption N/A | PR.DS-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı ENC-049 + ilgili path/rg; değer yok | ASSESS |
| ENC-050 | Token binding N/A | PR.IR-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı ENC-050 + ilgili path/rg; değer yok | ASSESS |
| ENC-051 | PQC FIPS 203 farkındalık yenileme | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı ENC-051 + ilgili path/rg; değer yok | ASSESS |
| ENC-052 | PQC FIPS 204 farkındalık yenileme | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı ENC-052 + ilgili path/rg; değer yok | ASSESS |
| ENC-053 | PQC FIPS 205 farkındalık yenileme | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı ENC-053 + ilgili path/rg; değer yok | ASSESS |
| ENC-054 | HNDL risk kaydı | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı ENC-054 + ilgili path/rg; değer yok | ASSESS |
| ENC-055 | Kripto çevikliği gereksinimi | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı ENC-055 + ilgili path/rg; değer yok | ASSESS |
| ENC-056 | Protokol dondurma yasağı | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı ENC-056 + ilgili path/rg; değer yok | ASSESS |
| ENC-057 | Karma imza stratejisi notu | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı ENC-057 + ilgili path/rg; değer yok | ASSESS |
| ENC-058 | Sertifika şeffaflığı N/A | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı ENC-058 + ilgili path/rg; değer yok | ASSESS |
| ENC-059 | Code signing hedefi | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı ENC-059 + ilgili path/rg; değer yok | ASSESS |
| ENC-060 | Commit imza hedefi | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı ENC-060 + ilgili path/rg; değer yok | ASSESS |
| ENC-061 | Provenance imza | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı ENC-061 + ilgili path/rg; değer yok | ASSESS |
| ENC-062 | SBOM imza | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı ENC-062 + ilgili path/rg; değer yok | ASSESS |
| ENC-063 | LLM API transport integrity | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı ENC-063 + ilgili path/rg; değer yok | ASSESS |
| ENC-064 | Webhook imza doğrulama N/A | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı ENC-064 + ilgili path/rg; değer yok | ASSESS |
| ENC-065 | JWT doğrulama N/A | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı ENC-065 + ilgili path/rg; değer yok | ASSESS |
| ENC-066 | OIDC token audience ASSESS | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı ENC-066 + ilgili path/rg; değer yok | ASSESS |
| ENC-067 | PATs düz metin yasağı | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı ENC-067 + ilgili path/rg; değer yok | ASSESS |
| ENC-068 | API anahtarı prefix tarama | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı ENC-068 + ilgili path/rg; değer yok | ASSESS |
| ENC-069 | QR/secret backup yasağı | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı ENC-069 + ilgili path/rg; değer yok | ASSESS |
| ENC-070 | Ekran görüntüsü secret yasağı | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı ENC-070 + ilgili path/rg; değer yok | ASSESS |
| ENC-071 | Notebook secret yasağı | ID.SC-02 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı ENC-071 + ilgili path/rg; değer yok | ASSESS |
| ENC-072 | Doküman gizli ek yasağı | PR.DS-02 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı ENC-072 + ilgili path/rg; değer yok | ASSESS |
| ENC-073 | Sıkıştırma bombası farkındalığı | GV.RR-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı ENC-073 + ilgili path/rg; değer yok | ASSESS |
| ENC-074 | Homomorfik/kullanılmayan kripto yok | ID.RA-05 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı ENC-074 + ilgili path/rg; değer yok | ASSESS |
| ENC-075 | Özel protokol yasağı | ID.AM-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı ENC-075 + ilgili path/rg; değer yok | ASSESS |
| ENC-076 | Rolling crypto DIY yasağı | ID.RA-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı ENC-076 + ilgili path/rg; değer yok | ASSESS |
| ENC-077 | Sabit IV/nonce tarama hedefi | GV.PO-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı ENC-077 + ilgili path/rg; değer yok | ASSESS |
| ENC-078 | Padding oracle sınıfı farkındalık | PR.AA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı ENC-078 + ilgili path/rg; değer yok | ASSESS |
| ENC-079 | Yan kanal N/A | PR.DS-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı ENC-079 + ilgili path/rg; değer yok | ASSESS |
| ENC-080 | TRNG/HSM N/A | PR.IR-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı ENC-080 + ilgili path/rg; değer yok | ASSESS |
| ENC-081 | Anahtar seremonisi N/A | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı ENC-081 + ilgili path/rg; değer yok | ASSESS |
| ENC-082 | Escrow politikası | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı ENC-082 + ilgili path/rg; değer yok | ASSESS |
| ENC-083 | Kripto envanter yenileme | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı ENC-083 + ilgili path/rg; değer yok | ASSESS |
| ENC-084 | Algoritma yaşlandırma listesi | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı ENC-084 + ilgili path/rg; değer yok | ASSESS |
| ENC-085 | FIPS modu iddiası yok | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı ENC-085 + ilgili path/rg; değer yok | ASSESS |
| ENC-086 | Common Criteria iddiası yok | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı ENC-086 + ilgili path/rg; değer yok | ASSESS |
| ENC-087 | Müşteri getirdi anahtar N/A | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı ENC-087 + ilgili path/rg; değer yok | ASSESS |
| ENC-088 | Çok bulut KEK N/A | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı ENC-088 + ilgili path/rg; değer yok | ASSESS |
| ENC-089 | Secret scanning exception kaydı | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı ENC-089 + ilgili path/rg; değer yok | ASSESS |
| ENC-090 | Vault placeholder standardı | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı ENC-090 + ilgili path/rg; değer yok | ASSESS |
| ENC-091 | Şifre politikası insan hesabı | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı ENC-091 + ilgili path/rg; değer yok | ASSESS |
| ENC-092 | Passkey hedefi | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı ENC-092 + ilgili path/rg; değer yok | ASSESS |
| ENC-093 | Shared password yasağı | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı ENC-093 + ilgili path/rg; değer yok | ASSESS |
| ENC-094 | Emergency break-glass kaydı | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı ENC-094 + ilgili path/rg; değer yok | ASSESS |
| ENC-095 | Kriptografik teslimat şampiyonu | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı ENC-095 + ilgili path/rg; değer yok | ASSESS |
| ENC-096 | Eğitim: secret hygiene | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı ENC-096 + ilgili path/rg; değer yok | ASSESS |
| ENC-097 | ENC kanıt yolu | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı ENC-097 + ilgili path/rg; değer yok | ASSESS |
| ENC-098 | ENC istisna N/A listesi | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı ENC-098 + ilgili path/rg; değer yok | ASSESS |
| ENC-099 | ENC peer review | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı ENC-099 + ilgili path/rg; değer yok | ASSESS |
| ENC-100 | ENC review döngüsü 021–100 | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı ENC-100 + ilgili path/rg; değer yok | ASSESS |
| CHG-021 | PR şablon güvenlik maddesi ASSESS | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı CHG-021 + ilgili path/rg; değer yok | ASSESS |
| CHG-022 | Zorunlu review sayısı ASSESS | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı CHG-022 + ilgili path/rg; değer yok | ASSESS |
| CHG-023 | CODEOWNERS güvenlik yolları yenileme | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı CHG-023 + ilgili path/rg; değer yok | ASSESS |
| CHG-024 | Admin bypass izleme | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı CHG-024 + ilgili path/rg; değer yok | ASSESS |
| CHG-025 | Force-push yasağı ana dal | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı CHG-025 + ilgili path/rg; değer yok | ASSESS |
| CHG-026 | Doğrudan commit yasağı main | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı CHG-026 + ilgili path/rg; değer yok | ASSESS |
| CHG-027 | Signed commit hedefi (change) | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı CHG-027 + ilgili path/rg; değer yok | ASSESS |
| CHG-028 | STATUS check zorunluluğu | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı CHG-028 + ilgili path/rg; değer yok | ASSESS |
| CHG-029 | Draft PR merceği | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı CHG-029 + ilgili path/rg; değer yok | ASSESS |
| CHG-030 | Fork PR maintainer edit ASSESS | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı CHG-030 + ilgili path/rg; değer yok | ASSESS |
| CHG-031 | Label high-risk değişim | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı CHG-031 + ilgili path/rg; değer yok | ASSESS |
| CHG-032 | Workflow değişikliği ikinci onay | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı CHG-032 + ilgili path/rg; değer yok | ASSESS |
| CHG-033 | Hook kural değişikliği denetimi | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı CHG-033 + ilgili path/rg; değer yok | ASSESS |
| CHG-034 | Scanner false-positive süreci | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı CHG-034 + ilgili path/rg; değer yok | ASSESS |
| CHG-035 | Bağımlılık bump ayrı PR | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı CHG-035 + ilgili path/rg; değer yok | ASSESS |
| CHG-036 | Major bump insan kapısı | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı CHG-036 + ilgili path/rg; değer yok | ASSESS |
| CHG-037 | Terraform plan review | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı CHG-037 + ilgili path/rg; değer yok | ASSESS |
| CHG-038 | State lock farkındalığı | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı CHG-038 + ilgili path/rg; değer yok | ASSESS |
| CHG-039 | Doküman-only yolu | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı CHG-039 + ilgili path/rg; değer yok | ASSESS |
| CHG-040 | Kod değişimi MODE notu | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı CHG-040 + ilgili path/rg; değer yok | ASSESS |
| CHG-041 | Rollback / git revert prosedürü | ID.SC-02 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı CHG-041 + ilgili path/rg; değer yok | ASSESS |
| CHG-042 | Tag immutable hedefi | PR.DS-02 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı CHG-042 + ilgili path/rg; değer yok | ASSESS |
| CHG-043 | Release notes güvenlik satırı | GV.RR-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı CHG-043 + ilgili path/rg; değer yok | ASSESS |
| CHG-044 | Hotfix dar kapsam | ID.RA-05 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı CHG-044 + ilgili path/rg; değer yok | ASSESS |
| CHG-045 | Feature flag N/A | ID.AM-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı CHG-045 + ilgili path/rg; değer yok | ASSESS |
| CHG-046 | Migration N/A | ID.RA-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı CHG-046 + ilgili path/rg; değer yok | ASSESS |
| CHG-047 | Schema change N/A | GV.PO-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı CHG-047 + ilgili path/rg; değer yok | ASSESS |
| CHG-048 | API breaking change N/A | PR.AA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı CHG-048 + ilgili path/rg; değer yok | ASSESS |
| CHG-049 | Skill sürümleme | PR.DS-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı CHG-049 + ilgili path/rg; değer yok | ASSESS |
| CHG-050 | Prompt dump yasağı değişim | PR.IR-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı CHG-050 + ilgili path/rg; değer yok | ASSESS |
| CHG-051 | Expert bio uydurma yasağı | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı CHG-051 + ilgili path/rg; değer yok | ASSESS |
| CHG-052 | Agency brief değişim ritmi | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı CHG-052 + ilgili path/rg; değer yok | ASSESS |
| CHG-053 | LATOS kart batch limiti | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı CHG-053 + ilgili path/rg; değer yok | ASSESS |
| CHG-054 | Paralel track silme yasağı | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı CHG-054 + ilgili path/rg; değer yok | ASSESS |
| CHG-055 | Merge kullanıcı onayı | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı CHG-055 + ilgili path/rg; değer yok | ASSESS |
| CHG-056 | Upstream-sync review | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı CHG-056 + ilgili path/rg; değer yok | ASSESS |
| CHG-057 | Submodule yasağı/ASSESS | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı CHG-057 + ilgili path/rg; değer yok | ASSESS |
| CHG-058 | LFS politika | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı CHG-058 + ilgili path/rg; değer yok | ASSESS |
| CHG-059 | Generated dosya disiplini | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı CHG-059 + ilgili path/rg; değer yok | ASSESS |
| CHG-060 | Lockfile yoksa açıklama | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı CHG-060 + ilgili path/rg; değer yok | ASSESS |
| CHG-061 | Lisans uyumu değişim | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı CHG-061 + ilgili path/rg; değer yok | ASSESS |
| CHG-062 | Gizli dosya .gitignore | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı CHG-062 + ilgili path/rg; değer yok | ASSESS |
| CHG-063 | Pre-commit yerel opsiyon | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı CHG-063 + ilgili path/rg; değer yok | ASSESS |
| CHG-064 | CI skip yasağı | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı CHG-064 + ilgili path/rg; değer yok | ASSESS |
| CHG-065 | Schedule workflow değişimi | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı CHG-065 + ilgili path/rg; değer yok | ASSESS |
| CHG-066 | Environment protection kuralı | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı CHG-066 + ilgili path/rg; değer yok | ASSESS |
| CHG-067 | OIDC role değişimi | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı CHG-067 + ilgili path/rg; değer yok | ASSESS |
| CHG-068 | Secret listesine ekleme süreci | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı CHG-068 + ilgili path/rg; değer yok | ASSESS |
| CHG-069 | Secret silme süreci | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı CHG-069 + ilgili path/rg; değer yok | ASSESS |
| CHG-070 | Erişim kaybı offboarding | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı CHG-070 + ilgili path/rg; değer yok | ASSESS |
| CHG-071 | Yeni collaborator onayı | ID.SC-02 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı CHG-071 + ilgili path/rg; değer yok | ASSESS |
| CHG-072 | Bot hesabı değişimi | PR.DS-02 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı CHG-072 + ilgili path/rg; değer yok | ASSESS |
| CHG-073 | App installation değişimi | GV.RR-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı CHG-073 + ilgili path/rg; değer yok | ASSESS |
| CHG-074 | Marketplace publish N/A | ID.RA-05 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı CHG-074 + ilgili path/rg; değer yok | ASSESS |
| CHG-075 | Pages publish N/A | ID.AM-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı CHG-075 + ilgili path/rg; değer yok | ASSESS |
| CHG-076 | Wiki değişim N/A | ID.RA-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı CHG-076 + ilgili path/rg; değer yok | ASSESS |
| CHG-077 | Issue template güvenlik | GV.PO-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı CHG-077 + ilgili path/rg; değer yok | ASSESS |
| CHG-078 | Discussion secret yasağı | PR.AA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı CHG-078 + ilgili path/rg; değer yok | ASSESS |
| CHG-079 | PR screenshot redaksiyon | PR.DS-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı CHG-079 + ilgili path/rg; değer yok | ASSESS |
| CHG-080 | Commit mesajı secret yasağı | PR.IR-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı CHG-080 + ilgili path/rg; değer yok | ASSESS |
| CHG-081 | Rebase vs merge politikası | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı CHG-081 + ilgili path/rg; değer yok | ASSESS |
| CHG-082 | Cherry-pick güvenlik fix | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı CHG-082 + ilgili path/rg; değer yok | ASSESS |
| CHG-083 | Backport N/A | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı CHG-083 + ilgili path/rg; değer yok | ASSESS |
| CHG-084 | Versiyon numarası VERSIONS.md | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı CHG-084 + ilgili path/rg; değer yok | ASSESS |
| CHG-085 | CHANGELOG güvenlik maddesi | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı CHG-085 + ilgili path/rg; değer yok | ASSESS |
| CHG-086 | Deprecation duyurusu | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı CHG-086 + ilgili path/rg; değer yok | ASSESS |
| CHG-087 | Acil erişim değişimi kaydı | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı CHG-087 + ilgili path/rg; değer yok | ASSESS |
| CHG-088 | CAB/hafif onay ritmi | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı CHG-088 + ilgili path/rg; değer yok | ASSESS |
| CHG-089 | Aylık expert refresh değişimi | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı CHG-089 + ilgili path/rg; değer yok | ASSESS |
| CHG-090 | Standards currency refresh | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı CHG-090 + ilgili path/rg; değer yok | ASSESS |
| CHG-091 | Threat landscape refresh | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı CHG-091 + ilgili path/rg; değer yok | ASSESS |
| CHG-092 | Skill depth DELTA | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı CHG-092 + ilgili path/rg; değer yok | ASSESS |
| CHG-093 | Matrix CSV eş zamanlı güncelleme | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı CHG-093 + ilgili path/rg; değer yok | ASSESS |
| CHG-094 | Sahipsiz dosya yasağı | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı CHG-094 + ilgili path/rg; değer yok | ASSESS |
| CHG-095 | Dosya adı istikrarı | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı CHG-095 + ilgili path/rg; değer yok | ASSESS |
| CHG-096 | Büyük PR bölme kuralı | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı CHG-096 + ilgili path/rg; değer yok | ASSESS |
| CHG-097 | Test kırılırsa merge yok | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı CHG-097 + ilgili path/rg; değer yok | ASSESS |
| CHG-098 | Ethics KALDI merge yok | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı CHG-098 + ilgili path/rg; değer yok | ASSESS |
| CHG-099 | Secret hit merge yok | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı CHG-099 + ilgili path/rg; değer yok | ASSESS |
| CHG-100 | CHG review döngüsü 021–100 | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı CHG-100 + ilgili path/rg; değer yok | ASSESS |
| TC-021 | SBOM format seçimi | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı TC-021 + ilgili path/rg; değer yok | ASSESS |
| TC-022 | SBOM kapsamı CI grafı | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı TC-022 + ilgili path/rg; değer yok | ASSESS |
| TC-023 | SBOM saklama yolu | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı TC-023 + ilgili path/rg; değer yok | ASSESS |
| TC-024 | SBOM tüketici dokümanı | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı TC-024 + ilgili path/rg; değer yok | ASSESS |
| TC-025 | Action SHA pin oranı ölçümü | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı TC-025 + ilgili path/rg; değer yok | ASSESS |
| TC-026 | Pin gap öncelik listesi | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı TC-026 + ilgili path/rg; değer yok | ASSESS |
| TC-027 | Immutable action tag yokluğu | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı TC-027 + ilgili path/rg; değer yok | ASSESS |
| TC-028 | 3. parti action allowlist taslağı | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı TC-028 + ilgili path/rg; değer yok | ASSESS |
| TC-029 | Action versiyon major sıçrama | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı TC-029 + ilgili path/rg; değer yok | ASSESS |
| TC-030 | Dependabot Actions açık | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı TC-030 + ilgili path/rg; değer yok | ASSESS |
| TC-031 | Dependabot npm grup PR'ları | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı TC-031 + ilgili path/rg; değer yok | ASSESS |
| TC-032 | SLSA seviye hedefi | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı TC-032 + ilgili path/rg; değer yok | ASSESS |
| TC-033 | Provenance build SHA bağlama | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı TC-033 + ilgili path/rg; değer yok | ASSESS |
| TC-034 | Attestation depolama | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı TC-034 + ilgili path/rg; değer yok | ASSESS |
| TC-035 | Immutable GitHub releases | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı TC-035 + ilgili path/rg; değer yok | ASSESS |
| TC-036 | Release artefact checksum | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı TC-036 + ilgili path/rg; değer yok | ASSESS |
| TC-037 | Reproducible workflow hedefi | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı TC-037 + ilgili path/rg; değer yok | ASSESS |
| TC-038 | Vendored katalog SBOM opsiyonel | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı TC-038 + ilgili path/rg; değer yok | ASSESS |
| TC-039 | Python stdlib beyanı | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı TC-039 + ilgili path/rg; değer yok | ASSESS |
| TC-040 | Hash pin scriptleri | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı TC-040 + ilgili path/rg; değer yok | ASSESS |
| TC-041 | zizmor/actionlint hedefi | ID.SC-02 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı TC-041 + ilgili path/rg; değer yok | ASSESS |
| TC-042 | Scorecard ölçüm planı | PR.DS-02 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı TC-042 + ilgili path/rg; değer yok | ASSESS |
| TC-043 | OSV tarama hedefi | GV.RR-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı TC-043 + ilgili path/rg; değer yok | ASSESS |
| TC-044 | deps.dev farkındalık | ID.RA-05 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı TC-044 + ilgili path/rg; değer yok | ASSESS |
| TC-045 | Socket.dev farkındalık | ID.AM-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı TC-045 + ilgili path/rg; değer yok | ASSESS |
| TC-046 | npm provenance farkındalık | ID.RA-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı TC-046 + ilgili path/rg; değer yok | ASSESS |
| TC-047 | Fork PR secret sızdırmazlık | GV.PO-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı TC-047 + ilgili path/rg; değer yok | ASSESS |
| TC-048 | pull_request_target kaçınma | PR.AA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı TC-048 + ilgili path/rg; değer yok | ASSESS |
| TC-049 | script injection farkındalığı | PR.DS-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı TC-049 + ilgili path/rg; değer yok | ASSESS |
| TC-050 | Untrusted checkout güvenliği | PR.IR-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı TC-050 + ilgili path/rg; değer yok | ASSESS |
| TC-051 | Cache poison farkındalığı | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı TC-051 + ilgili path/rg; değer yok | ASSESS |
| TC-052 | Artifact download güveni | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı TC-052 + ilgili path/rg; değer yok | ASSESS |
| TC-053 | Composite action şeffaflığı | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı TC-053 + ilgili path/rg; değer yok | ASSESS |
| TC-054 | Reusable workflow pin | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı TC-054 + ilgili path/rg; değer yok | ASSESS |
| TC-055 | Self-hosted runner yok teyidi | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı TC-055 + ilgili path/rg; değer yok | ASSESS |
| TC-056 | Runner label hijyeni | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı TC-056 + ilgili path/rg; değer yok | ASSESS |
| TC-057 | Image base yok beyanı | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı TC-057 + ilgili path/rg; değer yok | ASSESS |
| TC-058 | Dockerfile örnek izolasyonu | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı TC-058 + ilgili path/rg; değer yok | ASSESS |
| TC-059 | IaC module kaynak pin | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı TC-059 + ilgili path/rg; değer yok | ASSESS |
| TC-060 | Provider version constraint | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı TC-060 + ilgili path/rg; değer yok | ASSESS |
| TC-061 | Lockfile terraform ASSESS | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı TC-061 + ilgili path/rg; değer yok | ASSESS |
| TC-062 | Helm/K8s manifest imza N/A | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı TC-062 + ilgili path/rg; değer yok | ASSESS |
| TC-063 | Cosign/keyless hedef notu | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı TC-063 + ilgili path/rg; değer yok | ASSESS |
| TC-064 | Sigstore farkındalık | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı TC-064 + ilgili path/rg; değer yok | ASSESS |
| TC-065 | In-toto farkındalık | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı TC-065 + ilgili path/rg; değer yok | ASSESS |
| TC-066 | Git commit tree bütünlüğü | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı TC-066 + ilgili path/rg; değer yok | ASSESS |
| TC-067 | Signed tags hedefi | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı TC-067 + ilgili path/rg; değer yok | ASSESS |
| TC-068 | GPG anahtar envanteri | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı TC-068 + ilgili path/rg; değer yok | ASSESS |
| TC-069 | SSH signing hedefi | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı TC-069 + ilgili path/rg; değer yok | ASSESS |
| TC-070 | Merge commit doğrulanabilirliği | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı TC-070 + ilgili path/rg; değer yok | ASSESS |
| TC-071 | Subresource integrity N/A | ID.SC-02 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı TC-071 + ilgili path/rg; değer yok | ASSESS |
| TC-072 | Lockfile npm katalog | PR.DS-02 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı TC-072 + ilgili path/rg; değer yok | ASSESS |
| TC-073 | Pip hash-checking N/A | GV.RR-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı TC-073 + ilgili path/rg; değer yok | ASSESS |
| TC-074 | Go sum N/A | ID.RA-05 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı TC-074 + ilgili path/rg; değer yok | ASSESS |
| TC-075 | Rust audit N/A | ID.AM-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı TC-075 + ilgili path/rg; değer yok | ASSESS |
| TC-076 | Binary blob yasağı | ID.RA-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı TC-076 + ilgili path/rg; değer yok | ASSESS |
| TC-077 | Prebuilt tool checksum | GV.PO-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı TC-077 + ilgili path/rg; değer yok | ASSESS |
| TC-078 | Uzaktan kurulum yönlendirme yasağı | PR.AA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı TC-078 + ilgili path/rg; değer yok | ASSESS |
| TC-079 | Unpinned gist yasağı | PR.DS-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı TC-079 + ilgili path/rg; değer yok | ASSESS |
| TC-080 | Container digest pin N/A | PR.IR-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı TC-080 + ilgili path/rg; değer yok | ASSESS |
| TC-081 | Workflow permissions least | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı TC-081 + ilgili path/rg; değer yok | ASSESS |
| TC-082 | GITHUB_TOKEN write daraltma | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı TC-082 + ilgili path/rg; değer yok | ASSESS |
| TC-083 | id-token izin bilinçli | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı TC-083 + ilgili path/rg; değer yok | ASSESS |
| TC-084 | packages: write N/A | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı TC-084 + ilgili path/rg; değer yok | ASSESS |
| TC-085 | attestations izin hedefi | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı TC-085 + ilgili path/rg; değer yok | ASSESS |
| TC-086 | concurrency group | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı TC-086 + ilgili path/rg; değer yok | ASSESS |
| TC-087 | Cancel-in-progress bilinç | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı TC-087 + ilgili path/rg; değer yok | ASSESS |
| TC-088 | Matrix explosion sınırı | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı TC-088 + ilgili path/rg; değer yok | ASSESS |
| TC-089 | Third-party badge tıklama riski | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı TC-089 + ilgili path/rg; değer yok | ASSESS |
| TC-090 | GitHub App diff review | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı TC-090 + ilgili path/rg; değer yok | ASSESS |
| TC-091 | Marketplace install yasağı ajan | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı TC-091 + ilgili path/rg; değer yok | ASSESS |
| TC-092 | Untrusted skill ingest | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı TC-092 + ilgili path/rg; değer yok | ASSESS |
| TC-093 | Model ağırlığı yok | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı TC-093 + ilgili path/rg; değer yok | ASSESS |
| TC-094 | LFS pointer hijyeni | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı TC-094 + ilgili path/rg; değer yok | ASSESS |
| TC-095 | Large JSON secret tarama | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı TC-095 + ilgili path/rg; değer yok | ASSESS |
| TC-096 | CycloneDX CLI yok iddiası | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı TC-096 + ilgili path/rg; değer yok | ASSESS |
| TC-097 | Transparency log hedef notu | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı TC-097 + ilgili path/rg; değer yok | ASSESS |
| TC-098 | Consumer verify runbook | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı TC-098 + ilgili path/rg; değer yok | ASSESS |
| TC-099 | TC kanıt CSV satırı | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı TC-099 + ilgili path/rg; değer yok | ASSESS |
| TC-100 | TC review döngüsü 021–100 | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı TC-100 + ilgili path/rg; değer yok | ASSESS |
| COND-021 | MODE=ASSESS-ONLY koşulu | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı COND-021 + ilgili path/rg; değer yok | ASSESS |
| COND-022 | CANVA:ON kapalı koşulu | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı COND-022 + ilgili path/rg; değer yok | ASSESS |
| COND-023 | Secret yoksa dry-run | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı COND-023 + ilgili path/rg; değer yok | ASSESS |
| COND-024 | Ethics fail koşulu | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı COND-024 + ilgili path/rg; değer yok | ASSESS |
| COND-025 | Secret scan fail koşulu | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı COND-025 + ilgili path/rg; değer yok | ASSESS |
| COND-026 | validate.py fail koşulu | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı COND-026 + ilgili path/rg; değer yok | ASSESS |
| COND-027 | Fork PR koşulu | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı COND-027 + ilgili path/rg; değer yok | ASSESS |
| COND-028 | branch=main koruma koşulu | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı COND-028 + ilgili path/rg; değer yok | ASSESS |
| COND-029 | paths: SECURITY_* koşulu | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı COND-029 + ilgili path/rg; değer yok | ASSESS |
| COND-030 | paths: .github/workflows koşulu | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı COND-030 + ilgili path/rg; değer yok | ASSESS |
| COND-031 | Actor allowlist koşulu | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı COND-031 + ilgili path/rg; değer yok | ASSESS |
| COND-032 | Schedule vs workflow_dispatch | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı COND-032 + ilgili path/rg; değer yok | ASSESS |
| COND-033 | Environment yok koşulu | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı COND-033 + ilgili path/rg; değer yok | ASSESS |
| COND-034 | Risk skoru kaba eşik | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı COND-034 + ilgili path/rg; değer yok | ASSESS |
| COND-035 | P0 secret sızıntı koşulu | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı COND-035 + ilgili path/rg; değer yok | ASSESS |
| COND-036 | Untrusted ingest koşulu | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı COND-036 + ilgili path/rg; değer yok | ASSESS |
| COND-037 | Viral token vaadi koşulu | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı COND-037 + ilgili path/rg; değer yok | ASSESS |
| COND-038 | Sahte eklenti koşulu | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı COND-038 + ilgili path/rg; değer yok | ASSESS |
| COND-039 | 900M prompt koşulu | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı COND-039 + ilgili path/rg; değer yok | ASSESS |
| COND-040 | Expert bio uydurma koşulu | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı COND-040 + ilgili path/rg; değer yok | ASSESS |
| COND-041 | Exploit talep koşulu | ID.SC-02 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı COND-041 + ilgili path/rg; değer yok | ASSESS |
| COND-042 | Kimlik avı kiti talep koşulu | PR.DS-02 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı COND-042 + ilgili path/rg; değer yok | ASSESS |
| COND-043 | C2/malware dil koşulu | GV.RR-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı COND-043 + ilgili path/rg; değer yok | ASSESS |
| COND-044 | Kabuğa yönlendirmeli indirme tarif koşulu | ID.RA-05 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı COND-044 + ilgili path/rg; değer yok | ASSESS |
| COND-045 | rm -rf / koşulu | ID.AM-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı COND-045 + ilgili path/rg; değer yok | ASSESS |
| COND-046 | eval( koşulu | ID.RA-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı COND-046 + ilgili path/rg; değer yok | ASSESS |
| COND-047 | base64|sh koşulu | GV.PO-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı COND-047 + ilgili path/rg; değer yok | ASSESS |
| COND-048 | Yetki yükseltme saldırı tarifi koşulu | PR.AA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı COND-048 + ilgili path/rg; değer yok | ASSESS |
| COND-049 | Kimlik doldurma betiği talep koşulu | PR.DS-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı COND-049 + ilgili path/rg; değer yok | ASSESS |
| COND-050 | Kimlik doğrulama atlama yükü talep koşulu | PR.IR-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı COND-050 + ilgili path/rg; değer yok | ASSESS |
| COND-051 | Rate-limit aşım koşulu | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı COND-051 + ilgili path/rg; değer yok | ASSESS |
| COND-052 | Quota yoksa skip | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı COND-052 + ilgili path/rg; değer yok | ASSESS |
| COND-053 | Nightly pencere koşulu | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı COND-053 + ilgili path/rg; değer yok | ASSESS |
| COND-054 | Disk/büyük dosya koşulu | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı COND-054 + ilgili path/rg; değer yok | ASSESS |
| COND-055 | LFS beklenmedik koşulu | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı COND-055 + ilgili path/rg; değer yok | ASSESS |
| COND-056 | Submodule ekleme koşulu | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı COND-056 + ilgili path/rg; değer yok | ASSESS |
| COND-057 | Force push koşulu | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı COND-057 + ilgili path/rg; değer yok | ASSESS |
| COND-058 | Skip-ci koşulu | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı COND-058 + ilgili path/rg; değer yok | ASSESS |
| COND-059 | Dependabot minor vs major | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı COND-059 + ilgili path/rg; değer yok | ASSESS |
| COND-060 | Action tag vs SHA koşulu | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı COND-060 + ilgili path/rg; değer yok | ASSESS |
| COND-061 | permissions: write koşulu | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı COND-061 + ilgili path/rg; değer yok | ASSESS |
| COND-062 | id-token: write koşulu | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı COND-062 + ilgili path/rg; değer yok | ASSESS |
| COND-063 | pull_request_target koşulu | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı COND-063 + ilgili path/rg; değer yok | ASSESS |
| COND-064 | Self-hosted runner koşulu | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı COND-064 + ilgili path/rg; değer yok | ASSESS |
| COND-065 | Privileged k8s koşulu | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı COND-065 + ilgili path/rg; değer yok | ASSESS |
| COND-066 | Public secret koşulu | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı COND-066 + ilgili path/rg; değer yok | ASSESS |
| COND-067 | Chat'e yapıştırılan key koşulu | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı COND-067 + ilgili path/rg; değer yok | ASSESS |
| COND-068 | MCP enable koşulu | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı COND-068 + ilgili path/rg; değer yok | ASSESS |
| COND-069 | Canva OAuth koşulu | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı COND-069 + ilgili path/rg; değer yok | ASSESS |
| COND-070 | Agency merge koşulu | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı COND-070 + ilgili path/rg; değer yok | ASSESS |
| COND-071 | LATOS restore koşulu | ID.SC-02 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı COND-071 + ilgili path/rg; değer yok | ASSESS |
| COND-072 | Parallel agent silme koşulu | PR.DS-02 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı COND-072 + ilgili path/rg; değer yok | ASSESS |
| COND-073 | PR #34 açık bırakma | GV.RR-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı COND-073 + ilgili path/rg; değer yok | ASSESS |
| COND-074 | GHA pin uygulama koşulu | ID.RA-05 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı COND-074 + ilgili path/rg; değer yok | ASSESS |
| COND-075 | Compliance pack yok koşulu | ID.AM-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı COND-075 + ilgili path/rg; değer yok | ASSESS |
| COND-076 | IR playbook yok koşulu | ID.RA-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı COND-076 + ilgili path/rg; değer yok | ASSESS |
| COND-077 | Skill 20k eksik koşulu | GV.PO-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı COND-077 + ilgili path/rg; değer yok | ASSESS |
| COND-078 | Kontrol 600 eksik koşulu | PR.AA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı COND-078 + ilgili path/rg; değer yok | ASSESS |
| COND-079 | N/A kapsam koşulu | PR.DS-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı COND-079 + ilgili path/rg; değer yok | ASSESS |
| COND-080 | Waivers süre koşulu | PR.IR-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı COND-080 + ilgili path/rg; değer yok | ASSESS |
| COND-081 | UTC damga koşulu | PR.PS-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı COND-081 + ilgili path/rg; değer yok | ASSESS |
| COND-082 | AUDIT satırı koşulu | DE.CM-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı COND-082 + ilgili path/rg; değer yok | ASSESS |
| COND-083 | BILGI_TABANI satırı koşulu | RS.MA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı COND-083 + ilgili path/rg; değer yok | ASSESS |
| COND-084 | STATE güncelleme koşulu | RC.RP-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı COND-084 + ilgili path/rg; değer yok | ASSESS |
| COND-085 | Matrix CSV=katalog koşulu | GV.OV-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı COND-085 + ilgili path/rg; değer yok | ASSESS |
| COND-086 | Türkçe teslim koşulu | ID.SC-02 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı COND-086 + ilgili path/rg; değer yok | ASSESS |
| COND-087 | Kanıt path koşulu | PR.DS-02 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı COND-087 + ilgili path/rg; değer yok | ASSESS |
| COND-088 | Resmi URL koşulu | GV.RR-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı COND-088 + ilgili path/rg; değer yok | ASSESS |
| COND-089 | Star count şişirme koşulu | ID.RA-05 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı COND-089 + ilgili path/rg; değer yok | ASSESS |
| COND-090 | Bedava 1,6B token koşulu | ID.AM-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı COND-090 + ilgili path/rg; değer yok | ASSESS |
| COND-091 | OmniRoute iddia koşulu | ID.RA-01 | AC-3 SI-4 | A.5.9 A.8.9 | CIS-3 | A02 | ASSESS: katalog satırı COND-091 + ilgili path/rg; değer yok | ASSESS |
| COND-092 | İç müşteri verisi koşulu | GV.PO-01 | SC-7 SA-12 | A.5.15 A.8.12 | CIS-4 | A04 | ASSESS: katalog satırı COND-092 + ilgili path/rg; değer yok | ASSESS |
| COND-093 | Medikal claim koşulu | PR.AA-01 | SC-28 IR-4 | A.5.21 A.8.20 | CIS-5 | A07 | ASSESS: katalog satırı COND-093 + ilgili path/rg; değer yok | ASSESS |
| COND-094 | Rakip adı koşulu | PR.DS-01 | SI-4 CA-2 | A.8.9 A.8.24 | CIS-6 | A08 | ASSESS: katalog satırı COND-094 + ilgili path/rg; değer yok | ASSESS |
| COND-095 | Süperlatif koşulu | PR.IR-01 | SA-12 PL-2 | A.8.12 A.8.32 | CIS-8 | A09 | ASSESS: katalog satırı COND-095 + ilgili path/rg; değer yok | ASSESS |
| COND-096 | Marka TBD koşulu | PR.PS-01 | IR-4 AU-9 | A.8.20 A.5.24 | CIS-12 | A10 | ASSESS: katalog satırı COND-096 + ilgili path/rg; değer yok | ASSESS |
| COND-097 | BRIEF-ONLY teslim koşulu | DE.CM-01 | CA-2 CM-8 | A.8.24 A.5.1 | CIS-14 | ASVS-V1 | ASSESS: katalog satırı COND-097 + ilgili path/rg; değer yok | ASSESS |
| COND-098 | critic-copy henüz PASS değil | RS.MA-01 | PL-2 AC-3 | A.8.32 A.5.9 | CIS-15 | ASVS-V2 | ASSESS: katalog satırı COND-098 + ilgili path/rg; değer yok | ASSESS |
| COND-099 | COND kanıt CSV | RC.RP-01 | AU-9 SC-7 | A.5.24 A.5.15 | CIS-16 | Policy | ASSESS: katalog satırı COND-099 + ilgili path/rg; değer yok | ASSESS |
| COND-100 | COND review döngüsü 021–100 | GV.OV-01 | CM-8 SC-28 | A.5.1 A.5.21 | CIS-1 | A01 | ASSESS: katalog satırı COND-100 + ilgili path/rg; değer yok | ASSESS |
