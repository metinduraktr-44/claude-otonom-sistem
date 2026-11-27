# CTRL-FW-014 — Doküman/agent URL hijyeni (web filtering analog)

```yaml
id: CTRL-FW-014
ad: Doküman/agent URL hijyeni (web filtering analog)
açıklama: Agent fetch ve araştırma URL’leri resmi standart/docs allowlist kültürü; rastgele paste/kurulum yasağı.
NIST_CSF: ['Protect']
800-53: ['SI-3', 'SC-7']
ISO27001: ['A.8.23', 'A.5.7']
CIS: ['CIS-7', 'CIS-9']
OWASP: ['A10:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: SECURITY_RESEARCH kaynak URL’leri + ethics_check tehlikeli-indir pattern.
savunma_gerekçesi: Sosyal-medya ‘setup’ ve rastgele script yüzeyi bu OS’te birincil web riski.
```

## Açıklama
Agent fetch ve araştırma URL’leri resmi standart/docs allowlist kültürü; rastgele paste/kurulum yasağı.

## Doğrulama (ASSESS-ONLY)
- SECURITY_RESEARCH kaynak URL’leri + ethics_check tehlikeli-indir pattern.

## Savunma gerekçesi
Sosyal-medya ‘setup’ ve rastgele script yüzeyi bu OS’te birincil web riski.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
