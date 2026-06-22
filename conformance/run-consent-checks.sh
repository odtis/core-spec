#!/usr/bin/env bash
# P1-E06: Consent and privacy conformance smoke (ODTIS-0328..0332, ODTIS-0527).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/consent-service-check.sh"

echo "== Consent service checks (P1-E06) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/core-identity/test_explicit_consent_first_release.md \
  conformance/tests/core-identity/test_odtis_0329.md \
  conformance/tests/core-identity/test_consent_revocation.md \
  conformance/tests/core-identity/test_odtis_0331.md \
  conformance/tests/core-identity/test_odtis_0332.md \
  conformance/tests/core-identity/test_consent_audit_events.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "Consent package checks: PASS"
