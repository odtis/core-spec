#!/usr/bin/env python3
"""Generate FAQPage JSON-LD partial from site/FAQ.md for Google rich results."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAQ = ROOT / "site/FAQ.md"
OUT = ROOT / "site/overrides/partials/faq-ld.html"
SITE_URL = "https://odtis.org/site/FAQ/"


def strip_md(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_pairs(text: str) -> list[tuple[str, str]]:
    body = text
    if text.startswith("---"):
        body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    pairs: list[tuple[str, str]] = []
    pattern = re.compile(r"^### ([^\n]+)\n+(.+?)(?=^### |^## |\Z)", re.MULTILINE | re.DOTALL)
    for match in pattern.finditer(body):
        q = strip_md(match.group(1))
        block = match.group(2).strip()
        if block.startswith("!!!") or block.startswith("|") or block.startswith("```"):
            continue
        a = strip_md(block.split("\n\n")[0])
        if len(a) < 20:
            continue
        pairs.append((q, a[:500]))
    return pairs


def main() -> int:
    if not FAQ.is_file():
        print(f"ERROR: missing {FAQ}", file=sys.stderr)
        return 1

    pairs = extract_pairs(FAQ.read_text(encoding="utf-8"))
    if not pairs:
        print("WARN: no FAQ pairs extracted", file=sys.stderr)
        return 1

    payload = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in pairs
        ],
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        '<script type="application/ld+json">\n'
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + "\n</script>\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(pairs)} questions)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
