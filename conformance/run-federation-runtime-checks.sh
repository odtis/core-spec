#!/usr/bin/env bash
# P4-E01: Federation runtime conformance smoke (ODTIS-0407, ODTIS-0408).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

TN_SCRIPT="../core-impl/ven-trust-network/scripts/federation-runtime-check.sh"
OVERLAY_SCRIPT="../core-impl/scripts/federation-overlay-check.sh"

echo "== Federation runtime checks (P4-E01 / #25) =="

if [[ -x "$OVERLAY_SCRIPT" ]]; then
  bash "$OVERLAY_SCRIPT"
else
  echo "FAIL: ${OVERLAY_SCRIPT} not found or not executable" >&2
  exit 1
fi

if [[ -x "$TN_SCRIPT" ]]; then
  bash "$TN_SCRIPT"
else
  echo "FAIL: ${TN_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/federation/test_agreement_suspension_routing.md \
  conformance/tests/federation/test_federated_audit_instance_ids.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "Federation runtime package checks: PASS"
