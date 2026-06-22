#!/usr/bin/env bash
# #39: Documentation hygiene — TAREAS-IMPLEMENTACION archived, onboarding paths.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SCRIPT="../core-impl/scripts/doc-hygiene-check.sh"

echo "== Doc hygiene checks (#39) =="

if [[ -x "$SCRIPT" ]]; then
  bash "$SCRIPT"
else
  echo "FAIL: ${SCRIPT} not found or not executable" >&2
  exit 1
fi

echo ""
echo "Doc hygiene checks: PASS"
