#!/usr/bin/env bash
# Build ODTIS MkDocs site and sync to EC2 (see DEPLOY-EC2-ODTIS-ORG.md)
#
# One-time setup:
#   cp scripts/odtis-deploy.env.example scripts/odtis-deploy.env
#   # edit scripts/odtis-deploy.env with your host and SSH key
#
# Deploy:
#   ./scripts/deploy-ec2.sh
#
# Options:
#   --skip-build   rsync only (reuse existing build/odtis-spec-site/)
#   --skip-fix     skip remote chmod/SELinux fix after rsync
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$(cd "$ROOT/.." && pwd)/build/odtis-spec-site"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

SKIP_BUILD=0
SKIP_FIX=0
for arg in "$@"; do
  case "$arg" in
    --skip-build) SKIP_BUILD=1 ;;
    --skip-fix) SKIP_FIX=1 ;;
    -h|--help)
      sed -n '1,14p' "$0"
      exit 0
      ;;
    *)
      echo "Unknown option: $arg (try --help)" >&2
      exit 1
      ;;
  esac
done

# Load deploy config (local file preferred; not committed)
if [[ -f "$SCRIPT_DIR/odtis-deploy.env" ]]; then
  # shellcheck source=/dev/null
  source "$SCRIPT_DIR/odtis-deploy.env"
elif [[ -f "${HOME}/.odtis-deploy.env" ]]; then
  # shellcheck source=/dev/null
  source "${HOME}/.odtis-deploy.env"
fi

ODTIS_EC2_HOST="${ODTIS_EC2_HOST:-}"
ODTIS_SSH_KEY="${ODTIS_SSH_KEY:-}"
ODTIS_REMOTE_DIR="${ODTIS_REMOTE_DIR:-/var/www/odtis.org}"

if [[ -z "$ODTIS_EC2_HOST" || -z "$ODTIS_SSH_KEY" ]]; then
  cat >&2 <<EOF
ERROR: missing deploy configuration.

Create scripts/odtis-deploy.env (once):

  cp scripts/odtis-deploy.env.example scripts/odtis-deploy.env
  # edit ODTIS_EC2_HOST and ODTIS_SSH_KEY

Or export ODTIS_EC2_HOST and ODTIS_SSH_KEY in ~/.odtis-deploy.env
EOF
  exit 1
fi

if [[ ! -f "$ODTIS_SSH_KEY" ]]; then
  echo "ERROR: SSH key not found: $ODTIS_SSH_KEY" >&2
  exit 1
fi

SSH_OPTS=(-i "$ODTIS_SSH_KEY" -o BatchMode=yes -o StrictHostKeyChecking=accept-new)

if [[ "$SKIP_BUILD" -eq 0 ]]; then
  echo "==> Building site..."
  "$ROOT/scripts/build-site.sh"
else
  echo "==> Skipping build (--skip-build)"
  if [[ ! -f "$OUT/index.html" ]]; then
    echo "ERROR: no build at $OUT  -  run without --skip-build first" >&2
    exit 1
  fi
fi

echo "==> Syncing to $ODTIS_EC2_HOST:$ODTIS_REMOTE_DIR/"
rsync -avz --delete \
  -e "ssh ${SSH_OPTS[*]}" \
  "$OUT/" \
  "$ODTIS_EC2_HOST:$ODTIS_REMOTE_DIR/"

if [[ "$SKIP_FIX" -eq 0 ]]; then
  echo "==> Fixing permissions on remote (nginx read + SELinux)..."
  ssh "${SSH_OPTS[@]}" "$ODTIS_EC2_HOST" bash -s <<EOF
set -euo pipefail
sudo find "$ODTIS_REMOTE_DIR" -type d -exec chmod 755 {} +
sudo find "$ODTIS_REMOTE_DIR" -type f -exec chmod 644 {} +
sudo chcon -R -t httpd_sys_content_t "$ODTIS_REMOTE_DIR" 2>/dev/null || true
EOF
fi

echo ""
echo "Deployed: https://odtis.org"
echo "Host:     $ODTIS_EC2_HOST"
echo "Remote:   $ODTIS_REMOTE_DIR"
echo "Tip: purge Cloudflare cache if the browser shows an old version."
