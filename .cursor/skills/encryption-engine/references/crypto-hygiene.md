# Encryption & key hygiene (defense)

## İlkeler
1. Repo’da plaintext secret **yok** — `${VAR}` | `vault://` | `op://` | `<REDACTED>`.
2. Private key PEM blokları scanner ile KALDI.
3. Transit: HTTPS/TLS; zayıf cipher “nasıl kırılır” yok — yalnız yasak listesi.
4. Anahtar yaşam döngüsü dokümante (rotasyon/iptal) — değer yok.
5. CI secrets: GitHub encrypted secrets; echo yasak.

## Yasak algoritma notu (ASSESS)
- MD5/SHA1 password hashing bağlamında
- ECB mode
- 1024-bit RSA (yeni sistemlerde)

Tercih (genel): TLS 1.2+, AES-GCM, Ed25519/RSA-2048+ imza, Argon2/bcrypt (auth DB varsa; bu repo N/A).

## Repo kontrolleri
`CTRL-ENC-001` … `CTRL-ENC-012` → `ENCRYPTION/`

## Doğrulama
```bash
python3 scripts/secret_scan.py --self-test
python3 scripts/secret_scan.py scripts .cursor SECURITY ENCRYPTION
```

## Crypto-agility bağ
Algoritma envanteri değişince `crypto-agility` skill + `CTRL-ENC-004` güncelle.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
