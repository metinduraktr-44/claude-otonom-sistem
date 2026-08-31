# CTRL-ENC-010 — Disk şifreleme (host ASSESS)

```yaml
id: CTRL-ENC-010
ad: Disk şifreleme (host ASSESS)
açıklama: Geliştirici/CI disk FDE beklentisi (org politikası).
NIST_CSF: ['Protect']
800-53: ['SC-28']
ISO27001: ['A.8.1']
CIS: ['CIS-3']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: ORG politikası pointer.
savunma_gerekçesi: Cihaz kaybında veri koruması.
```

## Açıklama
Geliştirici/CI disk FDE beklentisi (org politikası).

## Doğrulama (ASSESS-ONLY)
- ORG politikası pointer.

## Savunma gerekçesi
Cihaz kaybında veri koruması.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
