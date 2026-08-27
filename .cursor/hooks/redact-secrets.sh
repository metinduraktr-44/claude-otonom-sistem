#!/usr/bin/env bash
# GUARDRAIL AKTİF — savunma-only, secret-redakte, exploit-yok
# beforeReadFile: secret içeren yolları uyar (değer basma)
set -euo pipefail

TARGET="${CURSOR_HOOK_FILE_PATH:-${1:-}}"
if [[ -z "$TARGET" ]] && [[ ! -t 0 ]]; then
  RAW="$(cat || true)"
  TARGET="$(printf '%s' "$RAW" | python3 -c 'import sys,json
raw=sys.stdin.read()
try:
  o=json.loads(raw)
  print(o.get("path") or o.get("file") or o.get("filePath") or "")
except Exception:
  print("")' 2>/dev/null || true)"
fi

base="$(basename -- "$TARGET" 2>/dev/null || true)"
case "$base" in
  .env|.env.*|*.pem|*.p12|id_rsa|id_ed25519|credentials.json|service-account*.json)
    if [[ "$base" != ".env.example" ]]; then
      echo "[redact-secrets] WARN: sensitive path type — treat contents as <REDACTED>" >&2
      echo "[redact-secrets] path=$(dirname -- "$TARGET")/<REDACTED_NAME>" >&2
    fi
    ;;
esac
exit 0
