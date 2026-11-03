# CTRL-ENC-013 — Çıktı sızıntı önleme — log/rapor redaksiyonu

```yaml
id: CTRL-ENC-013
ad: Çıktı sızıntı önleme — log/rapor redaksiyonu
açıklama: AUDIT_LOG, REPORTS, gunluk md: secret değer yok; konum+tip. LLM çıktısı redakte.
NIST_CSF: ['Protect', 'Detect']
800-53: ['SI-12', 'AU-9']
ISO27001: ['A.8.12', 'A.8.11']
CIS: ['CIS-3', 'CIS-8']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: secret_scan REPORTS; holding_report dry-run; chat secret yasağı.
savunma_gerekçesi: DLP analogu bu runtime’da log ve agent dökümü.
```

## Açıklama
AUDIT_LOG, REPORTS, gunluk md: secret değer yok; konum+tip. LLM çıktısı redakte.

## Doğrulama (ASSESS-ONLY)
- secret_scan REPORTS; holding_report dry-run; chat secret yasağı.

## Savunma gerekçesi
DLP analogu bu runtime’da log ve agent dökümü.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
