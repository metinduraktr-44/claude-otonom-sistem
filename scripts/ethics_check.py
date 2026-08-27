#!/usr/bin/env python3
"""ethics_check.py — block offensive/exploit content patterns (defense-only).

# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "REPORTS"
SKIP_DIRS = {".git", "katalog", "node_modules", "__pycache__", ".venv", "REPORTS"}
SKIP_FILES = {"ethics_check.py", "block-dangerous.sh", "secret_scan.py"}

# Offensive intent markers — not security research vocabulary in defensive context
BLOCK_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("exploit_poc", re.compile(r"(?i)\b(exploit\s+poc|weaponize[d]?|proof[- ]of[- ]concept\s+exploit)\b")),
    ("malware_c2", re.compile(r"(?i)\b(malware\s+dropper|command[- ]and[- ]control\s+server|c2\s+implant)\b")),
    ("phishing_kit", re.compile(r"(?i)\b(phishing\s+kit|credential\s+harvest(?:ing)?\s+page)\b")),
    ("creds_stuffing", re.compile(r"(?i)\b(credential\s+stuffing\s+script|brute[- ]force\s+login\s+tool)\b")),
    ("bypass_guide", re.compile(r"(?i)\b(auth(?:entication)?\s+bypass\s+payload|privilege\s+escalation\s+exploit)\b")),
    ("curl_pipe_bash", re.compile(r"(?i)curl[^\n]*\|\s*(?:ba)?sh")),
    ("rm_rf_root", re.compile(r"(?i)rm\s+-rf\s+/\s*$")),
]

# Allow defensive mentions / policy prohibitions listing banned patterns
ALLOW_CONTEXT = re.compile(
    r"(?i)(\bdetect(?:ion)?\b|\bdefend\b|\bd3fend\b|\bmitigat\w*\b|\bprevent\b|"
    r"\bharden\b|\bmonitor\b|\bblock\b|\balert\b|incident\s+response|"
    r"\byasak\b|\byok\b|\bdeny\b|\bforbid\b|\breddet\b|\bguardrail\b|\bfailclosed\b|"
    r"\btehlikeli\b|\bbanned\b|\bprohibited\b|do\s+not|\basla\b|\bpattern\b)"
)


def scan_text(text: str, path: Path) -> list[dict]:
    findings: list[dict] = []
    for i, line in enumerate(text.splitlines(), 1):
        for kind, pat in BLOCK_PATTERNS:
            if not pat.search(line):
                continue
            if ALLOW_CONTEXT.search(line):
                # policy / defensive framing that lists banned patterns
                continue
            try:
                rel = str(path.resolve().relative_to(ROOT))
            except ValueError:
                rel = str(path)
            findings.append(
                {
                    "file": rel,
                    "line": i,
                    "type": kind,
                    "snippet": "<REDACTED_OFFENSIVE_MATCH>",
                }
            )
    return findings


def iter_files(targets: list[Path]) -> list[Path]:
    out: list[Path] = []
    for t in targets:
        if t.is_file():
            if t.name not in SKIP_FILES and not (set(t.parts) & SKIP_DIRS):
                out.append(t)
            continue
        if not t.exists():
            continue
        for p in t.rglob("*"):
            if not p.is_file():
                continue
            if set(p.parts) & SKIP_DIRS:
                continue
            if p.name in SKIP_FILES:
                continue
            if p.suffix.lower() in {".md", ".py", ".sh", ".yml", ".yaml", ".mdc", ".txt"}:
                out.append(p)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Defense-only ethics/offensive pattern check")
    ap.add_argument("paths", nargs="*", default=["."], help="Files/dirs")
    ap.add_argument("--hook", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    targets = [Path(p) for p in args.paths]
    if args.hook:
        env_path = os.environ.get("CURSOR_HOOK_FILE_PATH")
        if env_path:
            targets = [Path(env_path)]
        elif not sys.stdin.isatty():
            raw = sys.stdin.read().strip()
            if raw:
                try:
                    o = json.loads(raw)
                    p = o.get("path") or o.get("file") or o.get("filePath")
                    if p:
                        targets = [Path(p)]
                except json.JSONDecodeError:
                    targets = [Path(raw)]

    findings: list[dict] = []
    for f in iter_files(targets):
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = f if f.is_absolute() else ROOT / f
        findings.extend(scan_text(text, rel))

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    summary = {
        "ts": ts,
        "tool": "ethics_check",
        "findings": len(findings),
        "items": findings[:50],
        "guardrail": "defense-only",
    }
    log_path = LOG_DIR / "ethics-check.jsonl"
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(summary, ensure_ascii=False) + "\n")

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"ethics_check: findings={len(findings)} log={log_path.relative_to(ROOT)}")
        for item in findings[:20]:
            print(f"  - {item['file']}:{item['line']} type={item['type']}")
        if findings:
            print("DENETIM: KALDI (ethics) — rewrite as defensive control/detection")
            return 1
        print("DENETIM: GECTI")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
