#!/usr/bin/env bash
# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok
# stop: faz/audit damgası
set -euo pipefail
TS="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
LOG="$ROOT/REPORTS"
mkdir -p "$LOG"
echo "{\"ts\":\"$TS\",\"hook\":\"stop\",\"mode\":\"ASSESS-ONLY\",\"guardrail\":\"active\",\"note\":\"phase-audit stub\"}" >> "$LOG/hook-stop.jsonl"
echo "[phase-audit] $TS · Security OS stop damgası yazıldı → REPORTS/hook-stop.jsonl"
exit 0
