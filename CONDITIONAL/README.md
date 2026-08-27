# CONDITIONAL

Starter control catalog (FAZ 3 expansion). MODE=`ASSESS-ONLY`.

| ID | Ad | NIST CSF |
|----|----|----------|
| [CTRL-CD-001](CTRL-CD-001.md) | Koşullu: CANVA:ON olmadan mutate yok | Protect, Govern |
| [CTRL-CD-002](CTRL-CD-002.md) | Koşullu: MODE=IMPLEMENT kapsamı | Govern |
| [CTRL-CD-003](CTRL-CD-003.md) | Koşullu: ANTHROPIC/GEMINI anahtarı yoksa dry-run | Protect |
| [CTRL-CD-004](CTRL-CD-004.md) | Koşullu: GITHUB_TOKEN yoksa static holding | Protect |
| [CTRL-CD-005](CTRL-CD-005.md) | Koşullu: ethics KALDI → dur | Govern, Protect |
| [CTRL-CD-006](CTRL-CD-006.md) | Koşullu: secret KALDI → commit engeli | Protect |
| [CTRL-CD-007](CTRL-CD-007.md) | Koşullu: production deploy yok (bu repo) | Protect |
| [CTRL-CD-008](CTRL-CD-008.md) | Koşullu: parallel agent izolasyonu | Protect |
| [CTRL-CD-009](CTRL-CD-009.md) | Koşullu: IR severity ≥ yüksek → exec bilgilendirme | Respond |
| [CTRL-CD-010](CTRL-CD-010.md) | Koşullu: compliance paket yalnız map | Govern |
| [CTRL-CD-011](CTRL-CD-011.md) | Koşullu: research kaynaksız yayın yok | Govern |
| [CTRL-CD-012](CTRL-CD-012.md) | Koşullu: arşiv ay sonu | Recover, Govern |
| [CTRL-CD-013](CTRL-CD-013.md) | Koşullu: MCP enable kullanıcı onayı | Protect, Govern |
| [CTRL-CD-014](CTRL-CD-014.md) | Koşullu: gap owner boşsa escalate | Govern |
| [CTRL-CD-015](CTRL-CD-015.md) | Koşullu: dual-OS çakışma önceliği | Govern |

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
