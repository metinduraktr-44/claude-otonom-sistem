# ROLE-CHANGE — Change Owner

```yaml
id: ROLE-CHANGE
ad: Change Owner
status: seed
mode: ASSESS-ONLY
```

## Görev
CM, IMPLEMENT kapsamı

## Kanıt / çıktı
- CHANGE/ · CTRL-CH-*

## Sınırlar
- Kişi uydurma / ranking claim YASAK.
- Secret değer yok; yalnızca ${VAR} / vault:// / <REDACTED>.
- ATT&CK yalnız detection eşlemesi.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
