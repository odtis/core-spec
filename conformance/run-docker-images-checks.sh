#!/usr/bin/env bash
# Phase 2: CI Docker image registry parity smoke (#35).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SCRIPT="../core-impl/scripts/ci-docker-images-check.sh"

echo "== CI Docker images checks (#35) =="

if [[ -x "$SCRIPT" ]]; then
  bash "$SCRIPT"
else
  echo "FAIL: ${SCRIPT} not found or not executable" >&2
  exit 1
fi

echo ""
echo "CI Docker images checks: PASS"
