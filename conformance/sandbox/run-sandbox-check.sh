#!/usr/bin/env bash
# Run L2 checks against a sandbox IdP (--target) and write a JSON report.
# L1-only lab (no live target): ./conformance/sandbox/run-sandbox-check.sh --l1-only
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

if [[ "${1:-}" == "--l1-only" ]]; then
  exec ./conformance/run-l1-lab.sh
fi

TARGET="${ODTIS_TARGET:-${1:-}}"
if [[ -z "$TARGET" ]]; then
  echo "Usage: ODTIS_TARGET=https://sandbox.example/realms/venid $0" >&2
  echo "   or: $0 https://sandbox.example/realms/venid" >&2
  echo "   or: $0 --l1-only   (repository lab validators only)" >&2
  exit 1
fi

STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
REPORT_DIR="$ROOT/conformance/reports"
REPORT="$REPORT_DIR/l2-sandbox-${STAMP}.json"
mkdir -p "$REPORT_DIR"

echo "L1 (repository lab)..."
./conformance/run-l1-lab.sh

echo "L2 (target=$TARGET)..."
python3 conformance/l2/run_l2.py --target "$TARGET" --output "$REPORT"

echo ""
echo "Report: $REPORT"
echo "Attach to GitHub issue: ODTIS sandbox conformance report"
