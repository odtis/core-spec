#!/usr/bin/env bash
# Set GitHub repository description and topics for odtis/core-spec (run once after making public).
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "error: GitHub CLI (gh) not found. Install: https://cli.github.com/" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT/VERSION")"

DESCRIPTION="Open Digital Trust Infrastructure Specification (ODTIS) - vendor-neutral digital identity, trust networks, and conformance (${VERSION})."

TOPICS=(
  odtis
  open-specification
  digital-identity
  trust-network
  digital-trust
  conformance
  oidc
  openapi
  identity-management
  zero-trust
)

echo "Repository: $(gh repo view --json nameWithOwner -q .nameWithOwner)"
echo "Description: $DESCRIPTION"
echo "Topics: ${TOPICS[*]}"

ARGS=(--description "$DESCRIPTION")
for topic in "${TOPICS[@]}"; do
  ARGS+=(--add-topic "$topic")
done

gh repo edit "${ARGS[@]}"

echo "Done."
