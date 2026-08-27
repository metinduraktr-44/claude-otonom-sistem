#!/usr/bin/env python3
"""secret_scan.py — defense-only secret pattern scanner (warn/redact log; never store secrets).

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
SKIP_DIRS = {
    ".git",
    "katalog",
    "node_modules",
    "__pycache__",
    ".venv",
    "ARCHIVE",
}

# High-signal patterns — values never written to logs
PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("aws_access_key_id", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("generic_api_key_assign", re.compile(r"(?i)(api[_-]?key|secret[_-]?key|access[_-]?token)\s*[:=]\s*['\"][^'\"]{12,}['\"]")),
    ("bearer_token", re.compile(r"(?i)authorization\s*[:=]\s*['\"]?bearer\s+[A-Za-z0-9\-._~+/]+=*")),
    ("private_key_header", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("github_pat", re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}")),
    ("slack_token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
]

ALLOW_PLACEHOLDERS = re.compile(
    r"(\$\{[A-Z0-9_]+\}|vault://|op://|<REDACTED>|<YOUR_[A-Z0-9_]+>)"
)


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & SKIP_DIRS:
        return True
    name = path.name
    if name.endswith(".example") or name == ".env.example":
        return False
    return False


def scan_text(text: str, path: Path) -> list[dict]:
    findings: list[dict] = []
    for i, line in enumerate(text.splitlines(), 1):
        if ALLOW_PLACEHOLDERS.search(line) and not re.search(
            r"AKIA[0-9A-Z]{16}|BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY", line
        ):
            # placeholder-heavy lines still checked for hard secrets above
            pass
        for kind, pat in PATTERNS:
            if pat.search(line):
                # skip empty assignments like KEY=
                if re.search(r"(?i)(api[_-]?key|secret|token)\s*[:=]\s*['\"]?\s*['\"]?$", line.strip()):
                    continue
                findings.append(
                    {
                        "file": str(path.relative_to(ROOT)),
                        "line": i,
                        "type": kind,
                        "value": "<REDACTED>",
                    }
                )
    return findings


def iter_files(targets: list[Path]) -> list[Path]:
    out: list[Path] = []
    for t in targets:
        if t.is_file():
            out.append(t)
            continue
        if not t.exists():
            continue
        for p in t.rglob("*"):
            if not p.is_file() or should_skip(p):
                continue
            if p.suffix.lower() in {
                ".md",
                ".py",
                ".sh",
                ".yml",
                ".yaml",
                ".json",
                ".tf",
                ".env",
                ".txt",
                ".toml",
                ".mdc",
            } or p.name.startswith(".env"):
                out.append(p)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Defense-only secret pattern scanner")
    ap.add_argument("paths", nargs="*", default=["."], help="Files/dirs to scan")
    ap.add_argument("--hook", action="store_true", help="Hook mode (stdin path optional)")
    ap.add_argument("--json", action="store_true", help="JSON summary to stdout")
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
        findings.extend(scan_text(text, f if f.is_absolute() else (ROOT / f)))

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    summary = {
        "ts": ts,
        "tool": "secret_scan",
        "findings": len(findings),
        "items": findings[:50],  # cap; values already <REDACTED>
        "note": "values never stored; location+type only",
    }
    log_path = LOG_DIR / "secret-scan.jsonl"
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(summary, ensure_ascii=False) + "\n")

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"secret_scan: findings={len(findings)} log={log_path.relative_to(ROOT)}")
        for item in findings[:20]:
            print(f"  - {item['file']}:{item['line']} type={item['type']} value=<REDACTED>")
        if findings:
            print("DENETIM: KALDI (secret pattern) — replace with ${VAR}/vault:///<REDACTED>")
            return 1
        print("DENETIM: GECTI")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
