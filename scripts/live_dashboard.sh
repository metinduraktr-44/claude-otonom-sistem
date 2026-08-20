#!/usr/bin/env bash
# LIVE AJANS DASHBOARD — salt-okunur terminal paneli (dosya yazmaz)
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

loop_once() {
  TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  clear 2>/dev/null || true
  echo "╔══════════════════════════════════════════════════════════════╗"
  echo "║  CLAUDE OTONOM SİSTEM — LIVE  $TS"
  echo "╚══════════════════════════════════════════════════════════════╝"
  echo
  echo "── GIT ──"
  git branch --show-current 2>/dev/null || true
  git log -1 --oneline 2>/dev/null || true
  git status -sb 2>/dev/null | head -5
  echo
  echo "── LLM ──"
  python3 scripts/gemini_client.py status 2>/dev/null | head -8
  python3 scripts/openrouter_client.py status 2>/dev/null | head -8
  echo
  echo "── SAYILAR / DOĞRULA (salt okuma) ──"
  python3 - <<'PY'
import json
from pathlib import Path

def j(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))

checks = []
try:
    m = j("data/mcp_hiyerarsi.json")
    checks.append(f"mcp={m.get('mcp_adet', m.get('adet', '?'))}")
except Exception as e:
    checks.append(f"mcp=ERR:{e}")
try:
    e = j("data/etki_sahipleri.json")
    checks.append(f"tech={e.get('adet', len(e.get('items', e.get('kisiler', []))))}")
except Exception:
    checks.append("tech=?")
try:
    o = j("data/ozel_yetenekler.json")
    checks.append(f"cult={o.get('adet', len(o.get('items', o.get('kisiler', []))))}")
except Exception:
    checks.append("cult=?")
try:
    sk = j("data/skill_envanteri.json")
    checks.append(f"skills={sk.get('skill_adet', sk.get('adet', '?'))}")
except Exception:
    checks.append("skills=?")
try:
    th = j("data/skill_title_haritasi.json")
    checks.append(f"skill_titles={th.get('title_adet', th.get('adet', '?'))}")
except Exception:
    checks.append("skill_titles=?")
try:
    h = j("data/holding_istirak_org.json")
    print(f"istirak={h['istirak_adet']}  rol={h['role_adet']}  prompt_hedef={h['prompt_hedef']}")
except Exception as e:
    print(f"holding_ERR={e}")
try:
    q = j("data/title_soru_500.json")
    print(f"title_soru={q['questions_per_title']}/role × {q['role_adet']} = {q['toplam_soru_indeks']}")
except Exception as e:
    print(f"title_soru_ERR={e}")
try:
    s = j("data/soru_bankasi.json")
    print(f"soru_bankasi={s['toplam_soru']}")
except Exception:
    print("soru_bankasi=?")
try:
    u = j("data/ulke_pazar_iskeleti.json")
    p = j("data/title_top_kisiler.json")
    print(f"ulke={u['ulke_adet']}  domain_kisi={len(p.get('domains', {}))}×100")
except Exception:
    print("ulke/kisi=?")
rk = len(list(Path("uretim/rol-kartlari").glob("*.md"))) if Path("uretim/rol-kartlari").exists() else 0
tr = len(list(Path("uretim/devir/istirak").glob("*TRANSFER.md"))) if Path("uretim/devir/istirak").exists() else 0
print(f"rol_kart={rk}  transfer={tr}")
print(" · ".join(checks))
print("DENETIM: GECTI (salt-okuma) · 🚩900B RED")
PY
  echo
  echo "── SON AUDIT ──"
  tail -2 AUDIT_LOG.jsonl 2>/dev/null || true
  echo
  echo "── SON BILGI ──"
  tail -4 BILGI_TABANI.md 2>/dev/null || true
  echo
  echo "── HOLDING KONSOLİDE (özet, dosya yazılmaz) ──"
  head -22 docs/HOLDING-KONSOLIDE.md 2>/dev/null || echo "(yok)"
  echo
  echo "── GÜNLÜK AJANS ──"
  ls -1t uretim/gunluk/*.md 2>/dev/null | head -3 || echo "(yok)"
  echo
  echo "── LIVE · 60s refresh · tmux: holding-live ──"
}

if [[ "${1:-}" == "--watch" ]]; then
  while true; do
    loop_once
    sleep 60
  done
else
  loop_once
fi
