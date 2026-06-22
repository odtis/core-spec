#!/usr/bin/env bash
# P1-E10: Phase 1 Core Identity conformance package (ODTIS-0533).
# Generates statement, validates, runs L2 (live if ODTIS_TARGET set), writes l2-report.md.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

OUT="$ROOT/implementation/statements/venid-phase1-core"
TARGET="${ODTIS_TARGET:-}"

echo "== Build conformance manifest =="
python3 scripts/build-conformance-manifest.py

echo "== Generate Phase 1 statement (core-identity, no Extended) =="
python3 scripts/generate-conformance-statement.py \
  --profile reference-architecture \
  --profile core-identity \
  --level L2 \
  --environment sandbox \
  --deployment-phase 1 \
  --operator "FinnectOS VenID Phase 1" \
  --out-dir "$OUT"

echo "== Validate statement (ODTIS-0533 phase/extended rules) =="
python3 scripts/validate-conformance-statement.py "$OUT/conformance-statement.yaml"

echo "== L2 automated checks =="
if [[ -n "$TARGET" ]]; then
  python3 conformance/l2/run_l2.py --target "$TARGET" --output "$OUT/l2-report.json" || L2_EXIT=$?
else
  echo "WARN: ODTIS_TARGET not set  -  running spec-only L2 checks"
  python3 conformance/l2/run_l2.py --output "$OUT/l2-report.json" || L2_EXIT=$?
fi
L2_EXIT="${L2_EXIT:-0}"

python3 scripts/render-l2-report.py \
  --statement "$OUT/conformance-statement.yaml" \
  --l2 "$OUT/l2-report.json" \
  --output "$OUT/l2-report.md"

echo ""
echo "Phase 1 package: $OUT"
echo "  - conformance-statement.yaml / .md"
echo "  - l2-report.json / .md"
if [[ "$L2_EXIT" -ne 0 ]]; then
  echo "L2 automated: FAIL (see l2-report.md; open gaps may require live stack)"
  exit "$L2_EXIT"
fi
echo "L2 automated: PASS"
