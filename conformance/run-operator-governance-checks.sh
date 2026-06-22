#!/usr/bin/env bash
# P3-E01: Operator governance conformance smoke (ODTIS-0501..0506).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/operator-governance-check.sh"

echo "== Operator governance checks (P3-E01) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

MATURITY="implementation/statements/venid-operator-maturity/operator-maturity.yaml"
if [[ -f "$MATURITY" ]]; then
  grep -q "phase4_claims_prohibited" "$MATURITY" \
    || { echo "FAIL: $MATURITY missing phase4_claims_prohibited" >&2; exit 1; }
  echo "OK: operator maturity statement (ODTIS-0505/0506)"
else
  echo "FAIL: $MATURITY not found" >&2
  exit 1
fi

echo ""
echo "Operator governance package checks: PASS"
