#!/usr/bin/env bash
# Extended profile Dockerfiles + config YAML smoke (#38).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SCRIPT="../core-impl/scripts/extended-build-check.sh"

echo "== Extended build checks (#38) =="

if [[ -x "$SCRIPT" ]]; then
  bash "$SCRIPT"
else
  echo "FAIL: ${SCRIPT} not found or not executable" >&2
  exit 1
fi

echo ""
echo "Extended build checks: PASS"
