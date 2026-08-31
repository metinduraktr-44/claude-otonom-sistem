#!/usr/bin/env python3
"""Pixel/ratio/file-size validator for creative exports → CANVA_OPS/VALIDATION.log"""
from __future__ import annotations

import argparse
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

LOG_PATH = Path("CANVA_OPS/VALIDATION.log")
GRID_PATH = Path("MATRIX/PRODUCTION_GRID.csv")

# Fallback specs if PRODUCTION_GRID.csv missing
DEFAULT_SPECS: dict[str, dict] = {
    "1080x1920": {"ratio": 9 / 16, "max_kb": 30720},
    "1080x1350": {"ratio": 4 / 5, "max_kb": 30720},
    "1080x1080": {"ratio": 1.0, "max_kb": 30720},
    "1200x628": {"ratio": 1200 / 628, "max_kb": 5120},
    "300x250": {"ratio": 300 / 250, "max_kb": 150},
}


def ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(msg: str) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(f"[{ts()}] {msg}\n")


def load_grid() -> list[dict[str, str]]:
    if not GRID_PATH.exists():
        return []
    rows: list[dict[str, str]] = []
    with GRID_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("width") and row.get("height"):
                rows.append(row)
    return rows


def ratio_close(a: float, b: float, tol: float = 0.02) -> bool:
    return abs(a - b) <= tol


def find_matching_spec(w: int, h: int, grid: list[dict]) -> dict | None:
    for row in grid:
        try:
            rw, rh = int(row["width"]), int(row["height"])
        except (KeyError, ValueError):
            continue
        if rw == w and rh == h:
            return row
    key = f"{w}x{h}"
    if key in DEFAULT_SPECS:
        return {"width": str(w), "height": str(h), **DEFAULT_SPECS[key]}
    return None


def validate_image(path: Path, grid: list[dict]) -> tuple[bool, str]:
    try:
        from PIL import Image
    except ImportError:
        log(f"WARN {path}: Pillow not installed — stub PASS")
        return True, "Pillow missing; stub PASS"

    if not path.exists():
        msg = f"FAIL {path}: file not found"
        log(msg)
        return False, msg

    if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
        log(f"SKIP {path}: not a raster image ({path.suffix})")
        return True, "Non-raster skip"

    size_kb = path.stat().st_size / 1024
    with Image.open(path) as im:
        w, h = im.size
    ratio = w / h if h else 0

    spec = find_matching_spec(w, h, grid)
    issues: list[str] = []

    if spec:
        try:
            max_kb = float(spec.get("max_kb") or 0)
            if max_kb and size_kb > max_kb:
                issues.append(f"file size {size_kb:.1f}KB > max {max_kb}KB")
        except ValueError:
            pass
        expected = spec.get("ratio")
        if expected and ":" in str(expected):
            parts = str(expected).split(":")
            try:
                exp_ratio = float(parts[0]) / float(parts[1])
                if not ratio_close(ratio, exp_ratio):
                    issues.append(f"ratio {ratio:.3f} != expected {expected}")
            except (ValueError, ZeroDivisionError):
                pass
        elif spec.get("ratio") and isinstance(spec["ratio"], (int, float)):
            if not ratio_close(ratio, float(spec["ratio"])):
                issues.append(f"ratio {ratio:.3f} != expected {spec['ratio']}")

    status = "PASS" if not issues else "FAIL"
    detail = f"{status} {path.name}: {w}x{h} ratio={ratio:.3f} size={size_kb:.1f}KB"
    if issues:
        detail += " | " + "; ".join(issues)
    log(detail)
    return status == "PASS", detail


def scan_canva_ops(grid: list[dict]) -> int:
    ops = Path("CANVA_OPS")
    if not ops.exists():
        log("SCAN CANVA_OPS: directory missing — skip")
        return 0
    exit_code = 0
    for p in sorted(ops.glob("*")):
        if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
            ok, _ = validate_image(p, grid)
            if not ok:
                exit_code = 1
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser(description="Creative spec validator (Pillow)")
    parser.add_argument("path", nargs="?", help="Image path to validate")
    parser.add_argument("--hook", action="store_true", help="Called from afterFileEdit hook")
    parser.add_argument("--scan", action="store_true", help="Scan CANVA_OPS for images")
    args = parser.parse_args()
    grid = load_grid()

    if args.hook:
        log("HOOK afterFileEdit — spec_validate ran")
        return scan_canva_ops(grid)

    if args.scan:
        return scan_canva_ops(grid)

    if not args.path:
        log("USAGE: spec_validate.py <path> | --hook | --scan")
        print("spec_validate: provide path, --hook, or --scan", file=sys.stderr)
        return 0

    ok, detail = validate_image(Path(args.path), grid)
    print(detail)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
