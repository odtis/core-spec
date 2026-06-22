#!/usr/bin/env bash
# P1-E01 / P2-E01: FAL controls conformance smoke (ODTIS-0106).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

TN_SCRIPT="../core-impl/ven-trust-network/scripts/fal-controls-check.sh"

echo "== FAL controls checks (ODTIS-0106) =="

if [[ -x "$TN_SCRIPT" ]]; then
  bash "$TN_SCRIPT"
else
  echo "FAIL: ${TN_SCRIPT} not found or not executable" >&2
  exit 1
fi

[[ -f "$ROOT/conformance/tests/core-identity/test_odtis_0106.md" ]] \
  || { echo "FAIL: missing test_odtis_0106.md" >&2; exit 1; }

echo ""
echo "FAL controls checks: PASS"
