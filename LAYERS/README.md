# LAYERS

Starter control catalog (FAZ 3 expansion). MODE=`ASSESS-ONLY`.

| ID | Ad | NIST CSF |
|----|----|----------|
| [CTRL-L-001](CTRL-L-001.md) | Politika katmanı — güvenlik politikası envanteri | Govern, Identify |
| [CTRL-L-002](CTRL-L-002.md) | Kimlik katmanı — ayrıcalıklı erişim envanteri | Protect |
| [CTRL-L-003](CTRL-L-003.md) | Ağ katmanı — güven sınırları diyagramı | Identify, Protect |
| [CTRL-L-004](CTRL-L-004.md) | Host katmanı — runner/OS sertleştirme kontrol listesi | Protect |
| [CTRL-L-005](CTRL-L-005.md) | Uygulama katmanı — girdi doğrulama standardı | Protect |
| [CTRL-L-006](CTRL-L-006.md) | Veri katmanı — sınıflandırma şeması | Identify, Protect |
| [CTRL-L-007](CTRL-L-007.md) | Tespit katmanı — log/telemetri minimum set | Detect |
| [CTRL-L-008](CTRL-L-008.md) | Yanıt katmanı — IR playbook iskeleti | Respond |
| [CTRL-L-009](CTRL-L-009.md) | Kurtarma katmanı — yedek/geri alma planı | Recover |
| [CTRL-L-010](CTRL-L-010.md) | Tedarik zinciri katmanı — bağımlılık sınırı | Protect, Identify |
| [CTRL-L-011](CTRL-L-011.md) | Agent güvenlik katmanı — ethics guardrail | Govern, Protect |
| [CTRL-L-012](CTRL-L-012.md) | Gizlilik katmanı — PII minimizasyonu | Protect |
| [CTRL-L-013](CTRL-L-013.md) | Değişiklik katmanı — MODE geçiş kaydı | Govern |
| [CTRL-L-014](CTRL-L-014.md) | Şeffaflık katmanı — karar gerekçesi | Govern |
| [CTRL-L-015](CTRL-L-015.md) | Süreklilik katmanı — aylık arşiv | Recover, Govern |
| [CTRL-SAMPLE-ACCESS](CTRL-SAMPLE-ACCESS.md) | Least privilege (sample) | Protect |

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
