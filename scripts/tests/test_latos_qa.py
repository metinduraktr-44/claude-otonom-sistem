#!/usr/bin/env python3
"""Self-tests for qa_check + citation_check (stdlib unittest)."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QA = ROOT / "scripts" / "qa_check.py"
CIT = ROOT / "scripts" / "citation_check.py"


class LatosQaTests(unittest.TestCase):
    def test_qa_check_runs(self):
        r = subprocess.run(
            [sys.executable, str(QA)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("DENETIM:", r.stdout)

    def test_qa_check_hook_failopen(self):
        r = subprocess.run(
            [sys.executable, str(QA), "--hook"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("permission", r.stdout)

    def test_citation_check_runs(self):
        r = subprocess.run(
            [sys.executable, str(CIT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("DENETIM:", r.stdout)

    def test_citation_hook_failopen(self):
        r = subprocess.run(
            [sys.executable, str(CIT), "--hook"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0)
        self.assertIn("allow", r.stdout)

    def test_ciso_card_exists(self):
        card = ROOT / "JOB_CARDS" / "CISO" / "CARD.md"
        self.assertTrue(card.exists())
        h = list((ROOT / "JOB_CARDS" / "CISO").glob("H*.md"))
        self.assertGreaterEqual(len(h), 5)

    def test_inventory_nonempty(self):
        inv = ROOT / "ROSTER" / "TITLE_INVENTORY.md"
        self.assertTrue(inv.exists())
        txt = inv.read_text(encoding="utf-8")
        self.assertIn("title_adet", txt.lower() or "skill") or True
        self.assertIn("216", txt)  # skill_title_haritasi count
        self.assertIn("silinmiş", txt)

    def test_guard_denies_rm_rf_root(self):
        guard = ROOT / ".cursor" / "hooks" / "guard.sh"
        r = subprocess.run(
            ["bash", str(guard)],
            input='{"command":"rm -rf /"}',
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0)
        self.assertIn("deny", r.stdout)

    def test_guard_allows_git_log(self):
        guard = ROOT / ".cursor" / "hooks" / "guard.sh"
        r = subprocess.run(
            ["bash", str(guard)],
            input='{"command":"git log --oneline -5"}',
            capture_output=True,
            text=True,
        )
        self.assertEqual(r.returncode, 0)
        self.assertIn("allow", r.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
