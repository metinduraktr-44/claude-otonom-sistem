# SECURITY_MATRIX — Crosswalk (tranche 001–020 × 6)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**MODE:** ASSESS-ONLY · **ts:** 2026-08-27T12:54:55Z · **rows:** 120 / 600

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

CSV: `matrix-001-020.csv`
