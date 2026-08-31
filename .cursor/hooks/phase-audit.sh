#!/usr/bin/env bash
# stop / phase-audit — fail-open; remind STATE + QA.
set -u
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT" || exit 0
TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
mkdir -p QA LATOS
{
  echo "## phase-audit $TS"
  if [[ -f LATOS/STATE.md ]]; then
    echo "LATOS/STATE.md: present"
    head -20 LATOS/STATE.md
  else
    echo "LATOS/STATE.md: missing"
  fi
  python3 scripts/qa_check.py --summary 2>/dev/null || echo "qa_check: skip/fail-open"
  python3 scripts/citation_check.py --summary 2>/dev/null || echo "citation_check: skip/fail-open"
} >> "QA/PHASE_AUDIT.log" 2>&1 || true
printf '%s\n' '{}'
exit 0
