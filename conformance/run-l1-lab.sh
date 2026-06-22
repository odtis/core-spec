#!/usr/bin/env bash
# ODTIS L1 laboratory validators (P0-E04)
# Repository integrity for VenID lab - no live sandbox target required.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "== ODTIS L1 lab =="
python3 scripts/build-conformance-manifest.py
python3 scripts/validate-manifest-coverage.py
python3 scripts/validate-registry.py
python3 scripts/validate-conformance-statement.py
PHASE1_STMT="$ROOT/implementation/statements/venid-phase1-core/conformance-statement.yaml"
if [[ -f "$PHASE1_STMT" ]]; then
  python3 scripts/validate-conformance-statement.py "$PHASE1_STMT"
fi
python3 scripts/validate-ri-map.py
python3 scripts/run-conformance.py --check-links

echo ""
echo "L1 lab: PASS"
