#!/usr/bin/env bash
# P4-E06: E-KYB conformance smoke (ODTIS-0364..0365).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/kyb-service-check.sh"

echo "== E-KYB checks (P4-E06) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/extended/test_ekyb_entity_separate.md \
  conformance/tests/extended/test_ekyb_representative_link.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "E-KYB package checks: PASS"
