#!/usr/bin/env bash
# Intent: failClosed on dangerous patterns when Cursor provides command via stdin/env.
# Missing input → fail-open (exit 0) so CI/agents are not bricked.
set +e
CMD="${CURSOR_SHELL_COMMAND:-${1:-}}"
if [[ -z "$CMD" ]] && [[ ! -t 0 ]]; then
  CMD=$(cat 2>/dev/null || true)
fi
if [[ -z "$CMD" ]]; then exit 0; fi
if echo "$CMD" | grep -Eiq 'rm[[:space:]]+-rf[[:space:]]+/|curl[^\n]*\|[[:space:]]*sh|wget[^\n]*\|[[:space:]]*sh|base64[[:space:]]+-d[^\n]*\|[[:space:]]*sh|mkfs\.|dd[[:space:]]+if=.*of=/dev/'; then
  echo "[dangerous-shell-block] RED: refused dangerous pattern" >&2
  exit 2
fi
exit 0
