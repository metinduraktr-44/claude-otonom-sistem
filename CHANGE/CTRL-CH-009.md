# CTRL-CH-009 — Doküman vs kod ayrımı

```yaml
id: CTRL-CH-009
ad: Doküman vs kod ayrımı
açıklama: FAZ genişlemesi docs/controls; runtime scripts ayrı PR tercihi.
NIST_CSF: ['Govern']
800-53: ['CM-4']
ISO27001: ['A.5.8']
CIS: ['CIS-1']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: PR kapsam notu.
savunma_gerekçesi: İnceleme yükünü yönetilebilir tutar.
```

## Açıklama
FAZ genişlemesi docs/controls; runtime scripts ayrı PR tercihi.

## Doğrulama (ASSESS-ONLY)
- PR kapsam notu.

## Savunma gerekçesi
İnceleme yükünü yönetilebilir tutar.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
