#!/usr/bin/env bash
# #26: E2E fail-closed denial + audit correlation cross-link (ODTIS-0535, ODTIS-0528).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SCRIPT="../core-impl/scripts/fail-closed-audit-e2e-check.sh"

echo "== Fail-closed audit E2E checks (#26) =="

[[ -x "$SCRIPT" ]] || {
  echo "FAIL: ${SCRIPT} not found or not executable" >&2
  exit 1
}

bash "$SCRIPT"

for test_doc in \
  conformance/tests/operator/test_fail_closed_denial_paths.md \
  conformance/tests/trust-network/test_exchange_audit_events.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "Fail-closed audit E2E package checks: PASS"
