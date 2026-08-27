# CTRL-L-008 — Yanıt katmanı — IR playbook iskeleti

```yaml
id: CTRL-L-008
ad: Yanıt katmanı — IR playbook iskeleti
açıklama: Olay sınıflandırma, iletişim, containment ASSESS-ONLY adımları.
NIST_CSF: ['Respond']
800-53: ['IR-4', 'IR-8']
ISO27001: ['A.5.24', 'A.5.26']
CIS: ['CIS-17']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: .cursor/skills/incident-response/references/playbook-skeleton.md.
savunma_gerekçesi: Olay anında karar gecikmesini azaltır.
```

## Açıklama
Olay sınıflandırma, iletişim, containment ASSESS-ONLY adımları.

## Doğrulama (ASSESS-ONLY)
- .cursor/skills/incident-response/references/playbook-skeleton.md.

## Savunma gerekçesi
Olay anında karar gecikmesini azaltır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
