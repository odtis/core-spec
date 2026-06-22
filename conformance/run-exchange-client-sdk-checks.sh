#!/usr/bin/env bash
# #19: Exchange client SDK documentation and unit smoke (ODTIS-0223).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

TN_SCRIPT="../core-impl/ven-trust-network/scripts/exchange-client-sdk-check.sh"

echo "== Exchange client SDK checks (#19) =="

[[ -x "$TN_SCRIPT" ]] || {
  echo "FAIL: ${TN_SCRIPT} not found or not executable" >&2
  exit 1
}

bash "$TN_SCRIPT"

[[ -f "$ROOT/implementation/component-bindings/exchange-client-sdk.yaml" ]] \
  || { echo "FAIL: missing exchange-client-sdk.yaml binding" >&2; exit 1; }

[[ -f "$ROOT/conformance/tests/trust-network/test_sender_multi_peer_routing.md" ]] \
  || { echo "FAIL: missing test_sender_multi_peer_routing.md" >&2; exit 1; }

echo ""
echo "Exchange client SDK package checks: PASS"
