#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_title_inventory.py — holding JSON + rol-kartlari + git silinmiş → ROSTER/TITLE_INVENTORY.md"""
import json
import os
import subprocess
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOLDING = os.path.join(ROOT, "data", "holding_istirak_org.json")
ROL_DIR = os.path.join(ROOT, "uretim", "rol-kartlari")
OUT = os.path.join(ROOT, "ROSTER", "TITLE_INVENTORY.md")


def git_deleted_roles():
    """Git history'den silinmiş rol-kartlari dosyalarını listele."""
    deleted = []
    try:
        r = subprocess.run(
            ["git", "log", "--all", "--diff-filter=D", "--summary", "--", "uretim/rol-kartlari/"],
            capture_output=True, text=True, cwd=ROOT, timeout=30,
        )
        for line in r.stdout.splitlines():
            if "delete mode" in line and "rol-kartlari/" in line:
                path = line.split()[-1]
                slug = os.path.basename(path).replace(".md", "")
                deleted.append({"slug": slug, "path": path, "source": "git-deleted"})
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return deleted


def main():
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data = json.load(open(HOLDING, encoding="utf-8"))
    roles = []
    for unit in data.get("units", []):
        uid = unit.get("id", "")
        uname = unit.get("unit", uid)
        for r in unit.get("roles", []):
            roles.append({
                "name": r.get("name", ""),
                "title": r.get("title", ""),
                "tier": r.get("tier", ""),
                "department": r.get("department", ""),
                "unit": uname,
                "unit_id": uid,
                "reports_to": r.get("reports_to", ""),
                "source": "holding-json",
                "status": "envanter",
            })

    existing_cards = set()
    if os.path.isdir(ROL_DIR):
        for f in os.listdir(ROL_DIR):
            if f.endswith(".md"):
                existing_cards.add(f.replace(".md", ""))

    deleted = git_deleted_roles()
    deleted_slugs = {d["slug"] for d in deleted}

    for r in roles:
        if r["name"] in existing_cards:
            r["source"] = "holding-json+rol-kartlari"
            r["status"] = "rol-karti-mevcut"
        elif r["name"] in deleted_slugs:
            r["source"] = "holding-json+git-deleted"
            r["status"] = "git-silinmis-kurtarilabilir"

    lines = [
        "# TITLE INVENTORY — LATOS Master Liste",
        "",
        f"> **Güncelleme:** {ts} UTC · **Kaynak:** `data/holding_istirak_org.json`",
        f"> **Toplam title:** {len(roles)} · **Hedef:** hiçbir title atlanmaz",
        "",
        "## Özet",
        "",
        f"| Metrik | Değer |",
        f"|--------|-------|",
        f"| Holding JSON role_adet | {data.get('role_adet', len(roles))} |",
        f"| Envantere yazılan | {len(roles)} |",
        f"| rol-kartlari mevcut | {len([r for r in roles if 'rol-kartlari' in r['source']])} |",
        f"| git silinmiş (kurtarılabilir) | {len([r for r in roles if r['status'] == 'git-silinmis-kurtarilabilir'])} |",
        f"| JOB_CARDS üretildi | 0 (Faz 4) |",
        "",
        "## Git Kurtarma Notu",
        "",
    ]
    if deleted:
        lines.append(f"- Git history'de **{len(deleted)}** silinmiş `uretim/rol-kartlari/*.md` tespit edildi.")
        lines.append("- Kurtarma: `git show <commit>^:<path>` veya `git restore --source=<commit>~1 -- <path>`")
        lines.append("- **İnsan onayı gerekli** — otomatik restore yapılmadı.")
    else:
        lines.append("- Git silinmiş rol dosyası bulunamadı veya git yok.")

    lines += ["", "## Title Listesi", "", "| # | slug | title | tier | unit | kaynak | durum |", "|---|------|-------|------|------|--------|-------|"]
    for i, r in enumerate(sorted(roles, key=lambda x: x["name"]), 1):
        lines.append(
            f"| {i} | `{r['name']}` | {r['title']} | {r['tier']} | {r['unit_id']} | {r['source']} | {r['status']} |"
        )

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"OK: {len(roles)} title → {OUT}")


if __name__ == "__main__":
    main()
