#!/usr/bin/env python3
import runpy, sys
from pathlib import Path
sys.argv = ["secret_scan.py"] + sys.argv[1:]
runpy.run_path(str(Path(__file__).resolve().parents[2] / "scripts" / "secret_scan.py"), run_name="__main__")
