#!/usr/bin/env bash
# Local pre-publish audit (run before making core-spec public). Not used in CI.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
FAIL=0

fail() { echo "FAIL: $*" >&2; FAIL=1; }
ok() { echo "OK: $*"; }

# Tracked secrets
if git ls-files --error-unmatch scripts/odtis-deploy.env &>/dev/null; then
  fail "scripts/odtis-deploy.env is tracked by git"
else
  ok "odtis-deploy.env not tracked"
fi
if git ls-files '*.pem' '*.key' 2>/dev/null | grep -q .; then
  fail "PEM/key files tracked: $(git ls-files '*.pem' '*.key')"
else
  ok "no PEM/key files tracked"
fi

# Sensitive strings in current tree (tracked files only)
PATTERNS=(
  '34\.227\.196\.69'
  'MvpKeyPair\.pem'
  '/Users/manuelmerida/'
  'BEGIN RSA PRIVATE KEY'
  'BEGIN OPENSSH PRIVATE KEY'
)
for pat in "${PATTERNS[@]}"; do
  if git grep -E "$pat" HEAD -- ':!scripts/audit-before-publish.sh' 2>/dev/null | grep -q .; then
    fail "pattern $pat found in HEAD"
    git grep -E "$pat" HEAD -- ':!scripts/audit-before-publish.sh' 2>/dev/null | head -3 >&2
  else
    ok "no $pat in HEAD"
  fi
done

# Private monorepo URLs (informational)
if git grep -E 'github\.com/finnectos/venezuela' HEAD 2>/dev/null | grep -q .; then
  fail "private monorepo URL still in tree"
else
  ok "no finnectos/venezuela links"
fi

# Open-source files
for f in LICENSE SECURITY.md CONTRIBUTING.md CODE_OF_CONDUCT.md; do
  if [[ -f "$f" ]]; then ok "$f present"; else fail "missing $f"; fi
done

# Local deploy config (optional warning)
if [[ ! -f scripts/odtis-deploy.env ]]; then
  echo "NOTE: scripts/odtis-deploy.env not on this machine (fine for contributors)"
fi

if [[ "$FAIL" -ne 0 ]]; then
  echo >&2
  echo "Audit failed. Fix issues before publishing." >&2
  exit 1
fi
echo
echo "Audit passed. Safe to publish core-spec as open source (review git history separately)."
