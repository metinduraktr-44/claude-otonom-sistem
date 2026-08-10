#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""llm_smoke.py — LLM saglayici baglanti testi.
Oncelik: OpenRouter -> Gemini -> Anthropic.
Kullanim: python3 scripts/llm_smoke.py
Ortam (Secrets paneli — chat'e YAPISTIRMA):
  OPENROUTER_API_KEY (+ ops. OPENROUTER_MODEL)
  GEMINI_API_KEY (+ ops. GEMINI_MODEL, varsayilan gemini-flash-latest)
  ANTHROPIC_API_KEY
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_agency import llm


def main():
    ork = os.environ.get("OPENROUTER_API_KEY", "").strip()
    gem = os.environ.get("GEMINI_API_KEY", "").strip()
    ank = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not ork and not gem and not ank:
        print("LLM ANAHTARI YOK.")
        print("Ekle (Secrets paneli — chat'e YAPISTIRMA):")
        print("  OPENROUTER_API_KEY (+ ops. OPENROUTER_MODEL)")
        print("  GEMINI_API_KEY (+ ops. GEMINI_MODEL=gemini-flash-latest)")
        print("  ANTHROPIC_API_KEY")
        return 0
    if ork:
        saglayici, model = "OpenRouter", os.environ.get("OPENROUTER_MODEL", "anthropic/claude-3.5-sonnet")
    elif gem:
        saglayici, model = "Gemini", os.environ.get("GEMINI_MODEL", "gemini-flash-latest")
    else:
        saglayici, model = "Anthropic", "claude-sonnet-4-5"
    print(f"Saglayici: {saglayici} · Model: {model}")
    out = llm("Tek kelimeyle yanit ver: 'canli'. Baska hicbir sey yazma.", max_tokens=32)
    if out is None:
        print("BAGLANTI BASARISIZ — yukaridaki SKIPPED satirina bak (anahtar/model/ag).")
        return 1
    print("YANIT:", out.strip()[:200])
    print("LLM BAGLANTISI: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
