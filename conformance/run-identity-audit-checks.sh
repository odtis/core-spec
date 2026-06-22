#!/usr/bin/env bash
# P1-E09: Identity audit events conformance smoke (ODTIS-0526, ODTIS-0527, ODTIS-0529).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/identity-audit-check.sh"

echo "== Identity audit checks (P1-E09) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/core-identity/test_identity_audit_events.md \
  conformance/tests/core-identity/test_consent_audit_events.md \
  conformance/tests/operator/test_event_envelope.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "Identity audit package checks: PASS"
