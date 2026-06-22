#!/usr/bin/env bash
# Reference Architecture profile smoke (ODTIS-0001..0010).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "== Reference Architecture: Extended no-weakening (ODTIS-0006) =="
bash "$ROOT/conformance/run-extended-no-weakening-checks.sh"

echo ""
echo "== Reference Architecture: claims, statements, and profile chain =="
python3 "$ROOT/scripts/validate-reference-architecture-smoke.py"

echo ""
echo "Reference Architecture checks: PASS"
