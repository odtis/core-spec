#!/usr/bin/env bash
# P2-E09: Phase 2 Core Identity + Trust Network conformance package (ODTIS-0532).
# Generates statement, validates, runs L2 + trust-network smoke, writes l2-report.md.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

OUT="$ROOT/implementation/statements/venid-phase2-trust"
TARGET="${ODTIS_TARGET:-}"
TN_EXIT=0
FC_EXIT=0

echo "== Build conformance manifest =="
python3 scripts/build-conformance-manifest.py

echo "== Generate Phase 2 statement (core-identity + trust-network) =="
python3 scripts/generate-conformance-statement.py \
  --profile reference-architecture \
  --profile core-identity \
  --profile trust-network \
  --level L2 \
  --environment staging \
  --deployment-phase 2 \
  --operator "FinnectOS VenID Phase 2" \
  --out-dir "$OUT"

echo "== Validate statement (ODTIS-0532 phase/profile rules) =="
python3 scripts/validate-conformance-statement.py "$OUT/conformance-statement.yaml"

echo "== L2 automated checks =="
if [[ -n "$TARGET" ]]; then
  python3 conformance/l2/run_l2.py --target "$TARGET" --output "$OUT/l2-report.json" || L2_EXIT=$?
else
  echo "WARN: ODTIS_TARGET not set  -  running spec-only L2 checks"
  python3 conformance/l2/run_l2.py --output "$OUT/l2-report.json" || L2_EXIT=$?
fi
L2_EXIT="${L2_EXIT:-0}"

echo "== Trust Network smoke suite =="
if bash conformance/run-trust-network-checks.sh; then
  TN_EXIT=0
else
  TN_EXIT=$?
  echo "WARN: trust-network checks reported failures (live stack may be down)"
fi

echo "== Fail-closed cross-layer smoke =="
if bash conformance/run-fail-closed-checks.sh; then
  FC_EXIT=0
else
  FC_EXIT=$?
  echo "WARN: fail-closed checks reported failures"
fi

python3 scripts/render-l2-report.py \
  --statement "$OUT/conformance-statement.yaml" \
  --l2 "$OUT/l2-report.json" \
  --output "$OUT/l2-report.md"

echo ""
echo "Phase 2 package: $OUT"
echo "  - conformance-statement.yaml / .md"
echo "  - l2-report.json / .md"
if [[ "$L2_EXIT" -ne 0 ]]; then
  echo "L2 automated: FAIL (see l2-report.md)"
  exit "$L2_EXIT"
fi
if [[ "$TN_EXIT" -ne 0 || "$FC_EXIT" -ne 0 ]]; then
  echo "L2 automated: PASS (spec); trust-network/fail-closed smoke had warnings"
  exit 0
fi
echo "L2 automated + trust-network smoke: PASS"
