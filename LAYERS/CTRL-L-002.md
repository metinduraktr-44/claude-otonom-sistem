# CTRL-L-002 — Kimlik katmanı — ayrıcalıklı erişim envanteri

```yaml
id: CTRL-L-002
ad: Kimlik katmanı — ayrıcalıklı erişim envanteri
açıklama: İnsan ve iş yükü kimliklerinin ayrıcalık sınıflandırması; break-glass vault:// referansı.
NIST_CSF: ['Protect']
800-53: ['AC-2', 'AC-6']
ISO27001: ['A.5.15', 'A.8.2']
CIS: ['CIS-5', 'CIS-6']
OWASP: ['A01:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: Rol matrisi ORG/ROLES + erişim inceleme takvimi CALENDAR/.
savunma_gerekçesi: Yetkisiz yükseltme tespitini kolaylaştırır; least privilege için ön koşul.
```

## Açıklama
İnsan ve iş yükü kimliklerinin ayrıcalık sınıflandırması; break-glass vault:// referansı.

## Doğrulama (ASSESS-ONLY)
- Rol matrisi ORG/ROLES + erişim inceleme takvimi CALENDAR/.

## Savunma gerekçesi
Yetkisiz yükseltme tespitini kolaylaştırır; least privilege için ön koşul.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
