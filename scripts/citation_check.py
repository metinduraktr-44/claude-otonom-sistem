#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""citation_check.py — EXPERTS/FORECASTS dosyalarında URL + timestamp kontrolü."""
import json
import os
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "REPORTS" / "citation-check.jsonl"
URL_RE = re.compile(r"https?://\S+", re.I)
TS_RE = re.compile(r"\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}Z)?")


def needs_citation(path: Path) -> bool:
    rel = str(path.relative_to(ROOT))
    return any(p in rel for p in ("EXPERTS/", "EXPERTS_TALENT/", "FORECASTS/", "RESEARCH/"))


def check(path: Path):
    issues = []
    if not path.suffix == ".md" or not needs_citation(path):
        return issues
    text = path.read_text(encoding="utf-8", errors="replace")
    if len(text.strip()) < 50:
        return issues
    has_url = bool(URL_RE.search(text))
    has_ts = bool(TS_RE.search(text))
    if not has_url:
        issues.append(f"[citation] {path.relative_to(ROOT)}: URL eksik — unverified işaretle")
    if not has_ts:
        issues.append(f"[citation] {path.relative_to(ROOT)}: timestamp eksik")
    return issues


def main():
    issues = []
    hook_file = os.environ.get("CURSOR_HOOK_FILE", "")
    if hook_file and os.path.isfile(hook_file):
        issues.extend(check(Path(hook_file)))

    os.makedirs(LOG.parent, exist_ok=True)
    entry = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "issues": issues}
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    for i in issues:
        print(i, file=sys.stderr)
    sys.exit(0)


if __name__ == "__main__":
    main()
