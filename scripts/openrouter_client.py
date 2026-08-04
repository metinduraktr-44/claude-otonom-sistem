#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OpenRouter LLM istemcisi — OPENROUTER_API_KEY ile canlı, yoksa dry-run.

API: https://openrouter.ai/api/v1 (OpenAI-uyumlu chat/completions)
İlke: secret ASLA commit edilmez; key yoksa None döner, döngü kırılmaz.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from typing import Any

BASE_URL = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1").rstrip("/")
DEFAULT_MODEL = os.environ.get(
    "OPENROUTER_MODEL",
    "anthropic/claude-sonnet-4",
)
HTTP_REFERER = os.environ.get("OPENROUTER_HTTP_REFERER", "https://github.com/metinduraktr-44/claude-otonom-sistem")
APP_TITLE = os.environ.get("OPENROUTER_APP_TITLE", "claude-otonom-sistem")


def api_key() -> str:
    return (os.environ.get("OPENROUTER_API_KEY") or "").strip()


def configured() -> bool:
    return bool(api_key())


def status() -> dict[str, Any]:
    key = api_key()
    return {
        "provider": "openrouter",
        "configured": bool(key),
        "key_prefix": (key[:12] + "…") if len(key) >= 12 else ("set" if key else ""),
        "model": DEFAULT_MODEL,
        "base_url": BASE_URL,
        "mode": "LIVE" if key else "DRY-RUN",
    }


def _headers() -> dict[str, str]:
    key = api_key()
    if not key:
        raise RuntimeError("OPENROUTER_API_KEY yok — dry-run")
    return {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "HTTP-Referer": HTTP_REFERER,
        "X-Title": APP_TITLE,
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
    """Tek tur chat. Key yoksa None. Hata olursa None + stderr mesajı."""
    if not configured():
        return None
    messages: list[dict[str, str]] = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    body = {
        "model": model or DEFAULT_MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    req = urllib.request.Request(
        f"{BASE_URL}/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers=_headers(),
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")[:400]
        print(f"OPENROUTER HTTP {e.code}: {err}")
        return None
    except Exception as e:
        print(f"OPENROUTER SKIPPED: {e}")
        return None
    choices = data.get("choices") or []
    if not choices:
        print("OPENROUTER: boş choices", list(data.keys()))
        return None
    msg = choices[0].get("message") or {}
    content = msg.get("content")
    if isinstance(content, list):
        return "".join(
            part.get("text", "") if isinstance(part, dict) else str(part) for part in content
        )
    return content if isinstance(content, str) else None


def models_probe(limit: int = 5) -> dict[str, Any]:
    """Key varken /models uç noktasını dener (smoke)."""
    out: dict[str, Any] = {"ok": False, **status()}
    if not configured():
        out["reason"] = "OPENROUTER_API_KEY eksik"
        return out
    req = urllib.request.Request(f"{BASE_URL}/models", headers=_headers(), method="GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        items = data.get("data") or []
        out["ok"] = True
        out["model_count"] = len(items)
        out["sample"] = [m.get("id") for m in items[:limit] if isinstance(m, dict)]
    except urllib.error.HTTPError as e:
        out["reason"] = f"HTTP {e.code}: {e.read().decode('utf-8', errors='replace')[:200]}"
    except Exception as e:
        out["reason"] = str(e)
    return out


def smoke_chat() -> dict[str, Any]:
    """1-token canlı ping: 'ping' → kısa yanıt."""
    st = status()
    if not st["configured"]:
        return {**st, "ok": False, "reason": "OPENROUTER_API_KEY eksik — Cursor Secrets / .env"}
    text = chat(
        "Yanıtla tek kelime: PONG",
        system="Kısa yanıt. Türkçe veya İngilizce tek kelime.",
        max_tokens=16,
        temperature=0,
    )
    return {
        **st,
        "ok": bool(text),
        "reply": (text or "")[:80],
        "reason": None if text else "chat boş/hata",
    }


if __name__ == "__main__":
    import sys

    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "status":
        print(json.dumps(status(), ensure_ascii=False, indent=2))
    elif cmd == "models":
        print(json.dumps(models_probe(), ensure_ascii=False, indent=2))
    elif cmd == "smoke":
        result = smoke_chat()
        print(json.dumps(result, ensure_ascii=False, indent=2))
        # key yok = dry-run exit 0; key var ama fail = 1
        if not configured():
            sys.exit(0)
        sys.exit(0 if result.get("ok") else 1)
    else:
        print("usage: openrouter_client.py [status|models|smoke]", file=sys.stderr)
        sys.exit(2)
