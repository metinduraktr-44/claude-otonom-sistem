#!/usr/bin/env python3
"""LATOS QA — job card structure + inventory diff stub (stdlib). Fail-open in --hook."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JOB = ROOT / "JOB_CARDS"
ROSTER = ROOT / "ROSTER" / "TITLE_INVENTORY.md"
MIN_CARD_CHARS = 2000
MIN_H_TARGET = 200  # headings target (soft)


def inventory_titles() -> set[str]:
    titles: set[str] = set()
    if not ROSTER.exists():
        return titles
    for line in ROSTER.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 2:
            continue
        name = cols[0]
        if name in {"Ad / Kod", "---"} or name.startswith("---"):
            continue
        if name.lower().startswith("ad /"):
            continue
        # normalize slug-ish
        titles.add(name.split("—")[0].strip())
        titles.add(name)
    return titles


def job_card_dirs() -> list[Path]:
    if not JOB.exists():
        return []
    return [p for p in JOB.iterdir() if p.is_dir() and not p.name.startswith(".")]


def check_card(path: Path) -> list[str]:
    issues: list[str] = []
    card = path / "CARD.md"
    if not card.exists():
        issues.append(f"[structural] {path.name}: CARD.md yok")
        return issues
    txt = card.read_text(encoding="utf-8", errors="replace")
    if len(txt) < MIN_CARD_CHARS:
        issues.append(
            f"[soft] {path.name}: CARD.md {len(txt)}<{MIN_CARD_CHARS} karakter "
            f"(hedef; partial OK — sahte doldurma)"
        )
    h_files = sorted(path.glob("H*.md"))
    if len(h_files) < 1:
        issues.append(f"[soft] {path.name}: H00N yok (self-expand beklenir)")
    elif len(h_files) < MIN_H_TARGET:
        issues.append(
            f"[soft] {path.name}: {len(h_files)}/{MIN_H_TARGET} H-dosyası "
            f"(hedef; partial OK)"
        )
    for hf in h_files:
        body = hf.read_text(encoding="utf-8", errors="replace")
        for section in ("Açıklama", "Yönlendirme", "Eğitim", "Aciklama", "Yonlendirme"):
            # soft: presence of at least one canonical header family
            pass
        if not re.search(r"(?i)(açıklama|aciklama|description)", body):
            issues.append(f"[soft] {hf}: Açıklama bölümü eksik")
        if not re.search(r"(?i)(yönlendirme|yonlendirme|guidance)", body):
            issues.append(f"[soft] {hf}: Yönlendirme bölümü eksik")
        if not re.search(r"(?i)(eğitim|egitim|training)", body):
            issues.append(f"[soft] {hf}: Eğitim bölümü eksik")
    return issues


def inventory_diff(card_dirs: list[Path]) -> list[str]:
    """Stub: cards whose folder name not found loosely in inventory."""
    inv = inventory_titles()
    if not inv:
        return ["[soft] inventory boş veya okunamadı — diff atlandı"]
    issues = []
    inv_l = {t.lower() for t in inv}
    for d in card_dirs:
        name = d.name
        if name.lower() in inv_l:
            continue
        # partial match
        if any(name.lower() in t or t in name.lower() for t in inv_l):
            continue
        issues.append(
            f"[diff-stub] JOB_CARDS/{name} envanterde birebir yok "
            f"(kontrol et; slug farkı olabilir)"
        )
    return issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hook", action="store_true", help="fail-open JSON for hooks")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--strict", action="store_true", help="soft issues → exit 1")
    args = ap.parse_args()

    issues: list[str] = []
    cards = job_card_dirs()
    for d in cards:
        issues.extend(check_card(d))
    issues.extend(inventory_diff(cards))

    hard = [i for i in issues if i.startswith("[structural]")]
    soft = [i for i in issues if not i.startswith("[structural]")]

    report = {
        "ts": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "cards": len(cards),
        "hard": hard,
        "soft": soft,
        "status": "KALDI" if hard or (args.strict and soft) else "GECTI",
    }

    if args.hook:
        # fail-open: always exit 0 for IDE hooks
        print(json.dumps({"permission": "allow", "qa": report}, ensure_ascii=False))
        return 0

    print(f"qa_check cards={report['cards']} hard={len(hard)} soft={len(soft)}")
    for i in hard + (soft if not args.summary else soft[:5]):
        print(" -", i)
    if args.summary and len(soft) > 5:
        print(f" - … +{len(soft)-5} soft")
    print("DENETIM:", report["status"])
    if hard:
        return 1
    if args.strict and soft:
        return 1
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        # fail-open for unexpected errors in hook contexts
        if "--hook" in sys.argv:
            print(json.dumps({"permission": "allow", "error": str(e)}))
            raise SystemExit(0)
        print("qa_check error:", e, file=sys.stderr)
        raise SystemExit(1)
