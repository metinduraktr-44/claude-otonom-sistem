#!/usr/bin/env python3
import runpy, sys
from pathlib import Path
sys.argv = ["ethics_check.py"] + sys.argv[1:]
runpy.run_path(str(Path(__file__).resolve().parents[2] / "scripts" / "ethics_check.py"), run_name="__main__")
