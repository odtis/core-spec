#!/usr/bin/env bash
# P1-E04: Verification API latency conformance (ODTIS-0318).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/verification-api-latency-check.sh"

echo "== Verification API latency checks (ODTIS-0318) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

[[ -f "$ROOT/conformance/tests/core-identity/test_odtis_0318.md" ]] \
  || { echo "FAIL: missing test_odtis_0318.md" >&2; exit 1; }

echo ""
echo "Verification API latency checks: PASS"
