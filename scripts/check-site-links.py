#!/usr/bin/env python3
"""Check internal links in built ODTIS MkDocs HTML output."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urldefrag, urljoin

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT.parent / "build" / "odtis-spec-site"

SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "javascript:", "#")
HREF_RE = re.compile(r"""href=["']([^"']+)["']""")


class LinkParser(HTMLParser):
    def __init__(self, page: Path) -> None:
        super().__init__()
        self.page = page
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self.links.append(href)


def md_page_target(href_path: str) -> Path:
    """Map MkDocs .md URL to built index.html path."""
    rel = href_path.lstrip("/")
    if rel.endswith(".md"):
        rel = rel[:-3]
    if rel.endswith("/README"):
        rel = rel[: -len("/README")]
    return SITE / rel / "index.html"


def resolve_target(page: Path, href: str) -> Path | None:
    href, _frag = urldefrag(href)
    href = unquote(href)
    if not href or href.startswith(SKIP_PREFIXES):
        return None
    if href.endswith(".md"):
        if href.startswith("/"):
            return md_page_target(href)
        resolved = (page.parent / href).resolve()
        try:
            return md_page_target(str(resolved.relative_to(SITE)))
        except ValueError:
            return None
    if href.startswith("/"):
        target = SITE / href.lstrip("/")
    else:
        target = (page.parent / href).resolve()
    return target


def exists(target: Path) -> bool:
    if target.is_file():
        return True
    candidates = [target, target / "index.html"]
    if target.name.upper() == "INDEX":
        candidates.append(target / "index.html")
    for candidate in candidates:
        if candidate.is_file():
            return True
        if candidate.is_dir() and (candidate / "index.html").is_file():
            return True
    # MkDocs: foo/ or foo without trailing slash
    if (target / "index.html").is_file():
        return True
    return False


def main() -> int:
    if not SITE.is_dir():
        print(f"ERROR: build output not found: {SITE}", file=sys.stderr)
        return 1

    broken: list[tuple[str, str, str]] = []
    raw_md: list[tuple[str, str]] = []

    for html in sorted(SITE.rglob("*.html")):
        if "overrides" in html.parts:
            continue
        text = html.read_text(encoding="utf-8", errors="replace")
        rel_page = html.relative_to(SITE)

        for href in set(HREF_RE.findall(text)):
            if href.startswith(SKIP_PREFIXES):
                continue
            if href.endswith((".md", ".yaml", ".yml", ".json")):
                target = resolve_target(html, href)
                if target is not None:
                    try:
                        target.relative_to(SITE)
                        if not exists(target):
                            raw_md.append((str(rel_page), href))
                    except ValueError:
                        pass
                continue
            target = resolve_target(html, href)
            if target is None:
                continue
            try:
                target.relative_to(SITE)
            except ValueError:
                continue
            if not exists(target):
                broken.append((str(rel_page), href, str(target.relative_to(SITE))))

    print(f"Scanned {len(list(SITE.rglob('*.html')))} HTML files under {SITE}")
    print()

    if raw_md:
        print(f"RAW .md/.yaml/.json hrefs ({len(raw_md)})  -  404 in production:")
        for page, href in sorted(raw_md)[:80]:
            print(f"  {page} -> {href}")
        if len(raw_md) > 80:
            print(f"  ... and {len(raw_md) - 80} more")
        print()

    if broken:
        print(f"BROKEN internal links ({len(broken)}):")
        for page, href, target in sorted(broken)[:80]:
            print(f"  {page} -> {href}  (missing: {target})")
        if len(broken) > 80:
            print(f"  ... and {len(broken) - 80} more")
        print()

    if not raw_md and not broken:
        print("OK - no broken internal links or raw .md hrefs")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
