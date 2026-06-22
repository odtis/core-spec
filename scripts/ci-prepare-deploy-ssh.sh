#!/usr/bin/env bash
# Write ODTIS_SSH_KEY from GitHub Actions secrets and validate PEM format.
set -euo pipefail

KEY_PATH="${1:-$HOME/.ssh/odtis_deploy.pem}"

if [[ -z "${ODTIS_SSH_KEY:-}" ]]; then
  cat >&2 <<'EOF'
ERROR: ODTIS_SSH_KEY is empty.

Add repository secret ODTIS_SSH_KEY in GitHub:
  Settings -> Secrets and variables -> Actions -> New repository secret

Value must be the FULL .pem file contents (not the file path), e.g.:
  -----BEGIN ... PRIVATE KEY-----
  (base64 lines)
  -----END ... PRIVATE KEY-----

Local copy to clipboard:
  pbcopy < ~/.ssh/your-deploy-key.pem
EOF
  exit 1
fi

if [[ -z "${ODTIS_EC2_HOST:-}" ]]; then
  cat >&2 <<'EOF'
ERROR: ODTIS_EC2_HOST is empty.

Add repository secret ODTIS_EC2_HOST, e.g.:
  ec2-user@YOUR_EC2_PUBLIC_IP
EOF
  exit 1
fi

mkdir -p "$(dirname "$KEY_PATH")"
python3 - "$KEY_PATH" <<'PY'
import os
import subprocess
import sys
from pathlib import Path

key = os.environ.get("ODTIS_SSH_KEY", "")
path = Path(sys.argv[1])

# Common paste mistakes: literal \n instead of newlines, or wrapped in quotes.
key = key.strip()
if key.startswith('"') and key.endswith('"'):
    key = key[1:-1]
if key.startswith("'") and key.endswith("'"):
    key = key[1:-1]
if "\\n" in key and "BEGIN" in key:
    key = key.replace("\\n", "\n")

if "BEGIN" not in key or "PRIVATE KEY" not in key:
    print(
        "ERROR: ODTIS_SSH_KEY does not look like a PEM private key "
        "(missing BEGIN/END PRIVATE KEY lines).",
        file=sys.stderr,
    )
    sys.exit(1)

if not key.endswith("\n"):
    key += "\n"

path.write_text(key, encoding="utf-8")
path.chmod(0o600)
PY

if ! ssh-keygen -y -f "$KEY_PATH" > /dev/null 2>&1; then
  cat >&2 <<'EOF'
ERROR: ODTIS_SSH_KEY is not a valid PEM private key (ssh-keygen rejected it).

Re-paste the secret from your local .pem file:
  pbcopy < ~/.ssh/your-deploy-key.pem

Do not paste the path (~/.ssh/...). Include BEGIN and END lines.
EOF
  exit 1
fi

echo "SSH key ready at $KEY_PATH"
