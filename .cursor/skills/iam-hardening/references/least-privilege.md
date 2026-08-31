# Least privilege (defense)

## İnsan
- Ayrıcalıklı roller ORG/ROLES
- Break-glass: vault:// pointer (değer yok)
- MFA beklentisi org politikası (ASSESS)

## İş yükü
- GHA `permissions:` okuma varsayılan
- Bot yalnız bilinen path’lere yazar
- LLM/Canva token’ları ayrı secret adları

## Kontroller
CTRL-SAMPLE-ACCESS, CTRL-L-002, ROLE-IAM

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
