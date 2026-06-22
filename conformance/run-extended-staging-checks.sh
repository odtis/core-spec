#!/usr/bin/env bash
# P4-E02..E06 / #12: Extended profile staging overlay + build smoke.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

BUILD_SCRIPT="../core-impl/scripts/extended-build-check.sh"

echo "== Extended staging checks (#12) =="

if [[ -x "$BUILD_SCRIPT" ]]; then
  bash "$BUILD_SCRIPT"
else
  echo "FAIL: ${BUILD_SCRIPT} not found or not executable" >&2
  exit 1
fi

[[ -f "$ROOT/implementation/evidence/extended-staging/lab-notes.md" ]] \
  || { echo "FAIL: missing extended-staging lab-notes.md" >&2; exit 1; }
[[ -f "$ROOT/implementation/component-bindings/extended-build.yaml" ]] \
  || { echo "FAIL: missing extended-build.yaml binding" >&2; exit 1; }

echo ""
echo "Extended staging checks: PASS"
