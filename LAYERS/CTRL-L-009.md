# CTRL-L-009 — Kurtarma katmanı — yedek/geri alma planı

```yaml
id: CTRL-L-009
ad: Kurtarma katmanı — yedek/geri alma planı
açıklama: Git history + branch koruması; kritik docs için snapshot ARCHIVE/.
NIST_CSF: ['Recover']
800-53: ['CP-9', 'CP-10']
ISO27001: ['A.8.13']
CIS: ['CIS-11']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: ARCHIVE/ ve branch protection ASSESS notu.
savunma_gerekçesi: Yanlış commit/sızıntı sonrası hızlı geri dönüş.
```

## Açıklama
Git history + branch koruması; kritik docs için snapshot ARCHIVE/.

## Doğrulama (ASSESS-ONLY)
- ARCHIVE/ ve branch protection ASSESS notu.

## Savunma gerekçesi
Yanlış commit/sızıntı sonrası hızlı geri dönüş.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
