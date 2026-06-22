#!/usr/bin/env bash
# P1-E02: OIDC IdP conformance smoke (ODTIS-0301..0308).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/oidc-conformance-check.sh"

echo "== OIDC IdP checks (P1-E02) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/core-identity/test_odtis_0301.md \
  conformance/tests/core-identity/test_pkce_required.md \
  conformance/tests/core-identity/test_odtis_0303.md \
  conformance/tests/core-identity/test_odtis_0304.md \
  conformance/tests/core-identity/test_redirect_uri_validation.md \
  conformance/tests/core-identity/test_consent_gated_claims.md \
  conformance/tests/core-identity/test_rp_initiated_logout.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "OIDC IdP package checks: PASS"
