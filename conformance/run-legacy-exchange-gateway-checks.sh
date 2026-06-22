#!/usr/bin/env bash
# #30: Single canonical exchange-gateway (ven-trust-network).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SCRIPT="../core-impl/scripts/legacy-exchange-gateway-check.sh"

echo "== Legacy exchange-gateway checks (#30) =="

if [[ -x "$SCRIPT" ]]; then
  bash "$SCRIPT"
else
  echo "FAIL: ${SCRIPT} not found or not executable" >&2
  exit 1
fi

BINDING="implementation/component-bindings/exchange-gateway.yaml"
[[ -f "$BINDING" ]] || { echo "FAIL: missing $BINDING" >&2; exit 1; }
grep -q 'ven-trust-network' "$BINDING" \
  || { echo "FAIL: exchange-gateway binding must reference ven-trust-network" >&2; exit 1; }
grep -q 'ven-identity-core/services/exchange-gateway' "$BINDING" \
  && { echo "FAIL: binding must not reference legacy identity-core gateway" >&2; exit 1; }

echo "OK: RI component binding points to ven-trust-network"
echo ""
echo "Legacy exchange-gateway checks: PASS"
