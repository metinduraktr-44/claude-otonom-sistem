#!/usr/bin/env python3
"""LATOS citation heuristic — EXPERTS / EXPERTS_TALENT URL+timestamp presence. Fail-open --hook."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [ROOT / "EXPERTS", ROOT / "EXPERTS_TALENT"]
URL_RE = re.compile(r"https?://\S+", re.I)
TS_RE = re.compile(
    r"\b20\d{2}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}Z)?\b|\btimestamp\b|\bts:\b",
    re.I,
)
UNVERIFIED_RE = re.compile(r"\bunverified\b", re.I)


def scan_file(path: Path) -> list[str]:
    issues = []
    txt = path.read_text(encoding="utf-8", errors="replace")
    if path.name in {"README.md", ".gitkeep"}:
        return issues
    # skip empty stubs
    if len(txt.strip()) < 40:
        return issues
    has_url = bool(URL_RE.search(txt))
    has_ts = bool(TS_RE.search(txt))
    has_unverified = bool(UNVERIFIED_RE.search(txt))
    if not has_url and not has_unverified:
        issues.append(f"[citation] {path}: URL yok ve unverified işareti yok")
    if not has_ts and not has_unverified:
        issues.append(f"[citation] {path}: timestamp yok (veya unverified değil)")
    return issues


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hook", action="store_true")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    issues: list[str] = []
    scanned = 0
    for base in TARGETS:
        if not base.exists():
            continue
        for p in base.rglob("*.md"):
            scanned += 1
            issues.extend(scan_file(p))

    report = {
        "ts": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "scanned": scanned,
        "issues": issues,
        "status": "KALDI" if (args.strict and issues) else "GECTI",
    }

    if args.hook:
        print(json.dumps({"permission": "allow", "citation": report}, ensure_ascii=False))
        return 0

    print(f"citation_check scanned={scanned} issues={len(issues)}")
    show = issues if not args.summary else issues[:8]
    for i in show:
        print(" -", i)
    if args.summary and len(issues) > 8:
        print(f" - … +{len(issues)-8}")
    print("DENETIM:", report["status"])
    if args.strict and issues:
        return 1
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        if "--hook" in sys.argv:
            print(json.dumps({"permission": "allow", "error": str(e)}))
            raise SystemExit(0)
        print("citation_check error:", e, file=sys.stderr)
        raise SystemExit(1)
