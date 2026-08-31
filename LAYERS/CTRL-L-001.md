# CTRL-L-001 — Politika katmanı — güvenlik politikası envanteri

```yaml
id: CTRL-L-001
ad: Politika katmanı — güvenlik politikası envanteri
açıklama: Yazılı güvenlik politikalarının (kabul edilebilir kullanım, erişim, olay) envanteri ve sahipliği.
NIST_CSF: ['Govern', 'Identify']
800-53: ['PL-1', 'PL-2']
ISO27001: ['A.5.1', 'A.5.2']
CIS: ['CIS-1']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Politika listesi + son gözden geçirme tarihi; POLICY/ veya docs/ altında pointer.
savunma_gerekçesi: Katmanlı savunmanın L0 temeli; ölçülebilir politika olmadan kontrol boşluğu kapanmaz.
```

## Açıklama
Yazılı güvenlik politikalarının (kabul edilebilir kullanım, erişim, olay) envanteri ve sahipliği.

## Doğrulama (ASSESS-ONLY)
- Politika listesi + son gözden geçirme tarihi; POLICY/ veya docs/ altında pointer.

## Savunma gerekçesi
Katmanlı savunmanın L0 temeli; ölçülebilir politika olmadan kontrol boşluğu kapanmaz.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
