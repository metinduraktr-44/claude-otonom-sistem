# Assets (Holding HQ — claude-otonom-sistem)

| Asset ID | Tip | Kritiklik | Not |
|----------|-----|-----------|-----|
| AST-SCRIPTS | Kod | Yüksek | `scripts/*.py` otomasyon |
| AST-GHA | CI | Yüksek | `.github/workflows/` |
| AST-CURSOR-SEC | Kontrol düzlemi | Yüksek | `.cursor/skills/*`, rules, hooks |
| AST-CURSOR-CANVA | Kreatif düzlem | Orta | Canva skills; BRIEF-ONLY |
| AST-DOCS-GIGA | Doküman | Orta | CILT13/14, IS-LISTESI |
| AST-AUDIT | Telemetri | Orta | `AUDIT_LOG.jsonl`, `BILGI_TABANI.md` |
| AST-KATALOG | Vendored | Düşük* | Tarama SKIP; tedarik riski ayrı |
| AST-INFRA-OTEL | İskelet | Düşük | Henüz canlı iddia yok |
| AST-TOOLS-SCAN | Savunma araç | Yüksek | secret/ethics scanners |

\*katalog içeriği yüksek hacimli; runtime güvenilirlik sınırının dışında tutulur.

Owner varsayılan: Security Architect (ORG/ROLES).

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
