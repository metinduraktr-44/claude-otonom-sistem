# Cloud posture ASSESS (bu repo)

## Gerçek kapsam
- Birincil: GitHub (repo + Actions). Bulut hesabı iddiası yok.
- `infra/terraform` / `infra/otel` = iskelet; canlı deploy iddiası YASAK.

## CIS benzeri checklist (GitHub)
- [ ] Branch protection ASSESS
- [ ] Actions secrets encrypted; log echo yok
- [ ] Dependabot PR incelemesi
- [ ] Workflow `permissions:` least privilege ASSESS
- [ ] Fork PR secrets izolasyonu bilinçli

## Çıktı
ASSESSMENTS/cloud-github.md (üretildiğinde) + gap satırları.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
