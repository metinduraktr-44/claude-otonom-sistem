# Holding Layer Gaps (ASSESS)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

| Katman | Mevcut | Gap |
|--------|--------|-----|
| L0 Gov | STATE/MODE | Board raporu şablonu |
| L1 Identity | dry-run clients | OIDC/environment protection |
| L2 Egress | bilinç | yazılmış allowlist dosyası |
| L3 CI | workflows | SHA pin oranı ölçümü |
| L4 App | validate | input trust tests |
| L5 Data | secret_scan | vault entegrasyon ASSESS |

Her gap → LAY/TC/COND kontrol veya Faz 5 pack.
