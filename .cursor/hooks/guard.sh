#!/usr/bin/env bash
# LATOS shell guard — fail-open. Deny dangerous patterns; allow git recovery.
set -u
INPUT=$(cat || true)
RESULT=$(INPUT="$INPUT" python3 - <<'PY'
import json, os, re, sys
raw = os.environ.get("INPUT", "")
cmd = raw
try:
    o = json.loads(raw)
    cmd = o.get("command") or (o.get("tool_input") or {}).get("command") or raw
except Exception:
    pass
cmd = cmd or ""
deny = [
    r"rm\s+-rf\s+/($|\s)",
    r"git\s+push\s+--force",
    r"git\s+push\s+-f(\s|$)",
    r"curl[^|\n]*\|\s*(ba)?sh",
    r"wget[^|\n]*\|\s*(ba)?sh",
]
for pat in deny:
    if re.search(pat, cmd, re.I):
        print('{"permission":"deny","agentMessage":"LATOS guard: dangerous shell pattern blocked"}')
        sys.exit(0)
if re.search(r"git\s+(log|show|restore|fsck|rev-parse|status|diff)", cmd, re.I):
    print('{"permission":"allow"}')
    sys.exit(0)
print('{"permission":"allow"}')
PY
) || RESULT='{"permission":"allow"}'
printf '%s\n' "$RESULT"
exit 0
