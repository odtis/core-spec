#!/usr/bin/env bash
# P3-E08: Federation agreements prep conformance smoke (ODTIS-0401..0406).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

TN_SCRIPT="../core-impl/ven-trust-network/scripts/federation-agreements-check.sh"

echo "== Federation prep checks (P3-E08) =="

if [[ -x "$TN_SCRIPT" ]]; then
  bash "$TN_SCRIPT"
else
  echo "FAIL: ${TN_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/federation/test_agreement_required_fields.md \
  conformance/tests/federation/test_explicit_activation.md \
  conformance/tests/federation/test_federation_cert_policy.md \
  conformance/tests/federation/test_federation_regulator_export.md \
  conformance/tests/federation/test_non_transitivity.md \
  conformance/tests/federation/test_transitive_route_reject.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "Federation prep package checks: PASS"
