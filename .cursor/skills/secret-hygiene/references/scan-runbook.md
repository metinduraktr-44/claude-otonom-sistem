# Secret Scan Runbook

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

## Komutlar
```bash
python3 scripts/secret_scan.py SECURITY_CONTEXT SECURITY_RESEARCH ORG EXPERTS LAYERS FIREWALLS ENCRYPTION CHANGE TRANSPARENT_CODE CONDITIONAL SECURITY_MATRIX .cursor/skills
python3 scripts/ethics_check.py SECURITY_CONTEXT SECURITY_RESEARCH LAYERS FIREWALLS ENCRYPTION CHANGE TRANSPARENT_CODE CONDITIONAL
```

## Öncesi
- Hedef path’leri daralt (katalog/ skip — script zaten skip eder).
- MODE=ASSESS-ONLY: bulgu → gap kaydı; otomatik “fix commit” yok.

## Sonrası triage
| Bulgu tipi | Aksiyon |
|------------|---------|
| placeholder (`${VAR}`) | OK — ignore |
| gerçek pattern | DUR · rotate talimatı (değer yazma) · dosyayı temizle |
| example dosyası | boş değer teyit |

## Hook entegrasyonu
afterFileEdit / beforeCommit: `secret_scan` failClosed. Tehlikeli shell: deny.

## False positive notları
- Dokümanda `api_key = "${API_KEY}"` → allow.
- `AKIA` + gerçek 16 char → bulgu (redakte).
- Markdown’ta “BEGIN PRIVATE KEY” eğitim yasağı cümlesi → ethics/scan bağlamına dikkat; örnek PEM yapıştırma.

## Kanıt
REPORTS altına JSON özet (değer yok). Matris: LAY/ENC secret kontrolleri.

## TODO (20k kalan)
GHA `::add-mask::` örnekleri, vault provider tablo, rotate runbook (değer içermeden), dil bazlı pattern genişletme ASSESS.
