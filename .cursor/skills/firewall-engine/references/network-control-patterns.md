# Firewall / network control patterns (defense)

## Amaç
Ağ ve egress kontrollerini **doküman + ASSESS** düzeyinde tanımlar. Exploit, bypass veya silahlı PoC yok.

## Pattern set
1. **Default deny inbound** — Bu Holding reposunda dinleyen servis yok; yeni port talebi CHANGE kaydı ister (`CTRL-FW-006`).
2. **Egress sınıflandırma** — GitHub API / LLM provider / Canva MCP ayrı trust zone (`trust-boundaries.md`).
3. **CI izolasyonu** — Actions job’larında secret echo yasak; pin’li `uses:` (`CTRL-FW-002`).
4. **MCP stub OFF** — `.cursor/mcp.security.stubs.example.json`; canlı tool iddiası yok.
5. **TLS-only harici** — `http://` istemci çağrısı ASSESS bulgusu (`CTRL-FW-011`).
6. **katalog SKIP** — Scanner gürültüsü ve yanlış pozitif ayrımı (`CTRL-FW-012`).

## Doğrulama checklist
- [ ] Egress tablosu güncel mi?
- [ ] Workflow’da `${{ secrets.* }}` log’a yazılıyor mu? (olmamalı)
- [ ] MCP security stub hâlâ example mı?
- [ ] matrix.md FW kontrolleri linkli mi?

## Anti-patterns
- “WAF var” iddiası (bu repo N/A — `CTRL-FW-007`)
- Sahte IP block listesini exploit rehberi gibi yazmak
- C2 / tunneling howto

## Framework map
NIST CSF Protect · 800-53 SC-7/AC-4 · CIS 12/13 · ISO A.8.20+

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
