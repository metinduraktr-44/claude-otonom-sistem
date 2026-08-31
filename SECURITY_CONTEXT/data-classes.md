# Data classes

| Sınıf | Örnek | Repo kuralı |
|-------|--------|-------------|
| Public | README, CILT docs, kontrol kartları | OK commit |
| Internal | ORG/ROLES RACI, gap taslakları | OK; PII yok |
| Confidential | Müşteri brief içeriği (SCENARIOS) | Minimise; arşiv politikası |
| Secret | API keys, tokens, private keys | **ASLA** plaintext — `${VAR}` / `vault://` / `op://` / `<REDACTED>` |

## Bu repoda Secret adayları (isimler — değer yok)
- `ANTHROPIC_API_KEY`
- `GEMINI_API_KEY` / Google AI
- `OPENROUTER_API_KEY`
- `GITHUB_TOKEN`
- Canva OAuth tokens (MCP; kullanıcı enable)
- GitHub Actions `secrets.*`

Scanner: `python3 scripts/secret_scan.py`

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
