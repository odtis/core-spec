#!/usr/bin/env bash
# P1-E05: RP client lifecycle conformance smoke (ODTIS-0319..0321, ODTIS-0337..0339).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/rp-client-lifecycle-check.sh"

echo "== RP client lifecycle checks (P1-E05) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/core-identity/test_odtis_0319.md \
  conformance/tests/core-identity/test_odtis_0320.md \
  conformance/tests/core-identity/test_odtis_0321.md \
  conformance/tests/core-identity/test_odtis_0337.md \
  conformance/tests/core-identity/test_odtis_0338.md \
  conformance/tests/core-identity/test_rp_suspension.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "RP client lifecycle package checks: PASS"
