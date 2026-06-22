#!/usr/bin/env bash
# ODTIS-0204 / #10: gateway mTLS staging interop smoke.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPT="$ROOT/../core-impl/ven-trust-network/scripts/mtls-live-check.sh"

echo "== mTLS live checks (#10 / ODTIS-0204) =="

[[ -x "$SCRIPT" ]] || {
  echo "FAIL: ${SCRIPT} not found or not executable" >&2
  exit 1
}

bash "$SCRIPT"

[[ -f "$ROOT/conformance/tests/trust-network/test_gateway_mtls.md" ]] \
  || { echo "FAIL: missing test_gateway_mtls.md" >&2; exit 1; }

echo ""
echo "mTLS live checks: PASS"
