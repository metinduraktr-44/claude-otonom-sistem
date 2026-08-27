# GHA Pin Policy (ASSESS)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

## Politika
1. Üçüncü parti Actions: **40-char commit SHA** + `# vX.Y.Z` yorumu.
2. `actions/*` için de SHA tercih (tutarlılık).
3. Dependabot `package-ecosystem: github-actions`.
4. Yeni Action: allowlist PR + gerekçe.
5. `pull_request_target` + fork checkout: yüksek risk — ASSESS’te işaretle; kullanım minimizasyonu.

## Doğrulama
```bash
# Tespit: tag referansları (gözden geçir)
rg -n "uses: .+@[vV0-9]" .github/workflows || true
rg -n "uses: .+@[0-9a-f]{40}" .github/workflows || true
```
(Çıktıyı raporla; otomatik “saldırı” yok.)

## Olay sınıfı yanıtı
Tag-repoint sınıfı → pin gap listesi + rotate secrets **prosedür referansı** (değer yok).

## Ref
https://safeguard.sh/resources/blog/how-to-pin-github-actions-to-shas-correctly (*erişim 2026-08-27*)
