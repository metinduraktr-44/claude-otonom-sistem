# ORG/ROLES — CISO & güvenlik unvanları (seed)

> Uydurma kişi yok; unvan/RACI şablonu. MODE=`ASSESS-ONLY`.

| Rol ID | Unvan | R | A | C | I | Birincil çıktı |
|--------|-------|---|---|---|---|----------------|
| ROLE-CISO | Chief Information Security Officer | strateji | risk kabulü | Board | Tüm org | MODE / politika onayı |
| ROLE-SEC-ARCH | Security Architect | kontrol tasarımı | mimari | Eng | CISO | LAYERS/FIREWALLS/… kartları |
| ROLE-COMP | Compliance Lead | framework map | audit takvimi | Legal | CISO | COMPLIANCE/ paket |
| ROLE-IR | Incident Response Lead | playbook | severity | SecEng | Exec | IR playbook |
| ROLE-APPSEC | Application Security Lead | kod/CI gate | AppSec backlog | Dev | CISO | secret/ethics gates |
| ROLE-PRIV | Privacy Engineer | PII minimizasyon | DPIA ASSESS | Legal | CISO | data-classes |
| ROLE-IAM | IAM Lead | erişim matrisi | break-glass | IT | CISO | ORG access reviews |
| ROLE-DET | Detection Engineer | detection map | alert kalitesi | IR | CISO | D3FEND/Sigma notları |
| ROLE-ETHICS | Ethics Guardian | dual-use refuse | ethics policy | All agents | CISO | ethics_check |
| ROLE-CHANGE | Change Owner | CM kaydı | IMPLEMENT scope | Arch | CISO | CHANGE/ + STATE |

## Dosyalar
- `ROLE-CISO.md` … tek sayfa görev özeti
- RACI özeti: bu tablo

## Holding bağ
Creative Agency unvanları ayrı (Canva OS). Çakışmada **Ethics Guardian kazanır** (`CTRL-CD-015`).

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
