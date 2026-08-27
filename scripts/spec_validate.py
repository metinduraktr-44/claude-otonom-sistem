#!/usr/bin/env python3
"""Pillow-based spec validator stub — logs to CANVA_OPS/VALIDATION.log"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

LOG_PATH = Path("CANVA_OPS/VALIDATION.log")
MATRIX_REF = Path("MATRIX/CHANNEL_MATRIX.md")


def ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(msg: str) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"[{ts()}] {msg}\n")


def validate_image(path: Path) -> tuple[bool, str]:
    try:
        from PIL import Image
    except ImportError:
        log(f"STUB {path}: Pillow not installed — skip dimension check")
        return True, "Pillow missing; stub PASS"

    if not path.exists():
        msg = f"FAIL {path}: file not found"
        log(msg)
        return False, msg

    if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
        log(f"SKIP {path}: not a raster image ({path.suffix})")
        return True, "Non-raster skip"

    with Image.open(path) as im:
        w, h = im.size
    ratio = round(w / h, 3) if h else 0
    summary = f"{path.name}: {w}x{h} ratio={ratio}"
    log(f"CHECK {summary}")
    # Stub: always PASS with dimensions logged; Faz 5 adds MATRIX rules
    return True, summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Spec validator stub")
    parser.add_argument("path", nargs="?", help="Image path to validate")
    parser.add_argument("--hook", action="store_true", help="Called from afterFileEdit hook")
    args = parser.parse_args()

    if args.hook:
        log("HOOK afterFileEdit — spec_validate stub (no path in hook mode)")
        return 0

    if not args.path:
        log("USAGE: spec_validate.py <path> | --hook")
        print("spec_validate: provide path or --hook", file=sys.stderr)
        return 0

    ok, detail = validate_image(Path(args.path))
    print(detail)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
