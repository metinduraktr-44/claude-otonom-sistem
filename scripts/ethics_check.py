#!/usr/bin/env python3
"""Defense-only ethics pattern checker.

Flags offensive-cyber intent markers in agent-produced docs (not educational
detection/D3FEND prose). Fail-open under --hook.

Usage:
  python3 scripts/ethics_check.py [--hook] [--self-test] [paths...]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# High-signal offensive intent (not mere mention of "malware" in a refuse sentence)
OFFENSE = [
    ("exploit_poc", re.compile(r"(?i)\b(weaponized\s+poc|exploit\s+poc|0day\s+exploit\s+code)\b")),
    ("phishing_kit", re.compile(r"(?i)\b(phishing\s+kit|credential\s+harvest(?:ing)?\s+page)\b")),
    ("c2_malware", re.compile(r"(?i)\b(c2\s+implant|ransomware\s+builder|malware\s+dropper\s+source)\b")),
    ("auth_bypass_howto", re.compile(r"(?i)\b(bypass\s+authentication\s+by|auth\s+bypass\s+steps)\b")),
]

# Lines that explicitly refuse / document guardrails are OK
SAFE_CONTEXT = re.compile(
    r"(?i)(refuse|yasak|defense-only|detect(?:ion)?|d3fend|no exploits|guardrail|REDACTED)"
)

SKIP_DIRS = {".git", "node_modules", "katalog", "__pycache__"}


def should_skip(path: Path) -> bool:
    rel = str(path)
    return any(f"/{d}/" in f"/{rel}/" or rel.startswith(d + "/") for d in SKIP_DIRS)


def scan_text(text: str, source: str) -> list[str]:
    issues = []
    for i, line in enumerate(text.splitlines(), 1):
        if SAFE_CONTEXT.search(line):
            continue
        for name, pat in OFFENSE:
            if pat.search(line):
                issues.append(f"{source}:{i}: {name}")
    return issues


def self_test() -> int:
    bad = "Here is a weaponized poc for the target\n"
    good = "Refuse weaponized poc requests — defense-only.\n"
    bad_hits = scan_text(bad, "bad")
    good_hits = scan_text(good, "good")
    print("SELF-TEST ethics_check:")
    print(" - bad_hits:", bad_hits)
    print(" - good_hits:", good_hits)
    if bad_hits and not good_hits:
        print("DOĞRULAMA: GEÇTİ")
        return 0
    print("DOĞRULAMA: KALDI")
    return 1


def iter_targets(paths: list[str]) -> list[Path]:
    if not paths:
        patterns = [
            ".cursor/**/*.md",
            ".cursor/**/*.mdc",
            "docs/CILT14*.md",
            "docs/IS-LISTESI-GIGA-SECURITY.md",
            "uretim/devir/CURSOR-GIGA-MASTER-SECURITY.md",
            "LAYERS/**/*.md",
            "SECURITY*/**/*.md",
            "IMPLEMENTATION/**/*.md",
            "ASSESSMENTS/**/*.md",
        ]
        out: list[Path] = []
        for g in patterns:
            out.extend(ROOT.glob(g))
        return [p for p in out if p.is_file()]
    out = []
    for p in paths:
        path = Path(p)
        if path.is_dir():
            out.extend(x for x in path.rglob("*") if x.is_file())
        elif path.is_file():
            out.append(path)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hook", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("paths", nargs="*")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    targets = iter_targets(args.paths)
    issues: list[str] = []
    for path in targets:
        if should_skip(path):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = str(path.relative_to(ROOT)) if path.is_absolute() else str(path)
        issues.extend(scan_text(text, rel))

    print(f"ethics_check: tarandı={len(targets)} bulgu={len(issues)}")
    for i in issues:
        print(" -", i)
    if issues:
        print("DENETIM: KALDI")
        return 0 if args.hook else 1
    print("DENETIM: GECTI")
    return 0


if __name__ == "__main__":
    sys.exit(main())
