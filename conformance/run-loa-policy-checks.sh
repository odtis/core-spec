#!/usr/bin/env bash
# P1-E01: LoA policy conformance smoke (ODTIS-0101..0108, ODTIS-0306).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/loa-policy-check.sh"

echo "== LoA policy checks (P1-E01) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/core-identity/test_odtis_0101.md \
  conformance/tests/core-identity/test_loa_claim.md \
  conformance/tests/core-identity/test_high_biometric_gate.md \
  conformance/tests/core-identity/test_annex_c_nist_loa_mapping.md \
  conformance/tests/core-identity/test_odtis_0105.md \
  conformance/tests/core-identity/test_odtis_0107.md \
  conformance/tests/core-identity/test_verification_loa_on_denial.md \
  conformance/tests/core-identity/test_odtis_0306.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "LoA policy package checks: PASS"
