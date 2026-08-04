# OZ-DENETIM SORU BANKASI (532 soru)
> Uretim: 2026-08-04T09:40:02Z · Kaynak: scripts/build_question_bank.py · data/soru_bankasi.json
Her ajan her surecte kendine bu sorulari sorar. Gunluk dongu (daily_agency.py) her kosumda ornekler ve standup'ta yanitlar. Kart basina alt-set: departman + kademe bloklari; tam banka (bu dosya) her title'a acik.

## Ozet: Evrensel 119 · Departman 386 (46 departman) · Kademe 27 · **Toplam 532**

## A. Evrensel sorular (tum roller)
### Strateji
1. Bu is ajansin ceyreklik OKR'inin hangisine hizmet ediyor; etmiyorsa neden kuyrukta?
2. Bugunku en yuksek etkili 3 aksiyonu dogru siraladim mi; kanit ne?
3. Bu karari 3 ay sonra savunabilir miyim; hangi varsayima dayaniyor?
4. Rakip/pazar hareketine 7 gun icinde POV urettim mi?
5. Kaynagi en yuksek marjinal getiriye mi tahsis ettim, aliskanliga mi?
6. Bu hedef matematiksel olarak mumkun mu; degilse kirmizi bayrak verdim mi?
### Yurutme
1. Cikti kopyala-yapistir hazir mi; alici ek is yapmadan kullanabilir mi?
2. Bir sonraki adimin sahibi ve tarihi net mi?
3. Bloklayici 4 saati asti mi; astiysa eskale ettim mi?
4. Bu gorevi tekrarlanabilir bir checklist'e donusturebilir miyim?
5. Dunku taahhudumu bugun kapattim mi; kapatmadiysam neden?
6. Isi en kucuk calisan parcaya boldum mu?
### Kalite-Dogrulama
1. 6 katmanin (structural/integrity/semantic/reference/known-patterns/review) hepsinden gecti mi?
2. SHA256 butunluk satiri guncel mi?
3. Bagimsiz bir gozle (ikinci ajan) review aldim mi?
4. Rework oranim artiyor mu; kok neden ne?
5. Bu ciktida tehlikeli desen (enjeksiyon/SSRF) taramasi yaptim mi?
### Veri-Durustlugu
1. Sundugum her sayi gercek bir kaynaktan mi; tahminleri acikca etiketledim mi?
2. Orneklem buyuklugu sonucu tasiyacak kadar mi?
3. Anomaliyi buyukluk + hipotezle mi raporladim?
4. KPI'nin tanimi yazili mi; tanimsiz metrik yayinlamadim degil mi?
5. Korelasyonu nedensellik gibi sunmadim degil mi?
### Guvenlik
1. Resmi kaynak (Anthropic/MCP) varken toplulук kaynagina mi gittim?
2. Script bundle eden bileşeni okumadan/ozetlemeden calistirdim mi?
3. 'Son commit dun' diye guvenlik varsaydim mi (guncellik yanilgisi)?
4. Kurulumu kanonik org'dan mi yaptim, fork'tan mi?
5. Marketplace-oncelik katmanini kontrol ettim mi?
### Gelir
1. Bu is 5 gelir kanalindan hangisini ilerletiyor?
2. Inbound lead yolu (README->iletisim) calisir durumda mi?
3. Referral firsatini kacirdim mi?
4. Pipeline degerini bu hafta guncelledim mi?
5. Bir sponsor/vendor gorusmesini ilerletmek icin bugun ne yaptim?
### Ogrenme
1. Bugun en az 1 kaynak (changelog/makale) okudum mu; ogrenimi damittim mi?
2. Bu ogrenim BILGI_TABANI.md'ye tek satir olarak girdi mi?
3. Departmanimin platformunda bu hafta ne degisti; takip ettim mi?
4. Ilgili sertifika/egitimden bir modul tamamladim mi?
5. Bir beta/yeni urun ozelligini test edip not aldim mi?
6. Onceki kosumun ciktisini okudum mu (zincir kirilmadi mi)?
### Toplanti
1. Standup satirim dun/bugun/blocker formatinda ve tek satir mi?
2. Tutanakta karar + aksiyon(sahip+tarih) + risk + bayrak var mi?
3. Kurul kararina K-no verdim mi?
4. Toplanti ciktisiz mi bitti (ciktisiz toplanti yok)?
### Eskalasyon
1. Butce/politika riskini fin/leg'e ilettim mi?
2. Imkansiz hedefi [ne]-[neden]-[alternatif] formatinda mi verdim?
3. Sessiz kalip riski gomdum mu?
4. Cross-departman cakismayi dogru mercie tasidim mi?
### Olcumleme
1. Bu aksiyonun basarisini hangi metrikle ve ne zaman olcecegim?
2. Atif modeli/olcum yontemi playbook'ta belgeli mi?
3. Holdout/artimsallik dusundum mu?
4. Dashboard SLA'sini tutturdum mu?
### Dokumantasyon
1. Bu isi baska bir ajan benim yardimim olmadan tekrarlayabilir mi?
2. Artefakti zaman damgaladim mi?
3. Playbook'u guncel tuttum mu?
### Onceliklendirme
1. P0 isleri gercekten P0 mi; yoksa kolay olani mi once yaptim?
2. Biten isi arsive tasidim mi?
3. Is listesini bugun yeniden onceliklendirdim mi?
### Risk
1. Bu degisikligin geri-alma (rollback) plani var mi?
2. En kotu senaryo ne; sinyalini nasil erken yakalarim?
3. Tek nokta bagimlilik yarattim mi?
### Isbirligi
1. Yukari/yatay/asagi arayuzlerimi bugun bilgilendirdim mi?
2. Baska bir departmanin isini kolaylastirmak icin ne yaptim?
3. Devrettigim isin sahibi net mi?
### Etik-Uyum
1. Reklam politikasi acisindan bu cikti temiz mi?
2. KVKK/GDPR acisindan veri isleme uygun mu?
3. Lisans (MIT) hijyenine uydum mu?
4. Gercek kisilere atfen sahte icerik uretmedim degil mi?
### Otomasyon
1. Bu manuel isi bir workflow'a cevirebilir miyim?
2. Actions yesil mi; kirmiziysa 24h icinde mudahale ettim mi?
3. Idempotent mi calisiyor (yeniden kosum bozmuyor mu)?
### Musteri
1. Bu cikti bir musteri sorusunu/ihtiyacini gercekten cozuyor mu?
2. Rapor anlatisi sayi+baglam+sonraki adim iceriyor mu?
3. Churn/risk sinyalini 14 gun onceden isaretledim mi?
### Inovasyon-Beta
1. Bu hafta hangi beta urunu/ozelligi denedim; bulgum ne?
2. Rakiplerin denemedigi bir aci buldum mu?
3. Deneyi hipotez->tasarim->kosum->ogrenim dongusuyle mi yuruttum?
### Makale-Icerik
1. Bugunun makalesi kaynakli, TR ozetli ve CTA'li mi?
2. Icerik ajansin inbound hunisine hizmet ediyor mu?
3. Editoryal rotasyondan siradaki konuyu sectim mi?
### Oz-Gelisim
1. Bu rolun ilk-30-gun hedeflerinin neresindeyim?
2. Anti-desenlerimden birine bugun dustum mu?
3. Bir sonraki kademeye hazirlik icin hangi beceriyi gelistiriyorum?
### Egitim-Sertifika
1. Rolumle ilgili bir sertifika modulunu bu hafta ilerlettim mi?
2. Yeni ogrendigim bir teknigi bir ciktiya uyguladim mi?
3. Ekipteki baska bir ajana ogrettigim bir sey oldu mu?
4. Bilgi acigimi isimlendirdim mi; kapatma plani ne?
### Panel-Guncelleme
1. Departmanimin platform changelog'unu bu hafta okudum mu?
2. Bir API/politika degisikligi mevcut kurulumu etkiliyor mu; migration gerekli mi?
3. Deprecation/sunset uyarisi var mi; takvime aldim mi?
4. Yeni bir panel ozelligi is akisimi hizlandirir mi?
### Kaynak-Okuma
1. Bugun okudugum kaynagin URL'ini nota ekledim mi?
2. Okudugumdan cikan tek somut aksiyon ne?
3. Kaynagin guvenilirligini (resmi>capraz-konsensus>gecmis>yildiz) degerlendirdim mi?
4. Celisen iki kaynagi nasil uzlastirdim?
### Surec-Zinciri
1. Bu kosum onceki kosumun ciktisini girdi aldi mi?
2. ts_start ve ts_end damgaladim mi?
3. Zincir kirilirsa DENETCI bulgusu duser mi; kontrol ettim mi?
4. Bir sonraki kosuma net bir girdi biraktim mi?
### Pazar-Rekabet
1. Rakip bir hamle yapti mi; 7 gun icinde POV cikardim mi?
2. Sektor benchmark'imi bu ay tazeledim mi?
3. Rakiplerin sahiplenmedigi bir konumlanma acigi var mi?
4. Bir pazar sinyalini erken yakalayip aksiyona cevirdim mi?
### Verimlilik-Token
1. Ciktiyi minimum token ile (progressive disclosure) mi urettim?
2. Ayni analizi tekrarladim mi; BILGI_TABANI'nda zaten var miydi?
3. Agir icerigi docs/'a koyup karti kisa mi tuttum?
4. Coklu benzer islemi tek cagrida grupladim mi?
5. Dolgu cumle urettim mi; sinyal/uzunluk oranim iyi mi?
### Toparlama-Retro
1. Bu is bolumunun retrosundan tek satir ogrenim cikti mi?
2. Tekrar eden bir hatayi kalici duzelttim mi (kok neden)?
3. Bir sonraki sprint icin tasinacak riski isaretledim mi?
### Sahiplik-Hesapverebilirlik
1. Bu isin tek net sahibi ben miyim; belirsizlik biraktim mi?
2. Bir hatayi savunmaya gecmeden sahiplendim mi?
3. Taahhut ettigim tarihi tutuyor muyum; tutmuyorsam erken haber verdim mi?
4. Baskasinin isini beklerken kendi tarafimi hazir tuttum mu?
5. Kararimin kanitini (link/commit/dosya) biraktim mi?
6. Bu cikti icin 'definition of done' karsilandi mi?
7. Bugun ajansi bir adim ileri goturen en somut sey neydi?
8. Yarina devrettigim en kritik acik madde ne; sahibi kim?
9. Bu isi bastan yapsam neyi farkli yapardim?
10. Olcebildigim bir ilerleme kaydettim mi, yoksa sadece mesgul mu gorundum?

## B. Departman sorulari
### ENG-PLT — Platform Mühendisliği
1. Platform Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Platform Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Platform Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Altyapı Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Altyapı Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Altyapı Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. API Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
8. API Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
9. API Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
10. Platform Mühendisliği departmani ana ciktisi (platform bileşen bakımı + API sözleşme denetimi) hedefte mi; sapma varsa kok neden ve duzeltme ne?
11. Platform Mühendisliği icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### ENG-APP — Uygulama Geliştirme
1. Backend Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Backend Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Backend Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Frontend Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Frontend Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Frontend Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Mobil Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
8. Mobil Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
9. Mobil Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
10. Uygulama Geliştirme departmani ana ciktisi (pilot paketleri için uygulama bileşeni üretimi) hedefte mi; sapma varsa kok neden ve duzeltme ne?
11. Uygulama Geliştirme icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### ENG-DEV — DevOps & SRE
1. DevOps Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. DevOps Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. DevOps Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Site Güvenilirlik Mühendisi (SRE) birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Site Güvenilirlik Mühendisi (SRE) ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Site Güvenilirlik Mühendisi (SRE) alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. DevOps & SRE departmani ana ciktisi (workflow sağlığı + gecelik döngü nöbeti) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. DevOps & SRE icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### ENG-QA — Kalite & Test
1. Test Otomasyon Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Test Otomasyon Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Test Otomasyon Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. QA Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. QA Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. QA Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Kalite & Test departmani ana ciktisi (6 katman doğrulama koşumu + validate.py bakımı) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Kalite & Test icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### AI-RES — AI Araştırma
1. AI Araştırmacısı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. AI Araştırmacısı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. AI Araştırmacısı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Model Değerlendirme Uzmanı (Evals) birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Model Değerlendirme Uzmanı (Evals) ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Model Değerlendirme Uzmanı (Evals) alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. AI Araştırma departmani ana ciktisi (günlük literatür/repo taraması → BILGI_TABANI damıtımı) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. AI Araştırma icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### AI-AGT — Ajan Mühendisliği
1. Ajan Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Ajan Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Ajan Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Orkestrasyon Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Orkestrasyon Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Orkestrasyon Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Araç (Tool) Entegrasyon Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
8. Araç (Tool) Entegrasyon Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
9. Araç (Tool) Entegrasyon Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
10. Ajan Mühendisliği departmani ana ciktisi (yeni ajan bileşeni üretimi (CILT2 şablonu)) hedefte mi; sapma varsa kok neden ve duzeltme ne?
11. Ajan Mühendisliği icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### AI-PRM — Prompt & Context Mühendisliği
1. Prompt Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Prompt Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Prompt Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Context Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Context Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Context Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Prompt & Context Mühendisliği departmani ana ciktisi (pilot promptlarının v-serisi iyileştirmesi) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Prompt & Context Mühendisliği icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### AI-SAF — AI Güvenliği & Hizalama
1. Hizalama Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Hizalama Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Hizalama Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Red-Team Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Red-Team Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Red-Team Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. AI Güvenliği & Hizalama departmani ana ciktisi (5 güvenlik kuralı denetimi + script inceleme (Kural 2)) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. AI Güvenliği & Hizalama icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### DAT-ENG — Veri Mühendisliği
1. Veri Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Veri Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Veri Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Veri Boru Hattı Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Veri Boru Hattı Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Veri Boru Hattı Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Veri Mühendisliği departmani ana ciktisi (AUDIT_LOG/BILGI_TABANI veri bütünlüğü) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Veri Mühendisliği icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### DAT-SCI — Veri Bilimi
1. Veri Bilimci birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Veri Bilimci ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Veri Bilimci alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Makine Öğrenmesi Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Makine Öğrenmesi Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Makine Öğrenmesi Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Veri Bilimi departmani ana ciktisi (pilot metrik modelleri (tahmin/fiyat)) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Veri Bilimi icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### DAT-BI — Analitik & BI
1. BI Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. BI Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. BI Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Veri Görselleştirme Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Veri Görselleştirme Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Veri Görselleştirme Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Analitik & BI departmani ana ciktisi (haftalık konsolide paket metrikleri) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Analitik & BI icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### PRD-MGT — Ürün Yönetimi
1. Ürün Yöneticisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Ürün Yöneticisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Ürün Yöneticisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Teknik Ürün Yöneticisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Teknik Ürün Yöneticisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Teknik Ürün Yöneticisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Ürün Yönetimi departmani ana ciktisi (bileşen yol haritası önceliklendirme) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Ürün Yönetimi icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### PRD-DSN — Tasarım
1. Ürün Tasarımcısı (UX) birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Ürün Tasarımcısı (UX) ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Ürün Tasarımcısı (UX) alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Arayüz Tasarımcısı (UI) birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Arayüz Tasarımcısı (UI) ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Arayüz Tasarımcısı (UI) alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Tasarım Sistemi Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
8. Tasarım Sistemi Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
9. Tasarım Sistemi Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
10. Tasarım departmani ana ciktisi (pilot arayüz/şablon tasarımları) hedefte mi; sapma varsa kok neden ve duzeltme ne?
11. Tasarım icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### PRD-OPS — Ürün Operasyonları
1. Ürün Operasyon Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Ürün Operasyon Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Ürün Operasyon Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Kullanıcı Araştırmacısı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Kullanıcı Araştırmacısı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Kullanıcı Araştırmacısı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Ürün Operasyonları departmani ana ciktisi (kullanım geri bildirimi → KARAR_LOGU girdisi) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Ürün Operasyonları icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### MKT-BRD — Marka & İçerik
1. Marka Stratejisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Marka Stratejisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Marka Stratejisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. İçerik Pazarlama Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. İçerik Pazarlama Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. İçerik Pazarlama Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Marka & İçerik departmani ana ciktisi (Movéa pilotu marka içerik üretimi) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Marka & İçerik icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### MKT-PRF — Performans Pazarlama (AdOps)
1. Performans Pazarlama Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Performans Pazarlama Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Performans Pazarlama Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Medya Satın Alma Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Medya Satın Alma Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Medya Satın Alma Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Atıf (Attribution) Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
8. Atıf (Attribution) Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
9. Atıf (Attribution) Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
10. Performans Pazarlama (AdOps) departmani ana ciktisi (Response DGA dikeyi: kampanya/atıf analizi) hedefte mi; sapma varsa kok neden ve duzeltme ne?
11. Performans Pazarlama (AdOps) icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### MKT-SEO — SEO & Organik Büyüme
1. SEO Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. SEO Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. SEO Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. İçerik Optimizasyon Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. İçerik Optimizasyon Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. İçerik Optimizasyon Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. SEO & Organik Büyüme departmani ana ciktisi (repo/ürün sayfası görünürlük artışı) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. SEO & Organik Büyüme icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### MKT-SOC — Sosyal Medya
1. Sosyal Medya Yöneticisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Sosyal Medya Yöneticisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Sosyal Medya Yöneticisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Topluluk Yöneticisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Topluluk Yöneticisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Topluluk Yöneticisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Sosyal Medya departmani ana ciktisi (LinkedIn yayın akışı (movea komutu ile)) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Sosyal Medya icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### REV-SLS — Satış
1. Satış Temsilcisi (AE) birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Satış Temsilcisi (AE) ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Satış Temsilcisi (AE) alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Satış Geliştirme Temsilcisi (SDR) birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Satış Geliştirme Temsilcisi (SDR) ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Satış Geliştirme Temsilcisi (SDR) alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Satış departmani ana ciktisi (ajans lead hunisi takibi (GELIR_MOTORU kanal 5)) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Satış icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### REV-PRT — İş Ortaklıkları
1. Ortaklık Yöneticisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Ortaklık Yöneticisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Ortaklık Yöneticisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Sponsorluk Geliştirme Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Sponsorluk Geliştirme Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Sponsorluk Geliştirme Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. İş Ortaklıkları departmani ana ciktisi (infra sponsorluk adayları (kanal 1) izleme) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. İş Ortaklıkları icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### REV-CSM — Müşteri Başarısı
1. Müşteri Başarı Yöneticisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Müşteri Başarı Yöneticisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Müşteri Başarı Yöneticisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Onboarding Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Onboarding Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Onboarding Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Müşteri Başarısı departmani ana ciktisi (pilot iç müşteri memnuniyet döngüsü) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Müşteri Başarısı icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### REV-OPS — Gelir Operasyonları
1. RevOps Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. RevOps Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. RevOps Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. CRM Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. CRM Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. CRM Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Gelir Operasyonları departmani ana ciktisi (gelir kanalı metrik panosu) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Gelir Operasyonları icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### MED-PUB — Yayıncılık & Makale
1. Teknik Yazar birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Teknik Yazar ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Teknik Yazar alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Editör birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Editör ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Editör alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Araştırma Yazarı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
8. Araştırma Yazarı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
9. Araştırma Yazarı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
10. Yayıncılık & Makale departmani ana ciktisi (GÜNDE MİN. 1 makale/güncelleme üretimi) hedefte mi; sapma varsa kok neden ve duzeltme ne?
11. Yayıncılık & Makale icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### MED-CRE — Video & Kreatif
1. Video Editörü birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Video Editörü ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Video Editörü alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Grafik Tasarımcısı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Grafik Tasarımcısı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Grafik Tasarımcısı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Video & Kreatif departmani ana ciktisi (tanıtım/kreatif varlık üretimi) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Video & Kreatif icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### MED-LOC — Yerelleştirme (TR)
1. Yerelleştirme Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Yerelleştirme Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Yerelleştirme Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Çevirmen-Editör birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Çevirmen-Editör ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Çevirmen-Editör alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Yerelleştirme (TR) departmani ana ciktisi (katalog bileşenlerinin TR/dikey uyarlaması) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Yerelleştirme (TR) icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### OPS-PMO — Program Yönetimi (PMO)
1. Program Yöneticisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Program Yöneticisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Program Yöneticisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Proje Koordinatörü birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Proje Koordinatörü ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Proje Koordinatörü alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Program Yönetimi (PMO) departmani ana ciktisi (günlük iş listesi dağıtımı + takip) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Program Yönetimi (PMO) icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### OPS-BIZ — İş Operasyonları
1. İş Operasyon Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. İş Operasyon Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. İş Operasyon Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Süreç İyileştirme Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Süreç İyileştirme Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Süreç İyileştirme Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. İş Operasyonları departmani ana ciktisi (operasyon ritmi (CILT6) uygulaması) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. İş Operasyonları icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### OPS-TLS — Araç & Tedarik
1. Araç Yönetim Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Araç Yönetim Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Araç Yönetim Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Tedarik Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Tedarik Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Tedarik Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Araç & Tedarik departmani ana ciktisi (araç envanteri + maliyet izleme) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Araç & Tedarik icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### FIN-FPA — Finansal Planlama (FP&A)
1. FP&A Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. FP&A Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. FP&A Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Bütçe Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Bütçe Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Bütçe Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Finansal Planlama (FP&A) departmani ana ciktisi (token/kredi bütçe takibi) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Finansal Planlama (FP&A) icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### FIN-ACC — Muhasebe & Raporlama
1. Muhasebe Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Muhasebe Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Muhasebe Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Finansal Raporlama Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Finansal Raporlama Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Finansal Raporlama Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Muhasebe & Raporlama departmani ana ciktisi (aylık finansal özet) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Muhasebe & Raporlama icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### FIN-REV — Gelir Motoru İzleme
1. Gelir Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Gelir Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Gelir Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Monetizasyon Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Monetizasyon Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Monetizasyon Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Gelir Motoru İzleme departmani ana ciktisi (GELIR_MOTORU.md 5 kanal KPI'ları) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Gelir Motoru İzleme icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### SEC-OPS — Güvenlik Operasyonları
1. Güvenlik Operasyon Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Güvenlik Operasyon Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Güvenlik Operasyon Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Olay Müdahale Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Olay Müdahale Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Olay Müdahale Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Güvenlik Operasyonları departmani ana ciktisi (günlük güvenlik taraması) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Güvenlik Operasyonları icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### SEC-AUD — Uyum Denetimi (5 Kural)
1. Denetçi (Auditor) birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Denetçi (Auditor) ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Denetçi (Auditor) alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Bileşen Güvenlik İnceleme Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Bileşen Güvenlik İnceleme Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Bileşen Güvenlik İnceleme Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Uyum Denetimi (5 Kural) departmani ana ciktisi (her yeni bileşen: 5 kural + script inceleme onayı) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Uyum Denetimi (5 Kural) icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### SEC-SUP — Tedarik Zinciri Güvenliği
1. Tedarik Zinciri Güvenlik Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Tedarik Zinciri Güvenlik Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Tedarik Zinciri Güvenlik Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Bağımlılık İzleme Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Bağımlılık İzleme Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Bağımlılık İzleme Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Tedarik Zinciri Güvenliği departmani ana ciktisi (upstream/bağımlılık değişiklik kontrolü) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Tedarik Zinciri Güvenliği icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### HRA-REC — Ajan İşe Alım
1. Ajan İşe Alım Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Ajan İşe Alım Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Ajan İşe Alım Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Yetenek Haritalama Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Yetenek Haritalama Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Yetenek Haritalama Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Ajan İşe Alım departmani ana ciktisi (katalogdan rol-bileşen eşleştirme (işe alım)) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Ajan İşe Alım icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### HRA-PRF — Performans & Kalite
1. Performans Değerlendirme Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Performans Değerlendirme Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Performans Değerlendirme Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Kalite Güvence Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Kalite Güvence Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Kalite Güvence Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Performans & Kalite departmani ana ciktisi (ajan çıktı kalite puanlama) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Performans & Kalite icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### HRA-LRN — Eğitim & Bilgi Tabanı
1. Bilgi Tabanı Küratörü birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Bilgi Tabanı Küratörü ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Bilgi Tabanı Küratörü alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Öğrenim Damıtma Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Öğrenim Damıtma Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Öğrenim Damıtma Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Eğitim & Bilgi Tabanı departmani ana ciktisi (BILGI_TABANI.md küratörlüğü (append-only)) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Eğitim & Bilgi Tabanı icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### LGL-LIC — Lisans Uyumu (MIT)
1. Lisans Uyum Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Lisans Uyum Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Lisans Uyum Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Atıf (Attribution) Denetçisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Atıf (Attribution) Denetçisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Atıf (Attribution) Denetçisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Lisans Uyumu (MIT) departmani ana ciktisi (MIT atıf bütünlüğü (LICENSE-UPSTREAM)) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Lisans Uyumu (MIT) icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### LGL-PRV — Veri Gizliliği
1. Gizlilik Uzmanı (KVKK/GDPR) birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Gizlilik Uzmanı (KVKK/GDPR) ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Gizlilik Uzmanı (KVKK/GDPR) alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Veri Sınıflandırma Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Veri Sınıflandırma Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Veri Sınıflandırma Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Veri Gizliliği departmani ana ciktisi (pilot verilerinde gizlilik kontrolü) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Veri Gizliliği icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### INF-MCP — MCP Entegrasyonları
1. MCP Entegrasyon Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. MCP Entegrasyon Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. MCP Entegrasyon Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Bağlayıcı (Connector) Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Bağlayıcı (Connector) Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Bağlayıcı (Connector) Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. MCP Entegrasyonları departmani ana ciktisi (MCP kataloğu bakım + yeni bağlayıcı değerlendirme) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. MCP Entegrasyonları icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### INF-SET — Ayar & Yapılandırma
1. Yapılandırma Yöneticisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Yapılandırma Yöneticisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Yapılandırma Yöneticisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Ortam (Environment) Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Ortam (Environment) Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Ortam (Environment) Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Ayar & Yapılandırma departmani ana ciktisi (settings şablonları + ortam standartları) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Ayar & Yapılandırma icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### INF-HKS — Hooks & Otomasyon
1. Hook Geliştirici birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Hook Geliştirici ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Hook Geliştirici alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Otomasyon Mühendisi birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Otomasyon Mühendisi ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Otomasyon Mühendisi alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Hooks & Otomasyon departmani ana ciktisi (damga/denetim hook zinciri bakımı) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Hooks & Otomasyon icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### INF-LOP — Döngüler & Zamanlama
1. Döngü Operatörü birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Döngü Operatörü ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Döngü Operatörü alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Zamanlama (Scheduler) Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Zamanlama (Scheduler) Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Zamanlama (Scheduler) Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Döngüler & Zamanlama departmani ana ciktisi (nightly + daily-agency + upstream-sync nöbeti) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Döngüler & Zamanlama icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### STR-INT — Pazar İstihbaratı
1. Pazar İstihbarat Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Pazar İstihbarat Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Pazar İstihbarat Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Trend Araştırmacısı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Trend Araştırmacısı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Trend Araştırmacısı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Pazar İstihbaratı departmani ana ciktisi (günlük ekosistem taraması (CILT3 haritası)) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Pazar İstihbaratı icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### STR-CMP — Rakip Analizi
1. Rakip Analiz Uzmanı birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Rakip Analiz Uzmanı ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Rakip Analiz Uzmanı alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Kıyaslama (Benchmark) Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Kıyaslama (Benchmark) Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Kıyaslama (Benchmark) Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Rakip Analizi departmani ana ciktisi (muadil repo/ürün kıyaslama raporu) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Rakip Analizi icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?
### STR-GRW — Büyüme & Yatırım
1. Büyüme Stratejisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
2. Büyüme Stratejisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
3. Büyüme Stratejisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
4. Yatırım Analisti birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?
5. Yatırım Analisti ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?
6. Yatırım Analisti alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?
7. Büyüme & Yatırım departmani ana ciktisi (gelir kanalı büyüme deneyleri) hedefte mi; sapma varsa kok neden ve duzeltme ne?
8. Büyüme & Yatırım icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?

## C. Kademe sorulari
### C-LEVEL
1. Ajans OKR attainment'i %80 ustunde mi; degilse kurtarma plani ne?
2. Bir faz kapisini kanitsiz GECTI saymadim degil mi?
3. Mikro-yonetime kaydim mi; yetkiyi dogru devrettim mi?
4. Sahibe danismadan bir taahhut verdim mi?
5. 5 gelir kanalinin hepsinin sahibi ve durumu net mi?
6. Kurul gundemini kanit-linkli hazirladim mi?
### EVP
1. Departman OKR skoru guncel mi; kirmizi OKR icin plan var mi?
2. Kadroyu asiri yukledim mi; kapasite dengeli mi?
3. Playbook'u merge oncesi onayladim mi?
4. Haftalik departman raporu yayinlandi mi?
5. Sponsor C-level'a haftalik raporladim mi?
### DIRECTOR
1. Birim backlog'u dogru onceliklendi mi?
2. Uzman ciktisini publish oncesi review ettim mi?
3. Birim retrosundan ogrenim damittim mi?
4. Cross-unit cakismayi EVP'ye tasidim mi?
### LEAD
1. Is akisi standardi/checklist guncel mi?
2. Uzman gorevlerini gunluk atadim/review ettim mi?
3. Haftalik is akisi ozetini yazdim mi?
4. Riski metrik kanitiyla mi bayrakladim?
### SPECIALIST
1. Ciktim kopyala-hazir ve checklist'li mi?
2. Bu hafta playbook'a 1 iyilestirme onerdim mi?
3. Isi metrik gerekcesi olmadan mi sundum?
4. Damgasiz cikti biraktim mi?
### ANALYST
1. Veri kesitim tanim-ekli mi?
2. Anomaliyi buyukluk+hipotezle mi isaretledim?
3. Tahmini acikca etiketledim mi?
4. Veri uydurmadim degil mi?
