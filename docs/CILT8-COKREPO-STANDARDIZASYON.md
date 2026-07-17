# CİLT 8 — ÇOK-REPO STANDARDİZASYON ANAYASASI
> Üretim: 2026-07-17 · Kapsam: metinduraktr-44 altındaki TÜM repolar · Motor: scripts/standardize_repo.py + .github/workflows/repo-health.yml
> İlke: her repo "elit OSS" community-health standardına taşınır — AMA repo-tipine göre, güvenli ve sadece-ekleme yöntemiyle.

## 0. KİMLİK
Bu cilt, sahibin 7 reposunu (adops-agents, claude-otonom-sistem, or-na.com, a-agency-tahmin-uzman-, performer-growth-hub, VizaTrack, cigkoftem-web-app) dünyanın en saygın açık-kaynak projelerinin (kubernetes, react, rust, vscode) yapısal desenine göre standardize eden operasyon anayasasıdır. Kaynak araştırma: docs/ARASTIRMA-OSS-STANDARTLARI (özet aşağıda).

## 1. ELİT STANDART (GitHub Community Profile + top-repo deseni)
Bir repoyu "0 → elit" taşıyan kontrol listesi (kaynak: docs.github.com community-profile + kubernetes/react/rust anatomisi):
- **README** (hero+badge → TL;DR → quickstart → features → install → usage → roadmap → contributing → license)
- **LICENSE** (default'lanamaz — repo başına bilinçli karar)
- **CODE_OF_CONDUCT.md** (Contributor Covenant)
- **CONTRIBUTING.md**
- **SECURITY.md** (zafiyet bildirim kanalı)
- **.github/ISSUE_TEMPLATE/*.yml** (form) + config.yml (blank_issues_enabled: false)
- **.github/PULL_REQUEST_TEMPLATE.md** (neden/ne/test/checklist)
- **.github/dependabot.yml** (npm + github-actions)
- **CODEOWNERS**, **ROADMAP.md/Projects v2**, **CHANGELOG.md** (repo tipine göre)

## 2. REPO-TİPİNE GÖRE FARKLAR (kritik)
| Öğe | sistem/OSS | web-uygulaması | ürün/marka |
|---|---|---|---|
| Sahte issue/PR/agency simülasyonu | Yalnız açık-kaynak sistemlerde (adops gibi) meşru | ❌ YAKIŞMAZ | ❌ KESİNLİKLE YASAK |
| LICENSE (MIT) | Tercihe bağlı | Dikkat: açık-kaynağa çevirir | ❌ Tescilli IP; MIT basma |
| FUNDING.yml | Uygun | Nadir | Hayır |
| SemVer + CHANGELOG | Zorunlu | Opsiyonel | Genelde gerekmez |
| Community-health dosyaları | Evet | Evet | Evet (güvenli, additive) |

**Altın kural:** community-health dosyaları (SECURITY/COC/CONTRIBUTING/şablonlar/dependabot) HER repoya güvenlidir — kodu/README'yi/LICENSE'ı ezmez. Sahte issue/agency simülasyonu SADECE açık-kaynak sistem repolarına (adops-agents) uygulanır; gerçek ürün/marka repolarına ASLA.

## 3. MOTOR (scripts/standardize_repo.py)
- Kullanım: `python3 scripts/standardize_repo.py <repo_dir> <tip> <ad> [--funding]`
- Tip: system | webapp | app | product
- Davranış: yalnızca EKSİK dosyayı ekler (idempotent); mevcut README/kod/LICENSE'a dokunmaz.
- 2026-07-17 koşumu: 6 repoya community-health tamamlandı (adops zaten tamdı).

## 4. GÜNLÜK SİSTEM (.github/workflows/repo-health.yml)
- Her gün 06:00 UTC: `standardize_repo.py`'yi umbrella'daki repo listesine karşı DRY-RUN çalıştırır, eksik dosya matrisi üretir → docs/REPO-SAGLIK-MATRISI.md.
- Gerçek uygulama (dosya ekleme + push) için `REPO_PAT` secret'ı gerekir (opsiyonel); yoksa yalnız rapor üretir (güvenli varsayılan).
- Böylece hiçbir repo sessizce standartın altına düşmez; sapma günlük raporla görünür.

## 5. LICENSE KARARI (🚩 SAHİBE BIRAKILDI)
6 reponun hiçbirinde LICENSE yok. Çoğu tescilli marka/ürün (Movéa, çiğköfte, Performer, VizaTrack) + IP_NOTICE taşıyor. MIT basmak istenmeden açık-kaynağa çevirir (geri-alınamaz). Karar sahibindir:
- Açık-kaynak istenen sistem repoları (adops MIT zaten) → MIT eklenebilir.
- Tescilli ürünler → "All Rights Reserved" NOTICE veya LICENSE eklenmez.

## 6. DENETİM
Her standardizasyon koşumu claude-otonom-sistem/AUDIT_LOG.jsonl'e damgalanır; öğrenim BILGI_TABANI.md'ye düşer. Cilt 1-7 kuralları (5 güvenlik kuralı, sinyal>uzunluk, imkânsız istek 🚩) bu cildin üstündedir.
