#!/usr/bin/env bash
# P3-E07 / #8: E-Registry staging overlay + extended conformance smoke.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/eregistry-adapter-check.sh"

echo "== E-Registry staging checks (#8) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/extended/test_eregistry_declaration_required.md \
  conformance/tests/extended/test_eregistry_no_civil_authority.md \
  conformance/tests/extended/test_eregistry_phase3_activation.md \
  conformance/tests/extended/test_eregistry_national_loa.md \
  conformance/tests/extended/test_national_loa_after_adapter.md \
  conformance/tests/extended/test_registry_hash_no_biometric_store.md \
  conformance/tests/extended/test_registry_verification_audit.md \
  conformance/tests/core-identity/test_odtis_0104.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "E-Registry staging checks: PASS"
