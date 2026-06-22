#!/usr/bin/env bash
# P3-E04: Regulator, incidents, liability conformance smoke (ODTIS-0514..0516).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/operator-regulator-check.sh"

echo "== Operator regulator checks (P3-E04) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

echo ""
echo "Operator regulator package checks: PASS"
