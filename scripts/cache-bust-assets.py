#!/usr/bin/env python3
"""Append a build version query string to site CSS/JS assets in built HTML."""

from __future__ import annotations

import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ASSETS = (
    "extra.css",
    "gitbook-theme.css",
    "mobile.css",
    "extra.js",
)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    out = root.parent / "build" / "odtis-spec-site"
    if not out.is_dir():
        print(f"Missing build output: {out}", file=sys.stderr)
        return 1

    version_file = root / "VERSION"
    version = version_file.read_text(encoding="utf-8").strip() if version_file.is_file() else "dev"
    sha = os.environ.get("ODTIS_BUILD_SHA", os.environ.get("GITHUB_SHA", "local"))[:12]
    version = f"{version}-{sha}"
    assets_alt = "|".join(re.escape(asset) for asset in ASSETS)
    pattern = re.compile(
        rf'((?:href|src)="(?:\.\./)*(?:site/)?(?:stylesheets|javascripts)/({assets_alt}))(?:\?[^"]*)?"'
    )

    updated = 0
    for html in out.rglob("*.html"):
        text = html.read_text(encoding="utf-8")
        new_text, count = pattern.subn(rf'\1?v={version}"', text)
        if count:
            html.write_text(new_text, encoding="utf-8")
            updated += count

    print(f"Cache-busted {updated} asset references (v={version})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
