# /kontrol-uret — Kontrol iskeleti üret

## Objective
Belirtilen motorda (LAYERS|FIREWALLS|ENCRYPTION|CHANGE|TRANSPARENT_CODE|CONDITIONAL) kontrol stub’ları üret.

## Requirements
- MODE=ASSESS-ONLY; tam 100’ü tek turda doldurma (batch ≤10 önerilir)
- Her kontrol: ID, amaç, D3FEND/NIST, doğrulama — exploit yok
- `20-control-mapping.mdc` uyumu

## Output
İlgili klasörde stub dosyalar + `SECURITY_MATRIX/matrix.md` satır güncellemesi
