#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Google Gemini (Generative Language API) istemcisi.

Env: GEMINI_API_KEY (veya GOOGLE_API_KEY)
Model: GEMINI_MODEL (varsayılan gemini-flash-latest)
Secret ASLA commit edilmez.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any

BASE = os.environ.get(
    "GEMINI_BASE_URL",
    "https://generativelanguage.googleapis.com/v1beta",
).rstrip("/")
DEFAULT_MODEL = os.environ.get("GEMINI_MODEL", "gemini-flash-latest")


def api_key() -> str:
    return (
        os.environ.get("GEMINI_API_KEY")
        or os.environ.get("GOOGLE_API_KEY")
        or ""
    ).strip()


def configured() -> bool:
    return bool(api_key())


def status() -> dict[str, Any]:
    key = api_key()
    return {
        "provider": "gemini",
        "configured": bool(key),
        "key_prefix": (key[:10] + "…") if len(key) >= 10 else ("set" if key else ""),
        "model": DEFAULT_MODEL,
        "base_url": BASE,
        "mode": "LIVE" if key else "DRY-RUN",
    }


def chat(
    prompt: str,
    *,
    system: str | None = None,
    model: str | None = None,
    max_tokens: int = 1600,
    temperature: float = 0.4,
    timeout: int = 120,
) -> str | None:
    if not configured():
        return None
    mid = model or DEFAULT_MODEL
    url = f"{BASE}/models/{mid}:generateContent"
    body: dict[str, Any] = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": max_tokens,
            "temperature": temperature,
        },
    }
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "X-goog-api-key": api_key(),
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")[:400]
        print(f"GEMINI HTTP {e.code}: {err}")
        return None
    except Exception as e:
        print(f"GEMINI SKIPPED: {e}")
        return None
    cands = data.get("candidates") or []
    if not cands:
        print("GEMINI: boş candidates", list(data.keys()))
        return None
    parts = ((cands[0].get("content") or {}).get("parts")) or []
    texts = [p.get("text", "") for p in parts if isinstance(p, dict) and p.get("text")]
    return "\n".join(texts) if texts else None


def smoke() -> dict[str, Any]:
    st = status()
    if not st["configured"]:
        return {**st, "ok": False, "reason": "GEMINI_API_KEY eksik"}
    text = chat(
        "Yanıtla tek kelime: PONG",
        system="Kısa yanıt. Tek kelime.",
        max_tokens=32,
        temperature=0,
    )
    return {
        **st,
        "ok": bool(text),
        "reply": (text or "")[:120],
        "reason": None if text else "chat boş/hata",
    }


if __name__ == "__main__":
    import sys

    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "status":
        print(json.dumps(status(), ensure_ascii=False, indent=2))
    elif cmd == "smoke":
        r = smoke()
        print(json.dumps(r, ensure_ascii=False, indent=2))
        sys.exit(0 if (r.get("ok") or not configured()) else 1)
    else:
        print("usage: gemini_client.py [status|smoke]", file=sys.stderr)
        sys.exit(2)
