#!/usr/bin/env bash
# ODTIS conformance runner wrapper
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
exec python3 scripts/run-conformance.py --rebuild "$@"
