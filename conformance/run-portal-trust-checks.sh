#!/usr/bin/env bash
# P2-E03: Portal API + portal-trust grant workflow conformance smoke (#11).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

TN_SCRIPT="../core-impl/ven-trust-network/scripts/portal-trust-check.sh"
GRANTS_SCRIPT="../core-impl/ven-trust-network/scripts/service-grants-check.sh"

echo "== Portal-trust checks (#11) =="

if [[ -x "$TN_SCRIPT" ]]; then
  bash "$TN_SCRIPT"
else
  echo "FAIL: ${TN_SCRIPT} not found or not executable" >&2
  exit 1
fi

if [[ -x "$GRANTS_SCRIPT" ]]; then
  echo ""
  bash "$GRANTS_SCRIPT"
else
  echo "FAIL: ${GRANTS_SCRIPT} not found or not executable" >&2
  exit 1
fi

echo ""
echo "Portal-trust checks: PASS"
