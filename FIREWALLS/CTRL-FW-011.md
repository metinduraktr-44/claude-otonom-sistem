# CTRL-FW-011 — TLS zorunluluğu (harici)

```yaml
id: CTRL-FW-011
ad: TLS zorunluluğu (harici)
açıklama: HTTPS-only harici çağrılar; cleartext yasak.
NIST_CSF: ['Protect']
800-53: ['SC-8', 'SC-13']
ISO27001: ['A.8.24']
CIS: ['CIS-3']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Client kodunda http:// yok tarama (exclude katalog).
savunma_gerekçesi: Transit gizlilik ve bütünlük.
```

## Açıklama
HTTPS-only harici çağrılar; cleartext yasak.

## Doğrulama (ASSESS-ONLY)
- Client kodunda http:// yok tarama (exclude katalog).

## Savunma gerekçesi
Transit gizlilik ve bütünlük.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
