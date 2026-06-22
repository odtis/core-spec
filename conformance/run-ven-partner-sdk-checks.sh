#!/usr/bin/env bash
# #31: Ven Partner SDK consolidation and autodiscovery smoke (ODTIS-0214).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

TN_SCRIPT="../core-impl/ven-trust-network/scripts/ven-partner-sdk-check.sh"

echo "== Ven Partner SDK checks (#31) =="

[[ -x "$TN_SCRIPT" ]] || {
  echo "FAIL: ${TN_SCRIPT} not found or not executable" >&2
  exit 1
}

bash "$TN_SCRIPT"

[[ -f "$ROOT/implementation/component-bindings/ven-partner-sdk.yaml" ]] \
  || { echo "FAIL: missing ven-partner-sdk.yaml binding" >&2; exit 1; }

[[ -f "$ROOT/conformance/tests/trust-network/test_odtis_0214.md" ]] \
  || { echo "FAIL: missing test_odtis_0214.md" >&2; exit 1; }

echo ""
echo "Ven Partner SDK package checks: PASS"
