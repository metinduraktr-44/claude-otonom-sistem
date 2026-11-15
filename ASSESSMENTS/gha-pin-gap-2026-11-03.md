# GHA pin gap ASSESS — 2026-11-03T11:47:59Z

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**MODE:** ASSESS-ONLY — workflow dosyaları bu turda değiştirilmedi.

## Bulgu
- 12 workflow tarandı.
- Tag pin (`@v4` / `@v5` / `@v7`) **25** `uses:` satırı; **40 karakter SHA pin yok**.
- `skill-ajans-dongu.yml` hâlâ `actions/setup-python@v5` (diğerleri v7) — sürüm sapması.
- PR #33 dependabot setup-python 5→7 ayrı açık PR; bu tur merge yok.

## Öncelik (uygulama sonraki tur, MODE değişince)
1. `actions/checkout` ve `actions/setup-python` SHA pin
2. Sürüm hizası (v5 kalanı)
3. permissions: least-privilege yeniden okuma

## Doğrulama
`rg "uses:" .github/workflows` + SHA40 yokluğu.

## Savunma gerekçesi
Hareket eden tag tedarik zinciri kaydırması; tespit/gap. Exploit yok.
