# CTRL-ENC-004 — Kripto çeviklik — algoritma envanteri

```yaml
id: CTRL-ENC-004
ad: Kripto çeviklik — algoritma envanteri
açıklama: Kullanılan/planlanan algoritmalar listesi; zayıf alg. yasak listesi.
NIST_CSF: ['Protect', 'Identify']
800-53: ['SC-13']
ISO27001: ['A.8.24']
CIS: ['CIS-3']
OWASP: ['A02:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: crypto-agility skill references.
savunma_gerekçesi: Algoritma kırıldığında hızlı geçiş.
```

## Açıklama
Kullanılan/planlanan algoritmalar listesi; zayıf alg. yasak listesi.

## Doğrulama (ASSESS-ONLY)
- crypto-agility skill references.

## Savunma gerekçesi
Algoritma kırıldığında hızlı geçiş.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
