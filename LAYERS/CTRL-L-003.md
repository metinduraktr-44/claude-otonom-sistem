# CTRL-L-003 — Ağ katmanı — güven sınırları diyagramı

```yaml
id: CTRL-L-003
ad: Ağ katmanı — güven sınırları diyagramı
açıklama: Trust boundary’lerin dokümante edilmesi (CI runner, GitHub, yerel agent, harici API).
NIST_CSF: ['Identify', 'Protect']
800-53: ['SC-7', 'CA-3']
ISO27001: ['A.8.20', 'A.8.22']
CIS: ['CIS-12']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: SECURITY_CONTEXT/trust-boundaries.md güncelliği.
savunma_gerekçesi: Segmentasyon ve firewall kurallarının hedefi netleşir.
```

## Açıklama
Trust boundary’lerin dokümante edilmesi (CI runner, GitHub, yerel agent, harici API).

## Doğrulama (ASSESS-ONLY)
- SECURITY_CONTEXT/trust-boundaries.md güncelliği.

## Savunma gerekçesi
Segmentasyon ve firewall kurallarının hedefi netleşir.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
