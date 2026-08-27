# Risk Öncelik Rubriği (ASSESS)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

## Skala
| Seviye | Tanım | Örnek holding |
|--------|-------|---------------|
| P0 | Secret ifşa veya CI supply-chain anında | plaintext key, floating Action tag |
| P1 | Yetki genişliği / state sızıntı potansiyeli | permissions write-all, tfvars |
| P2 | İzolasyon / hijyen | katalog install, doküman drift |
| P3 | İyileştirme | diyagram güzelleştirme |

## Olasılık × Etki (kaba)
- Yüksek olasılık + yüksek etki → P0
- Düşük olasılık + yüksek etki → P1 (HNDL, Action compromise sınıfı)
- Saldırı adımı yazılmaz; yalnızca sınıf + kontrol ID

## Çıktı
`P? | tehdit sınıfı | kontrol | sahip rol`
