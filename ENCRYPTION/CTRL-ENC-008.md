# CTRL-ENC-008 — Özel anahtar yok (repo)

```yaml
id: CTRL-ENC-008
ad: Özel anahtar yok (repo)
açıklama: BEGIN PRIVATE KEY blokları yasak; scanner flag.
NIST_CSF: ['Protect']
800-53: ['IA-5', 'SC-12']
ISO27001: ['A.8.24']
CIS: ['CIS-3']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: secret_scan private_key_block.
savunma_gerekçesi: Anahtar sızıntısı felaketini engeller.
```

## Açıklama
BEGIN PRIVATE KEY blokları yasak; scanner flag.

## Doğrulama (ASSESS-ONLY)
- secret_scan private_key_block.

## Savunma gerekçesi
Anahtar sızıntısı felaketini engeller.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
