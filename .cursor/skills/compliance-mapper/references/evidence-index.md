# Evidence Index Pattern

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

## Kanıt tipi
| Tip | Örnek artefakt | Saklama |
|-----|----------------|---------|
| Config | workflow `permissions:` snippet | git |
| Scan | `REPORTS/secret_scan_*.json` (redacted) | REPORTS |
| Doc | inventory / attack-surface | SECURITY_CONTEXT |
| Process | AUDIT_LOG.jsonl satırı | root |
| Control | `LAYERS/controls-001-020.md` satırı | motor klasör |

## Kanıt kaydı şablonu
```
control_id: LAY-001
claim: Defense-in-depth inventory exists
evidence: SECURITY_CONTEXT/inventory.md
verify: file exists + last_updated
result: PASS|GAP
```

## Audit hazırlık
- Secret değeri kanıt DEĞİLDİR.
- Screenshot yerine path + hash (SHA256 of file) tercih.
- Üçüncü parti sertifika PDF’leri `ARCHIVE/` (sonra).
