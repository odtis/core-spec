#!/usr/bin/env bash
# #29: gov-api Annex A S7  -  defer decision and non-orphan OpenAPI contract.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SCRIPT="../core-impl/scripts/gov-api-decision-check.sh"

echo "== gov-api decision checks (#29) =="

if [[ -x "$SCRIPT" ]]; then
  bash "$SCRIPT"
else
  echo "FAIL: ${SCRIPT} not found or not executable" >&2
  exit 1
fi

BINDING="implementation/component-bindings/gov-api.yaml"
[[ -f "$BINDING" ]] || { echo "FAIL: missing $BINDING" >&2; exit 1; }
grep -q 'status: deferred' "$BINDING" \
  || { echo "FAIL: gov-api binding must be deferred" >&2; exit 1; }

GAPS="implementation/gaps/gaps.yaml"
grep -q 'GAP-IC-GOV-API' "$GAPS" \
  || { echo "FAIL: gaps.yaml missing GAP-IC-GOV-API" >&2; exit 1; }

python3 scripts/validate-openapi.py

echo ""
echo "gov-api decision checks: PASS"
