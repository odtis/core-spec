#!/usr/bin/env bash
# P4-E05: E-Signature conformance smoke (ODTIS-0361..0363).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/esignature-check.sh"

echo "== E-Signature checks (P4-E05) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/extended/test_esignature_loa_binding.md \
  conformance/tests/extended/test_esignature_pki_keys.md \
  conformance/tests/extended/test_esignature_audit_events.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "E-Signature package checks: PASS"
