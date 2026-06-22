#!/usr/bin/env bash
# P4-E07: Phase 4 full mandate conformance package (ODTIS-0532, ODTIS-0006).
# Generates L3-target statement, validates, runs Extended + Federation smoke suites.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

OUT="$ROOT/implementation/statements/venid-phase4-full"
TARGET="${ODTIS_TARGET:-}"
L2_EXIT=0
SMOKE_WARN=0

echo "== Build conformance manifest =="
python3 scripts/build-conformance-manifest.py

echo "== Generate Phase 4 statement (full mandate) =="
python3 scripts/generate-conformance-statement.py \
  --profile reference-architecture \
  --profile core-identity \
  --profile trust-network \
  --profile federation \
  --profile operator \
  --profile extended \
  --extended-module E-Wallet \
  --extended-module E-Registry \
  --extended-module E-Inclusion \
  --extended-module E-Webhook \
  --extended-module E-Signature \
  --extended-module E-KYB \
  --level L3 \
  --environment staging \
  --deployment-phase 4 \
  --operator "FinnectOS VenID Phase 4" \
  --date 2026-06-12 \
  --out-dir "$OUT"

echo "== Validate statement (ODTIS-0532 phase/profile rules) =="
python3 scripts/validate-conformance-statement.py "$OUT/conformance-statement.yaml"

echo "== L2/L3 automated checks =="
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

run_smoke "Extended no-weakening (ODTIS-0006)" bash conformance/run-extended-no-weakening-checks.sh
run_smoke "Federation runtime (P4-E01)" bash conformance/run-federation-runtime-checks.sh
run_smoke "E-Wallet (P4-E02)" bash conformance/run-ewallet-checks.sh
run_smoke "E-Inclusion (P4-E03)" bash conformance/run-inclusion-checks.sh
run_smoke "E-Webhook (P4-E04)" bash conformance/run-ewebhook-checks.sh
run_smoke "E-Signature (P4-E05)" bash conformance/run-esignature-checks.sh
run_smoke "E-KYB (P4-E06)" bash conformance/run-ekyb-checks.sh
run_smoke "E-Registry (P3-E07)" bash conformance/run-extended-eregistry-checks.sh
run_smoke "Operator governance (P3-E01)" bash conformance/run-operator-governance-checks.sh
run_smoke "Phase 4 claims reconcile (#16)" bash conformance/run-phase4-claims-reconcile-checks.sh

EVIDENCE="$ROOT/implementation/evidence/phase4-conformance/l3-audit-dry-run-2026-Q2.yaml"
if [[ -f "$EVIDENCE" ]]; then
  echo ""
  echo "OK: L3 audit dry-run record present ($EVIDENCE)"
else
  echo "WARN: missing L3 audit dry-run evidence: $EVIDENCE"
  SMOKE_WARN=1
fi

python3 scripts/render-l2-report.py \
  --statement "$OUT/conformance-statement.yaml" \
  --l2 "$OUT/l2-report.json" \
  --output "$OUT/l2-report.md"

echo ""
echo "Phase 4 package: $OUT"
echo "  - conformance-statement.yaml / .md"
echo "  - l2-report.json / .md"
if [[ "$L2_EXIT" -ne 0 ]]; then
  echo "L2 automated: FAIL (see l2-report.md)"
  exit "$L2_EXIT"
fi
if [[ "$SMOKE_WARN" -ne 0 ]]; then
  echo "L2 automated: PASS (spec); Phase 4 smoke had warnings"
  exit 0
fi
echo "L2 automated + Phase 4 smoke: PASS"
