#!/usr/bin/env bash
# ODTIS-0532 / #17: L3 external auditor evidence pack readiness.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SCRIPT="../core-impl/scripts/l3-auditor-evidence-check.sh"
PACK="implementation/evidence/phase4-conformance/l3-auditor-evidence-pack-2026.yaml"
ENGAGEMENT="implementation/evidence/phase4-conformance/l3-auditor-engagement-2026.yaml"

echo "== L3 auditor evidence checks (#17) =="

[[ -f "$PACK" ]] || { echo "FAIL: missing $PACK" >&2; exit 1; }
[[ -f "$ENGAGEMENT" ]] || { echo "FAIL: missing $ENGAGEMENT" >&2; exit 1; }

if [[ -x "$SCRIPT" ]]; then
  bash "$SCRIPT"
else
  echo "FAIL: ${SCRIPT} not found or not executable" >&2
  exit 1
fi

python3 scripts/validate-conformance-statement.py \
  implementation/statements/venid-phase4-full/conformance-statement.yaml

echo ""
echo "L3 auditor evidence checks: PASS"
