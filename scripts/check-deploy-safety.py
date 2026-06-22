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
)

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("private key block", re.compile(r"BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY")),
    ("AWS access key", re.compile(r"AKIA[0-9A-Z]{16}")),
]


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
        if path.name == "check-deploy-safety.py":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        rel = path.relative_to(ROOT)
        for blocked_ip in BLOCKED_IPS:
            if blocked_ip in text:
                failures.append(f"{rel}: blocked deploy IP ({blocked_ip})")
        for fragment in BLOCKED_PATH_FRAGMENTS:
            if fragment in text:
                failures.append(f"{rel}: blocked path or key reference ({fragment})")
        for label, pattern in PATTERNS:
            for match in pattern.finditer(text):
                failures.append(f"{rel}: {label} ({match.group(0)[:24]}...)")
    if failures:
        print("FAIL - deploy safety check found sensitive or host-specific values:", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1
    print("OK - no deploy secrets or host-specific paths in tracked files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
