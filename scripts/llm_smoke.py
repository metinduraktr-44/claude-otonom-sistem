#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""llm_smoke.py — LLM saglayici baglanti testi (OpenRouter tercih, Anthropic geri dusum).
Anahtar ortamda yoksa GUVENLI cikar (dongu kirilmaz), nasil eklenecegini soyler.
Kullanim: python3 scripts/llm_smoke.py
Ortam: OPENROUTER_API_KEY (+ ops. OPENROUTER_MODEL) veya ANTHROPIC_API_KEY (Secrets panelinden).
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from daily_agency import llm  # ayni saglayici katmani (OpenRouter->Anthropic)


def main():
    ork = os.environ.get("OPENROUTER_API_KEY", "").strip()
    ank = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not ork and not ank:
        print("LLM ANAHTARI YOK.")
        print("Ekle (Secrets paneli — chat'e YAPISTIRMA): OPENROUTER_API_KEY")
        print("  ops. OPENROUTER_MODEL (varsayilan: anthropic/claude-3.5-sonnet)")
        print("Anahtar eklenince bu test canli dogrulama yapar.")
        return 0
    saglayici = "OpenRouter" if ork else "Anthropic"
    model = os.environ.get("OPENROUTER_MODEL", "anthropic/claude-3.5-sonnet") if ork else "claude-sonnet-4-5"
    print(f"Saglayici: {saglayici} · Model: {model}")
    out = llm("Tek kelimeyle yanit ver: 'canli'. Baska hicbir sey yazma.", max_tokens=16)
    if out is None:
        print("BAGLANTI BASARISIZ — yukaridaki SKIPPED satirina bak (anahtar/model/ag).")
        return 1
    print("YANIT:", out.strip()[:200])
    print("LLM BAGLANTISI: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
