# CTRL-L-004 — Host katmanı — runner/OS sertleştirme kontrol listesi

```yaml
id: CTRL-L-004
ad: Host katmanı — runner/OS sertleştirme kontrol listesi
açıklama: CI/CD runner ve geliştirme VM’leri için ASSESS-ONLY sertleştirme checklist’i.
NIST_CSF: ['Protect']
800-53: ['CM-6', 'SI-2']
ISO27001: ['A.8.9']
CIS: ['CIS-4', 'CIS-10']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: ASSESSMENTS/host-hardening.md veya gap satırı.
savunma_gerekçesi: Tedarik zinciri ve runner kaçırma yüzeyini daraltır.
```

## Açıklama
CI/CD runner ve geliştirme VM’leri için ASSESS-ONLY sertleştirme checklist’i.

## Doğrulama (ASSESS-ONLY)
- ASSESSMENTS/host-hardening.md veya gap satırı.

## Savunma gerekçesi
Tedarik zinciri ve runner kaçırma yüzeyini daraltır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
