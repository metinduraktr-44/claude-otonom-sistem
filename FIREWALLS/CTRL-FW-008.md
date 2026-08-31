# CTRL-FW-008 — API rate-limit beklentisi

```yaml
id: CTRL-FW-008
ad: API rate-limit beklentisi
açıklama: Gemini/OpenRouter istemcilerinde geri çekilme; anahtar ${VAR}.
NIST_CSF: ['Protect']
800-53: ['SC-5']
ISO27001: ['A.8.16']
CIS: ['CIS-13']
OWASP: ['A04:2021']
status: assess
mode: ASSESS-ONLY
doğrulama_yöntemi: scripts/*_client.py rate/retry okuması.
savunma_gerekçesi: Anahtar yakma ve DoS benzeri kötüye kullanımı sınırlar.
```

## Açıklama
Gemini/OpenRouter istemcilerinde geri çekilme; anahtar ${VAR}.

## Doğrulama (ASSESS-ONLY)
- scripts/*_client.py rate/retry okuması.

## Savunma gerekçesi
Anahtar yakma ve DoS benzeri kötüye kullanımı sınırlar.

> DEFENSE-ONLY: detection, hardening, compliance, IR playbooks. No exploits, phishing, malware, C2, ransomware, bypass, weaponized PoCs. ATT&CK only for detection/D3FEND mapping. Secrets: ${VAR}|vault://|op://|<REDACTED> only.
