# PUSH TALİMATI — GÜNCEL (2026-07-27 · K4)
> Cowork oturumlarının GitHub YAZMA yetkisi yok (salt-okunur proxy, 403 teyit 19+20+26+27 Tem ×2). Bundle-pull standart yöntem. 2 dakikalık iş.
>
> ⚡⚡ **28 Tem GÜNCELLEMESİ — Seçenek B fiilen GERÇEKLEŞTİ (kısmi):** Metin devir paketini GitHub-yazma-yetkili
> bir CCR (Claude Code Remote) oturumuna yapıştırdı; `scripts/daily_agency.py` + 4 F0 workflow +
> IS_LISTESI + bu dosya + AJANS-GUNLUK-GOZETIM + AUDIT union **origin/main'e API-push ile yazıldı**.
> Bu yol bundle-pull'a kalıcı alternatiftir. **Kalan kapsam:** 19-20 Tem bundle içerikleri (CILT5-8 docs,
> OZ-DENETIM-SORU-BANKASI, ROADMAP, KARAR_LOGU, GELIR_MOTORU, rol kartları, uretim/ dosyaları,
> SENKRON_LOG/UPSTREAM_SHA, K-017 v3 çıktıları) hâlâ Cowork projesi/bundle'larda — ya Metin yerel
> bundle-pull yapar ya da içerik CCR oturumuna parça parça yapıştırılır.

## ⚡ 27 Tem GÜNCELLEMESİ — adops için daha kolay yol
adops-agents 20260720 bundle'ı 27 Tem K4 koşumunda güncel main (44b4ad1) üzerine temiz merge edildi ve **çatışmasız yeni bundle** üretildi:
- **Dosya:** `uretim/devir/adops-agents-K4-onarim-20260727.bundle.base64` (projede, `local_path` ile doğrulanarak yazıldı) + 27 Tem konuşma eki (.bundle, doğrudan kullan)
- **SHA256 (.bundle):** `cf35e4189ceb3bcc2d423e7016d6ba1a713e197d4066e51c38dba91cae973cf2`
- **Uygulama (öncül = 27 Tem ucu; conflict beklenmez):**
```bash
cd adops-agents && git pull origin main
git pull adops-agents-K4-onarim-20260727.bundle main
git push origin main
```
claude-otonom-sistem için aşağıdaki 20260720 yolu geçerliliğini korur (45KB bundle oturum-içi yeniden aktarılamıyor — 07-26 kuralı; origin bu bundle'ın tabanından bağımsız ilerlediği için pull sırasında otomatik merge olur, sorun değil).

---

## (20 Tem · K4 ONARIM v2 — geçerli ana talimat)
> ⚠️ 19 Tem otonom bundle'ının PROJE KOPYASI BOZUK/KESİK çıktı (pack sha1 uyuşmadı — inline yazım hatası). 20 Tem koşumu içeriği kanonik proje dokümanlarından YENİDEN İNŞA etti; artık bundle'lar `local_path` ile yazılıyor ve yazım sonrası doğrulanıyor. **claude-otonom için geçerli devir: 20260720 bundle'ı.**

## Bundle dosyaları (iki kaynak)
1. **Konuşma eki:** 20 Tem K4 oturumunda SendUserFile ile gönderildi (.bundle olarak, base64'süz — doğrudan kullan). adops için 27 Tem eki daha güncel.
2. **Proje dokümanı (kalıcı):** `claude-otonom-sistem/uretim/devir/claude-otonom-K4-onarim-20260720.bundle.base64` (ve adops için üstteki 20260727) → `base64 -d dosya.base64 > dosya.bundle`

## SHA256 (indirme sonrası `sha256sum` ile doğrula)
```
b104c47d6f3c0a49c3144b55769d2a23e20130f02630156107912ed0d538e1c8  claude-otonom-K4-onarim-20260720.bundle
ff69ea69f28954b1eae163395894157650ab3e7ee7b835008d5dbc3d06cdc8f8  adops-agents-K4-onarim-20260720.bundle (yerine 20260727 önerilir)
cf35e4189ceb3bcc2d423e7016d6ba1a713e197d4066e51c38dba91cae973cf2  adops-agents-K4-onarim-20260727.bundle
```

## Uygulama (yerel makinede)
```bash
# 1) claude-otonom-sistem — 2 commit (b785122 → d49e84d → c08f5a1)
cd claude-otonom-sistem && git pull origin main
git pull claude-otonom-K4-onarim-20260720.bundle main
git push origin main

# 2) adops-agents — üstteki 27 Tem bloğunu kullan (çatışmasız)
```
claude-otonom bundle'ı 20 Tem sabahki origin ucu (b785122) üzerine kurulu — origin o günden beri otomatik commit'lerle ilerledi; `git pull origin main` sonrası bundle pull'unda merge otomatik olur (dosya kümeleri ayrık, conflict beklenmez).
> ⚠️ 28 Tem notu: origin artık CCR-push edilmiş IS_LISTESI/PUSH-TALIMATI/AUDIT kopyalarını içeriyor —
> bundle-pull'da bu dosyalarda conflict çıkarsa çözüm kuralı: iki tarafın da satırları KORUNUR (union,
> silme yok); şüphede en-güncel-damgalı blok üstte.

## Seçenek B — Cowork'a GitHub bağla (kalıcı çözüm)
claude.ai → Settings → Connectors → GitHub → `metinduraktr-44/*` yazma izni. Sonraki günlük koşumlar doğrudan push eder; bundle devri biter.
> ⚡ 28 Tem: Bu seçeneğin CCR-oturumu varyantı fiilen çalıştı (üstteki güncelleme).

## İçerik — claude-otonom-sistem (c08f5a1)
docs/: CILT5 (jeneratörden birebir, 1021 doğrulandı) + CILT6 + CILT7 + CILT8 + EGITIM-PROGRAMI + ORG-SEMASI + OZ-DENETIM-SORU-BANKASI (859, jeneratörden) · kök: ROADMAP + IS_LISTESI (#18 dahil) + KARAR_LOGU (K-018'e kadar) + GELIR_MOTORU (5 kanal) + BILGI_TABANI + AUDIT_LOG (union, 29 satir) · katalog/: UPSTREAM_SHA (50a1263) + SENKRON_LOG (3 satır) · pilots/: 4 ORG-EGITIM · uretim/: gunluk 07-17/07-19/07-20-MKT-SOC + haftalık paket + mcp-uyum + seo + agentic-makale + adcp + sosyal-dinleme-monitoru · scripts/: org_uret.py + soru_bankasi_uret.py (İş #17 kısmi — yeniden inşa edildi).
**Hâlâ kayıp (İş #17):** istirak_uret.py · departman_meta.py · rol_karti_uret.py · 1247 rol kartı · VERSIONS.md. ~~daily_agency.py + 4 workflow~~ ✅ **27 Tem K4-3'te YENİDEN ÜRETİLDİ + 28 Tem CCR'de origin'e PUSH EDİLDİ.**
**Push sonrası ayrıca işlenecek (proje dokümanlarından):** 07-21→27 üretimleri (mcp-uyum-denetcisi agent · makale v2 + yayın paketi · 93-config tarama raporu · MED-CRE/MED-LOC günlükleri · rakip-fiyat-izleme · tr-yerellestirme-stil-kilavuzu) + SENKRON_LOG 4-7. satırlar + güncel BILGI_TABANI + **İş #17 restorasyonu:** ~~scripts/daily_agency.py + 4 workflow~~ ✅ origin'de (org.json için repoda `python3 scripts/daily_agency.py --org-json` koşulur; doğrulama: `--dogrula` → "46 departman, rotasyon birebir")

## İçerik — adops-agents (20260727 bundle: 49d58ce + merge 619545c)
docs/ORG-BAGLANTI.md (MKT-PRF org bağı + K-014 holding deltası) — 27 Tem ucuna merge edilmiş hâli.

## Push sonrası
`AJANS-GUNLUK-GOZETIM` yeşile döner; İş #15/#18/#20/#21 `.claude/` yerleşimleri ve İş #17 kalan jeneratörler (istirak_uret/departman_meta/rol_karti_uret + kartlar + VERSIONS) sıradaki koşumlarda. İş #2: workflow dosyaları artık origin'de — `workflow_dispatch` teyidi koşulabilir. İş #3: ANTHROPIC_API_KEY'i GitHub → Settings → Secrets → Actions'a Metin ekler (chat'e yapıştırılan anahtar için rotasyon önerildi).
