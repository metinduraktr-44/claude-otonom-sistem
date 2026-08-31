# ROLE-IAM — IAM Lead

```yaml
id: ROLE-IAM
ad: IAM Lead
status: seed
mode: ASSESS-ONLY
```

## Görev
Least privilege, erişim gözden geçirme

## Kanıt / çıktı
- CTRL-SAMPLE-ACCESS · CTRL-L-002

## Sınırlar
- Kişi uydurma / ranking claim YASAK.
- Secret değer yok; yalnızca ${VAR} / vault:// / <REDACTED>.
- ATT&CK yalnız detection eşlemesi.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
