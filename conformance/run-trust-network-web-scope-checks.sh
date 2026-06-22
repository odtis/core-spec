#!/usr/bin/env bash
# #32: ven-trust-network-web informative scope vs portal-trust ODTIS surface.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SCRIPT="../core-impl/scripts/trust-network-web-scope-check.sh"

echo "== Trust network web scope checks (#32) =="

if [[ -x "$SCRIPT" ]]; then
  bash "$SCRIPT"
else
  echo "FAIL: ${SCRIPT} not found or not executable" >&2
  exit 1
fi

[[ -f "implementation/evidence/trust-network-web/scope-2026.yaml" ]] \
  || { echo "FAIL: missing scope-2026.yaml" >&2; exit 1; }
[[ -f "implementation/component-bindings/trust-network-web.yaml" ]] \
  || { echo "FAIL: missing trust-network-web.yaml binding" >&2; exit 1; }

echo ""
echo "Trust network web scope checks: PASS"
