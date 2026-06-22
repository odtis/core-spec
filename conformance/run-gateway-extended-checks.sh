#!/usr/bin/env bash
# P4-E02..E06 / #13: API gateway extended routes smoke.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SCRIPT="../core-impl/scripts/gateway-extended-check.sh"

echo "== Gateway extended checks (#13) =="

if [[ -x "$SCRIPT" ]]; then
  bash "$SCRIPT"
else
  echo "FAIL: ${SCRIPT} not found or not executable" >&2
  exit 1
fi

[[ -f "$ROOT/implementation/evidence/extended-gateway/lab-notes.md" ]] \
  || { echo "FAIL: missing extended-gateway lab-notes.md" >&2; exit 1; }

echo ""
echo "Gateway extended checks: PASS"
