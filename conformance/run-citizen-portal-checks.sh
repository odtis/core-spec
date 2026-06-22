#!/usr/bin/env bash
# P1-E07: Citizen portal conformance smoke (ODTIS-0322..0324, portal UI 0332).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/citizen-portal-check.sh"

echo "== Citizen portal checks (P1-E07) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/core-identity/test_odtis_0322.md \
  conformance/tests/core-identity/test_odtis_0323.md \
  conformance/tests/core-identity/test_odtis_0324.md \
  conformance/tests/core-identity/test_odtis_0332.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "Citizen portal package checks: PASS"
