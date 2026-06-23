#!/usr/bin/env bash
# Static L2 smoke for Reliance Extensions pilot (Capa B overlay).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FAIL=0
if [[ -x "$ROOT/.venv-site/bin/python" ]]; then
  PYTHON="$ROOT/.venv-site/bin/python"
else
  PYTHON=python3
fi

pass() { echo "OK: $1"; }
fail() { echo "FAIL: $1" >&2; FAIL=1; }

run() {
  local name="$1"
  shift
  echo ""
  echo "== $name =="
  if "$@"; then
    pass "$name"
  else
    fail "$name"
  fi
}

echo "== Reliance Extensions L2 smoke =="
echo "as_of: $(date -u +%Y-%m-%dT%H:%M:%SZ)"

run "Annex E validator" "$PYTHON" "$ROOT/scripts/validate-reliance-annex.py"
run "RI-MAP validator" "$PYTHON" "$ROOT/scripts/validate-ri-map.py" --warn-only-paths
run "Pilot conformance statement" "$PYTHON" "$ROOT/scripts/validate-conformance-statement.py" \
  "$ROOT/implementation/statements/venid-reliance-pilot/conformance-statement.yaml"
run "Reliance overlay binding present" test -f "$ROOT/implementation/component-bindings/reliance-overlay.yaml"
run "R-Base field catalog present" test -f "$ROOT/registry/reliance-profiles.yaml"

run "Pilot modules and core IDs" "$PYTHON" -c "
import re, sys
from pathlib import Path
root = Path('$ROOT')
text = (root / 'implementation/statements/venid-reliance-pilot/conformance-statement.yaml').read_text()
mods = re.search(r'\"reliance_extensions\":\s*\[(.*?)\]', text, re.S)
if not mods or 'R-Base' not in mods.group(1):
    sys.exit('missing R-Base')
for mod in ('R-Agent-Authority', 'R-Crypto-Agility', 'R-Document-Capture'):
    if mod not in mods.group(1):
        sys.exit(f'missing {mod}')
reqs = set(re.findall(r'\"(ODTIS-\d{4})\"', text))
for rid in ('ODTIS-0701', 'ODTIS-0707', 'ODTIS-0708', 'ODTIS-0710', 'ODTIS-0715', 'ODTIS-0723'):
    if rid not in reqs:
        sys.exit(f'missing {rid}')
print('pilot modules OK')
"

echo ""
if [[ "$FAIL" -eq 0 ]]; then
  echo "Reliance L2 smoke: PASS"
  exit 0
fi
echo "Reliance L2 smoke: FAIL"
exit 1
