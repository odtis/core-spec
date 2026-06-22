#!/usr/bin/env python3
"""Fail if tracked files contain deploy secrets or host-specific infrastructure."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BLOCKED_IPS = frozenset({"34.227.196.69"})
BLOCKED_PATH_FRAGMENTS = (
    "/Users/",
    "MvpKeyPair.pem",
    "manuelmerida/development",
    "finnectos/venezuela",
    "venezuela/odtis",
)

# Documentation / CI helpers may mention PEM format; scan for real key material only.
REAL_PEM_BLOCK = re.compile(
    r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----\s+[A-Za-z0-9+/=\s]{80,}"
    r"\s+-----END (?:RSA |OPENSSH |EC )?PRIVATE KEY-----",
    re.MULTILINE,
)

AWS_KEY = re.compile(r"AKIA[0-9A-Z]{16}")

# Paths allowed to mention deploy setup (placeholders only, no real secrets).
EXEMPT_REL_PATHS = frozenset(
    {
        "scripts/check-deploy-safety.py",
        "scripts/GITHUB-DEPLOY-SECRETS.md",
        "scripts/ci-prepare-deploy-ssh.sh",
        "scripts/odtis-deploy.env.example",
        "scripts/DEPLOY-EC2-ODTIS-ORG.md",
    }
)


def tracked_files() -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / p for p in out.stdout.decode("utf-8").split("\0") if p]


def main() -> int:
    failures: list[str] = []
    for path in tracked_files():
        rel = path.relative_to(ROOT).as_posix()
        if rel in EXEMPT_REL_PATHS:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for blocked_ip in BLOCKED_IPS:
            if blocked_ip in text:
                failures.append(f"{rel}: blocked deploy IP ({blocked_ip})")
        for fragment in BLOCKED_PATH_FRAGMENTS:
            if fragment in text:
                failures.append(f"{rel}: blocked path or key reference ({fragment})")
        if REAL_PEM_BLOCK.search(text):
            failures.append(f"{rel}: private key block (PEM material)")
        for match in AWS_KEY.finditer(text):
            failures.append(f"{rel}: AWS access key ({match.group(0)})")
    if failures:
        print("FAIL - deploy safety check found sensitive or host-specific values:", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1
    print("OK - no deploy secrets or host-specific paths in tracked files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
