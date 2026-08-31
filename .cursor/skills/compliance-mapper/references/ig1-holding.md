# CIS IG1 — Holding Uygunluk Seed

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

CIS Controls v8.1 IG1 (temel hijyen) holding otomasyonuna kabaca:

| CIS | Holding ASSESS | Motor |
|-----|----------------|-------|
| 1 Inventory | SECURITY_CONTEXT | LAY |
| 2 (software) | stdlib-only + katalog izole | TC |
| 3 Data Protection | secret_scan, dry-run | ENC/secret |
| 4 Secure Config | hooks, permissions | LAY/FW |
| 5 Account Mgmt | GHA identities | IAM/COND |
| 6 Access Control | least privilege | COND |
| 7 Continuous Vuln | pin gap, research CVE sınıfı | TC |
| 8 Audit Log | AUDIT_LOG, REPORTS | LAY |
| 14 Awareness | GUARDRAIL + EXPERTS | ORG |
| 15 Service Provider | Actions allowlist | TC |
| 16 Application | scripts review | CHG |
| 17 Incident | SecOps rol + IR skill | COND/RS |

Tam 153 safeguard kopyalanmaz — ID + ASSESS sorusu.
