# Holding STRIDE Map (Defense)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

Kaynak bağlam: `SECURITY_CONTEXT/attack-surface.md` · `SECURITY_RESEARCH/threat-landscape.md`

## Varlıklar
| Varlık | Trust zone |
|--------|------------|
| GitHub Actions runners | CI |
| `scripts/*.py` generators | Dev workstation / CI |
| LLM API outbound | External |
| `data/`, `uretim/`, `katalog/` içerik | Content |
| Terraform state (observability) | Infra |
| AUDIT_LOG / REPORTS | Audit |

## STRIDE → kontrol

| Tehdit | Örnek (sınıf) | Mitigasyon motoru | NIST CSF |
|--------|---------------|-------------------|----------|
| Spoofing | Sahte Action sürümü | TC pin SHA | PR.AA |
| Tampering | Workflow dosya değişimi | CHANGE + branch protect | PR.DS |
| Repudiation | İzlenmeyen LLM yazımı | AUDIT_LOG + LAY logging | DE.CM |
| Info Disclosure | Secret in log | secret-hygiene | PR.DS |
| DoS | Workflow spam | COND rate ASSESS | PR.IR |
| EoP | Geniş token | IAM / COND | PR.AA |

## Öncelik (holding)
P0 secret + Action pin · P1 permissions/Terraform · P2 katalog izolasyonu

## Referans yöntem
Adam Shostack / STRIDE (kamuya açık yöntem); OWASP threat modeling — savunma çıktısı.  
ASVS 5.0 ilgili doğrulama maddeleri checklist olarak kullanılır (tam metin kopyalanmaz).
