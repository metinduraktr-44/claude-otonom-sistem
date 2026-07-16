# CİLT 2 — BİLEŞEN PROMPT KÜTÜPHANESİ (repo-doğrulanmış)
### aitmpl.com'un 8 bileşen tipi için ayrı ayrı detaylı master prompt
**Kaynak:** `github.com/davila7/claude-code-templates` (gerçek dosya yapısı incelendi) · **Kapsam:** Chat + Code + Cowork · **Dil:** Türkçe
**Bağlam:** Bu belge Cilt 1'in (Proje Anayasası) devamıdır. Umbrella mimari, gecelik takvim ve gelir çerçevesi Cilt 1'de; burada **her kategori için üretim + gecelik iyileştirme prompt'u** var.

---

## 0. REPO GERÇEĞİ (doğrulanmış — varsayım değil)

**Dizin yapısı:**
```
cli-tool/components/
├── agents/[kategori]/*.md          # 600+ ajan
├── commands/[kategori]/*.md        # 200+ komut
├── mcps/[kategori]/*.json          # 55+ MCP
├── settings/[kategori]/*.json      # 60+ ayar
├── hooks/[kategori]/*.json         # 39+ kanca
└── skills/[kategori]/*/SKILL.md    # yüzlerce yetenek (progressive disclosure)
```
Web katalogundaki sayılar (853/421/281...) kürasyonlu/tekilleştirilmiş sayımlardır; repodaki ham sayılar üsttekiler.

**Kurulum komutları (gerçek):**
```
npx claude-code-templates@latest --agent [kategori]/[ad] --yes
npx claude-code-templates@latest --command [kategori]/[ad] --yes
npx claude-code-templates@latest --mcp [kategori]/[ad] --yes
npx claude-code-templates@latest --setting [kategori]/[ad] --yes
npx claude-code-templates@latest --hook [kategori]/[ad] --yes
npx claude-code-templates@latest --skill [ad]   # örn: pdf-anthropic,docx,xlsx,pptx
```

**Gerçek doğrulama sistemi (senin "denetleme/doğrulama/zaman damgası" katmanının temeli):**
1. **Structural Validator** — dosya formatı, YAML frontmatter, zorunlu alanlar, encoding
2. **Integrity Validator** — SHA256 hash + sürüm takibi (kurcalama tespiti)
3. **Semantic Validator** — zararlı desen, prompt injection, tehlikeli komut tespiti
4. **Reference Validator** — dış URL doğrulama, SSRF engelleme
5. **SkillSpector** (NVIDIA, Apache-2.0) — 64 açık deseni, statik `--no-llm` (API key gerekmez)
6. **component-reviewer** alt-ajanı — HER bileşen değişikliğini commit'ten önce denetler

> Bu 6 katman, senin "her işlem sonunda doğrula + zaman damgası" isteğinin **gerçek, çalışan** karşılığıdır. Aşağıdaki her kategori prompt'u bu katmanlara bağlanır.

---

## HER KATEGORİ PROMPT'UNUN ORTAK "DENETİM KUYRUĞU"

Aşağıdaki 8 prompt'un her birinin sonuna bu blok eklenir (kopyalarken dahil et):

```
## DENETİM & ZAMAN DAMGASI KUYRUĞU (zorunlu)
1. ts_start = date -u +"%Y-%m-%dT%H:%M:%SZ"   (Code'da gerçek; Chat'te verilen tarih)
2. Üretimi yap
3. 4+2 doğrulayıcıyı uygula:
   [ ] Structural: frontmatter tam mı, zorunlu alanlar var mı
   [ ] Integrity: dosyanın SHA256'sını hesapla, VERSIONS.md'ye yaz
   [ ] Semantic: prompt injection / tehlikeli komut var mı
   [ ] Reference: dış URL güvenli mi (SSRF yok)
   [ ] SkillSpector mantığı: bilinen açık deseni var mı
   [ ] component-reviewer: bağımsız gözle son kontrol
4. Sonuç: GEÇTİ → kaydet | KALDI → düzelt → 3'e dön
5. ts_end damgası + AUDIT_LOG.jsonl'a satır
6. Öğrenimi BILGI_TABANI.md'ye ekle → bir sonraki gece girdi olur (zincir)
Çıktı altbilgisi: ⏱️[ts_start→ts_end] 🔍[GEÇTİ/KALDI] 📚[öğrenim] 🔗[önceki kullanıldı?]
```

---

# 1️⃣ SKILLS (Yetenekler)

**Ne (doğrulanmış):** Anthropic'in *progressive disclosure* deseniyle Claude'un bağlama göre **otomatik yüklediği** modüler yetenek. Model-invoked: kullanıcı "PDF"/"database"/"Excel" deyince ilgili skill kendiliğinden aktifleşir. Gerçek örnekler: `pdf-processing-pro`, `algorithmic-art`, `mcp-builder`, `canvas-design`, `docx`, `xlsx`, `pptx`, `artifacts-builder`.

**Gerçek anatomi (`SKILL.md`):**
```markdown
---
name: [kisa-ad]
description: [NE yapar + NE ZAMAN tetiklenir — kritik satır]
allowed-tools: Read, Write, Bash, Grep, Glob
model: sonnet
user-invocable: true
---
# [Başlık]
[Kimlik: "Sen ... uzmanısın"]
## Ne zaman aktifleş
## Adım adım yordam
## Örnekler
## Referanslar (references/ klasörü — büyük içerik burada, ana dosya kısa)
```

**Üretim + gecelik iyileştirme prompt'u:**
```
Rol: BAŞ MİMAR + PROMPT MÜHENDİSİ.
Görev: [alan] için bir SKILL üret.
Kurallar:
- description'ı TETİKLEYİCİ olarak yaz: "Use when [tetikleyiciler]". 
  Bu %80 iş. Kötü description = skill hiç aktifleşmez.
- Ana SKILL.md kısa olsun; ağır içerik references/ altına (progressive disclosure).
- allowed-tools'u minimal tut (en az yetki ilkesi).
Gecelik döngü:
- Dün üretilen skill'lerin tetiklenme oranını değerlendir (hangi bağlamda çağrıldı/çağrılmadı)
- En zayıf 1 description'ı yeniden yaz, test senaryosu üret, doğrula
- BILGI_TABANI'na "hangi description kalıbı daha iyi tetikliyor" öğrenimini ekle
+ ORTAK DENETİM KUYRUĞU
```
Kurulum: `npx claude-code-templates@latest --skill [ad]`

---

# 2️⃣ AGENTS (Ajanlar)

**Ne (doğrulanmış):** Belirli alanın uzmanı alt-model. `.md` dosyası. Claude Agent SDK ile **global** çalıştırılabilir (`--create-agent` → her yerden çağrılır). Gerçek örnekler: `code-reviewer`, `security-auditor`, `react-expert`, `database-architect`, `deployer`, `component-reviewer`.

**Gerçek anatomi (CONTRIBUTING'den):**
```markdown
---
name: [ad]
description: [uzmanlık + ne zaman çağrılır]
tools: Read, Edit, Bash
model: sonnet
---
# [Ajan Adı]
[Amaç]
## Expertise
- Alan bilgisi / yetkinlikler / kullanım durumları
## Instructions
[Claude'a nasıl davranacağı — net]
## Examples
[Pratik örnekler]
```

**Üretim + gecelik iyileştirme prompt'u:**
```
Rol: BAŞ MİMAR.
Görev: [alan] uzmanı bir AGENT üret.
Kurallar:
- Çıktı sözleşmesi zorunlu: sorun → kanıt → düzeltme (kod bloğu).
- tools alanını görevin gerektirdiği minimumla sınırla.
- component-reviewer mantığıyla kendini denetleyecek bir "self-check" bölümü ekle.
Global ürünleştirme (GELİR):
- npx claude-code-templates@latest --create-agent [ad]
- Sonra her yerden: [ad] "görev" → müşteriye satılabilir mikro-hizmet
Gecelik döngü:
- Ajanların dünkü çıktılarını rubric'e vur; en çok "KALDI" alan ajanın Instructions'ını iyileştir
- Yeni bir uzmanlık boşluğu tespit et → yeni ajan taslağı üret
+ ORTAK DENETİM KUYRUĞU
```
Kurulum: `npx claude-code-templates@latest --agent [kategori]/[ad] --yes`

---

# 3️⃣ COMMANDS (Komutlar)

**Ne (doğrulanmış):** Özel slash komutları; `.md` dosyası. Gerçek örnekler: `/generate-tests`, `/optimize-bundle`, `/check-security`, `/setup-testing`, `/security-audit`.

**Gerçek anatomi:**
```markdown
---
description: [ne yapar]
---
# /[komut-adı]
[Kısa açıklama]
[Talimat: framework'ü otomatik algıla, kenar durumları kapsa, çıktı formatı belirt]
```

**Üretim + gecelik iyileştirme prompt'u:**
```
Rol: OTOMASYON MÜHENDİSİ.
Görev: sık tekrar eden [iş] için bir COMMAND üret.
Kurallar:
- Tek amaç, net girdi/çıktı. Komut "sihirli düğme" gibi olmalı.
- Parametre gerekiyorsa $ARGUMENTS kullan.
Gecelik döngü:
- Dün en çok elle tekrarlanan işi tespit et → onu komuta dönüştür
- Mevcut komutlardan kullanılmayanı arşivle (sadeleştirme)
+ ORTAK DENETİM KUYRUĞU
```
Kurulum: `npx claude-code-templates@latest --command [kategori]/[ad] --yes`

---

# 4️⃣ SETTINGS (Ayarlar)

**Ne (doğrulanmış):** Claude Code yapılandırma dosyaları (`.json`). Gerçek örnekler: `performance/mcp-timeouts`, `read-only-mode`, `statusline/*`.

**Gerçek anatomi (`settings.json` parçası):**
```json
{
  "permissions": { "allow": ["Read","Edit"], "deny": ["Bash(rm*)"] },
  "env": { "MCP_TIMEOUT": "30000" },
  "statusLine": { "type": "command", "command": "..." }
}
```

**Üretim + gecelik iyileştirme prompt'u:**
```
Rol: OTOMASYON MÜHENDİSİ + DENETÇİ.
Görev: güvenli ve verimli bir SETTING profili üret.
Kurallar:
- En az yetki: tehlikeli komutları deny'a al (rm, force-push).
- Timeout/memory değerlerini iş yüküne göre ayarla.
Gecelik döngü:
- Dün oluşan hataları (timeout, izin reddi) tara → ilgili ayarı düzelt
- read-only-mode gereken bağlamları işaretle
+ ORTAK DENETİM KUYRUĞU
```
Kurulum: `npx claude-code-templates@latest --setting [kategori]/[ad] --yes`

---

# 5️⃣ HOOKS (Kancalar)

**Ne (doğrulanmış):** Olay-tetikli otomasyon; genelde `.json`. Gerçek örnekler: `git/pre-commit-validation`, `git/prevent-force-push`, `automation/simple-notifications`. **Zaman damgası mekanizmanın motoru budur.**

**Gerçek anatomi:**
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit",
      "hooks": [{ "type": "command",
        "command": "echo \"$(date -u +%Y-%m-%dT%H:%M:%SZ) EDIT $CLAUDE_FILE_PATHS\" >> AUDIT_LOG.jsonl" }]
    }],
    "Stop": [{ "hooks": [{ "type":"command", "command":"npm run lint" }] }]
  }
}
```

**Üretim + gecelik iyileştirme prompt'u:**
```
Rol: OTOMASYON MÜHENDİSİ.
Görev: her işleme GERÇEK zaman damgası basan + doğrulama çalıştıran HOOK'lar üret.
Kurallar:
- PostToolUse → her Edit/Write sonrası date -u damgası + AUDIT_LOG.jsonl'a satır
- PreToolUse → tehlikeli komutu engelle (prevent-force-push mantığı)
- Stop → lint/test + component-reviewer çağrısı
Gecelik döngü:
- AUDIT_LOG'u tara; damgasız kalan işlem var mı → kanca boşluğunu kapat
+ ORTAK DENETİM KUYRUĞU
```
Kurulum: `npx claude-code-templates@latest --hook [kategori]/[ad] --yes`

---

# 6️⃣ MCPs (Model Context Protocol Entegrasyonları)

**Ne (doğrulanmış):** Dış servis bağlayıcıları (`.mcp.json`). Gerçek örnekler: `database/neon`, `development/github-integration`, `database/postgresql-integration`. Sende zaten bağlı MCP'ler var (Gmail, Drive, Notion, Slack, Shopify, HubSpot, Supermetrics, Figma vb.).

**Gerçek anatomi (`.mcp.json`):**
```json
{
  "mcpServers": {
    "github": { "command": "npx", "args": ["-y","@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" } }
  }
}
```

**Üretim + gecelik iyileştirme prompt'u:**
```
Rol: BAŞ MİMAR + İŞ/GELİR STRATEJİSTİ.
Görev: işine değer katan MCP zincirini kur.
Kurallar:
- Sır yönetimi: token'ları env'den al, asla dosyaya gömme (Reference Validator).
- Her MCP için "ne zaman kullan" notu yaz.
GELİR bağlantısı:
- Supermetrics/HubSpot MCP → performans raporu otomasyonu (faturalanabilir)
- Shopify MCP → VESTRA/Movéa ürün-envanter otomasyonu
Gecelik döngü:
- Dün hangi MCP çağrısı başarısız/yavaş → düzelt; yeni entegrasyon boşluğu tespit et
+ ORTAK DENETİM KUYRUĞU
```
Kurulum: `npx claude-code-templates@latest --mcp [kategori]/[ad] --yes`
🚩 Not: Bazı MCP'ler (dış API'ler) ücretli kota harcar — bağlarken kontrol et.

---

# 7️⃣ LOOPS (Döngüler)

**Ne:** Yinelemeli, kendine-referanslı iş akışı zincirleri (üret → değerlendir → iyileştir → tekrar). Repoda daha az standartlaştırılmış; senin "her gece tekrarla + zincirleme öğrenme" isteğinin doğrudan karşılığı. Cilt 1'deki öğrenme döngüsü = bir Loop tanımıdır.

**Anatomi (öneri — komut+hook birleşimi):**
```
LOOP: gecelik-iyilestirme
  girdi: dünkü AUDIT_LOG + BILGI_TABANI
  adımlar: OKU → DAMIT → ÜRET → DENETLE(4+2) → KAYDET → DAMGA
  çıkış koşulu: DENETÇİ GEÇTİ verene kadar iterasyon
  zincir: bu iterasyonun öğrenimi → sonraki iterasyonun girdisi
```

**Üretim prompt'u:**
```
Rol: OTOMASYON MÜHENDİSİ.
Görev: [amaç] için sonsuz-değil-kontrollü bir LOOP tasarla.
Kurallar:
- Her iterasyon damgalı; maksimum iterasyon sınırı koy (maliyet kontrolü 🚩).
- Çıkış koşulu net (DENETÇİ GEÇTİ / N iterasyon / süre).
- Zincirleme: iterasyon N'in öğrenimi N+1'e girdi.
+ ORTAK DENETİM KUYRUĞU
```
Kurulum: Scheduled/Routines'e gecelik prompt olarak koşulur (Cilt 1, Bölüm 5).

---

# 8️⃣ PLUGINS (Eklentiler)

**Ne (doğrulanmış):** Paketlenmiş bileşen setleri; marketplace üzerinden kurulur. Gerçek komut: `/plugin install <ad>@<marketplace>`. Kurulanlar dashboard'da otomatik görünür. `--plugins` ile yönetim paneli açılır.

**Anatomi (plugin = bir marketplace altında gruplanmış agent+command+skill+hook seti):**
```
marketplace/[plugin-adi]/
├── agents/*.md
├── commands/*.md
├── skills/*/SKILL.md
└── plugin.json   (meta: ad, sürüm, bileşen listesi)
```

**Üretim + gecelik iyileştirme prompt'u:**
```
Rol: BAŞ MİMAR.
Görev: kendi işine özel bir PLUGIN paketle (örn. "performance-marketing-suite").
İçerik: ilgili tüm skill/agent/command/hook'ları tek pakette topla.
GELİR: bu paketi bir ürün/lisans olarak konumla (Tahmin Uzmanı ile örtüşür).
Gecelik döngü:
- Pakete yeni doğrulanmış bileşen ekle; sürümü artır (Integrity Validator: SHA256+version)
+ ORTAK DENETİM KUYRUĞU
```
Yönetim: `npx claude-code-templates@latest --plugins`

---

## 9. GLOBAL AJAN = SOMUT GELİR MEKANİZMASI (repo-doğrulanmış)

Repoda gerçek bir ürünleştirme yolu var — bunu gelir motoruna bağlarız:
```
# Bir kez kur
npx claude-code-templates@latest --create-agent [ad]
# Her yerden çağır (terminal, CI, script)
[ad] "görev tanımı"
# Yönet
npx claude-code-templates@latest --list-agents
npx claude-code-templates@latest --update-agent [ad]
```
**Ürün fikri:** İşine özel global ajanlar (ör. `pmarketing-auditor`, `scrubs-copywriter`, `ibb-media-planner`) → müşteriye "AI mikro-hizmet" olarak sunulur. Her çağrı faturalanabilir çıktı üretir. Bu, "prompt tek başına para üretmez" sorununun **gerçek çözümüdür**: ajanı işine koşarsın, çıktı satılır.

---

## 10. CİLT 1 + CİLT 2 KURULUM SIRASI (birleşik)

1. **Chat:** Claude Project "CLAUDE OTONOM SİSTEM" → Cilt 1 Ana Master Prompt'u custom instructions'a
2. **Code:** `.claude/` altına Cilt 2'deki 8 kategoriden en az birer örnek üret + `--hook` ile zaman-damga kancasını kur
3. **Doğrulama:** 4+2 doğrulayıcı kuyruğunu her üretime bağla; VERSIONS.md + AUDIT_LOG.jsonl aç
4. **Gecelik:** Cilt 1 Bölüm 5 routine'ini Scheduled/Routines'e koş (03:00), Loop olarak zincirle
5. **Gelir:** `--create-agent` ile işine özel global ajan üret → Bölüm 9 ürün modeli
6. **Bana söyle:** Gelir motorunu **hangi işine** bağlayayım (İBB Kültür AŞ / VESTRA / Movéa / Tahmin Uzmanı / Response DGA) → o iş için gecelik üretim prompt'unu + teslim akışını Cilt 3 olarak yazarım.

---

### KAPANIŞ
Cilt 2, senin "her kategori için ayrı detaylı prompt" isteğinin **repo-doğrulanmış** karşılığıdır: 8 kategorinin gerçek anatomisi, gerçek kurulum komutları, her biri için üretim + gecelik iyileştirme prompt'u, ve hepsinin bağlandığı **gerçek 6 katmanlı denetim/zaman-damga sistemi**. Eksik tek girdi: gelir motorunun hangi işine bağlanacağı. Onu söyle, Cilt 3'te uçtan uca kuralım.
