#!/usr/bin/env bash
# P1-E03: Identity core conformance smoke (ODTIS-0306, 0309, 0310..0314).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/identity-core-check.sh"

echo "== Identity core checks (P1-E03) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/core-identity/test_account_recovery.md \
  conformance/tests/core-identity/test_odtis_0306.md \
  conformance/tests/core-identity/test_odtis_0310.md \
  conformance/tests/core-identity/test_odtis_0311.md \
  conformance/tests/core-identity/test_odtis_0312.md \
  conformance/tests/core-identity/test_odtis_0313.md \
  conformance/tests/core-identity/test_odtis_0314.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "Identity core package checks: PASS"
