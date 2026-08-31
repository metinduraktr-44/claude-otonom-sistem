---
description: Security OS bootstrap doğrula; SECURITY/STATE READY; MODE=ASSESS-ONLY
---

# /baslat-security

1. Doğrula: security rules/skills, SECURITY_*/LAYERS, scripts/secret_scan.py + ethics_check.py.
2. `SECURITY/STATE.md`: faz=0, mode=ASSESS-ONLY.
3. Çalıştır: `python3 scripts/secret_scan.py --self-test` · `ethics_check.py --self-test`.
4. Çıktı: FAZ 0–8 tablosu + `/devam` veya `/gap-analizi`.
