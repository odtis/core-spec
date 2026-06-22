#!/usr/bin/env bash
# Build ODTIS MkDocs site and prepare for odtis.org deployment.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
OUT="$(cd "$ROOT/.." && pwd)/build/odtis-spec-site"
CNAME="${ODTIS_SITE_CNAME:-odtis.org}"

"$ROOT/scripts/build-site.sh"

echo "$CNAME" > "$OUT/CNAME"
echo "Wrote $OUT/CNAME"

if [[ -n "${ODTIS_DEPLOY_DEST:-}" ]]; then
mkdir -p "$ODTIS_DEPLOY_DEST"
rsync -a --delete "$OUT/" "$ODTIS_DEPLOY_DEST/"
echo "Synced to $ODTIS_DEPLOY_DEST"
fi

cat <<EOF

Deploy options:

1) Static host - sync build output:
ODTIS_DEPLOY_DEST=/var/www/odtis.org ./scripts/deploy-site.sh

2) GitHub Pages (from repo with gh auth):
cd odtis && source .venv-site/bin/activate
mkdocs gh-deploy -f site/mkdocs.yml --remote-branch gh-pages

3) EC2 rsync - see scripts/deploy-ec2.sh and scripts/odtis-deploy.env.example

Output: $OUT
CNAME: $CNAME
EOF
