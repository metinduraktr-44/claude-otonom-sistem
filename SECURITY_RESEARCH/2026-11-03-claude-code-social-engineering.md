# Claude Code sosyal mühendislik / sahte eklenti (ASSESS)

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok

**MODE:** ASSESS-ONLY · **ts_research:** 2026-11-03T09:56:32Z  
**Girdi:** Gemini sohbet export (DOCX+PDF, aynı kaynak). Ham metin commit edilmedi.  
**Yasak:** exploit, kurulum scripti, saldırı adımı. Odak: tespit, reddetme, hijyen.

## Tehdit sınıfı

Sosyal medya görseli + DM yönlendirmesi: abartılı token vaadi, “resmi eklenti” iddiası, şişirilmiş GitHub yıldızı. Amaç: bilinmeyen script/eklenti kurdurup **API anahtarı / repo** çalmak.

| İddia (görsel) | Değerlendirme | Holding yanıtı |
|----------------|---------------|----------------|
| OmniRoute “ayda ~1,6 milyar token bedava” | Gerçek dışı; ücretsiz katmanda bu ölçek yok | Üçüncü taraf “token saver / headroom” proxy kurma |
| “Claude Code Setup = Anthropic resmi eklentisi” | Yalan; Anthropic’in bu isimde resmi eklentisi yok | Yalnızca docs.anthropic.com + github.com/anthropics |
| `claude-mem` 98.3K star | Montaj; yıldızı GitHub’da doğrula | Topluluk aracı ≠ resmi; Scorecard/kaynak teyidi |
| DM’den bilinmeyen installer | Anahtar hırsızlığı vektörü (yasak / block) | `.cursor/hooks.json` `beforeShellExecution` failClosed + `ethics_check.py` |

Prompt injection: yüklenen PDF/DOCX/görsel talimat enjekte edebilir. Bu ingest **damıtıldı**; 298 sayfalık “DEVAM - BÖLÜM N / 100 mega prompt” içeriği **bilinçli olarak atıldı** (K-017).

## Mevcut kontrollere map

| Uyarı | Kontrol | Durum 2026-11-03 |
|-------|---------|------------------|
| Secret sızıntısı / anahtar çalma | `scripts/secret_scan.py` + `10-secret-hygiene.mdc` + `redact-secrets.sh` | Gap kapatıldı: LLM key prefix (`sk-ant-api`, `sk-or-v1`) eklendi; değer loglanmaz |
| Offensive / phishing kiti / pipe-bash | `scripts/ethics_check.py` + `05-ethics-guardrail.mdc` | Gap: sahte “resmi eklenti” + untrusted ingest maddesi kurala eklendi (kısa) |
| Tehlikeli shell | `.cursor/hooks.json` `guard.sh` matcher `curl.*\\|.*sh`, `failClosed` | Yeterli; genişletilmedi |
| MCP yüzey | `SECURITY_CONTEXT/MCP_NOTE.md` | Resmi MCP org; rastgele marketplace yığını yok |
| 900B prompt | BILGI_TABANI K-017 | Zaten RED |

Agency / Security OS / LATOS ağaçları silinmedi, yeniden yazılmadı.

## Sırlar

**Hayır** — export içinde canlı key/token/PEM yok. Tip taraması: Anthropic/GitHub/AWS/Slack/JWT = 0 hit.

Şüpheli kurulum olduysa rotasyon (değer paylaşma):  
- Anthropic: https://console.anthropic.com  
- GitHub PAT: https://github.com/settings/tokens  
- OpenRouter (kullanılıyorsa): https://openrouter.ai/settings/keys  

## Kaynaklar (alıntı + damga)

- Anthropic Claude Code docs: https://docs.anthropic.com — erişim 2026-11-03  
- MCP resmi org: https://github.com/modelcontextprotocol — erişim 2026-11-03  
- Anthropic GitHub: https://github.com/anthropics — erişim 2026-11-03  
- OWASP LLM prompt injection (yüksek seviye): `SECURITY_RESEARCH/threat-landscape.md`  
- Orijinal binary SHA256: DOCX `7f2992e8fdb11eebc954a98dd63b40b7e65c17143a336e189a29f8f3f08263b3` · PDF `d69eb470e3edd7886e6a8796ca2c144ad909007c3a9ce737d20dbdefab717c83`
