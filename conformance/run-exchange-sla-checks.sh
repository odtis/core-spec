#!/usr/bin/env bash
# P2-E07: Exchange audit, SLA, and zero-trust conformance smoke (#23).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

AUDIT_SCRIPT="../core-impl/ven-trust-network/scripts/exchange-audit-check.sh"

echo "== Exchange SLA and zero-trust checks (#23) =="

if [[ -x "$AUDIT_SCRIPT" ]]; then
  bash "$AUDIT_SCRIPT"
else
  echo "FAIL: ${AUDIT_SCRIPT} not found or not executable" >&2
  exit 1
fi

echo ""
echo "Exchange SLA checks: PASS"
