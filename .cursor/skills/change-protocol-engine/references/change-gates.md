# Change protocol (defense CM)

## MODE makinesi
```
ASSESS-ONLY  --(explicit scope + CISO/Change Owner)-->  IMPLEMENT
IMPLEMENT    --(done / abort)-->  ASSESS-ONLY + STATE stamp
```

## Zorunlu kapılar
| Gate | Araç | Fail davranışı |
|------|------|----------------|
| Yapı | `validate.py` | CI red |
| Secret | `secret_scan.py` | CLI exit 1 |
| Ethics | `ethics_check.py` | CLI exit 1 |
| Spec | `spec_validate.py` | self-test / PR |

## Değişiklik sınıfları
1. **Docs/controls** — FAZ genişlemesi; düşük risk
2. **Scanner/hooks** — AppSec Lead C
3. **Workflow** — Change Owner + pin review
4. **Live MCP/Canva** — kullanıcı flag olmadan YASAK

## Rollback
- Tercih: `git revert` (force-push yok)
- Bot dosyaları: `git restore AUDIT_LOG.jsonl BILGI_TABANI.md …`

## Kartlar
`CHANGE/CTRL-CH-*.md`

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
