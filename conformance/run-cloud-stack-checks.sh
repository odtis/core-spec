#!/usr/bin/env bash
# Cloud stack + staging overlay smoke (#28).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

CS_SCRIPT="../core-impl/ven-cloud-stack/scripts/cloud-stack-check.sh"
INFRA_SCRIPT="../core-impl/ven-infra-core/scripts/security-platform-check.sh"

echo "== Cloud stack checks (#28) =="
if [[ -x "$CS_SCRIPT" ]]; then
  bash "$CS_SCRIPT"
else
  echo "FAIL: ${CS_SCRIPT} not found" >&2
  exit 1
fi

echo ""
echo "== Infra staging matrix (#7) =="
if [[ -x "$INFRA_SCRIPT" ]]; then
  bash "$INFRA_SCRIPT"
else
  echo "FAIL: ${INFRA_SCRIPT} not found" >&2
  exit 1
fi

echo ""
echo "Cloud stack checks: PASS"
