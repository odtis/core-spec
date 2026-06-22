#!/usr/bin/env bash
# Partner node kit distribution smoke (#37 / ODTIS-0512).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

KIT_SCRIPT="../core-impl/ven-trust-network/scripts/partner-node-kit-check.sh"

echo "== Partner node kit checks (#37 / ODTIS-0512) =="

[[ -x "$KIT_SCRIPT" ]] || {
  echo "FAIL: ${KIT_SCRIPT} not found or not executable" >&2
  exit 1
}

bash "$KIT_SCRIPT"

[[ -f "$ROOT/implementation/component-bindings/partner-node-kit.yaml" ]] \
  || { echo "FAIL: missing partner-node-kit.yaml binding" >&2; exit 1; }

[[ -f "$ROOT/conformance/tests/operator/test_odtis_0512.md" ]] \
  || { echo "FAIL: missing test_odtis_0512.md" >&2; exit 1; }

echo ""
echo "Partner node kit package checks: PASS"
