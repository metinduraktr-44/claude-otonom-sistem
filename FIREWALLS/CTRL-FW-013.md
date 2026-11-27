# CTRL-FW-013 — Bulut hizmeti kullanım envanteri (GitHub/GHA/LLM)

```yaml
id: CTRL-FW-013
ad: Bulut hizmeti kullanım envanteri (GitHub/GHA/LLM)
açıklama: Holding OS ‘cloud’ yüzeyi: GitHub, Actions, isteğe bağlı Gemini/OpenRouter; müşteri SaaS yok varsayımı.
NIST_CSF: ['Identify', 'Protect']
800-53: ['SA-9', 'CA-3']
ISO27001: ['A.5.23']
CIS: ['CIS-15']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: SECURITY_CONTEXT/inventory.md + trust-boundaries.md cloud satırları.
savunma_gerekçesi: Paylaşılan sorumluluk ve üçüncü taraf işlemci sınırı netleşir.
```

## Açıklama
Holding OS ‘cloud’ yüzeyi: GitHub, Actions, isteğe bağlı Gemini/OpenRouter; müşteri SaaS yok varsayımı.

## Doğrulama (ASSESS-ONLY)
- SECURITY_CONTEXT/inventory.md + trust-boundaries.md cloud satırları.

## Savunma gerekçesi
Paylaşılan sorumluluk ve üçüncü taraf işlemci sınırı netleşir.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
