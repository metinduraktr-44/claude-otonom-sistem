# CTRL-FW-001 — Egress allowlist politikası (doküman)

```yaml
id: CTRL-FW-001
ad: Egress allowlist politikası (doküman)
açıklama: Harici API çağrıları için izinli domain listesi (docs düzeyinde ASSESS).
NIST_CSF: ['Protect']
800-53: ['SC-7']
ISO27001: ['A.8.20']
CIS: ['CIS-12']
OWASP: ['A05:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: SECURITY_CONTEXT/trust-boundaries.md egress bölümü.
savunma_gerekçesi: Beklenmeyen veri sızıntısı / C2 benzeri çıkışı engelleme niyeti (detection map).
```

## Açıklama
Harici API çağrıları için izinli domain listesi (docs düzeyinde ASSESS).

## Doğrulama (ASSESS-ONLY)
- SECURITY_CONTEXT/trust-boundaries.md egress bölümü.

## Savunma gerekçesi
Beklenmeyen veri sızıntısı / C2 benzeri çıkışı engelleme niyeti (detection map).

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
