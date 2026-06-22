#!/usr/bin/env bash
# ODTIS-0506 / #16: Phase 4 target packaging vs published Phase 2 scope reconciliation.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SCRIPT="../core-impl/scripts/phase4-claims-reconcile-check.sh"

echo "== Phase 4 claims reconcile checks (#16) =="

if [[ -x "$SCRIPT" ]]; then
  bash "$SCRIPT"
else
  echo "FAIL: ${SCRIPT} not found or not executable" >&2
  exit 1
fi

PHASE4="$ROOT/implementation/statements/venid-phase4-full/conformance-statement.yaml"
if [[ -f "$PHASE4" ]]; then
  python3 scripts/validate-conformance-statement.py "$PHASE4"
  echo "OK: venid-phase4-full conformance statement validates"
else
  echo "FAIL: missing $PHASE4" >&2
  exit 1
fi

echo ""
echo "Phase 4 claims reconcile checks: PASS"
