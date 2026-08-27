# TLS & Key Policy (ASSESS)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

## TLS
- Min: TLS 1.2; hedef 1.3.
- Sertifika doğrulama kapatma YASAK (script’lerde `verify=False` avı ASSESS).
- Outbound allowlist: bilinen API host’ları (FW motoru ile).

## Anahtar / secret
- Uzun ömürlü key dokümanda yok.
- Dönüş: sağlayıcı konsolunda rotate — değeri repoya yazma.
- Terraform sensitive + remote state encryption ASSESS.
- GitHub Actions secrets; log mask.

## 800-53 / ISO
SC-8 transmission · SC-12 key gen · SC-13 crypto · SC-28 at-rest · ISO A.8.24

## Doğrulama
- Kod grep: `verify=False`, `ssl._create_unverified_context` (tespit)
- Workflow: secrets kullanım satırları
- Envanter güncellemesi
