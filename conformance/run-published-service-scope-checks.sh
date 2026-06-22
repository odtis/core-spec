#!/usr/bin/env bash
# ODTIS-0501 / #15: Published service scope + staging overlay alignment.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SCRIPT="../core-impl/scripts/published-service-scope-check.sh"

echo "== Published service scope checks (#15) =="

if [[ -x "$SCRIPT" ]]; then
  bash "$SCRIPT"
else
  echo "FAIL: ${SCRIPT} not found or not executable" >&2
  exit 1
fi

[[ -f "$ROOT/implementation/evidence/published-service-scope/staging-overlays-2026.yaml" ]] \
  || { echo "FAIL: missing staging-overlays-2026.yaml" >&2; exit 1; }

echo ""
echo "Published service scope checks: PASS"
