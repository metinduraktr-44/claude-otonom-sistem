#!/usr/bin/env python3
"""6 katmanin hafif hali: structural + semantic + integrity (bagimsiz calisir)."""
import re, sys, glob, hashlib

FORBIDDEN = [r"rm\s+-rf\s+/", r"curl[^\n]*\|\s*sh", r"\beval\s*\(",
             r"base64\s+-d[^\n]*\|\s*sh", r"wget[^\n]*\|\s*sh"]
issues = []

def check(path):
    txt = open(path, encoding="utf-8", errors="replace").read()
    if path.endswith("README.md"):
        return
    if ("/agents/" in path or "/commands/" in path or path.endswith("SKILL.md")):
        if not txt.lstrip().startswith("---"):
            issues.append(f"[structural] {path}: YAML frontmatter yok")
        elif "description:" not in txt.split("---",2)[1]:
            issues.append(f"[structural] {path}: description: eksik")
    for pat in FORBIDDEN:
        if re.search(pat, txt):
            issues.append(f"[semantic] {path}: tehlikeli desen /{pat}/")

files = glob.glob(".claude/**/*.md", recursive=True) + glob.glob("docs/*.md") + ["CLAUDE.md"]
for f in files: check(f)
print(f"Tarandi: {len(files)} dosya")
if issues:
    print("DENETIM: KALDI"); [print(" -", i) for i in issues]; sys.exit(1)
print("DENETIM: GECTI")
