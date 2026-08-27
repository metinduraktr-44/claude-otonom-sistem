# GHA Secret Masking ASSESS

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

## Amaç
CI log’larında secret ifşasını azaltmak. Değer yazılmaz; yalnızca yöntem.

## Kontroller
1. GitHub Actions Secrets — UI/org secrets; workflow `secrets.*` referansı.
2. `::add-mask::` — runtime üretilen token’lar için (değer commit’e girmez).
3. Step summary / artefact — secret satırı yok; secret_scan after write.
4. `permissions: contents: read` default; write yalnızca gerekçeli job.
5. Fork PR: secrets kullanılmayan job path’i (COND-004).

## Holding map
- `scripts/*_client.py` dry-run → key yoksa ağ yok
- `docs/SECRETS-DRYRUN-MATRISI.md` ad kataloğu
- ENC-014 / LAY-005 / COND-011

## Doğrulama
- Workflow’ta `secrets.` kullanımları listelenir
- Örnek `.env` değerleri boş
- REPORTS JSON `value=<REDACTED>`

## NIST/CIS
PR.DS · AU-9 · IA-5 · CIS-3 · CIS-8 · ISO A.8.12
