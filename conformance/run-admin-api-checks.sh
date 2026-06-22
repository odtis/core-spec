#!/usr/bin/env bash
# P3-E01: Admin API operator conformance smoke (#9).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

IC_SCRIPT="../core-impl/ven-identity-core/scripts/admin-api-check.sh"

echo "== Admin API checks (#9) =="

if [[ -x "$IC_SCRIPT" ]]; then
  bash "$IC_SCRIPT"
else
  echo "FAIL: ${IC_SCRIPT} not found or not executable" >&2
  exit 1
fi

echo ""
echo "Admin API checks: PASS"
