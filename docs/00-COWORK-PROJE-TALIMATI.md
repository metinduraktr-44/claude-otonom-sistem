# COWORK PROJESİNE KURULUM — 3 ADIM

Bu paket iki bağımsız yapı içerir:
1. **claude-otonom-sistem/** → şemsiye sistem (GitHub: metinduraktr-44/claude-otonom-sistem)
2. **adops-agents/** → ayrı gelir girişimi (ikinci GitHub reposu)

## Adım 1 — Cowork projesine dosyaları ekle
Cowork projesi → sağ panel **Files** → bu klasördeki HER ŞEYİ sürükle-bırak.
(Ya da proje ayarları → Project knowledge → dosyaları ekle.)

## Adım 2 — Proje talimatını yapıştır
Proje ayarları → **Instructions** alanına
`claude-otonom-sistem/CLAUDE.md` içeriğini AYNEN yapıştır.
Bu, projedeki her Chat/Cowork oturumunun orkestratör anayasası olur.

## Adım 3 — Gecelik döngüyü kur
- claude.ai → **Scheduled** → yeni görev → `claude-otonom-sistem/docs/CILT1` Bölüm 5.2'deki
  GECELİK ROUTINE PROMPT'unu yapıştır → her gece 03:00.
- GitHub tarafı: her iki repoda Actions'ı aç (nightly-improve.yml hazır).
  🚩 LLM üretim adımı için repo secret `ANTHROPIC_API_KEY` gerekir → ücretli API kredisi.

## Çalışma düzeni
| Alan | İş |
|---|---|
| Chat (proje içi) | Strateji, kurul, karar → KARAR_LOGU.md |
| Cowork (bu proje) | Makale okuma→damıtma, deliverable üretimi → BILGI_TABANI.md büyür |
| Code | Bileşen üretimi (.claude/), gerçek `date -u` damgası, AUDIT_LOG.jsonl |

Her işlem: damga → yap → denetle (6 katman) → öğren → damga. Zincir her gece döner.
