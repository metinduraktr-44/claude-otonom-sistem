#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_question_bank.py — 500+ oz-denetim sorusu bankasini deterministik uretir.
Yapi: A) Evrensel (tum roller) + B) Departman (org.json aileleri) + C) Kademe.
Cikti: data/soru_bankasi.json + docs/OZ-DENETIM-SORU-BANKASI.md
Kaynak taksonomi: kullanicinin verdigi 501-soru deseni + .claude/org/org.json
Kullanim: python3 scripts/build_question_bank.py   (once --org-json uretilmis olmali)
"""
import json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORG = os.path.join(ROOT, ".claude", "org", "org.json")
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# ---- A) EVRENSEL SORULAR (tum roller) — kategori: [sorular]
EVRENSEL = {
 "Strateji": [
  "Bu is ajansin ceyreklik OKR'inin hangisine hizmet ediyor; etmiyorsa neden kuyrukta?",
  "Bugunku en yuksek etkili 3 aksiyonu dogru siraladim mi; kanit ne?",
  "Bu karari 3 ay sonra savunabilir miyim; hangi varsayima dayaniyor?",
  "Rakip/pazar hareketine 7 gun icinde POV urettim mi?",
  "Kaynagi en yuksek marjinal getiriye mi tahsis ettim, aliskanliga mi?",
  "Bu hedef matematiksel olarak mumkun mu; degilse kirmizi bayrak verdim mi?",
 ],
 "Yurutme": [
  "Cikti kopyala-yapistir hazir mi; alici ek is yapmadan kullanabilir mi?",
  "Bir sonraki adimin sahibi ve tarihi net mi?",
  "Bloklayici 4 saati asti mi; astiysa eskale ettim mi?",
  "Bu gorevi tekrarlanabilir bir checklist'e donusturebilir miyim?",
  "Dunku taahhudumu bugun kapattim mi; kapatmadiysam neden?",
  "Isi en kucuk calisan parcaya boldum mu?",
 ],
 "Kalite-Dogrulama": [
  "6 katmanin (structural/integrity/semantic/reference/known-patterns/review) hepsinden gecti mi?",
  "SHA256 butunluk satiri guncel mi?",
  "Bagimsiz bir gozle (ikinci ajan) review aldim mi?",
  "Rework oranim artiyor mu; kok neden ne?",
  "Bu ciktida tehlikeli desen (enjeksiyon/SSRF) taramasi yaptim mi?",
 ],
 "Veri-Durustlugu": [
  "Sundugum her sayi gercek bir kaynaktan mi; tahminleri acikca etiketledim mi?",
  "Orneklem buyuklugu sonucu tasiyacak kadar mi?",
  "Anomaliyi buyukluk + hipotezle mi raporladim?",
  "KPI'nin tanimi yazili mi; tanimsiz metrik yayinlamadim degil mi?",
  "Korelasyonu nedensellik gibi sunmadim degil mi?",
 ],
 "Guvenlik": [
  "Resmi kaynak (Anthropic/MCP) varken toplulук kaynagina mi gittim?",
  "Script bundle eden bileşeni okumadan/ozetlemeden calistirdim mi?",
  "'Son commit dun' diye guvenlik varsaydim mi (guncellik yanilgisi)?",
  "Kurulumu kanonik org'dan mi yaptim, fork'tan mi?",
  "Marketplace-oncelik katmanini kontrol ettim mi?",
 ],
 "Gelir": [
  "Bu is 5 gelir kanalindan hangisini ilerletiyor?",
  "Inbound lead yolu (README->iletisim) calisir durumda mi?",
  "Referral firsatini kacirdim mi?",
  "Pipeline degerini bu hafta guncelledim mi?",
  "Bir sponsor/vendor gorusmesini ilerletmek icin bugun ne yaptim?",
 ],
 "Ogrenme": [
  "Bugun en az 1 kaynak (changelog/makale) okudum mu; ogrenimi damittim mi?",
  "Bu ogrenim BILGI_TABANI.md'ye tek satir olarak girdi mi?",
  "Departmanimin platformunda bu hafta ne degisti; takip ettim mi?",
  "Ilgili sertifika/egitimden bir modul tamamladim mi?",
  "Bir beta/yeni urun ozelligini test edip not aldim mi?",
  "Onceki kosumun ciktisini okudum mu (zincir kirilmadi mi)?",
 ],
 "Toplanti": [
  "Standup satirim dun/bugun/blocker formatinda ve tek satir mi?",
  "Tutanakta karar + aksiyon(sahip+tarih) + risk + bayrak var mi?",
  "Kurul kararina K-no verdim mi?",
  "Toplanti ciktisiz mi bitti (ciktisiz toplanti yok)?",
 ],
 "Eskalasyon": [
  "Butce/politika riskini fin/leg'e ilettim mi?",
  "Imkansiz hedefi [ne]-[neden]-[alternatif] formatinda mi verdim?",
  "Sessiz kalip riski gomdum mu?",
  "Cross-departman cakismayi dogru mercie tasidim mi?",
 ],
 "Olcumleme": [
  "Bu aksiyonun basarisini hangi metrikle ve ne zaman olcecegim?",
  "Atif modeli/olcum yontemi playbook'ta belgeli mi?",
  "Holdout/artimsallik dusundum mu?",
  "Dashboard SLA'sini tutturdum mu?",
 ],
 "Dokumantasyon": [
  "Bu isi baska bir ajan benim yardimim olmadan tekrarlayabilir mi?",
  "Artefakti zaman damgaladim mi?",
  "Playbook'u guncel tuttum mu?",
 ],
 "Onceliklendirme": [
  "P0 isleri gercekten P0 mi; yoksa kolay olani mi once yaptim?",
  "Biten isi arsive tasidim mi?",
  "Is listesini bugun yeniden onceliklendirdim mi?",
 ],
 "Risk": [
  "Bu degisikligin geri-alma (rollback) plani var mi?",
  "En kotu senaryo ne; sinyalini nasil erken yakalarim?",
  "Tek nokta bagimlilik yarattim mi?",
 ],
 "Isbirligi": [
  "Yukari/yatay/asagi arayuzlerimi bugun bilgilendirdim mi?",
  "Baska bir departmanin isini kolaylastirmak icin ne yaptim?",
  "Devrettigim isin sahibi net mi?",
 ],
 "Etik-Uyum": [
  "Reklam politikasi acisindan bu cikti temiz mi?",
  "KVKK/GDPR acisindan veri isleme uygun mu?",
  "Lisans (MIT) hijyenine uydum mu?",
  "Gercek kisilere atfen sahte icerik uretmedim degil mi?",
 ],
 "Otomasyon": [
  "Bu manuel isi bir workflow'a cevirebilir miyim?",
  "Actions yesil mi; kirmiziysa 24h icinde mudahale ettim mi?",
  "Idempotent mi calisiyor (yeniden kosum bozmuyor mu)?",
 ],
 "Musteri": [
  "Bu cikti bir musteri sorusunu/ihtiyacini gercekten cozuyor mu?",
  "Rapor anlatisi sayi+baglam+sonraki adim iceriyor mu?",
  "Churn/risk sinyalini 14 gun onceden isaretledim mi?",
 ],
 "Inovasyon-Beta": [
  "Bu hafta hangi beta urunu/ozelligi denedim; bulgum ne?",
  "Rakiplerin denemedigi bir aci buldum mu?",
  "Deneyi hipotez->tasarim->kosum->ogrenim dongusuyle mi yuruttum?",
 ],
 "Makale-Icerik": [
  "Bugunun makalesi kaynakli, TR ozetli ve CTA'li mi?",
  "Icerik ajansin inbound hunisine hizmet ediyor mu?",
  "Editoryal rotasyondan siradaki konuyu sectim mi?",
 ],
 "Oz-Gelisim": [
  "Bu rolun ilk-30-gun hedeflerinin neresindeyim?",
  "Anti-desenlerimden birine bugun dustum mu?",
  "Bir sonraki kademeye hazirlik icin hangi beceriyi gelistiriyorum?",
 ],
 "Egitim-Sertifika": [
  "Rolumle ilgili bir sertifika modulunu bu hafta ilerlettim mi?",
  "Yeni ogrendigim bir teknigi bir ciktiya uyguladim mi?",
  "Ekipteki baska bir ajana ogrettigim bir sey oldu mu?",
  "Bilgi acigimi isimlendirdim mi; kapatma plani ne?",
 ],
 "Panel-Guncelleme": [
  "Departmanimin platform changelog'unu bu hafta okudum mu?",
  "Bir API/politika degisikligi mevcut kurulumu etkiliyor mu; migration gerekli mi?",
  "Deprecation/sunset uyarisi var mi; takvime aldim mi?",
  "Yeni bir panel ozelligi is akisimi hizlandirir mi?",
 ],
 "Kaynak-Okuma": [
  "Bugun okudugum kaynagin URL'ini nota ekledim mi?",
  "Okudugumdan cikan tek somut aksiyon ne?",
  "Kaynagin guvenilirligini (resmi>capraz-konsensus>gecmis>yildiz) degerlendirdim mi?",
  "Celisen iki kaynagi nasil uzlastirdim?",
 ],
 "Surec-Zinciri": [
  "Bu kosum onceki kosumun ciktisini girdi aldi mi?",
  "ts_start ve ts_end damgaladim mi?",
  "Zincir kirilirsa DENETCI bulgusu duser mi; kontrol ettim mi?",
  "Bir sonraki kosuma net bir girdi biraktim mi?",
 ],
 "Pazar-Rekabet": [
  "Rakip bir hamle yapti mi; 7 gun icinde POV cikardim mi?",
  "Sektor benchmark'imi bu ay tazeledim mi?",
  "Rakiplerin sahiplenmedigi bir konumlanma acigi var mi?",
  "Bir pazar sinyalini erken yakalayip aksiyona cevirdim mi?",
 ],
 "Verimlilik-Token": [
  "Ciktiyi minimum token ile (progressive disclosure) mi urettim?",
  "Ayni analizi tekrarladim mi; BILGI_TABANI'nda zaten var miydi?",
  "Agir icerigi docs/'a koyup karti kisa mi tuttum?",
  "Coklu benzer islemi tek cagrida grupladim mi?",
  "Dolgu cumle urettim mi; sinyal/uzunluk oranim iyi mi?",
 ],
 "Toparlama-Retro": [
  "Bu is bolumunun retrosundan tek satir ogrenim cikti mi?",
  "Tekrar eden bir hatayi kalici duzelttim mi (kok neden)?",
  "Bir sonraki sprint icin tasinacak riski isaretledim mi?",
 ],
 "Sahiplik-Hesapverebilirlik": [
  "Bu isin tek net sahibi ben miyim; belirsizlik biraktim mi?",
  "Bir hatayi savunmaya gecmeden sahiplendim mi?",
  "Taahhut ettigim tarihi tutuyor muyum; tutmuyorsam erken haber verdim mi?",
  "Baskasinin isini beklerken kendi tarafimi hazir tuttum mu?",
  "Kararimin kanitini (link/commit/dosya) biraktim mi?",
  "Bu cikti icin 'definition of done' karsilandi mi?",
  "Bugun ajansi bir adim ileri goturen en somut sey neydi?",
  "Yarina devrettigim en kritik acik madde ne; sahibi kim?",
  "Bu isi bastan yapsam neyi farkli yapardim?",
  "Olcebildigim bir ilerleme kaydettim mi, yoksa sadece mesgul mu gorundum?",
 ],
}

# ---- C) KADEME SORULARI
KADEME = {
 "C-LEVEL": [
  "Ajans OKR attainment'i %80 ustunde mi; degilse kurtarma plani ne?",
  "Bir faz kapisini kanitsiz GECTI saymadim degil mi?",
  "Mikro-yonetime kaydim mi; yetkiyi dogru devrettim mi?",
  "Sahibe danismadan bir taahhut verdim mi?",
  "5 gelir kanalinin hepsinin sahibi ve durumu net mi?",
  "Kurul gundemini kanit-linkli hazirladim mi?",
 ],
 "EVP": [
  "Departman OKR skoru guncel mi; kirmizi OKR icin plan var mi?",
  "Kadroyu asiri yukledim mi; kapasite dengeli mi?",
  "Playbook'u merge oncesi onayladim mi?",
  "Haftalik departman raporu yayinlandi mi?",
  "Sponsor C-level'a haftalik raporladim mi?",
 ],
 "DIRECTOR": [
  "Birim backlog'u dogru onceliklendi mi?",
  "Uzman ciktisini publish oncesi review ettim mi?",
  "Birim retrosundan ogrenim damittim mi?",
  "Cross-unit cakismayi EVP'ye tasidim mi?",
 ],
 "LEAD": [
  "Is akisi standardi/checklist guncel mi?",
  "Uzman gorevlerini gunluk atadim/review ettim mi?",
  "Haftalik is akisi ozetini yazdim mi?",
  "Riski metrik kanitiyla mi bayrakladim?",
 ],
 "SPECIALIST": [
  "Ciktim kopyala-hazir ve checklist'li mi?",
  "Bu hafta playbook'a 1 iyilestirme onerdim mi?",
  "Isi metrik gerekcesi olmadan mi sundum?",
  "Damgasiz cikti biraktim mi?",
 ],
 "ANALYST": [
  "Veri kesitim tanim-ekli mi?",
  "Anomaliyi buyukluk+hipotezle mi isaretledim?",
  "Tahmini acikca etiketledim mi?",
  "Veri uydurmadim degil mi?",
 ],
}


def dept_questions(d):
    """B) Departman sorulari — aile basi 3 kalip + KPI hedef/tanim."""
    ad = d["name_tr"]
    qs = []
    for aile in d["aileler"]:
        qs.append(f"{aile} birimi icin bu hafta en yuksek etkili kaldirac neydi; metrik gerekcesi ne?")
        qs.append(f"{aile} ciktisinda tekrarlanabilir bir iyilestirme/checklist uretebildim mi?")
        qs.append(f"{aile} alaninda bir beta/yeni ozellik veya platform guncellemesi cikti mi; test edip not aldim mi?")
    qs.append(f"{ad} departmani ana ciktisi ({d['cikti']}) hedefte mi; sapma varsa kok neden ve duzeltme ne?")
    qs.append(f"{ad} icin bu haftaki KPI tanimi ve kaynagi yazili mi; tahmin iceriyorsa etiketli mi?")
    return qs


def main():
    if not os.path.exists(ORG):
        raise SystemExit("org.json yok — once: python3 scripts/daily_agency.py --org-json")
    org = json.load(open(ORG, encoding="utf-8"))
    depts = org["departments"]

    evrensel_flat = [q for cat in EVRENSEL.values() for q in cat]
    dept_map = {d["code"]: dept_questions(d) for d in depts}
    dept_total = sum(len(v) for v in dept_map.values())
    kademe_total = sum(len(v) for v in KADEME.values())
    toplam = len(evrensel_flat) + dept_total + kademe_total

    bank = {
        "generated": NOW,
        "source": "scripts/build_question_bank.py (.claude/org/org.json)",
        "toplam": toplam,
        "evrensel_kategori": {k: v for k, v in EVRENSEL.items()},
        "departman": dept_map,
        "kademe": KADEME,
    }
    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    json.dump(bank, open(os.path.join(ROOT, "data", "soru_bankasi.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    L = [f"# OZ-DENETIM SORU BANKASI ({toplam} soru)",
         f"> Uretim: {NOW} · Kaynak: scripts/build_question_bank.py · data/soru_bankasi.json",
         "Her ajan her surecte kendine bu sorulari sorar. Gunluk dongu (daily_agency.py) her kosumda ornekler ve standup'ta yanitlar. Kart basina alt-set: departman + kademe bloklari; tam banka (bu dosya) her title'a acik.",
         "", f"## Ozet: Evrensel {len(evrensel_flat)} · Departman {dept_total} ({len(depts)} departman) · Kademe {kademe_total} · **Toplam {toplam}**",
         "", "## A. Evrensel sorular (tum roller)"]
    for cat, qs in EVRENSEL.items():
        L.append(f"### {cat}")
        L += [f"{i+1}. {q}" for i, q in enumerate(qs)]
    L += ["", "## B. Departman sorulari"]
    for d in depts:
        L.append(f"### {d['code']} — {d['name_tr']}")
        L += [f"{i+1}. {q}" for i, q in enumerate(dept_map[d["code"]])]
    L += ["", "## C. Kademe sorulari"]
    for tier, qs in KADEME.items():
        L.append(f"### {tier}")
        L += [f"{i+1}. {q}" for i, q in enumerate(qs)]
    open(os.path.join(ROOT, "docs", "OZ-DENETIM-SORU-BANKASI.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

    print(f"URETILDI: {toplam} soru → data/soru_bankasi.json + docs/OZ-DENETIM-SORU-BANKASI.md")
    print(f"  Evrensel: {len(evrensel_flat)} · Departman: {dept_total} · Kademe: {kademe_total}")


if __name__ == "__main__":
    main()
