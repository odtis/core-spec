#!/usr/bin/env python3
"""Normalize Markdown links for MkDocs strict build.

Fixes:
- Directory links (trailing slash) -> index README or INDEX.md
- Excluded artifacts (.yaml, .json, scripts/, tests/, traceability/) -> GitHub blob URLs
- Monorepo docs outside docs_dir -> GitHub blob URLs
- Root README.md links -> site/REPOSITORY-README.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ODTIS_GITHUB = "https://github.com/odtis/core-spec/blob/main"
PUBLICATIONS_GITHUB = "https://github.com/finnectos/venezuela/blob/main"

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

DIR_TARGETS: dict[str, str] = {
    "spec/": "spec/INDEX.md",
    "spec/profiles/": "spec/profiles/README.md",
    "registry/": "registry/README.md",
    "registry/events/schemas/": "registry/README.md",
    "annexes/": "annexes/README.md",
    "annexes/A-openapi-registry/": "annexes/A-openapi-registry/README.md",
    "annexes/B-threat-mitigations/": "annexes/B-threat-mitigations/README.md",
    "annexes/C-standards-mapping/": "annexes/C-standards-mapping/README.md",
    "annexes/D-extended-profiles/": "annexes/D-extended-profiles/README.md",
    "conformance/": "conformance/README.md",
    "conformance/tests/": "conformance/tests/README.md",
    "conformance/profiles/core-identity/": "conformance/profiles/core-identity/README.md",
    "conformance/profiles/trust-network/": "conformance/profiles/trust-network/README.md",
    "conformance/profiles/federation/": "conformance/profiles/federation/README.md",
    "conformance/profiles/operator/": "conformance/profiles/operator/README.md",
    "conformance/profiles/extended/": "conformance/profiles/extended/README.md",
    "traceability/": "traceability/README.md",
    "publication/": "publication/HOW-TO-CITE.md",
    "governance/": "governance/README.md",
    "governance/review/": "governance/review/README.md",
    "governance/rfc/": "governance/rfc/README.md",
    "implementation/": "implementation/README.md",
    "ietf/": "ietf/README.md",
    "ietf/drafts/": "ietf/README.md",
    "site/": "site/STATUS.md",
}

EXCLUDED_SUFFIXES = (
    ".yaml",
    ".yml",
    ".json",
    ".openapi.yaml",
    ".py",
    ".sh",
)

SKIP_PATH_PARTS = {".venv-site", "build", ".git"}


def is_external(url: str) -> bool:
    return url.startswith(("http://", "https://", "mailto:", "#"))


def resolve_path(source: Path, url: str) -> Path | None:
    if is_external(url) or url.startswith("#"):
        return None
    target = (source.parent / url).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return target
    return target


def repo_relative(source: Path, url: str) -> str | None:
    target = resolve_path(source, url)
    if target is None:
        return None
    try:
        return target.relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return None


def monorepo_relative(source: Path, url: str) -> str | None:
    target = resolve_path(source, url)
    if target is None:
        return None
    try:
        return target.relative_to(ROOT.resolve().parent).as_posix()
    except ValueError:
        return None


def is_excluded_repo_path(rel: str) -> bool:
    if rel.startswith("scripts/"):
        return True
    if rel.startswith("traceability/"):
        return True
    if rel.startswith("conformance/tests/") and rel.endswith(".md"):
        return True
    if rel.startswith("conformance/profiles/") and rel.endswith("README.md"):
        return True
    if rel.endswith(EXCLUDED_SUFFIXES):
        return True
    if "/.spectral." in rel:
        return True
    return False


def directory_target(url: str) -> str | None:
    if not url.endswith("/"):
        return None
    if url in DIR_TARGETS:
        return DIR_TARGETS[url]
    # Relative directory paths: match suffix
    for key, value in sorted(DIR_TARGETS.items(), key=lambda kv: len(kv[0]), reverse=True):
        if url.endswith(key) or url == key.rstrip("/"):
            prefix = url[: -len(key)] if url.endswith(key) else ""
            return f"{prefix}{value}"
    candidate = f"{url}README.md"
    return candidate


def github_odtis(rel: str) -> str:
    return f"{ODTIS_GITHUB}/{rel}"


def github_publications(rel: str) -> str:
    return f"{PUBLICATIONS_GITHUB}/{rel}"


def transform_link(source: Path, url: str) -> str | None:
    if is_external(url):
        return None

    if url in ("README.md", "../README.md", "../../README.md"):
        depth = source.relative_to(ROOT).parent
        prefix = "../" * len(depth.parts) if depth.parts else "./"
        return f"{prefix}site/REPOSITORY-README.md"

    if url.endswith("/"):
        if url.endswith("events/schemas/") or url.endswith("registry/events/schemas/"):
            rel = repo_relative(source, url) or "registry/events/schemas"
            if not rel.endswith("/"):
                rel = rel.rstrip("/") + "/"
            return github_odtis(rel.rstrip("/")).replace("/blob/", "/tree/")
        mapped = directory_target(url)
        return mapped

    rel = repo_relative(source, url)
    if rel == "README.md":
        depth = len(source.relative_to(ROOT).parent.parts)
        prefix = "../" * depth if depth else "./"
        return f"{prefix}site/REPOSITORY-README.md"

    if rel and is_excluded_repo_path(rel):
        return github_odtis(rel)

    mono = monorepo_relative(source, url)
    if mono and mono.startswith("docs/"):
        return github_publications(mono)

    # Path resolves outside odtis docs_dir (parent monorepo)
    target = resolve_path(source, url)
    if target and not str(target).startswith(str(ROOT.resolve())):
        if mono:
            return github_publications(mono)

    return None


def process_file(path: Path, apply: bool) -> int:
    text = path.read_text(encoding="utf-8")
    changes = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal changes
        label, url = match.group(1), match.group(2)
        if url.startswith("#") or is_external(url):
            return match.group(0)
        new_url = transform_link(path, url)
        if new_url and new_url != url:
            changes += 1
            return f"[{label}]({new_url})"
        return match.group(0)

    updated = LINK_RE.sub(repl, text)
    if changes and apply:
        path.write_text(updated, encoding="utf-8")
    return changes


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(part in SKIP_PATH_PARTS for part in path.parts):
            continue
        if path.name == "README.md" and path.parent == ROOT:
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write fixes to disk")
    parser.add_argument("--check", action="store_true", help="Exit 1 if fixes needed")
    args = parser.parse_args()
    apply = args.apply or not args.check

    total = 0
    touched: list[tuple[str, int]] = []
    for path in iter_markdown_files():
        count = process_file(path, apply=apply if args.apply else False)
        if args.check and count:
            touched.append((str(path.relative_to(ROOT)), count))
            total += count
        elif args.apply:
            if count:
                touched.append((str(path.relative_to(ROOT)), count))
            total += count

    if args.check:
        if total:
            print(f"ERROR: {total} link(s) need normalization in {len(touched)} file(s)", file=sys.stderr)
            for rel, count in touched[:20]:
                print(f"  {rel}: {count}", file=sys.stderr)
            if len(touched) > 20:
                print(f"  ... and {len(touched) - 20} more files", file=sys.stderr)
            return 1
        print("OK - site markdown links normalized")
        return 0

    if args.apply:
        print(f"Updated {total} link(s) across {len(touched)} file(s)")
        for rel, count in touched:
            if count:
                print(f"  {rel}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
