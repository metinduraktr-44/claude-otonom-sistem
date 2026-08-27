# Layer Model — Holding

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

## Katmanlar
| Katman | Ad | Holding örneği |
|--------|----|----------------|
| L0 | Governance | STATE, CISO politikası, MODE |
| L1 | Identity | GHA token, branch protection |
| L2 | Network/Egress | Runner outbound API allowlist ASSESS |
| L3 | Workload/CI | Workflows, permissions, pin |
| L4 | Application/Scripts | Python generators, validate |
| L5 | Data/Secrets | env, tf sensitive, AUDIT |

## İlkeler
- Her katmanda bağımsız kontrol; tek kontroye güvenme.
- Üst katman başarısız → alt katman detect/fail-closed.
- D3FEND: Harden, Detect, Isolate, Deceive(yok — holding’de kullanma), Evict(IR).

## CSF map
L0→GV · L1→PR.AA · L2→PR.IR · L3→PR.PS · L4→PR.DS · L5→PR.DS/DE.CM
