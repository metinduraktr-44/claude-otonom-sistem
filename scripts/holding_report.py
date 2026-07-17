#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HOLDING KONSOLİDE RAPOR — data/holding.json'dan günlük portföy durumu üretir.
GITHUB_TOKEN varsa GitHub API ile her birimin son commit/açık issue/CI durumunu çeker;
yoksa (varsayılan) statik künye + kontrol listesi üretir. Çıktı: docs/HOLDING-KONSOLIDE.md"""
import json, os, datetime, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
H = json.load(open(os.path.join(ROOT, "data", "holding.json"), encoding="utf-8"))
TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
OWNER = "metinduraktr-44"

def api(path):
    if not TOKEN:
        return None
    req = urllib.request.Request(f"https://api.github.com/repos/{OWNER}/{path}",
        headers={"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except Exception:
        return None

L = [f"# HOLDING KONSOLİDE RAPOR — {H['holding']}",
     f"> Üretim: {NOW} · Kaynak: data/holding.json · Mod: {'CANLI (API)' if TOKEN else 'STATİK (token yok)'}",
     "", "## Kurul", "| Rol | Görev |", "|---|---|"]
for b in H["board"]:
    L.append(f"| {b['role']} | {b['duty']} |")

L += ["", "## İş Birimleri", "| Birim | Repo | Segment | Alan | Gelir | Son commit | Açık issue |",
      "|---|---|---|---|---|---|---|"]
for u in H["units"]:
    last, issues = "—", "—"
    if TOKEN:
        info = api(u["repo"])
        if info:
            last = (info.get("pushed_at") or "—")[:10]
            issues = str(info.get("open_issues_count", "—"))
    L.append(f"| {u['unit']} | {u['repo']} | {u['segment']} | {u['domain']} | {'✓' if u['revenue_model'] else '—'} | {last} | {issues} |")

seg = {}
for u in H["units"]:
    seg.setdefault(u["segment"], []).append(u["unit"])
L += ["", "## Segment Dağılımı"]
for s, us in seg.items():
    L.append(f"- **{s}**: {', '.join(us)}")

L += ["", "## Ortak Hizmetler"] + [f"- {s}" for s in H["shared_services"]]
L += ["", "## Ritim",
      f"- Günlük: {H['cadence']['gunluk']} · Haftalık: {H['cadence']['haftalik']} · Aylık: {H['cadence']['aylik']}"]
L += ["", "## Günün Holding Öz-Denetimi",
      "- [ ] Her birimin son commit'i 48 saatten taze mi (ölü birim var mı)?",
      "- [ ] Gelir motoru birimlerinde (AdOps/Tahmin/Performer) bu hafta ilerleme var mı?",
      "- [ ] Marka birimleri (Movéa/VizaTrack/Çiğköftem) community-health standardında mı?",
      "- [ ] Çapraz-sinerji fırsatı: AdOps bir markaya iç-müşteri hizmeti verebilir mi?",
      "- [ ] Sermaye/gelir taahhüdü sahip onayından geçti mi (CILT1)?"]

os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
open(os.path.join(ROOT, "docs", "HOLDING-KONSOLIDE.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print(f"HOLDING-KONSOLIDE.md yazildi ({'API' if TOKEN else 'statik'})")
