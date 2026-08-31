# CTRL-CD-003 — Koşullu: ANTHROPIC/GEMINI anahtarı yoksa dry-run

```yaml
id: CTRL-CD-003
ad: Koşullu: ANTHROPIC/GEMINI anahtarı yoksa dry-run
açıklama: API key yok → iskelet çıktı; üretilmiş secret yok.
NIST_CSF: ['Protect']
800-53: ['AC-3', 'IA-5']
ISO27001: ['A.8.5']
CIS: ['CIS-5']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: daily_agency / llm clients dry-run.
savunma_gerekçesi: Ücretli/gizli çağrı sürprizi yok.
```

## Açıklama
API key yok → iskelet çıktı; üretilmiş secret yok.

## Doğrulama (ASSESS-ONLY)
- daily_agency / llm clients dry-run.

## Savunma gerekçesi
Ücretli/gizli çağrı sürprizi yok.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
