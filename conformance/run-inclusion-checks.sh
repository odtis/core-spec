#!/usr/bin/env bash
# P4-E03: E-Inclusion conformance smoke (ODTIS-0354..0357).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/inclusion-service-check.sh"

echo "== E-Inclusion checks (P4-E03) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/extended/test_inclusion_assisted_consent.md \
  conformance/tests/extended/test_inclusion_representative_verify.md \
  conformance/tests/extended/test_inclusion_no_loa_bypass.md \
  conformance/tests/extended/test_inclusion_accessibility_offline.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "E-Inclusion package checks: PASS"
