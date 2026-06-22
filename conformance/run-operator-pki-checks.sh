#!/usr/bin/env bash
# P3-E02: Operator PKI stewardship conformance smoke (ODTIS-0507..0510).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

TN_SCRIPT="../core-impl/ven-trust-network/scripts/operator-pki-stewardship-check.sh"

echo "== Operator PKI stewardship checks (P3-E02) =="

if [[ -x "$TN_SCRIPT" ]]; then
  bash "$TN_SCRIPT"
else
  echo "FAIL: ${TN_SCRIPT} not found or not executable" >&2
  exit 1
fi

REGISTRY="../core-impl/ven-trust-network/docs/pki/cp-cps-registry.yaml"
if [[ -f "$REGISTRY" ]]; then
  grep -q 'conformance_statement_refs' "$REGISTRY" \
    || { echo "FAIL: cp-cps-registry missing conformance refs" >&2; exit 1; }
  echo "OK: CP/CPS referenced for conformance (ODTIS-0507)"
fi

echo ""
echo "Operator PKI stewardship package checks: PASS"
