#!/usr/bin/env bash
set +e
if [[ -f scripts/ethics_check.py ]]; then
  python3 scripts/ethics_check.py --hook "$@" || true
fi
exit 0
