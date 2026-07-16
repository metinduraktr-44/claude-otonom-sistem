#!/usr/bin/env bash
# Appends a UTC-timestamped line to AUDIT_LOG.jsonl
set -euo pipefail
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
EVENT="${1:-manual}"
echo "{\"ts\":\"$TS\",\"event\":\"$EVENT\"}" >> AUDIT_LOG.jsonl
echo "$TS $EVENT"
