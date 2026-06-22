#!/usr/bin/env bash
# Build ODTIS MkDocs site to ../build/odtis-spec-site/ (workspace level, gitignored)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
OUT="$(cd "$ROOT/.." && pwd)/build/odtis-spec-site"

export ODTIS_BUILD_SHA="${ODTIS_BUILD_SHA:-$(git -C "$ROOT" rev-parse --short HEAD 2>/dev/null || echo local)}"

VENV="$ROOT/.venv-site"
if [[ ! -d "$VENV" ]]; then
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -q -r site/requirements.txt
fi

python3 "$ROOT/scripts/validate-site-language.py"
python3 "$ROOT/scripts/normalize-ascii-punctuation.py" --check
python3 "$ROOT/scripts/sync-site-release-meta.py"
python3 "$ROOT/scripts/expand-product-requirements.py"
python3 "$ROOT/scripts/generate-phased-backlog.py"
python3 "$ROOT/scripts/generate-site-indexes.py"
python3 "$ROOT/scripts/generate-spec-section-indexes.py"
python3 "$ROOT/scripts/build-conformance-manifest.py"
python3 "$ROOT/scripts/generate-profile-docs.py"
python3 "$ROOT/scripts/generate-profile-readmes.py"
python3 "$ROOT/scripts/generate-component-bindings-docs.py"
python3 "$ROOT/scripts/validate-component-bindings.py"
python3 "$ROOT/scripts/validate-section-completeness.py"
python3 "$ROOT/scripts/sync-test-status-from-smokes.py" --assume-pass
python3 "$ROOT/scripts/generate-coverage-report.py"
python3 "$ROOT/scripts/fix-markdown-link-labels.py" --apply
python3 "$ROOT/scripts/fix-root-level-links.py"
python3 "$ROOT/scripts/fix-deep-relative-links.py"
python3 "$ROOT/scripts/inject-seo-meta.py"
python3 "$ROOT/scripts/generate-faq-schema.py"

"$VENV/bin/mkdocs" build -f site/mkdocs.yml --strict
python3 "$ROOT/scripts/copy-site-artifacts.py"
python3 "$ROOT/scripts/check-site-links.py"
python3 "$ROOT/scripts/cache-bust-assets.py"
echo "Built: $OUT"
