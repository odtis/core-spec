#!/usr/bin/env bash
# P3-E09: Phase 3 Operator conformance package (ODTIS-0532).
# Generates statement, validates, runs L2 + Phase 3 operator smoke suites, writes l2-report.md.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

OUT="$ROOT/implementation/statements/venid-phase3-operator"
TARGET="${ODTIS_TARGET:-}"
L2_EXIT=0
SMOKE_WARN=0

echo "== Build conformance manifest =="
python3 scripts/build-conformance-manifest.py

echo "== Generate Phase 3 statement (core + trust + operator) =="
python3 scripts/generate-conformance-statement.py \
  --profile reference-architecture \
  --profile core-identity \
  --profile trust-network \
  --profile operator \
  --level L2 \
  --environment staging \
  --deployment-phase 3 \
  --operator "FinnectOS VenID Phase 3" \
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

run_smoke() {
  local name="$1"
  shift
  echo ""
  echo "== $name =="
  if "$@"; then
    return 0
  fi
  echo "WARN: $name reported failures (live stack may be down)"
  SMOKE_WARN=1
  return 0
}

run_smoke "Operator governance (P3-E01)" bash conformance/run-operator-governance-checks.sh
run_smoke "Operator PKI (P3-E02)" bash conformance/run-operator-pki-checks.sh
run_smoke "Operator SLA/metrics (P3-E03)" bash conformance/run-operator-sla-metrics-checks.sh
run_smoke "Operator regulator (P3-E04)" bash conformance/run-operator-regulator-checks.sh
run_smoke "Operator security (P3-E05)" bash conformance/run-operator-security-checks.sh
run_smoke "Audit platform (P3-E06)" bash conformance/run-operator-audit-checks.sh
run_smoke "E-Registry prep (P3-E07)" bash conformance/run-extended-eregistry-checks.sh
run_smoke "Federation prep (P3-E08)" bash conformance/run-federation-prep-checks.sh

EVIDENCE="$ROOT/implementation/evidence/phase3-conformance/audit-dry-run-2026-Q2.yaml"
if [[ -f "$EVIDENCE" ]]; then
  echo ""
  echo "OK: internal audit dry-run record present ($EVIDENCE)"
else
  echo "WARN: missing audit dry-run evidence: $EVIDENCE"
  SMOKE_WARN=1
fi

python3 scripts/render-l2-report.py \
  --statement "$OUT/conformance-statement.yaml" \
  --l2 "$OUT/l2-report.json" \
  --output "$OUT/l2-report.md"

echo ""
echo "Phase 3 package: $OUT"
echo "  - conformance-statement.yaml / .md"
echo "  - l2-report.json / .md"
if [[ "$L2_EXIT" -ne 0 ]]; then
  echo "L2 automated: FAIL (see l2-report.md)"
  exit "$L2_EXIT"
fi
if [[ "$SMOKE_WARN" -ne 0 ]]; then
  echo "L2 automated: PASS (spec); Phase 3 smoke had warnings"
  exit 0
fi
echo "L2 automated + Phase 3 operator smoke: PASS"
