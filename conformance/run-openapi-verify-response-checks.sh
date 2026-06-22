#!/usr/bin/env bash
# P1-E04: Annex A VerifyResponse OpenAPI conformance (ODTIS-0316, ODTIS-0317, ODTIS-0108).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/openapi-verify-response-check.sh"

echo "== OpenAPI VerifyResponse checks =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

[[ -f "$ROOT/conformance/tests/core-identity/test_openapi_verify_response.md" ]] \
  || { echo "FAIL: missing test_openapi_verify_response.md" >&2; exit 1; }

echo ""
echo "OpenAPI VerifyResponse checks: PASS"
