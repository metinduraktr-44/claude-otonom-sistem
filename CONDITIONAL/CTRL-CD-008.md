# CTRL-CD-008 — Koşullu: parallel agent izolasyonu

```yaml
id: CTRL-CD-008
ad: Koşullu: parallel agent izolasyonu
açıklama: Canva senaryoları SCENARIOS/{urun}/{n}/ altında.
NIST_CSF: ['Protect']
800-53: ['SC-2', 'AC-4']
ISO27001: ['A.8.22']
CIS: ['CIS-12']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: SCENARIOS/ yapı.
savunma_gerekçesi: Çapraz kontaminasyon yok.
```

## Açıklama
Canva senaryoları SCENARIOS/{urun}/{n}/ altında.

## Doğrulama (ASSESS-ONLY)
- SCENARIOS/ yapı.

## Savunma gerekçesi
Çapraz kontaminasyon yok.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
