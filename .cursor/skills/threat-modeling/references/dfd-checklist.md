# DFD Checklist — Holding Automation

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

## Adımlar
1. Harici aktörler: Maintainer, GHA, LLM provider, Terraform backend.
2. Process: validate, nightly, holding_report, llm_smoke.
3. Data store: git repo, Actions secrets store, local env, remote state.
4. Data flow: clone → script → API → markdown çıktı → commit.
5. Boundary: (a) internet↔runner (b) runner↔secret store (c) content↔model.

## Her akış için sorular (ASSESS)
- Kim kimliği kanıtlar?
- Veri sınıflandırması (secret / public / internal)?
- Bütünlük kontrolü (pin, signature, review)?
- Log’da secret var mı?
- Başarısızlıkta fail-closed mı?

## Çıktı şablonu
```
Flow: <ad>
Boundary: <a|b|c>
Threat classes: <STRIDE harfleri>
Controls: <ID list>
Residual risk: <kabul|mitigate|transfer>
```

## Yasak
Adım adım saldırı senaryosu, payload, bypass tarifi.
