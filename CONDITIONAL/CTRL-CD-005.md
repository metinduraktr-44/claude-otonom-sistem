# CTRL-CD-005 — Koşullu: ethics KALDI → dur

```yaml
id: CTRL-CD-005
ad: Koşullu: ethics KALDI → dur
açıklama: ethics_check KALDI ise üretim durur / reddeder.
NIST_CSF: ['Govern', 'Protect']
800-53: ['SI-4', 'IR-4']
ISO27001: ['A.5.1']
CIS: ['CIS-14']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: 05-ethics-guardrail + /etik-denetim.
savunma_gerekçesi: Zararlı içeriğin yayılmasını keser.
```

## Açıklama
ethics_check KALDI ise üretim durur / reddeder.

## Doğrulama (ASSESS-ONLY)
- 05-ethics-guardrail + /etik-denetim.

## Savunma gerekçesi
Zararlı içeriğin yayılmasını keser.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
