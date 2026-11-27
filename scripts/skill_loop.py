#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill_loop.py — LATOS skill döngüsü (stdlib). Nightly-safe dry-run.

Akış: ARCHIVE ay damgası oku → skip (ay stamped) → INDEX yenile → (opsiyonel) domain dalga.

🚩 900.000.000 karakter/prompt RED. Bu script 900k+ dosya YAZMAZ.
Top-100 uydurma yok. Tenant/credential yoksa dry-run.
Nightly kırıcı değil: exit 0 (hata stderr + kod 0, --strict ile 1).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
INV = ROOT / "data" / "skill_envanteri.json"
HARITA = ROOT / "data" / "skill_title_haritasi.json"
ROSTER = ROOT / "ROSTER" / "TITLE_INVENTORY.md"
INDEX_MD = ROOT / "SKILLS_TALENT" / "SKILL_LOOP_INDEX.md"
INDEX_JSON = ROOT / "data" / "skill_loop_index.json"
CAL = ROOT / "CALENDAR" / "LATOS_RESEARCH.md"
ARCHIVE_DIR = ROOT / "ARCHIVE"

NOW = dt.datetime.now(dt.timezone.utc)
TS = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
MONTH = NOW.strftime("%Y-%m")
TODAY = NOW.strftime("%Y-%m-%d")
MAX_FILE = 120_000  # 900k+ yazma yasağı (script çıktıları için tavan)
PROMPTS = 122

# İlk INDEX üretiminde (JSON yokken) bu domainler partial. Sonraki turlar JSON status kazanır.
PARTIAL_DOMAINS = {"AN-CH", "AN-MIX"}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def archive_stamp_path() -> Path:
    return ARCHIVE_DIR / MONTH / "latos" / f"skill-loop-{MONTH}.md"


def month_stamped() -> bool:
    p = archive_stamp_path()
    if not p.exists():
        return False
    text = p.read_text(encoding="utf-8", errors="replace")
    return MONTH in text and "skill-loop" in text.lower()


def titles_by_domain(harita: dict) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for t in harita.get("titles", []):
        did = t.get("domain_id") or "HOLDING"
        out.setdefault(did, []).append(t.get("title") or "")
    return out


def skill_status(skill: str, domain_id: str, existing: dict[str, str] | None) -> str:
    if existing and skill in existing:
        return existing[skill]
    if domain_id in PARTIAL_DOMAINS:
        return "partial"
    return "pending"


def build_rows(inv: dict, harita: dict, existing: dict[str, str] | None) -> list[dict[str, Any]]:
    by_dom = titles_by_domain(harita)
    rows = []
    skills = inv.get("skills") or []
    for i, item in enumerate(skills, 1):
        sk = item["skill"]
        did = item.get("domain_id") or "GEN-OPS"
        dad = item.get("domain_ad") or did
        titles = [t for t in by_dom.get(did, []) if t][:4]
        rows.append({
            "n": i,
            "skill": sk,
            "domain_id": did,
            "domain_ad": dad,
            "titles": titles,
            "status": skill_status(sk, did, existing),
            "c_level": item.get("c_level") or "",
            "prompt_slots": PROMPTS,
        })
    return rows


def load_existing_status() -> dict[str, str]:
    if not INDEX_JSON.exists():
        return {}
    try:
        obj = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    out = {}
    for r in obj.get("rows") or []:
        if r.get("skill") and r.get("status"):
            out[r["skill"]] = r["status"]
    return out


def write_index(rows: list[dict[str, Any]], inv: dict) -> None:
    pending = sum(1 for r in rows if r["status"] == "pending")
    partial = sum(1 for r in rows if r["status"] == "partial")
    done = sum(1 for r in rows if r["status"] == "done")
    lines = [
        "# SKILL LOOP INDEX — LATOS",
        "",
        f"> Damga: `{TS}` UTC · ay `{MONTH}` · kaynak `data/skill_envanteri.json` ({inv.get('adet')} skill / {inv.get('domain_adet')} domain)",
        "> Hiçbir skill satırı atlanmaz. Satır iskelet = **pending**. Tam 696×122×900M **tek oturumda yapılmaz**.",
        "> 🚩 900.000.000 karakter tek prompt **RED / fiziksel imkânsız**. Sözleşme 4–12 KiB + `P00n.md` fazlı.",
        "> Title bağ: `data/skill_title_haritasi.json` domain C→WORKER zinciri (Holding 633 ayrı envanter).",
        "",
        "## Özet",
        "",
        "| Metrik | Değer |",
        "|--------|-------|",
        f"| Skill satır | {len(rows)} |",
        f"| pending | {pending} |",
        f"| partial | {partial} |",
        f"| done | {done} |",
        f"| partial domain_id | `{', '.join(sorted({r['domain_id'] for r in rows if r['status']=='partial'})) or '—'}` |",
        "",
        "## Döngü sözleşmesi",
        "",
        "1. ARCHIVE ay damgası oku (`ARCHIVE/YYYY-MM/latos/skill-loop-YYYY-MM.md`)",
        "2. Damgalı ay → **SKIP** (takvim yazma)",
        "3. RESEARCH not: URL + UTC ts; kişi yoksa `unverified`",
        "4. Title bağ + (opsiyonel) JOB_CARD skeleton",
        "5. EXPERTS_TALENT seed — uydurma ranking yok",
        "6. `PROMPTS/` INDEX 122 slot + P001–P003 (900M iddiası yok)",
        "7. `python3 scripts/skill_loop.py --dry-run`",
        "",
        "## Satırlar",
        "",
        "| # | skill | domain | title bağ (max 4) | status | C-rapor |",
        "|---|-------|--------|-------------------|--------|---------|",
    ]
    for r in rows:
        titles = "; ".join(r["titles"]) if r["titles"] else "(domain title backlog)"
        titles = titles.replace("|", "/")
        lines.append(
            f"| {r['n']} | `{r['skill']}` | `{r['domain_id']}` {r['domain_ad']} | {titles} | {r['status']} | {r['c_level']} |"
        )
    lines += [
        "",
        "## Backlog (dürüst)",
        "",
        f"- {pending} skill **pending** — RESEARCH/prompt/expert yok.",
        f"- {partial} skill **partial** — bu tur domain dalgası.",
        "- Holding `ROSTER/TITLE_INVENTORY.md` 633 title ayrı QA (`scripts/qa_check.py`).",
        "- 100 kültür/sanat/spor yetenek × top-100: Faz 6 fazlı; bu tur 1 seed (satranç/FIDE).",
        "",
    ]
    text = "\n".join(lines) + "\n"
    if len(text) > MAX_FILE * 4:
        raise SystemExit(f"INDEX too large ({len(text)}) — abort")
    INDEX_MD.parent.mkdir(parents=True, exist_ok=True)
    INDEX_MD.write_text(text, encoding="utf-8")
    payload = {
        "ts": TS,
        "month": MONTH,
        "adet": len(rows),
        "pending": pending,
        "partial": partial,
        "done": done,
        "flag": "900M_RED",
        "rows": [
            {"skill": r["skill"], "domain_id": r["domain_id"], "status": r["status"], "titles": r["titles"]}
            for r in rows
        ],
    }
    INDEX_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_calendar_if_needed(force: bool) -> str:
    stamped = month_stamped()
    if stamped and not force:
        return f"SKIP calendar {MONTH} (ARCHIVE stamped)"
    cal_lines = [
        "# LATOS RESEARCH Calendar",
        "",
        "> Aylık: ARCHIVE oku → araştır → yaz. Damgalı ay **SKIP**.",
        "> Komut: `python3 scripts/skill_loop.py --dry-run`",
        "",
        "| Ay | Aksiyon | Damga |",
        "|----|---------|-------|",
        f"| {MONTH} | ClickHouse (AN-CH) + Mixpanel (AN-MIX) skill dalgası · INDEX 696 | {TS} |",
        "| 2026-12 | Sonraki domain dalgası (pending kuyruk) | pending |",
        "",
        "Kaynak not: `RESEARCH/2026-11-16_clickhouse-mixpanel-skill-loop.md`",
        "",
    ]
    stamp = archive_stamp_path()
    stamp_body = (
        f"# skill-loop {MONTH}\n\n"
        f"- ts: {TS}\n"
        f"- index: `SKILLS_TALENT/SKILL_LOOP_INDEX.md`\n"
        f"- domains: AN-CH, AN-MIX\n"
        f"- 🚩 900M RED\n"
        f"- skip-rule: this file present → next run SKIP calendar write\n"
    )
    CAL.parent.mkdir(parents=True, exist_ok=True)
    CAL.write_text("\n".join(cal_lines) + "\n", encoding="utf-8")
    stamp.parent.mkdir(parents=True, exist_ok=True)
    stamp.write_text(stamp_body, encoding="utf-8")
    return f"WRITE calendar {MONTH}"


def dogrula(rows: list[dict[str, Any]], inv: dict) -> list[str]:
    warns = []
    if len(rows) != int(inv.get("adet") or 0):
        warns.append(f"INDEX {len(rows)} != envanter {inv.get('adet')}")
    if len(rows) < 600:
        warns.append("INDEX < 600 — skill atlama şüphesi")
    skills = [r["skill"] for r in rows]
    if len(skills) != len(set(skills)):
        warns.append("duplicate skill slug")
    if INDEX_MD.exists() and INDEX_MD.stat().st_size > 900_000:
        warns.append("INDEX.md >900k char — YASAK eşiğe yakın")
    return warns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="INDEX yaz; takvim damgalıysa skip")
    ap.add_argument("--force", action="store_true", help="ay damgasını yoksay")
    ap.add_argument("--strict", action="store_true", help="uyarıda exit 1")
    ap.add_argument(
        "--mark-partial",
        default="",
        help="virgülle skill slug: pending→partial (JSON existing üzerine)",
    )
    args = ap.parse_args()
    if not INV.exists() or not HARITA.exists():
        print("[skill-loop] envanter yok", file=sys.stderr)
        return 0 if not args.strict else 1
    inv = load_json(INV)
    harita = load_json(HARITA)
    existing = load_existing_status()
    for slug in [s.strip() for s in args.mark_partial.split(",") if s.strip()]:
        existing[slug] = "partial"
    rows = build_rows(inv, harita, existing)
    write_index(rows, inv)
    # --dry-run: INDEX her zaman; takvim yalnız damgasız veya --force
    cal_msg = write_calendar_if_needed(force=args.force)
    warns = dogrula(rows, inv)
    print(f"[skill-loop] ts={TS} rows={len(rows)} {cal_msg}")
    for w in warns:
        print(f"[skill-loop] WARN {w}", file=sys.stderr)
    if args.strict and warns:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
