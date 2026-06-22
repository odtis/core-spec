#!/usr/bin/env bash
# P1-E08: API gateway transport conformance smoke (ODTIS-0325..0327, ODTIS-0521..0523).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/gateway-transport-check.sh"

echo "== Gateway transport checks (P1-E08) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/core-identity/test_odtis_0325.md \
  conformance/tests/core-identity/test_odtis_0326.md \
  conformance/tests/core-identity/test_odtis_0327.md \
  conformance/tests/core-identity/test_owasp_baseline.md \
  conformance/tests/operator/test_odtis_0522.md \
  conformance/tests/core-identity/test_liveness_high_loa.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "Gateway transport package checks: PASS"
