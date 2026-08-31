# PQC Roadmap ASSESS (FIPS 203/204/205)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**Normatif:** NIST FIPS 203 (ML-KEM), 204 (ML-DSA), 205 (SLH-DSA) — 2024-08-13.  
https://csrc.nist.gov/pubs/fips/203/final · NIST duyuru: https://www.nist.gov/news-events/news/2024/08/announcing-approval-three-federal-information-processing-standards-fips

## Holding gerçekliği
- Uygulama sunucusu / özel TLS terminator yok.
- Outbound HTTPS istemcileri (LLM API) OS/Python TLS yığınına bağlı.
- İmza: git commit / release attestation gelecekte (TC motoru).

## Fazlı plan (ASSESS)
| Faz | İş | Çıktı |
|-----|-----|-------|
| A | Envanter: hangi bağlantılar TLS kullanıyor | tablo |
| B | Klasik algoritma politikası (TLS1.2+; zayıf cipher yasak listesi — isim düzeyinde) | ENC-00x |
| C | PQC hibrit KEM izleme (istemci kütüphane desteği) | gap |
| D | Code signing / provenance için ML-DSA veya klasik+PQC hibrit | TC+ENC |
| E | Vault/key wrap PQC | vault ASSESS |

## Harvest-now-decrypt-later
Uzun ömürlü gizli veri yok varsayımı holding için makul; yine de API token rotasyonu + kısa TTL tercih.

## Yasak
Kırılabilirlik PoC, brute-force tool, weak key üretimi örneği.
