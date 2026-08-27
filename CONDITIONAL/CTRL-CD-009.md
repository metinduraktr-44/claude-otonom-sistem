# CTRL-CD-009 — Koşullu: IR severity ≥ yüksek → exec bilgilendirme

```yaml
id: CTRL-CD-009
ad: Koşullu: IR severity ≥ yüksek → exec bilgilendirme
açıklama: Playbook’ta severity eşiği ve iletişim listesi.
NIST_CSF: ['Respond']
800-53: ['IR-4', 'IR-6']
ISO27001: ['A.5.24']
CIS: ['CIS-17']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: incident-response playbook.
savunma_gerekçesi: Eskalasyon gecikmesini azaltır.
```

## Açıklama
Playbook’ta severity eşiği ve iletişim listesi.

## Doğrulama (ASSESS-ONLY)
- incident-response playbook.

## Savunma gerekçesi
Eskalasyon gecikmesini azaltır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
