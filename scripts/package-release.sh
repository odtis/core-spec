#!/usr/bin/env bash
# Package ODTIS release tarball for Zenodo or offline distribution.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT/VERSION")"
STAMP="$(date -u +%Y%m%d)"
OUT_DIR="$ROOT/publication/zenodo/snapshots"
ARCHIVE="$OUT_DIR/odtis-${VERSION}-${STAMP}.tar.gz"
CHECKSUMS="$OUT_DIR/SHA256SUMS"

cd "$ROOT"
mkdir -p "$OUT_DIR"

tar -czf "$ARCHIVE" \
  --exclude='.venv-site' \
  --exclude='build' \
  --exclude='conformance/reports/*.json' \
  --exclude='.DS_Store' \
  --exclude='.git' \
  .

(
  cd "$OUT_DIR"
  shasum -a 256 "$(basename "$ARCHIVE")" > SHA256SUMS
)

echo "Archive: $ARCHIVE"
echo "Checksums: $CHECKSUMS"
cat "$CHECKSUMS"
