#!/usr/bin/env bash
# P3-E03: Operator SLA, partners, metrics conformance smoke (ODTIS-0511..0513).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/operator-sla-metrics-check.sh"
TN_SCRIPT="../core-impl/ven-trust-network/scripts/operator-sla-metrics-check.sh"

echo "== Operator SLA and metrics checks (P3-E03) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found" >&2
  exit 1
fi

if [[ -x "$TN_SCRIPT" ]]; then
  echo ""
  bash "$TN_SCRIPT"
else
  echo "FAIL: ${TN_SCRIPT} not found" >&2
  exit 1
fi

echo ""
echo "Operator SLA/metrics package checks: PASS"
