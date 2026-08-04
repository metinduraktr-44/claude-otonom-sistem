#!/usr/bin/env bash
# LIVE AJANS DASHBOARD — terminalde sürekli durum
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
  git branch --show-current
  git log -1 --oneline
  git status -sb | head -8
  echo
  echo "── DOĞRULA ──"
  python3 scripts/mcp_ajans_etki_uret.py --dogrula 2>&1 | tail -3
  python3 scripts/skill_ajans_uretim.py --dogrula 2>&1 | tail -3
  python3 scripts/holding_istirak_ajans_uret.py --dogrula 2>&1 | tail -2
  python3 scripts/title_soru_kisi_uret.py --dogrula 2>&1 | tail -2
  python3 scripts/validate.py 2>&1 | tail -3
  echo
  echo "── SAYILAR ──"
  python3 - <<'PY'
import json
from pathlib import Path
def j(p):
  return json.loads(Path(p).read_text(encoding='utf-8'))
h=j('data/holding_istirak_org.json')
q=j('data/title_soru_500.json')
p=j('data/title_top_kisiler.json')
s=j('data/soru_bankasi.json')
u=j('data/ulke_pazar_iskeleti.json')
print(f"istirak={h['istirak_adet']}  rol={h['role_adet']}  prompt_hedef={h['prompt_hedef']}")
print(f"soru_bankasi={s['toplam_soru']}  title_soru={q['questions_per_title']}/role × {q['role_adet']} = {q['toplam_soru_indeks']}")
print(f"ulke={u['ulke_adet']}  domain_kisi={len(p['domains'])}×100")
print(f"rol_kart={len(list(Path('uretim/rol-kartlari').glob('*.md')))}  transfer={len(list(Path('uretim/devir/istirak').glob('*TRANSFER.md')))}")
print(f"mcp/skill dogrula dosyalari hazir · 🚩900B RED")
PY
  echo
  echo "── SON AUDIT ──"
  tail -3 AUDIT_LOG.jsonl
  echo
  echo "── SON BILGI ──"
  tail -5 BILGI_TABANI.md
  echo
  echo "── HOLDING KONSOLİDE (özet) ──"
  python3 scripts/holding_report.py >/dev/null
  head -25 docs/HOLDING-KONSOLIDE.md
  echo
  echo "── GÜNLÜK AJANS ──"
  python3 scripts/daily_agency.py 2>&1 | tail -5
  ls -1t uretim/gunluk/*.md 2>/dev/null | head -3
  echo
  echo "── LIVE LOOP · sonraki tur 60s · Ctrl+C durdur ──"
  echo "{\"ts\":\"$TS\",\"event\":\"live_dashboard_tick\"}" >> AUDIT_LOG.jsonl
}

# tek shot veya --watch
if [[ "${1:-}" == "--watch" ]]; then
  while true; do
    loop_once
    sleep 60
  done
else
  loop_once
fi
