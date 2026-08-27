#!/usr/bin/env bash
# LATOS + Security guard — beforeShellExecution
# Tehlikeli komutları reddet; git kurtarma komutlarına izin ver
set -euo pipefail

CMD="${CURSOR_HOOK_COMMAND:-${1:-}}"
if [[ -z "$CMD" ]] && [[ ! -t 0 ]]; then
  RAW="$(cat || true)"
  CMD="$(printf '%s' "$RAW" | python3 -c 'import sys,json
raw=sys.stdin.read()
cmd=""
try:
  o=json.loads(raw)
  cmd=o.get("command") or o.get("cmd") or ""
except Exception:
  cmd=raw
print(cmd)' 2>/dev/null || true)"
fi

# Git kurtarma — allow
if printf '%s' "$CMD" | grep -Eiq 'git (log|show|restore|checkout|fsck|rev-parse)'; then
  exit 0
fi

# Tehlikeli kalıplar — deny
DENY_PATTERNS=(
  'rm[[:space:]]+-rf[[:space:]]+/'
  'rm[[:space:]]+-rf[[:space:]]+~'
  'curl[^|]*\|[[:space:]]*bash'
  'wget[^|]*\|[[:space:]]*bash'
  'curl[^|]*\|[[:space:]]*sh'
  'git[[:space:]]+push[[:space:]]+.*--force'
  'chmod[[:space:]]+-R[[:space:]]+777[[:space:]]+/'
  'mkfs\.'
  'dd[[:space:]]+if=.*of=/dev/'
)

for pat in "${DENY_PATTERNS[@]}"; do
  if printf '%s' "$CMD" | grep -Eiq -- "$pat"; then
    echo "[guard] DENY — defense-only policy" >&2
    exit 2
  fi
done

exit 0
