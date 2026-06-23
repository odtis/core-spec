#!/usr/bin/env bash
# P5-E01: Reliance Extensions pilot conformance package (ODTIS-0532 + section 11).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

OUT="$ROOT/implementation/statements/venid-reliance-pilot"
TARGET="${ODTIS_TARGET:-}"
REL_EXIT=0
L2_EXIT=0

echo "== Build conformance manifest =="
python3 scripts/build-conformance-manifest.py

echo "== Validate existing pilot statement =="
python3 scripts/validate-conformance-statement.py "$OUT/conformance-statement.yaml"

echo "== L2 automated checks (incl. reliance schema) =="
if [[ -n "$TARGET" ]]; then
  python3 conformance/l2/run_l2.py --target "$TARGET" --output "$OUT/l2-report.json" || L2_EXIT=$?
else
  echo "WARN: ODTIS_TARGET not set - running spec-only L2 checks"
  python3 conformance/l2/run_l2.py --output "$OUT/l2-report.json" || L2_EXIT=$?
fi
L2_EXIT="${L2_EXIT:-0}"

echo "== Reliance Extensions smoke suite =="
if bash conformance/run-reliance-checks.sh; then
  REL_EXIT=0
else
  REL_EXIT=$?
  echo "WARN: reliance smoke reported failures"
fi

python3 scripts/render-l2-report.py \
  --statement "$OUT/conformance-statement.yaml" \
  --l2 "$OUT/l2-report.json" \
  --output "$OUT/l2-report.md"

echo ""
echo "Reliance pilot package: $OUT"
echo "  - conformance-statement.yaml / .md"
echo "  - l2-report.json / .md"
if [[ "$L2_EXIT" -ne 0 ]]; then
  echo "L2 automated: FAIL (see l2-report.md)"
  exit "$L2_EXIT"
fi
if [[ "$REL_EXIT" -ne 0 ]]; then
  echo "L2 automated: PASS (spec); reliance smoke had warnings"
  exit 0
fi
echo "L2 automated + reliance smoke: PASS"
