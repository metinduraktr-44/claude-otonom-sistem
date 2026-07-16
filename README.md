# CLAUDE OTONOM SİSTEM 🧠
**Kendini besleyen (self-improving), zaman damgalı, gecelik çalışan Claude orkestrasyon sistemi.**
Chat + Code + Cowork tek çatı altında · aitmpl.com bileşen mimarisiyle uyumlu · TR

> Model kendini "train" etmez — **bilgi tabanı her gece büyür**: oku → damıt → üret → doğrula → damgala → zincirle. Gerçek mekanizma budur ve bu repo onu uçtan uca kurar.

## 📁 Yapı
```
docs/CILT1-PROJE-ANAYASASI.md        # Umbrella mimari + ana master prompt + gecelik takvim
docs/CILT2-BILESEN-PROMPT-KUTUPHANESI.md  # 8 bileşen tipi için üretim promptları (repo-doğrulanmış)
CLAUDE.md                             # Orkestratör (Claude Code bunu otomatik okur)
BILGI_TABANI.md                       # Kümülatif hafıza — her gece büyür
AUDIT_LOG.jsonl                       # Her işlem için zaman damgalı kayıt
KARAR_LOGU.md                         # Kararlar + gerekçe + tarih
.claude/{skills,agents,commands}/     # Üretilen bileşenler buraya
scripts/{nightly.sh,validate.py,timestamp.sh}
.github/workflows/nightly-improve.yml # Her gece 03:00 (İstanbul) otomatik döngü
.github/workflows/validate.yml        # Her push/PR'da 6 katman doğrulama
```

## ⚡ Kullanım
1. **Chat:** claude.ai → Projects → "CLAUDE OTONOM SİSTEM" → `CLAUDE.md` içeriğini Custom Instructions'a yapıştır, `docs/` + `BILGI_TABANI.md`'yi proje bilgisine ekle.
2. **Code:** Repoyu klonla → Claude Code aç → `CLAUDE.md` otomatik yüklenir → Cilt 2 promptlarıyla bileşen üret.
3. **Gecelik:** Actions sekmesini aç → `nightly-improve` her gece 03:00'te koşar (damga + doğrula + bilgi tabanını büyüt).

## 🔍 Doğrulama & Zaman Damgası
Her işlem: `ts_start` → yap → 6 katman doğrula (structural / integrity-SHA256 / semantic / reference / patterns / review) → GEÇTİ/KALDI → `ts_end` → `AUDIT_LOG.jsonl` → öğrenim `BILGI_TABANI.md`'ye → **bir sonraki işlem bunu girdi alır (zincir)**.

## 💰 Gelir
Bu sistem üretim motorudur; gelir gerçek işe bağlanınca oluşur (Cilt 1 §7: İBB Kültür AŞ / VESTRA / Movéa / Tahmin Uzmanı / Response DGA). Kardeş repo: **AdOps Agents** (dikey, gelir-odaklı paket).

## ⚠️ Notlar
- Gecelik LLM üretimi için `ANTHROPIC_API_KEY` secret'ı gerekir → **ücretli kredi harcar**. Yoksa görev damga+doğrulama modunda yine çalışır.
- +900T karakter / otonom self-training fiziksel olarak imkânsızdır; bu repo **çalışan eşdeğerini** kurar (bkz. Cilt 1 §0).

Lisans: MIT

## katalog/ — Tam Bileşen Kütüphanesi
[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) kataloğunun tamamı (8 kategori: agents · commands · skills · hooks · mcps · settings · loops · sandbox), MIT lisansıyla (`katalog/LICENSE-UPSTREAM`). İndeks: `katalog/KATALOG_INDEKS.md`. Bileşenler işe alınırken CILT2 kurallarıyla Türkçe/dikey yapılandırılır.

## pilots/ — Pilot İş Paketleri (repo-hazır)
| Paket | İş | Ana bileşen |
|---|---|---|
| `pilots/tahmin-agents` | Tahmin Uzmanı | v-serisi prompt iyileştirici ajan |
| `pilots/vestra-agents` | VESTRA (e-ticaret) | rakip fiyat izleyici |
| `pilots/kultur-agents` | İBB Kültür AŞ | etkinlik tarayıcı |
| `pilots/movea-agents` | Movéa | marka içerik ajanı |

Her paket ayrı repoya bölünmeye hazır (`git subtree split` veya kopyala-push). Ajans dikeyi (Response DGA) ayrı repoda: **adops-agents**.
