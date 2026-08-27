# Pin Gap Ölçüm Yöntemi (ASSESS)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

## Metrik
`pin_ratio = sha_pinned_uses / total_uses`

## Adımlar
1. `.github/workflows/*.yml` envanter
2. `uses:` satırlarını sınıflandır: SHA40 / tag / branch
3. Gap listesi → TC-002
4. Dependabot Actions PR ASSESS
5. Sonuç REPORTS’a (secret yok)

## Hedef
İlk geçiş: kritik job’lar %100 SHA; sonra tüm workflow.
