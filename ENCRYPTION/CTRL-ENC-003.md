# CTRL-ENC-003 — Anahtar yaşam döngüsü (doküman)

```yaml
id: CTRL-ENC-003
ad: Anahtar yaşam döngüsü (doküman)
açıklama: Rotasyon, sahiplik, iptal prosedürü — vault:// pointer.
NIST_CSF: ['Protect']
800-53: ['SC-12', 'SC-17']
ISO27001: ['A.8.24']
CIS: ['CIS-3']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: ENCRYPTION/key-lifecycle.md (bu kontrol + README pointer).
savunma_gerekçesi: Eski anahtarların sürünmesini engeller.
```

## Açıklama
Rotasyon, sahiplik, iptal prosedürü — vault:// pointer.

## Doğrulama (ASSESS-ONLY)
- ENCRYPTION/key-lifecycle.md (bu kontrol + README pointer).

## Savunma gerekçesi
Eski anahtarların sürünmesini engeller.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
