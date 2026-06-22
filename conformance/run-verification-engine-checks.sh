#!/usr/bin/env bash
# P1-E03: Verification engine conformance smoke (ODTIS-0311..0314, ODTIS-0523).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/verification-engine-check.sh"

echo "== Verification engine checks (P1-E03) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/core-identity/test_odtis_0311.md \
  conformance/tests/core-identity/test_odtis_0312.md \
  conformance/tests/core-identity/test_odtis_0313.md \
  conformance/tests/core-identity/test_odtis_0314.md \
  conformance/tests/core-identity/test_liveness_high_loa.md \
  conformance/tests/core-identity/test_annex_b_liveness_mapping.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "Verification engine package checks: PASS"
