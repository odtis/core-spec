#!/usr/bin/env bash
# P4-E04: E-Webhook conformance smoke (ODTIS-0358..0360, ODTIS-0531).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/ewebhook-check.sh"

echo "== E-Webhook checks (P4-E04) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

for test_doc in \
  conformance/tests/extended/test_ewebhook_rp_registration.md \
  conformance/tests/extended/test_ewebhook_retry_backoff.md \
  conformance/tests/extended/test_ewebhook_pii_minimize.md \
  conformance/tests/extended/test_ewebhook_hmac_delivery.md \
  conformance/tests/operator/test_odtis_0531.md
do
  [[ -f "$ROOT/$test_doc" ]] || { echo "FAIL: missing $test_doc" >&2; exit 1; }
done

echo ""
echo "E-Webhook package checks: PASS"
