#!/usr/bin/env bash
# P1-E06: Privacy compliance conformance smoke (ODTIS-0333..0336).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/privacy-compliance-check.sh"

echo "== Privacy compliance checks (P1-E06) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/core-identity/test_odtis_0333.md \
  conformance/tests/core-identity/test_odtis_0334.md \
  conformance/tests/core-identity/test_odtis_0335.md \
  conformance/tests/core-identity/test_odtis_0336.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "Privacy package checks: PASS"
