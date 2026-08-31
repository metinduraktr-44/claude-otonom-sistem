#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""qa_check.py — LATOS QA hook: title inventory diff, char target skeleton check."""
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "ROSTER" / "TITLE_INVENTORY.md"
JOB_CARDS = ROOT / "JOB_CARDS"
LOG = ROOT / "REPORTS" / "qa-check.jsonl"


def load_inventory_slugs():
    if not INVENTORY.exists():
        return set()
    slugs = set()
    for line in INVENTORY.read_text(encoding="utf-8").splitlines():
        m = re.search(r"\| `\S+` \|", line)
        if m:
            slugs.add(m.group(0).strip("| ` ").rstrip("` "))
    return slugs


def job_card_slugs():
    if not JOB_CARDS.is_dir():
        return set()
    return {d.name for d in JOB_CARDS.iterdir() if d.is_dir() and (d / "CARD.md").exists()}


def check_file(path: Path):
    """Faz 0: skeleton check only — warn if CARD.md exists but <2000 chars."""
    warnings = []
    if path.suffix != ".md":
        return warnings
    rel = str(path.relative_to(ROOT))
    if "JOB_CARDS/" in rel and path.name == "CARD.md":
        text = path.read_text(encoding="utf-8", errors="replace")
        if len(text) < 2000:
            warnings.append(f"[qa] {rel}: {len(text)} chars (hedef 2000+ — Faz 4 skeleton OK)")
        headings = len(re.findall(r"^#{1,6}\s+", text, re.M))
        if headings < 200 and len(text) > 500:
            warnings.append(f"[qa] {rel}: {headings} başlık (hedef 200+ — fazlı üretim)")
    return warnings


def main():
    warnings = []
    inv = load_inventory_slugs()
    cards = job_card_slugs()
    missing_cards = inv - cards
    if inv and missing_cards:
        warnings.append(f"[qa] {len(missing_cards)}/{len(inv)} title için JOB_CARDS yok (Faz 4 bekleniyor)")

    hook_file = os.environ.get("CURSOR_HOOK_FILE", "")
    if hook_file and os.path.isfile(hook_file):
        warnings.extend(check_file(Path(hook_file)))

    os.makedirs(LOG.parent, exist_ok=True)
    entry = {"warnings": warnings, "inventory_count": len(inv), "job_cards": len(cards)}
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    for w in warnings:
        print(w, file=sys.stderr)
    sys.exit(0)


if __name__ == "__main__":
    main()
