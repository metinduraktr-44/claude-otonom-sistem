# CTRL-CD-007 — Koşullu: production deploy yok (bu repo)

```yaml
id: CTRL-CD-007
ad: Koşullu: production deploy yok (bu repo)
açıklama: npx convex deploy vb. yok; sadece doküman/otomasyon.
NIST_CSF: ['Protect']
800-53: ['CM-7']
ISO27001: ['A.8.9']
CIS: ['CIS-4']
OWASP: []
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: AGENTS.md runtime tanımı.
savunma_gerekçesi: Yanlış prod etkisi sıfır.
```

## Açıklama
npx convex deploy vb. yok; sadece doküman/otomasyon.

## Doğrulama (ASSESS-ONLY)
- AGENTS.md runtime tanımı.

## Savunma gerekçesi
Yanlış prod etkisi sıfır.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
