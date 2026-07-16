# CLAUDE OTONOM SİSTEM — PROJE ANAYASASI & MASTER PROMPT KÜTÜPHANESİ
### aitmpl.com bileşenlerinden yola çıkan, kendini besleyen (self-improving), zaman damgalı, gecelik çalışan Claude sistemi
**Kapsam:** Chat + Code + Cowork · **Dil:** Türkçe · **Statü:** Uygulanabilir (gerçek özelliklerle)

---

## 0. ÖNCE GERÇEKLİK KONTROLÜ (bunu atlama)

Bu belge, "imkânsız olanı taklit eden" değil, **gerçekten çalışan** bir sistem kurar. Netleştirelim:

| İstediğin | Gerçekte ne yapılabilir |
|---|---|
| +900 trilyon karakter çıktı | ❌ İmkânsız (≈900 TB metin). Yerine: **maksimum yoğunlukta**, eksiksiz, kopyala-yapıştır prompt sistemi. Değer = sinyal yoğunluğu, uzunluk değil. |
| Claude her gece kendini "train" etsin | ❌ Model ağırlıkları sabit. ✅ Yerine: **bilgi dosyası her gece büyür** (oku→damıt→yaz→ertesi gün kullan). Buna "öğrenme döngüsü" diyoruz. |
| Anthropic + rakiplerin iç eğitimini al, sınavla doğrula | ❌ İç veri gizli. ✅ Yerine: **halka açık** kılavuz/blog/makale damıtımı + **öz-denetim rubric'i**. |
| Her gece ekip kur, toplantı yap | ✅ Tek prompt içinde **çok-uzman kurul personası** simülasyonu + toplantı notu çıktısı. |
| Zaman damgası her adımda | ✅ Code (CLI) içinde gerçek `date -u` çıktısıyla **kanıtlanabilir UTC damgası**; Chat'te verilen tarih. |
| Otonom gelir üret | ⚠️ Prompt tek başına para üretmez. ✅ Sistemi **gerçek işine** (İBB/Movéa/VESTRA) bağlarsın → faturalanabilir çıktı üretir. Bkz. Bölüm 7. |

**Maliyet kırmızı bayrağı:** Gecelik ağır otomasyon kota/ücret harcar. Scheduled/Routines/Dispatch + bazı MCP'ler ek maliyet yaratabilir. Planlarken bunu hesaba kat.

---

## 1. aitmpl.com NEDİR? (sade, doğrulanmış anlatım)

**aitmpl.com = "Claude Code Templates"** — davila7'nin açık kaynak (MIT lisanslı) projesi. `github.com/davila7/claude-code-templates` (~28k yıldız). Claude Code için **hazır yapılandırmalar kataloğu** ve bir **CLI aracı**.

Kurulum tek satır: `npx claude-code-templates@latest` (interaktif seçim açar).

### 8 bileşen tipi — ne işe yarar

| Bileşen | Nedir | Nereye kurulur | Örnek |
|---|---|---|---|
| **Skills (Yetenekler ~853)** | Kademeli açılımlı (progressive disclosure) yeniden kullanılabilir yetenek. Bir `SKILL.md` + yardımcı dosyalar. | `.claude/skills/` | PDF işleme, Excel otomasyonu, DOCX üretimi |
| **Agents (Ajanlar ~421)** | Belirli alanın uzmanı alt-model rolü | `.claude/agents/` | code-reviewer, security-auditor, database-architect |
| **Commands (Komutlar ~281)** | Özel slash komutları | `.claude/commands/` | `/generate-tests`, `/optimize-bundle` |
| **Settings (Ayarlar ~68)** | Claude Code yapılandırmaları | `.claude/settings.json` | timeout, memory, output style |
| **Hooks (Kancalar ~58)** | Otomasyon tetikleyicileri (olay bazlı) | `.claude/settings.json` içinde `hooks` | pre-commit doğrulama, iş bitince aksiyon |
| **MCPs (~93)** | Dış servis entegrasyonları | `.mcp.json` | GitHub, PostgreSQL, Stripe, AWS |
| **Loops (Döngüler ~18)** | Yinelemeli iş akışları | proje düzeyi | otomatik iyileştirme döngüleri |
| **Plugins (~32)** | Paketlenmiş bileşen setleri | plugin marketplace | hazır "toolkit"ler |

**Kritik içgörü (tersine mühendisliğin özü):** Bu bileşenlerin neredeyse hepsi **düz metin dosyalarıdır** — üstte YAML frontmatter, altta talimatlar. "Sihir" yok. Yapıyı anladığında **kendininkini yazabilirsin**. Bütün "tersine mühendislik" işi budur.

---

## 2. SIFIR BİLGİLİ BİRİ İÇİN TERSİNE MÜHENDİSLİK REHBERİ

> Hedef: Hiç bilmeyen biri, bu bileşenlerin **anatomisini** anlasın ve kendi versiyonunu üretebilsin.

### Adım 1 — Bir bileşenin iç yapısını gör
Her Skill şu iskelettedir:

```markdown
---
name: pdf-processor
description: PDF dosyalarını okur, birleştirir, form doldurur. Kullanıcı PDF'ten bahsedince tetiklenir.
---

# PDF İşleme

## Ne zaman kullan
- Kullanıcı .pdf dosyasından bahsediyorsa
- Metin/tablo çıkarma, birleştirme, form doldurma istiyorsa

## Nasıl yap
1. ...adım adım talimat...
2. ...

## Örnekler
...
```

**Anahtar kural:** `description` alanı = **tetikleyici**. İyi yazılmış description, Claude'un o yeteneği doğru anda çağırmasını sağlar. Kötü description = yetenek hiç tetiklenmez. Tersine mühendislikte %80 iş buradadır.

### Adım 2 — Agent anatomisi
```markdown
---
name: performance-optimizer
description: React/bundle performans darboğazlarını bulur ve düzeltir.
tools: Read, Edit, Bash   # hangi araçlara erişebilir
---
Sen kıdemli bir performans mühendisisin. Görevin:
- Bundle boyutunu analiz et
- Gereksiz re-render'ları bul
- Somut, uygulanabilir düzeltmeler öner
Çıktı formatı: sorun → kanıt → düzeltme (kod bloğu).
```

### Adım 3 — Command anatomisi
```markdown
---
description: Test üretir
---
Verilen dosya için kapsamlı birim testleri yaz. 
Kenar durumlarını (edge case) kapsa. 
Framework'ü otomatik algıla.
```
Kullanıcı `/generate-tests` yazınca bu talimat çalışır.

### Adım 4 — Hook anatomisi (otomasyon)
`settings.json` içinde:
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit",
      "hooks": [{ "type": "command", "command": "npm run lint" }]
    }]
  }
}
```
Anlamı: Claude bir dosyayı her düzenlediğinde otomatik `npm run lint` çalışır. **Zaman damgası mekanizmamızın temeli budur** (Bölüm 6).

### Adım 5 — Kendi bileşenini üret (0→1)
1. `.claude/skills/benim-yeteneğim/SKILL.md` oluştur
2. Frontmatter'a **net tetikleyici description** yaz
3. "Ne zaman kullan" + "Nasıl yap" + "Örnek" bölümlerini doldur
4. Claude Code'da test et: yeteneğin tetiklenip tetiklenmediğine bak
5. Description'ı iyileştir → tekrar test → damgala (Bölüm 6)

**Bölüm 8'de** her tip için hazır boş şablon var; kopyala-doldur.

---

## 3. PROJE MİMARİSİ — Chat + Code + Cowork tek çatı altında

Senin "bir proje kapsamı altında ilerlet" isteğinin somut kurulumu:

### 3.1 Claude **Project** kur (claude.ai)
- Sol menü → **Projects** → yeni proje: **"CLAUDE OTONOM SİSTEM"**
- Projenin **Custom Instructions** alanına → **Bölüm 4'teki ANA MASTER PROMPT**'u yapıştır
- Bilgi dosyalarını (aşağıda) projeye ekle

### 3.2 Rol dağılımı — hangi iş nerede

| Alan | Görevi | Ne koyarsın |
|---|---|---|
| **Chat (Project)** | Strateji, kurul toplantıları, planlama, karar | Master prompt (custom instructions), `BILGI_TABANI.md`, `KARAR_LOGU.md` |
| **Code (Claude Code)** | Gerçek dosya işleri: bileşen üretimi, gerçek zaman damgası, gecelik routine | `.claude/` klasörü (skills/agents/commands/hooks), `AUDIT_LOG.jsonl`, `date` komutu |
| **Cowork** | Çok adımlı bilgi işi: makale okuma→damıtma, deliverable üretimi | Gecelik "oku→yaz" görevleri, çok araçlı akışlar |

### 3.3 Ortak bilgi dosyaları (sistemin "hafızası")
Sistemin "öğrenmesi" bu dosyaların büyümesiyle olur:

```
/CLAUDE-OTONOM-SISTEM/
├── ANAYASA.md              # bu belge (değişmez kurallar)
├── BILGI_TABANI.md         # her gece büyüyen damıtılmış bilgi
├── KARAR_LOGU.md           # alınan kararlar + gerekçe + tarih
├── AUDIT_LOG.jsonl         # her işlem için zaman damgalı satır
├── UZMAN_KURULU.md         # persona tanımları
├── GELIR_MOTORU.md         # işine bağlı gelir akışı (Bölüm 7)
└── .claude/
    ├── skills/
    ├── agents/
    ├── commands/
    └── settings.json (hooks dahil)
```

---

## 4. ⭐ ANA MASTER PROMPT (KOPYALA-YAPIŞTIR)

> Bunu Claude Project'in **Custom Instructions** alanına veya Claude Code'un **CLAUDE.md** dosyasına yapıştır. Sistemin beyni budur.

```
# SİSTEM ANAYASASI — CLAUDE OTONOM ORKESTRATÖR

## KİMLİK
Sen bir "uzman kurulu" orkestratörüsün. Tek bir asistan gibi değil, 
aşağıdaki uzmanların birleşik zekâsı gibi davranırsın. Her görevde 
ilgili uzman(lar)ı devreye alır, aralarında kısa bir "kurul" yapar, 
sonra tek, net bir çıktı üretirsin.

## UZMAN KURULU (persona seti)
1. BAŞ MİMAR — sistem tasarımı, bileşen anatomisi, tersine mühendislik
2. PROMPT MÜHENDİSİ — tetikleyici/description optimizasyonu, çıktı sözleşmesi
3. OTOMASYON MÜHENDİSİ — hooks, routines, scheduled, CI/CD, zaman damgası
4. BİLGİ DAMITICISI — makale/doküman okur, sinyali çıkarır, bilgi tabanına yazar
5. DENETÇİ — her çıktıyı rubric'e göre denetler, kırmızı bayrak kaldırır
6. İŞ/GELİR STRATEJİSTİ — çıktıyı faturalanabilir değere bağlar

## İŞLETİM İLKELERİ
- SİNYAL > UZUNLUK. Dolgu yok. Her cümle iş görür.
- Her görev: (a) ilgili uzmanları seç → (b) 2-4 satırlık kurul özeti → 
  (c) tek net çıktı → (d) DENETÇİ onayı → (e) zaman damgası.
- Belirsizlik varsa varsayımı açıkça yaz, durmadan devam et.
- Asla imkânsızı taklit etme; imkânsız istekte KIRMIZI BAYRAK protokolü çalışır.

## KIRMIZI BAYRAK PROTOKOLÜ
Bir istek şu durumlardaysa DUR ve net uyarı ver:
- Fiziksel/matematiksel imkânsız (ör. ulaşılamaz uzunluk/hacim)
- Ek ücret/kota gerektiriyor
- Gizli/erişilemez veri gerektiriyor
- Güvenlik/etik sınır
Uyarı formatı: 🚩 [ne] · [neden] · [gerçekçi alternatif]

## ZAMAN DAMGASI & DENETİM PROTOKOLÜ (her işlemde)
Her anlamlı işlem şu döngüden geçer:
  [1] BAŞLA → damga: ISO-8601 UTC (Code'da `date -u +"%Y-%m-%dT%H:%M:%SZ"`)
  [2] YAP → işlemi gerçekleştir
  [3] DENETLE → DENETÇİ rubric'i uygular
  [4] ÖĞREN → çıkarımı BILGI_TABANI.md'ye tek satır ekle
  [5] BİTİR → damga + AUDIT_LOG.jsonl'a kayıt
Bir sonraki işlem, [4]'te öğrenileni girdi olarak kullanır (zincir).

AUDIT_LOG.jsonl satır formatı:
{"ts_start":"...","ts_end":"...","islem":"...","uzmanlar":[...],
 "girdi_ozet":"...","cikti_ozet":"...","denetim":"GECTI|KALDI",
 "ogrenim":"...","onceki_ogrenim_kullanildi":"evet|hayir"}

## ÖĞRENME DÖNGÜSÜ (self-improving — model değil, bilgi tabanı büyür)
Her çalışmada:
- Yeni bir şey öğrenildiyse → BILGI_TABANI.md'ye "## [tarih] — [konu]" başlığıyla ekle
- Bir sonraki görev, ilgili başlıkları önce okur, sonra iş yapar
- Böylece sistem her gün daha bilgili başlar (kümülatif hafıza)

## ÇIKTI SÖZLEŞMESİ
Her cevabın sonunda:
--- 
⏱️ Damga: [UTC] · 🔍 Denetim: [GEÇTİ/KALDI] · 📚 Öğrenim: [1 satır] · 
🔗 Önceki öğrenim kullanıldı: [evet/hayır]

## DİL
Türkçe. Terse, komut-tipi, McKinsey Kıdemli Ortak tonu. 
Yapılandırılmış, kopyala-yapıştır hazır çıktı. Genel/boş dil yok.
```

---

## 5. GECELİK EĞİTİM TAKVİMİ & ROUTINE (7/24 — gerçekçi versiyon)

Sende **Scheduled** (Home), **Routines** ve **Dispatch (Beta)** (Code) var. Gerçek "her gece" mekanizması bunlardır.

### 5.1 Kurulum — 3 yol
- **Chat/Home → Scheduled:** Bir prompt'u seç, tekrar aralığı ver (her gece 03:00). Basit, tıkla-kur.
- **Code → Routines:** Kod tabanlı gecelik görev; bash + gerçek zaman damgası + dosya yazma.
- **Code → Dispatch (Beta):** Arka planda otonom görev tetikleme.

### 5.2 GECELİK ROUTINE PROMPT'U (kopyala → Scheduled/Routines'e yapıştır)

```
# GECELİK ÖĞRENME & ÜRETİM DÖNGÜSÜ — her gece 03:00

Bugünün UTC damgasını al (Code'da: date -u). Sonra sırayla:

FAZ 1 — OKU (damga)
- Şu kaynaklardan son 24 saatin önemli gelişmelerini tara:
  · Anthropic Engineering blog / prompt & agent kılavuzları (halka açık)
  · OpenAI, Google DeepMind, Meta AI halka açık blog/dokümanları
  · İşine dair alan (performance marketing / programmatic / e-ticaret)
- Her kaynaktan en fazla 3 sinyal çıkar. Telif: uzun alıntı yok, kendi cümlenle.

FAZ 2 — KURUL (damga)
- 6 uzman personayla 5 dakikalık "kurul toplantısı" simüle et
- Çıktı: 1 sayfa toplantı notu (karar + aksiyon maddeleri)

FAZ 3 — DAMIT & YAZ (damga)
- Bugünün öğrenimlerini BILGI_TABANI.md'ye "## [UTC-tarih]" başlığıyla ekle
- Bir önceki gecenin öğrenimini oku, bugünküyle çeliştiği yeri işaretle

FAZ 4 — ÜRET (damga)
- Bugünün bilgisiyle 1 somut deliverable üret (bkz. GELIR_MOTORU.md)
- Örn: yeni bir skill/agent taslağı, ya da işine dair bir analiz

FAZ 5 — DENETLE & KAYDET (damga)
- DENETÇİ rubric'i uygula (aşağıda)
- AUDIT_LOG.jsonl'a tam satır ekle
- KARAR_LOGU.md'ye özet + tarih ekle

Her fazın başı ve sonu damgalı. Bir sonraki gece, bu gecenin 
BILGI_TABANI + AUDIT_LOG kayıtlarını girdi alır (zincir).
```

### 5.3 Haftalık ritim (öneri)
| Gün | Odak |
|---|---|
| Pzt | Yeni **skill** üretimi + test |
| Sal | **Agent** kütüphanesi genişletme |
| Çar | **MCP/entegrasyon** deneme |
| Per | **Gelir motoru** çıktısı (Bölüm 7) |
| Cum | Haftalık **denetim & konsolidasyon** |
| Cmt/Paz | Hafif: makale okuma + bilgi tabanı temizliği |

---

## 6. ZAMAN DAMGASI + DENETİM PROTOKOLÜ (kanıtlanabilir versiyon)

### 6.1 Gerçek damga nasıl alınır
- **Code (CLI) — kanıtlanabilir:** `date -u +"%Y-%m-%dT%H:%M:%SZ"` → gerçek sistem saati, log dosyasına yazılır. **Tercih edilen yol.**
- **Chat/Scheduled:** Modele verilen tarihi kullanır (yaklaşık). Kesin kanıt gerekiyorsa Code kullan.

### 6.2 Denetim rubric'i (DENETÇİ bunu uygular)
Her çıktı 6 kritere göre GEÇTİ/KALDI alır:
1. **Doğruluk** — iddialar kaynağa dayanıyor mu?
2. **Yoğunluk** — dolgu var mı? (varsa KALDI)
3. **Uygulanabilirlik** — kopyala-yapıştır çalışır mı?
4. **Zincir** — önceki öğrenim kullanıldı mı?
5. **Damga** — baş-son UTC damgası var mı?
6. **Kırmızı bayrak** — imkânsız/ücretli/gizli bir şey sessizce kabul edildi mi? (edildiyse KALDI)

KALDI alırsa → düzelt → tekrar denetle → sonra kaydet.

### 6.3 Zincirleme (senin "bir sonraki işlemde tekrar train et" isteğin)
```
İşlem N: yap → öğren → ÖĞRENİM_N'i BILGI_TABANI'na yaz → damga
İşlem N+1: ÖĞRENİM_N'i OKU → onunla yeni işi yap → ÖĞRENİM_(N+1) → damga
...her gece tekrar
```
Bu, "modelin yeniden eğitilmesi" değil ama **davranışsal olarak aynı sonucu** verir: sistem her adımda birikmiş bilgiyle çalışır.

---

## 7. GELİR ÜRETİM MEKANİZMASI — [SENİ BURAYA YÖNLENDİRİYORUM]

**Dürüst gerçek:** Prompt tek başına para üretmez. Gelir, bu sistemi **gerçek, faturalanabilir işine** bağladığında oluşur. Sende zaten güçlü gelir kaynakları var; sistemi bunlardan birine "üretim hattı" olarak koşarız.

### Seçenekler — hangisine bağlayalım? (bana söyle, o bölümü doldurayım)

| # | İşin | Sistem ne üretir (gecelik) | Gelir yolu |
|---|---|---|---|
| A | **İBB Kültür AŞ medya planı** | Rakip/etkinlik verisi taraması, bütçe senaryoları, tab güncellemeleri | Ajans hizmet bedeli / proje |
| B | **VESTRA** (medikal scrubs) | Rakip fiyat izleme, paid media ROAS modeli güncelleme, ürün açıklaması | E-ticaret satışı |
| C | **Movéa** (premium scrubs) | Marka içerik üretimi, LinkedIn/sosyal varlık, pazar analizi | Marka satışı |
| D | **Tahmin Uzmanı** (AI ajans sistemi) | Prompt v-serisi iyileştirme, ajan kütüphanesi, öz-geliştirme döngüsü | SaaS / lisans |
| E | **Response DGA yeni iş** | Otomatik pitch deck taslakları, rakip analizi, outreach metinleri | Yeni müşteri geliri |

### Gelir motoru iskeleti (seçim yapınca netleşir)
```
GELIR_MOTORU.md:
- HEDEF İŞ: [A/B/C/D/E]
- GECELİK ÇIKTI: [somut deliverable]
- KALİTE EŞİĞİ: [DENETÇİ rubric geçmeli]
- TESLİM: [nereye/nasıl] 
- ÖLÇÜM: [hangi metrik parayla ilişkili]
```

> **Aksiyon:** Bana "Gelir motorunu **[X]**'e bağla" de. Ben de o iş için gecelik üretim prompt'unu, teslim akışını ve ölçüm çerçevesini bu belgeye eklerim.

---

## 8. TERS MÜHENDİSLİK ŞABLONLARI — kendi bileşenini üret (kopyala-doldur)

### 8.1 Boş SKILL şablonu
```markdown
---
name: [kısa-ad]
description: [NE yapar + NE ZAMAN tetiklenir. Bu satır kritik — tetikleyici.]
---
# [Başlık]
## Ne zaman kullan
- [durum 1]
## Nasıl yap
1. [adım]
## Örnek
[somut örnek]
```

### 8.2 Boş AGENT şablonu
```markdown
---
name: [ad]
description: [uzmanlık alanı + ne zaman çağrılır]
tools: Read, Edit, Bash
---
Sen [rol]sün. Görevin: [net görev].
Çıktı formatı: [sözleşme].
```

### 8.3 Boş COMMAND şablonu
```markdown
---
description: [ne yapar]
---
[talimat]. Framework'ü otomatik algıla. Kenar durumları kapsa.
```

### 8.4 Boş HOOK (settings.json)
```json
{ "hooks": { "PostToolUse": [{ "matcher": "Edit",
  "hooks": [{ "type":"command", "command":"[komut]" }] }] } }
```

### 8.5 aitmpl.com'dan hazır kurma
```
npx claude-code-templates@latest --agent [kategori]/[ad] --yes
npx claude-code-templates@latest --command [kategori]/[ad] --yes
npx claude-code-templates@latest --mcp [kategori]/[ad] --yes
npx claude-code-templates@latest --hook [kategori]/[ad] --yes
```
Önce kur → çalıştır → içini aç (düz metin) → **kendine göre değiştir** = tersine mühendislik tamam.

---

## 9. HALKA AÇIK KAYNAKLAR (damıtılacak — "top ekiplerin materyali")

İç veri değil, **halka açık** ve meşru kaynaklar. Gecelik döngü bunları tarar:
- **Anthropic:** Engineering blog, prompt engineering & agent building kılavuzları, `anthropics/skills` ve `anthropics/claude-code` (GitHub, resmi)
- **OpenAI:** halka açık cookbook/blog
- **Google DeepMind / Google AI:** halka açık teknik blog
- **Meta AI / diğer:** halka açık araştırma özetleri
- **Topluluk:** `wshobson/agents`, `obra/superpowers` (aitmpl.com'un kaynak gösterdiği MIT repolar)

> Not: "Eğitimlerini alıp sınavla doğrulama" = iç veriyi kopyalamak değil. Yaptığımız: halka açık en iyi pratikleri damıtıp **kendi rubric'inle** sistemin çıktısını doğrulamak.

---

## 10. 30 DAKİKADA BAŞLA (kontrol listesi)

- [ ] claude.ai → **Projects** → "CLAUDE OTONOM SİSTEM" oluştur
- [ ] Bölüm 4 master prompt'u → Custom Instructions'a yapıştır
- [ ] Bilgi dosyalarını oluştur (BILGI_TABANI, KARAR_LOGU, AUDIT_LOG, UZMAN_KURULU)
- [ ] Claude Code kur → `.claude/` klasörü aç
- [ ] aitmpl.com'dan 2-3 örnek bileşen kur (Bölüm 8.5) → içini incele
- [ ] Bölüm 8 şablonlarıyla **1 kendi skill'ini** üret + test et
- [ ] Bölüm 5.2 gecelik routine'i → **Scheduled/Routines**'e kur (03:00)
- [ ] Gerçek damga için Code'da `date -u` çalıştığını doğrula
- [ ] Bana "Gelir motorunu **[X]**'e bağla" de → Bölüm 7'yi özelleştireyim

---

### KAPANIŞ
Bu belge, senin vizyonunun **çalışan** hâlidir: imkânsız uzunluk/otonom-train yerine, gerçek özellikler (Scheduled/Routines/Dispatch), gerçek zaman damgası (Code `date`), gerçek kümülatif hafıza (bilgi tabanı) ve gerçek gelir bağlantısı (senin işin) üzerine kurulu. Sıradaki adım tek: **gelir motorunu hangi işine bağlayacağını söyle**, gerisini bu iskelete işleyelim.
