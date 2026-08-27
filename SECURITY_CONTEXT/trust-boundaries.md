# Trust boundaries

```text
[Developer / Cursor Agent]
        |  git push (no secrets in tree)
        v
[GitHub remote] --Actions--> [ubuntu runner]
        |                         |
        |                         +--> scripts/validate.py
        |                         +--> secret_scan / ethics_check (when wired)
        |
        +--> optional LLM APIs (Gemini/OpenRouter/Anthropic) via ${VAR}
        +--> optional GitHub API via ${GITHUB_TOKEN}
        +--> optional Canva MCP (OFF unless CANVA:ON + OAuth)
```

| Boundary | İç | Dış | Kontrol |
|----------|----|-----|---------|
| Repo tree | docs, scripts, .cursor | Public GitHub | secret_scan, no plaintext keys |
| CI runner | checkout + python3 | Actions marketplace | pin versions ASSESS |
| LLM egress | prompt + skeleton | Provider API | key in secrets; dry-run if unset |
| Canva | BRIEF-ONLY default | mcp.canva.com | flag + OAuth |
| katalog/ | vendored MIT | — | SKIP_DIRS scanners |

MODE=`ASSESS-ONLY`.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
