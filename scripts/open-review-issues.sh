#!/usr/bin/env bash
# Create GitHub issues for ODTIS review cycle 1 (requires gh auth + remote).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REVIEW="$ROOT/governance/review"
RFC="$ROOT/governance/rfc/2026-06-12-federation-interoperability.md"
DRY=false

for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY=true ;;
    -h|--help)
      echo "Usage: $0 [--dry-run]"
      exit 0
      ;;
  esac
done

if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI not found. Copy issue bodies from governance/review/ manually." >&2
  exit 1
fi

create_issue() {
  local title="$1"
  local body_file="$2"
  local label="$3"
  if $DRY; then
    echo "[dry-run] gh issue create --title \"$title\" --label \"$label\" --body-file $body_file"
  else
    gh issue create --title "$title" --label "$label" --body-file "$body_file"
  fi
}

create_issue "[ODTIS clarify] ODTIS-0331 test linkage (FB-001)" \
  "$REVIEW/clarify-001-5.1.4-test-linkage.md" "odtis,clarification"

create_issue "[ODTIS RFC] Federation interoperability (FB-002)" \
  "$RFC" "odtis,rfc"

create_issue "[ODTIS clarify] HA metrics boundary ODTIS-10 vs Book 2 ch.14 (FB-003)" \
  "$REVIEW/clarify-002-ha-informative-boundary.md" "odtis,clarification"

create_issue "[ODTIS clarify] Autodiscovery SHOULD scope ODTIS-4.6.1 (FB-004)" \
  "$REVIEW/clarify-003-autodiscovery-should.md" "odtis,clarification"

create_issue "[ODTIS sandbox] L2 structural baseline (FB-005)" \
  "$REVIEW/sandbox-001-l2-report-template.md" "odtis,conformance,sandbox"

echo "Done. Track decisions in governance/REVIEW-LOG.yaml"
