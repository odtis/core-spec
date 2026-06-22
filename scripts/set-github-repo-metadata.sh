#!/usr/bin/env bash
# Configure GitHub repository metadata for odtis/core-spec (run after gh auth login).
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "error: GitHub CLI (gh) not found. Install: https://cli.github.com/" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT/VERSION")"
REPO="$(gh repo view --json nameWithOwner -q .nameWithOwner)"

DESCRIPTION="Open Digital Trust Infrastructure Specification (ODTIS) - vendor-neutral digital identity, trust networks, and conformance (${VERSION})."
HOMEPAGE="https://odtis.org"

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

echo "Repository: $REPO"
echo "Description: $DESCRIPTION"
echo "Homepage: $HOMEPAGE"
echo "Topics: ${TOPICS[*]}"

ARGS=(--description "$DESCRIPTION" --homepage "$HOMEPAGE")
for topic in "${TOPICS[@]}"; do
  ARGS+=(--add-topic "$topic")
done

gh repo edit "${ARGS[@]}"

echo "Enabling Discussions..."
gh api -X PATCH "repos/${REPO}" -f has_discussions=true

echo "Done. Next: follow .github/GITHUB-SETUP.md for categories, branch protection, and pinned welcome post."
