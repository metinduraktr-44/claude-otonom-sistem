# CTRL-CD-006 — Koşullu: secret KALDI → commit engeli

```yaml
id: CTRL-CD-006
ad: Koşullu: secret KALDI → commit engeli
açıklama: secret_scan bulgusu → düzeltmeden ilerleme yok.
NIST_CSF: ['Protect']
800-53: ['IA-5', 'SI-4']
ISO27001: ['A.8.24']
CIS: ['CIS-3']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Hook + CLI exit 1.
savunma_gerekçesi: Credential sızıntısını durdurur.
```

## Açıklama
secret_scan bulgusu → düzeltmeden ilerleme yok.

## Doğrulama (ASSESS-ONLY)
- Hook + CLI exit 1.

## Savunma gerekçesi
Credential sızıntısını durdurur.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
