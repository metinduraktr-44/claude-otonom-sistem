#!/usr/bin/env bash
# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok
# stop: faz/audit damgası
set -euo pipefail
TS="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
LOG="$ROOT/REPORTS"
mkdir -p "$LOG"
echo "{\"ts\":\"$TS\",\"hook\":\"stop\",\"security_mode\":\"ASSESS-ONLY\",\"latos_phase\":\"0-1\",\"guardrail\":\"active\",\"note\":\"phase-audit Security+LATOS\"}" >> "$LOG/hook-stop.jsonl"
echo "[phase-audit] $TS · Security OS + LATOS stop damgası → REPORTS/hook-stop.jsonl"
exit 0
