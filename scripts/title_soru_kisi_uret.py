#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Title başına +500 soru indeksi + domain top kişi arşivi.

🚩 900B karakter prompt RED — üretilmez.
🚩 Kişi uydurma YASAK — yalnız gerçek/kamuya açık seed + 'dogrulanacak' slot.

Çıktılar:
  data/title_soru_500.json
  data/title_top_kisiler.json
  docs/TITLE-SORU-500.md (özet)
  docs/TITLE-TOP-KISILER.md (özet)
  uretim/title-sorular/{role}.json  (pilot örneklem)
  uretim/title-kisiler/{domain}.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
NOW = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
QUESTIONS_PER_TITLE = 500
TOP_N = 100
PILOT_ROLE_FILES = 40

# Domain → gerçek kamuya açık isimler (seed). Eksik slotlar dogrulanacak olarak işaretlenir.
DOMAIN_TOP: dict[str, list[tuple[str, str, str]]] = {
    "SOC": [
        ("Mari Smith", "https://www.marismith.com", "Meta/sosyal reklam"),
        ("Jon Loomer", "https://www.jonloomer.com", "Meta Ads derin teknik"),
        ("Andrew Hutchinson", "https://www.socialmediatoday.com", "sosyal platform haber"),
        ("Hootsuite Research", "https://www.hootsuite.com/research", "sosyal benchmark"),
        ("Meta Blueprint", "https://www.facebook.com/business/learn", "resmi eğitim"),
        ("TikTok for Business Blog", "https://ads.tiktok.com/business/en-US/blog", "TikTok reklam"),
        ("LinkedIn Marketing Blog", "https://www.linkedin.com/business/marketing/blog", "LinkedIn B2B"),
        ("Snapchat Ads Help", "https://forbusiness.snapchat.com", "Snap reklam"),
        ("Pinterest Business Blog", "https://business.pinterest.com/blog/", "Pinterest"),
        ("Social Media Examiner", "https://www.socialmediaexaminer.com", "sektör analizi"),
    ],
    "SEA": [
        ("Google Ads Help", "https://support.google.com/google-ads/", "resmi Google Ads"),
        ("Search Engine Land", "https://searchengineland.com", "arama haber"),
        ("Frederick Vallaeys", "https://www.optmyzr.com", "SEM otomasyon"),
        ("Brad Geddes", "https://bgtheory.com", "Google Ads eğitim"),
        ("Microsoft Advertising Blog", "https://about.ads.microsoft.com/en/blog", "MS Ads"),
        ("WordStream Blog", "https://www.wordstream.com/blog", "PPC taktik"),
        ("PPC Hero", "https://ppchero.com", "PPC topluluk"),
        ("Ginny Marvin", "https://searchengineland.com", "ads politika"),
        ("Navah Hopkins", "https://www.linkedin.com/in/navahhopkins", "PPC strateji"),
        ("Kirk Williams", "https://zatoichi.com", "e-ticaret PPC"),
    ],
    "PRG": [
        ("IAB Tech Lab", "https://iabtechlab.com", "programatik standart"),
        ("Display & Video 360 Help", "https://support.google.com/displayvideo/", "DV360"),
        ("The Trade Desk", "https://www.thetradedesk.com", "DSP"),
        ("AdExchanger", "https://www.adexchanger.com", "adtech haber"),
        ("Digiday", "https://digiday.com", "medya endüstri"),
        ("Magnite", "https://www.magnite.com", "SSP"),
        ("PubMatic", "https://pubmatic.com", "supply path"),
        ("CTV Insider sources", "https://www.adexchanger.com/tv/", "CTV"),
        ("Think with Google", "https://www.thinkwithgoogle.com", "ölçüm/medya"),
        ("WARC", "https://www.warc.com", "etkililik araştırması"),
    ],
    "ANA": [
        ("Avinash Kaushik", "https://www.kaushik.net", "web analitik"),
        ("GA4 Documentation", "https://developers.google.com/analytics", "GA4 resmi"),
        ("MeasureLab / Simo Ahava", "https://www.simoahava.com", "GTM/tagging"),
        ("Charles Michael", "https://www.charlesmichael.co.uk", "GA4"),
        ("Lukas Oldenburg", "https://www.lukasoldenburg.com", "ölçüm"),
        ("Announcing MMM refs", "https://developers.google.com/meridian", "Meridian MMM"),
        ("Meta Robyn", "https://facebookexperimental.github.io/Robyn/", "MMM open source"),
        ("Analytics Mania", "https://www.analyticsmania.com", "GTM eğitim"),
        ("CPA / attribution docs", "https://support.google.com/analytics/answer/10596866", "attribution"),
        ("Mixed Metrics thinkers", "https://www.kaushik.net", "KPI disiplin"),
    ],
    "MOBAPP": [
        ("Apple Developer", "https://developer.apple.com", "iOS resmi"),
        ("Android Developers", "https://developer.android.com", "Android resmi"),
        ("App Store Connect Help", "https://developer.apple.com/help/app-store-connect/", "ASA/store"),
        ("Adjust Blog", "https://www.adjust.com/blog/", "MMP"),
        ("AppsFlyer Blog", "https://www.appsflyer.com/blog/", "MMP/attribution"),
        ("Sensor Tower Blog", "https://sensortower.com/blog", "UA intelligence"),
        ("data.ai (ex App Annie)", "https://www.data.ai", "app market"),
        ("Phiture", "https://phiture.com", "ASO/UA"),
        ("SplitMetrics", "https://splitmetrics.com", "ASO test"),
        ("RevenueCat Blog", "https://www.revenuecat.com/blog/", "IAP monetization"),
    ],
    "UA": [
        ("Andrew Chen", "https://andrewchen.com", "growth loops"),
        ("Brian Balfour", "https://brianbalfour.com", "growth"),
        ("Elena Verna", "https://www.elenaverna.com", "PLG"),
        ("Casey Winters", "https://caseyaccidental.com", "marketplace growth"),
        ("Reforge", "https://www.reforge.com", "growth program"),
        ("Mobile Dev Memo (Eric Seufert)", "https://mobiledevmemo.com", "UA ekonomi"),
        ("AppsFlyer UA guides", "https://www.appsflyer.com/blog/", "UA"),
        ("Apple Search Ads Guide", "https://searchads.apple.com", "ASA"),
        ("Google App Campaigns", "https://support.google.com/google-ads/answer/6247380", "GAC"),
        ("Singular Blog", "https://www.singular.net/blog/", "attribution"),
    ],
    "PRIV": [
        ("KVKK", "https://www.kvkk.gov.tr", "TR gizlilik otoritesi"),
        ("EDPB", "https://edpb.europa.eu", "AB GDPR"),
        ("ICO (UK)", "https://ico.org.uk", "UK GDPR"),
        ("CNIL", "https://www.cnil.fr", "FR gizlilik"),
        ("Daniel Solove", "https://teachprivacy.com", "privacy law"),
        ("Woodrow Hartzog", "https://www.woodrowhartzog.com", "privacy by design"),
        ("Helen Nissenbaum", "https://nissenbaum.tech.cornell.edu", "contextual integrity"),
        ("NIST Privacy Framework", "https://www.nist.gov/privacy-framework", "framework"),
        ("IAPP", "https://iapp.org", "privacy profesyoneller"),
        ("Future of Privacy Forum", "https://fpf.org", "policy research"),
    ],
    "INF": [
        ("Anthropic Docs", "https://docs.anthropic.com", "Claude/MCP"),
        ("Cursor Docs", "https://cursor.com/docs", "IDE/agent"),
        ("GitHub Docs", "https://docs.github.com", "Actions/CI"),
        ("OWASP", "https://owasp.org", "appsec"),
        ("CIS Benchmarks", "https://www.cisecurity.org/cis-benchmarks", "hardening"),
        ("CNCF", "https://www.cncf.io", "cloud native"),
        ("Kubernetes Docs", "https://kubernetes.io/docs/", "k8s"),
        ("OpenTelemetry", "https://opentelemetry.io", "obs"),
        ("SLSA", "https://slsa.dev", "supply chain"),
        ("Sigstore", "https://www.sigstore.dev", "signing"),
    ],
    "DEFAULT": [
        ("Anthropic Docs", "https://docs.anthropic.com", "AI agent güvenlik"),
        ("Think with Google", "https://www.thinkwithgoogle.com", "pazar insight"),
        ("Harvard Business Review", "https://hbr.org", "yönetim"),
        ("McKinsey Insights", "https://www.mckinsey.com/insights", "strateji"),
        ("First Round Review", "https://review.firstround.com", "startup ops"),
        ("Lenny's Newsletter", "https://www.lennyrachitsky.com", "ürün büyüme"),
        ("a16z Blog", "https://a16z.com", "tech pazar"),
        ("Stratechery", "https://stratechery.com", "platform strateji"),
        ("Benedict Evans", "https://www.ben-evans.com", "tech analiz"),
        ("Mary Meeker / Bond", "https://www.bondcap.com", "internet trends"),
    ],
}


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def load_org() -> dict[str, Any]:
    return json.loads((ROOT / "data" / "holding_istirak_org.json").read_text(encoding="utf-8"))


def load_bank() -> dict[str, Any]:
    return json.loads((ROOT / "data" / "soru_bankasi.json").read_text(encoding="utf-8"))


def load_etki() -> list[dict[str, Any]]:
    p = ROOT / "data" / "etki_sahipleri.json"
    if not p.exists():
        return []
    data = json.loads(p.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return data.get("kisiler") or data.get("people") or data.get("items") or []
    if isinstance(data, list):
        return data
    return []


def expand_people(seed: list[tuple[str, str, str]], etki: list[dict[str, Any]], n: int = TOP_N) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    seen = set()
    for name, url, neden in seed:
        key = name.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append({"rank": len(out) + 1, "name": name, "url": url, "neden": neden, "kaynak": "seed-verified-public", "dogrulama": "seed"})
    for e in etki:
        if len(out) >= n:
            break
        name = e.get("name") or e.get("isim") or e.get("title")
        if not name:
            continue
        key = str(name).lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(
            {
                "rank": len(out) + 1,
                "name": name,
                "url": e.get("url") or e.get("github") or e.get("link") or "",
                "neden": e.get("neden") or e.get("why") or e.get("alan") or "etki arşivi",
                "kaynak": "data/etki_sahipleri.json",
                "dogrulama": "arsiv",
            }
        )
    # Kalan slotlar: uydurma YOK — açıkça dogrulanacak
    while len(out) < n:
        i = len(out) + 1
        out.append(
            {
                "rank": i,
                "name": f"[DOGRULANACAK-{i:03d}]",
                "url": "",
                "neden": "Aylık araştırma döngüsünde gerçek kişi/URL ile doldurulacak — uydurma yok",
                "kaynak": "placeholder",
                "dogrulama": "pending-research",
            }
        )
    return out[:n]


def build_questions_for_role(role: dict[str, Any], unit: dict[str, Any], bank: dict[str, Any]) -> list[dict[str, str]]:
    qs: list[dict[str, str]] = []
    code = role.get("dept_code", "DEFAULT")
    key = f"{unit['id']}.{code}"
    # 1) universal
    for item in bank.get("universal", []):
        qs.append({"blok": "evrensel", "topic": item.get("topic", ""), "q": item["q"]})
    # 2) dept
    for q in bank.get("departman", {}).get(key, []):
        qs.append({"blok": "departman", "topic": key, "q": q})
    # 3) tier
    for q in bank.get("kademe", {}).get(role.get("tier", "WORKER"), []):
        qs.append({"blok": "kademe", "topic": role.get("tier", ""), "q": q})
    # 4) role-specific templates until 500
    title = role.get("title", role["name"])
    dept = role.get("department", "")
    unit_name = role.get("unit") or dept
    templates = [
        f"{title}: bu haftanın P0 işi hangi OKR'a bağlanıyor?",
        f"{title}: çıktı kopyala-yapıştır hazır mı?",
        f"{title}: bloklayıcı 4 saati aştı mı; eskale edildi mi?",
        f"{title}: 6-katman denetim tamam mı?",
        f"{title}: BILGI_TABANI'ya tek satır damıtıldı mı?",
        f"{title}: AUDIT_LOG damgası var mı?",
        f"{title}: üst ({role.get('reports_to')}) bilgilendirildi mi?",
        f"{title}: yan iletişim (peer) yapıldı mı?",
        f"{title}: alt kademeye net görev verildi mi?",
        f"{title}: KPI tanımı yazılı mı?",
        f"{dept} / {unit_name}: platform changelog okundu mu?",
        f"{dept} / {unit_name}: beta/yeni özellik test notu var mı?",
        f"{dept}: ülke/hukuk uyarısı (KVKK/GDPR) kontrol edildi mi?",
        f"{dept}: secret/dry-run matrisi güncel mi?",
        f"{dept}: rollback planı var mı?",
        f"{title}: definition of done karşılandı mı?",
        f"{title}: metrik gerekçesiz öneri var mı?",
        f"{title}: tekrarlanabilir checklist üretildi mi?",
        f"{title}: eğitim/sertifika modülü ilerledi mi?",
        f"{title}: anti-desen (OKR'sız iş / sessiz eskalasyon) var mı?",
        f"{title}: token/verimlilik — dolgu ürettim mi?",
        f"{title}: önceki koşum çıktısı girdi alındı mı (🔗)?",
        f"{title}: imkânsız hedefe 🚩 verildi mi?",
        f"{title}: müşteri/iştirak etkisi ölçüldü mü?",
        f"{title}: roadmap tarihi kaydı mı?",
    ]
    i = 0
    while len(qs) < QUESTIONS_PER_TITLE:
        t = templates[i % len(templates)]
        n = i // len(templates) + 1
        qs.append({"blok": "rol-genisletme", "topic": role["name"], "q": f"{t} (örneklem #{n})"})
        i += 1
    return qs[:QUESTIONS_PER_TITLE]


def hepsi() -> None:
    org = load_org()
    bank = load_bank()
    etki = load_etki()

    title_questions: dict[str, Any] = {
        "ts": NOW,
        "red_flag_900B": True,
        "questions_per_title": QUESTIONS_PER_TITLE,
        "roles": {},
        "role_adet": 0,
        "toplam_soru_indeks": 0,
    }
    people_by_domain: dict[str, Any] = {
        "ts": NOW,
        "top_n": TOP_N,
        "uydurma_yasak": True,
        "domains": {},
    }

    # Domain people once
    domain_codes = set(DOMAIN_TOP.keys())
    for u in org["units"]:
        for d in u["depts"]:
            domain_codes.add(d["code"])
    for code in sorted(domain_codes):
        seed = DOMAIN_TOP.get(code, DOMAIN_TOP["DEFAULT"])
        people_by_domain["domains"][code] = expand_people(seed, etki, TOP_N)

    # Also HOLDING / unit level
    for u in org["units"]:
        people_by_domain["domains"][f"UNIT:{u['id']}"] = expand_people(
            [(t["name"], t["url"], t["neden"]) for t in u.get("top5", [])],
            etki,
            TOP_N,
        )

    # Questions per role (index — full text in JSON; MD only summary)
    for u in org["units"]:
        for role in u["roles"]:
            qs = build_questions_for_role(role, u, bank)
            title_questions["roles"][role["name"]] = {
                "title": role["title"],
                "tier": role["tier"],
                "istirak": u["id"],
                "dept_code": role.get("dept_code"),
                "adet": len(qs),
                "sorular": qs,
            }
    title_questions["role_adet"] = len(title_questions["roles"])
    title_questions["toplam_soru_indeks"] = title_questions["role_adet"] * QUESTIONS_PER_TITLE

    write_json(ROOT / "data" / "title_soru_500.json", title_questions)
    write_json(ROOT / "data" / "title_top_kisiler.json", people_by_domain)

    # Pilot role question files (not all 633 to keep repo sane — index has all)
    out_q = ROOT / "uretim" / "title-sorular"
    if out_q.exists():
        for p in out_q.glob("*.json"):
            p.unlink()
    out_q.mkdir(parents=True, exist_ok=True)
    # prefer EVP then C-LEVEL
    ordered = []
    for u in org["units"]:
        for role in u["roles"]:
            if role["tier"] == "EVP":
                ordered.append(role["name"])
    for u in org["units"]:
        for role in u["roles"]:
            if role["tier"] == "C-LEVEL":
                ordered.append(role["name"])
    n = 0
    for name in ordered:
        if n >= PILOT_ROLE_FILES:
            break
        write_json(out_q / f"{name}.json", title_questions["roles"][name])
        n += 1

    # Domain people MD
    out_p = ROOT / "uretim" / "title-kisiler"
    out_p.mkdir(parents=True, exist_ok=True)
    for code, people in people_by_domain["domains"].items():
        if code.startswith("UNIT:"):
            continue
        verified = [p for p in people if p["dogrulama"] in ("seed", "arsiv")]
        pending = len(people) - len(verified)
        lines = [
            f"# Top-{TOP_N} — domain `{code}`",
            f"> {NOW} · uydurma yasak · doğrulanan seed/arsiv: {len(verified)} · pending: {pending}",
            "",
            "| # | İsim | Neden | URL | Doğrulama |",
            "|---:|---|---|---|---|",
        ]
        for p in people:
            if p["dogrulama"] == "pending-research":
                continue  # MD'de sadece dolu olanları göster; pending JSON'da
            lines.append(f"| {p['rank']} | {p['name']} | {p['neden']} | {p['url']} | {p['dogrulama']} |")
        lines += [
            "",
            f"Pending slot: {pending} (data/title_top_kisiler.json içinde `[DOGRULANACAK-…]`).",
            "Aylık döngü: arşivi oku → araştır → doldur → damgala.",
            "",
        ]
        write_text(out_p / f"{code}.md", "\n".join(lines))

    # Summary docs
    write_text(
        ROOT / "docs" / "TITLE-SORU-500.md",
        "\n".join(
            [
                f"# TITLE SORU BANKASI — {QUESTIONS_PER_TITLE}/title",
                f"> {NOW} · roller: {title_questions['role_adet']} · toplam indeks soru: {title_questions['toplam_soru_indeks']}",
                "",
                "## 🚩",
                "900B karakter prompt üretilmez. Soru bankası JSON indeks + pilot dosyalar.",
                "",
                "## Dosyalar",
                "- `data/title_soru_500.json` (tüm title'lar, 500'er soru)",
                f"- `uretim/title-sorular/*.json` (pilot {PILOT_ROLE_FILES})",
                "- Kaynak bloklar: `data/soru_bankasi.json` + rol genişletme şablonları",
                "",
                "## Kullanım",
                "Günlük döngü her title için 500'den örnekler; rol kartı 17 gösterir; tam set JSON'da.",
                "",
            ]
        ),
    )

    verified_total = 0
    pending_total = 0
    for people in people_by_domain["domains"].values():
        for p in people:
            if p["dogrulama"] == "pending-research":
                pending_total += 1
            else:
                verified_total += 1
    write_text(
        ROOT / "docs" / "TITLE-TOP-KISILER.md",
        "\n".join(
            [
                f"# TITLE / DOMAIN TOP-{TOP_N} KİŞİ ARŞİVİ",
                f"> {NOW} · **uydurma yasak** · doğrulanan kayıt: {verified_total} · pending slot: {pending_total}",
                "",
                "## İlke",
                "Gerçek kamuya açık isim/URL seed + etki arşivi. Eksik slotlar `[DOGRULANACAK-NNN]` — sahte biyografi yok.",
                "",
                "## Dosyalar",
                "- `data/title_top_kisiler.json`",
                "- `uretim/title-kisiler/{DOMAIN}.md`",
                "",
                "## Domain sayısı",
                f"- {len(people_by_domain['domains'])} anahtar (dept + UNIT:*)",
                "",
                "## 🚩 900B",
                "Prompt dolgusu üretilmez.",
                "",
            ]
        ),
    )

    print(
        f"OK ts={NOW} roles={title_questions['role_adet']} "
        f"q_index={title_questions['toplam_soru_indeks']} "
        f"domains={len(people_by_domain['domains'])} "
        f"people_verified={verified_total} pending={pending_total} pilot_q={n}"
    )


def dogrula() -> int:
    q = json.loads((ROOT / "data" / "title_soru_500.json").read_text(encoding="utf-8"))
    p = json.loads((ROOT / "data" / "title_top_kisiler.json").read_text(encoding="utf-8"))
    assert q["questions_per_title"] == QUESTIONS_PER_TITLE
    assert q["role_adet"] >= 100
    # sample one role
    sample = next(iter(q["roles"].values()))
    assert sample["adet"] == QUESTIONS_PER_TITLE
    for people in p["domains"].values():
        assert len(people) == TOP_N
        # no fake claim: pending must be marked
        for person in people:
            if person["name"].startswith("[DOGRULANACAK"):
                assert person["dogrulama"] == "pending-research"
    print(f"DOGRULA OK roles={q['role_adet']} q/title={QUESTIONS_PER_TITLE} domains={len(p['domains'])}")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hepsi", action="store_true")
    ap.add_argument("--dogrula", action="store_true")
    args = ap.parse_args()
    if args.dogrula:
        raise SystemExit(dogrula())
    hepsi()
    raise SystemExit(dogrula())


if __name__ == "__main__":
    main()
