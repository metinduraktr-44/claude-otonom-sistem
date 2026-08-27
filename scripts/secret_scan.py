#!/usr/bin/env python3
"""Defense-only secret hygiene scanner.

Detects high-risk *patterns*; reports REDACTED evidence — never stores raw secrets.
Placeholders ${VAR} / vault:// / op:// / <REDACTED> are allowed.

Usage:
  python3 scripts/secret_scan.py [--hook] [--self-test] [paths...]
Exit: 0 = GECTI (or fail-open hook), 1 = KALDI (CLI)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Patterns that look like real secrets — matches are NEVER printed in full
PATTERNS = [
    ("aws_access_key_id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("aws_secret_access_key", re.compile(r"(?i)aws_secret_access_key\s*[:=]\s*['\"]?[A-Za-z0-9/+=]{40}")),
    ("generic_api_key_assignment", re.compile(r"(?i)(api[_-]?key|secret[_-]?key|access[_-]?token)\s*[:=]\s*['\"][^'\"\n]{12,}['\"]")),
    ("bearer_jwt_like", re.compile(r"\bBearer\s+eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b")),
    ("private_key_block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
]

ALLOW_MARKERS = ("${", "vault://", "op://", "<REDACTED>", "REDACTED")

SKIP_DIRS = {
    ".git",
    "node_modules",
    "katalog",
    ".claude/katalog-mit",
    "__pycache__",
    "uretim/gunluk",
}


def redact(s: str) -> str:
    if len(s) <= 8:
        return "<REDACTED>"
    return s[:4] + "…" + "<REDACTED>"


def is_allowed_line(line: str) -> bool:
    return any(m in line for m in ALLOW_MARKERS)


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & SKIP_DIRS:
        return True
    rel = str(path.relative_to(ROOT)) if path.is_absolute() else str(path)
    for d in SKIP_DIRS:
        if rel.startswith(d.rstrip("/") + "/") or rel == d:
            return True
    return False


def scan_text(text: str, source: str) -> list[str]:
    issues = []
    for i, line in enumerate(text.splitlines(), 1):
        if is_allowed_line(line):
            continue
        for name, pat in PATTERNS:
            m = pat.search(line)
            if m:
                issues.append(f"{source}:{i}: {name} → {redact(m.group(0))}")
    return issues


def scan_path(path: Path) -> list[str]:
    if should_skip(path):
        return []
    try:
        data = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    return scan_text(data, str(path.relative_to(ROOT) if path.is_absolute() else path))


def self_test() -> int:
    """Prove AKIA-like pattern flags as REDACTED without storing secrets."""
    # Build synthetically so this source file does not embed a contiguous AKIA… literal.
    synthetic = "AKIA" + "IOSFODNN7" + "EXAMPLE"
    fixture = f"aws_key = {synthetic}\n"
    issues = scan_text(fixture, "fixture")
    ok = any("aws_access_key_id" in i and "<REDACTED>" in i for i in issues)
    leaked = any(synthetic in i for i in issues)
    print("SELF-TEST secret_scan:")
    for i in issues:
        print(" -", i)
    if ok and not leaked:
        print("DOĞRULAMA: GEÇTİ (pattern flagged, value REDACTED)")
        return 0
    print("DOĞRULAMA: KALDI")
    return 1


def iter_targets(paths: list[str]) -> list[Path]:
    if not paths:
        globs = [
            "scripts/**/*.py",
            ".cursor/**/*",
            "docs/*.md",
            "SECURITY*/**/*",
            "LAYERS/**/*",
            "tools/security-scanners/**/*",
            "AGENTS.md",
            "STATE.md",
            "SECURITY.md",
        ]
        out: list[Path] = []
        for g in globs:
            out.extend(ROOT.glob(g))
        return [p for p in out if p.is_file()]
    out = []
    for p in paths:
        path = Path(p)
        if path.is_dir():
            out.extend([x for x in path.rglob("*") if x.is_file()])
        elif path.is_file():
            out.append(path)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hook", action="store_true", help="Fail-open for editor hooks")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("paths", nargs="*")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    targets = iter_targets(args.paths)
    issues: list[str] = []
    for path in targets:
        issues.extend(scan_path(path.resolve()))

    print(f"secret_scan: tarandı={len(targets)} bulgu={len(issues)}")
    for i in issues:
        print(" -", i)
    if issues:
        print("DENETIM: KALDI")
        return 0 if args.hook else 1
    print("DENETIM: GECTI")
    return 0


if __name__ == "__main__":
    sys.exit(main())
