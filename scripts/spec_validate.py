#!/usr/bin/env python3
"""Creative Agency OS — visual/spec validation (stdlib PNG IHDR; optional Pillow).

Writes append-only lines to CANVA_OPS/VALIDATION.log.
Hooks: --hook → always exit 0 (fail-open).
CLI: --strict → exit 1 on failures.
"""
from __future__ import annotations

import argparse
import struct
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "CANVA_OPS" / "VALIDATION.log"

try:
    from PIL import Image  # type: ignore

    HAS_PIL = True
except Exception:
    HAS_PIL = False
    Image = None  # type: ignore


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def ensure_log() -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    if not LOG.exists():
        LOG.write_text("# VALIDATION.log — append-only\n", encoding="utf-8")


def append_log(line: str) -> None:
    ensure_log()
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line.rstrip() + "\n")


def read_png_ihdr(path: Path) -> tuple[int, int, int] | None:
    """Return (width, height, bit_depth) from PNG IHDR or None."""
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    # IHDR: length(4) + type(4) + data(13) …
    if data[12:16] != b"IHDR":
        return None
    width, height, bit_depth = struct.unpack(">IIB", data[16:25])
    return width, height, bit_depth


def validate_image(path: Path) -> list[str]:
    issues: list[str] = []
    if not path.is_file():
        return [f"missing file: {path}"]

    suffix = path.suffix.lower()
    if suffix == ".png":
        ihdr = read_png_ihdr(path)
        if not ihdr:
            issues.append("PNG header/IHDR okunamadı")
        else:
            w, h, _ = ihdr
            if w < 1 or h < 1:
                issues.append(f"geçersiz boyut {w}x{h}")
            if w * h > 100_000_000:
                issues.append(f"aşırı piksel {w}x{h}")
    elif suffix in {".jpg", ".jpeg", ".webp", ".gif"}:
        if not HAS_PIL:
            issues.append(
                "TODO(Pillow): non-PNG için Pillow yok — yalnızca varlık kontrolü"
            )
    else:
        issues.append(f"desteklenmeyen uzantı: {suffix or '(yok)'}")

    if HAS_PIL and suffix in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
        try:
            with Image.open(path) as im:  # type: ignore[misc]
                im.verify()
            with Image.open(path) as im:  # type: ignore[misc]
                w, h = im.size
                if w < 32 or h < 32:
                    issues.append(f"çok küçük {w}x{h}")
                # Rough empty check: extreme compression / tiny palette only — skip heavy scan
        except Exception as e:  # noqa: BLE001
            issues.append(f"Pillow verify fail: {e}")

    return issues


def collect_targets(paths: list[str]) -> list[Path]:
    if not paths:
        export_dir = ROOT / "CANVA_OPS" / "exports"
        if export_dir.is_dir():
            return sorted(
                p
                for p in export_dir.rglob("*")
                if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"}
            )
        return []
    out: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if not p.is_absolute():
            p = (Path.cwd() / p).resolve()
        if p.is_dir():
            out.extend(
                q
                for q in p.rglob("*")
                if q.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"}
            )
        else:
            out.append(p)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Validate creative exports (PNG IHDR / optional Pillow)."
    )
    ap.add_argument("paths", nargs="*", help="File(s) or dir(s); default CANVA_OPS/exports")
    ap.add_argument(
        "--hook",
        action="store_true",
        help="Fail-open for Cursor hooks (always exit 0)",
    )
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 if any target fails",
    )
    ap.add_argument(
        "--self-test",
        action="store_true",
        help="Write a tiny fixture PNG and validate it",
    )
    args = ap.parse_args(argv)

    ensure_log()
    ts = utc_now()
    engine = "Pillow" if HAS_PIL else "stdlib-IHDR"
    # TODO: full perceptual empty/contrast checks require Pillow + numpy — not bundled.

    if args.self_test:
        fix = ROOT / "CANVA_OPS" / "exports" / "_fixture_1x1.png"
        fix.parent.mkdir(parents=True, exist_ok=True)
        # Minimal 1x1 IHDR-valid PNG (red pixel)
        png = (
            b"\x89PNG\r\n\x1a\n"
            b"\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde"
            b"\x00\x00\x00\x0cIDATx\x9cc\xf8\xcf\xc0\x00\x00\x00\x03\x00\x01\x00\x05\xfe\xd4\xef"
            b"\x00\x00\x00\x00IEND\xaeB`\x82"
        )
        # Use a well-formed tiny PNG via struct-built IHDR + empty IDAT may fail Pillow;
        # prefer writing known-good minimal file:
        png = bytes.fromhex(
            "89504e470d0a1a0a0000000d4948445200000001000000010802000000907753de"
            "0000000c49444154789c63f8cfc00000000300010005fed4ef0000000049454e44ae426082"
        )
        fix.write_bytes(png)
        args.paths = [str(fix)]

    targets = collect_targets(args.paths)
    if not targets:
        msg = f"[{ts}] INFO engine={engine} targets=0 (skip)"
        append_log(msg)
        print(msg)
        print("DENETIM: GECTI (no targets)")
        return 0

    failed = 0
    for t in targets:
        issues = validate_image(t)
        rel = t
        try:
            rel = t.relative_to(ROOT)
        except ValueError:
            pass
        if issues:
            failed += 1
            line = f"[{ts}] KALDI {rel} :: {'; '.join(issues)}"
        else:
            line = f"[{ts}] GECTI {rel} engine={engine}"
        append_log(line)
        print(line)

    summary = f"[{ts}] SUMMARY checked={len(targets)} failed={failed} engine={engine}"
    append_log(summary)
    print(summary)

    if failed:
        print("DENETIM: KALDI")
        if args.hook:
            return 0
        return 1 if args.strict else 0

    print("DENETIM: GECTI")
    return 0


if __name__ == "__main__":
    sys.exit(main())
