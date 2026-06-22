#!/usr/bin/env bash
# P3-E06: Audit platform and regulator export conformance smoke (ODTIS-0530).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

TN_SCRIPT="../core-impl/ven-trust-network/scripts/audit-platform-check.sh"

echo "== Operator audit platform checks (P3-E06) =="

if [[ -x "$TN_SCRIPT" ]]; then
  bash "$TN_SCRIPT"
else
  echo "FAIL: ${TN_SCRIPT} not found or not executable" >&2
  exit 1
fi

TEST_DOC="$ROOT/conformance/tests/operator/test_audit_export_pii_minimized.md"
[[ -f "$TEST_DOC" ]] || { echo "FAIL: missing $TEST_DOC" >&2; exit 1; }
grep -q 'ODTIS-0530' "$TEST_DOC" || { echo "FAIL: test doc missing ODTIS-0530" >&2; exit 1; }

echo ""
echo "Operator audit platform package checks: PASS"
