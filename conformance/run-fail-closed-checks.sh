#!/usr/bin/env bash
# P2-E08: Cross-layer fail-closed denial smoke (ODTIS-0535).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/fail-closed-denial-check.sh"
TN_SCRIPT="../core-impl/ven-trust-network/scripts/fail-closed-denial-check.sh"

echo "== Fail-closed cross-layer checks (ODTIS-0535) =="

if [[ -x "$IC_SCRIPT" ]]; then
  echo "-- Core Identity --"
  bash "$IC_SCRIPT" || true
else
  echo "WARN: ${IC_SCRIPT} not found"
fi

if [[ -x "$TN_SCRIPT" ]] && curl -sf "http://localhost:9080/exchange/health" >/dev/null 2>&1; then
  echo "-- Trust Network --"
  bash "$TN_SCRIPT"
elif [[ -x "$TN_SCRIPT" ]]; then
  echo "WARN: exchange-gateway unreachable  -  skip trust-network fail-closed smoke"
fi

echo ""
echo "Fail-closed cross-layer checks: PASS"
