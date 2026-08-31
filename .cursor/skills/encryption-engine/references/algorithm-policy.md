# Algorithm Allow/Deny (İsim Düzeyi)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

## Allow (hedef)
- TLS 1.2 / 1.3
- AES-GCM (at-rest, sağlayıcı tarafı)
- SHA-256+ bütünlük
- Ed25519 / ECDSA P-256 (klasik imza) — geçiş planlı
- ML-KEM / ML-DSA / SLH-DSA (PQC roadmap)

## Deny (isim listesi — kırma tarifi yok)
- MD5 / SHA-1 bütünlük
- RC4 / 3DES
- TLS 1.0 / 1.1
- `verify=False` / custom trust-all

## Doğrulama
Kod/config grep (tespit); ENC-008.

## Kaynak
FIPS 203/204/205 · NIST SP 800-52 TLS rehberi (referans URL standards-currency).
