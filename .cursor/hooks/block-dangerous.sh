#!/usr/bin/env bash
# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok
# beforeShellExecution: tehlikeli kalıpları reddet (failClosed)
set -euo pipefail

CMD="${CURSOR_HOOK_COMMAND:-${1:-}}"
# Cursor bazı sürümlerde stdin JSON verir
if [[ -z "$CMD" ]] && [[ ! -t 0 ]]; then
  RAW="$(cat || true)"
  CMD="$(printf '%s' "$RAW" | python3 -c 'import sys,json,re
raw=sys.stdin.read()
cmd=""
try:
  o=json.loads(raw)
  cmd=o.get("command") or o.get("cmd") or ""
except Exception:
  cmd=raw
print(cmd)' 2>/dev/null || true)"
fi

DENY_PATTERNS=(
  'rm[[:space:]]+-rf[[:space:]]+/'
  'rm[[:space:]]+-rf[[:space:]]+~'
  'curl[^|]*\|[[:space:]]*bash'
  'wget[^|]*\|[[:space:]]*bash'
  'curl[^|]*\|[[:space:]]*sh'
  'chmod[[:space:]]+-R[[:space:]]+777[[:space:]]+/'
  'mkfs\.'
  'dd[[:space:]]+if=.*of=/dev/'
  ':\(\)\{:\|:&\};:'
  'base64[[:space:]]+-d.*\|[[:space:]]*bash'
  'history[[:space:]]*-c'
  'cat[[:space:]]+.*\.env[^=]*\|'
  'scp[[:space:]].*\.env'
)

for pat in "${DENY_PATTERNS[@]}"; do
  if printf '%s' "$CMD" | grep -Eiq -- "$pat"; then
    echo "[block-dangerous] DENY pattern matched — defense-only policy" >&2
    echo "[block-dangerous] refused command (redacted)" >&2
    exit 2
  fi
done

exit 0
