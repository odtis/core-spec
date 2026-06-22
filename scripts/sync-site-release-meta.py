#!/usr/bin/env python3
"""Sync VERSION and build metadata into MkDocs config and public build artifacts."""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"
MKDOCS = ROOT / "site/mkdocs.yml"
BUILD_META = ROOT / "site/BUILD-META.json"
INDEX_MD = ROOT / "index.md"

COPYRIGHT_RE = re.compile(
    r"^(  copyright: ).*ODTIS.*$",
    re.M,
)
VERSION_EXTRA_RE = re.compile(r"^  odtis_version:.*$", re.M)
SHA_EXTRA_RE = re.compile(r"^  odtis_build_sha:.*$", re.M)
TIME_EXTRA_RE = re.compile(r"^  odtis_build_time:.*$", re.M)
HERO_VERSION_RE = re.compile(
    r"(<!-- GENERATED:site-release-version:START -->).*?(<!-- GENERATED:site-release-version:END -->)",
    re.S,
)


def read_version() -> str:
    return VERSION_FILE.read_text(encoding="utf-8").strip()


def resolve_build_sha() -> str:
    env_sha = os.environ.get("ODTIS_BUILD_SHA") or os.environ.get("GITHUB_SHA")
    if env_sha:
        return env_sha
    try:
        import subprocess

        sha = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        return sha or "local"
    except (OSError, subprocess.CalledProcessError):
        return "local"


def build_meta(version: str) -> dict[str, str]:
    sha = resolve_build_sha()
    when = os.environ.get("ODTIS_BUILD_TIME", "")
    if not when:
        when = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "odtis_version": version,
        "build_sha": sha,
        "build_time": when,
        "site_url": "https://digitaltrustinfrastructure.org",
        "repository": "https://github.com/odtis/core-spec",
    }


def upsert_line(text: str, pattern: re.Pattern[str], line: str) -> str:
    if pattern.search(text):
        return pattern.sub(line, text, count=1)
    anchor = "extra:\n"
    if anchor in text:
        return text.replace(anchor, anchor + line + "\n", 1)
    return text + "\n" + line + "\n"


def sync_mkdocs(version: str, meta: dict[str, str]) -> bool:
    text = MKDOCS.read_text(encoding="utf-8")
    year = datetime.now(timezone.utc).year
    new_copyright = (
        f'  copyright: Copyright &copy; {year} '
        f'<a href="https://github.com/odtis/core-impl">VenID</a> / FinnectOS &middot; '
        f'ODTIS {version} &middot; '
        f'<a href="/site/LICENSE/">CC BY 4.0</a>'
    )
    updated = COPYRIGHT_RE.sub(new_copyright, text, count=1)
    updated = upsert_line(updated, VERSION_EXTRA_RE, f'  odtis_version: "{version}"')
    updated = upsert_line(
        updated,
        SHA_EXTRA_RE,
        f'  odtis_build_sha: "{meta["build_sha"]}"',
    )
    updated = upsert_line(
        updated,
        TIME_EXTRA_RE,
        f'  odtis_build_time: "{meta["build_time"]}"',
    )
    if updated != text:
        MKDOCS.write_text(updated, encoding="utf-8")
        return True
    return False


def sync_index_hero(version: str) -> bool:
    if not INDEX_MD.is_file():
        return False
    block = (
        "<!-- GENERATED:site-release-version:START -->\n"
        f'<p class="odtis-landing-hero__version">Published release '
        f'<a href="/VERSION">{version}</a> · '
        f'<a href="/site/BUILD-META.json">build info</a></p>\n'
        "<!-- GENERATED:site-release-version:END -->"
    )
    text = INDEX_MD.read_text(encoding="utf-8")
    if HERO_VERSION_RE.search(text):
        new_text = HERO_VERSION_RE.sub(block, text, count=1)
    else:
        marker = '<p class="odtis-landing-hero__kicker">ODTIS</p>'
        new_text = text.replace(marker, marker + "\n\n" + block, 1)
    if new_text != text:
        INDEX_MD.write_text(new_text, encoding="utf-8")
        return True
    return False


def write_build_meta(meta: dict[str, str]) -> None:
    BUILD_META.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")


def sync_status_page(version: str) -> bool:
    status = ROOT / "site/STATUS.md"
    if not status.is_file():
        return False
    text = status.read_text(encoding="utf-8")
    new_text = re.sub(
        r'(<strong>Version:</strong> <a href="/VERSION">)[^<]+(</a>)',
        rf"\g<1>{version}\g<2>",
        text,
        count=1,
    )
    new_text = re.sub(
        r"readiness assessment for ODTIS [^.\n]+",
        f"readiness assessment for ODTIS {version}",
        new_text,
        count=1,
    )
    if new_text != text:
        status.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> int:
    version = read_version()
    meta = build_meta(version)
    changed = False
    if sync_mkdocs(version, meta):
        print(f"Updated {MKDOCS.relative_to(ROOT)}")
        changed = True
    if sync_index_hero(version):
        print(f"Updated {INDEX_MD.relative_to(ROOT)}")
        changed = True
    if sync_status_page(version):
        print(f"Updated {(ROOT / 'site/STATUS.md').relative_to(ROOT)}")
        changed = True
    write_build_meta(meta)
    print(f"Wrote {BUILD_META.relative_to(ROOT)}")
    if not changed:
        print(f"OK - site release meta @ {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
