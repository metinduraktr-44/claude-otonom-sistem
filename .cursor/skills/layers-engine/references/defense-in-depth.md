# Defense-in-depth layers

## Katman modeli (Holding uyarlaması)

| Katman | Odak | Starter kontroller |
|--------|------|--------------------|
| L0 Policy | Politika / ethics | CTRL-L-001, L-011, L-013 |
| L1 Identity | IAM / least privilege | CTRL-L-002, CTRL-SAMPLE-ACCESS |
| L2 Network | Trust boundaries / FW | CTRL-L-003 + FIREWALLS/* |
| L3 Host | Runner/OS ASSESS | CTRL-L-004 |
| L4 App | Input validation / CI | CTRL-L-005, CHANGE gates |
| L5 Data | Sınıflandırma / crypto | CTRL-L-006, ENCRYPTION/* |
| L6 Detect/Respond | Log, IR, recover | CTRL-L-007…L-009, L-015 |

## İş akışı
1. `SECURITY_CONTEXT/` oku
2. Gap: `SECURITY_MATRIX/GAP-TEMPLATE.md`
3. Kart üret: alan sözleşmesi `compliance-mapper/references/nist-csf-control-fields.md` (+ TR alanlar: ad, açıklama, doğrulama_yöntemi, savunma_gerekçesi)
4. matrix.md güncelle

## Anti-pattern
Tek “silver bullet” kontrol; filler metinle 20k hedefi; exploit PoC.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
