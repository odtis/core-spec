#!/usr/bin/env bash
# P4-E02: E-Wallet (OID4VP) conformance smoke (ODTIS-0340..0343, ODTIS-0524).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/wallet-service-check.sh"

echo "== E-Wallet checks (P4-E02) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/core-identity/test_odtis_0340.md \
  conformance/tests/core-identity/test_odtis_0341.md \
  conformance/tests/core-identity/test_odtis_0342.md \
  conformance/tests/core-identity/test_odtis_0343.md \
  conformance/tests/operator/test_odtis_0524.md \
  conformance/tests/extended/test_ewallet_holder_vp.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "E-Wallet package checks: PASS"
