#!/usr/bin/env bash
# P3-E05: Security and secrets platform conformance smoke (ODTIS-0518..0520, 0525).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

INFRA_SCRIPT="../core-impl/ven-infra-core/scripts/security-platform-check.sh"

echo "== Operator security platform checks (P3-E05) =="

if [[ -x "$INFRA_SCRIPT" ]]; then
  bash "$INFRA_SCRIPT"
else
  echo "FAIL: ${INFRA_SCRIPT} not found or not executable" >&2
  exit 1
fi

echo ""
echo "Operator security platform package checks: PASS"
