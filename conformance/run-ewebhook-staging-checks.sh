#!/usr/bin/env bash
# P4-E04 / #14: E-Webhook staging overlay + live conformance smoke.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "== E-Webhook staging checks (#14) =="
bash ./conformance/run-ewebhook-checks.sh

[[ -f "$ROOT/implementation/evidence/ewebhook/lab-notes.md" ]] \
  || { echo "FAIL: missing ewebhook lab-notes.md" >&2; exit 1; }

echo ""
echo "E-Webhook staging checks: PASS"
