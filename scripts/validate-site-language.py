#!/usr/bin/env python3
"""Fail if MkDocs-publishable Markdown contains Spanish (or other non-English) prose."""

from __future__ import annotations

import fnmatch
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MKDOCS = ROOT / "site" / "mkdocs.yml"

# Lines matching these patterns are allowed (filenames, policy meta, proper names).
ALLOW_LINE = re.compile(
    r"Mérida|"
    r"PLAN-EJECUCION-FASES|PLAN-FASES|PLAN-PHASES|"
    r"normativa-estandares-referencia|REPORTE-COBERTURA|"
    r"Spanish edition|Book 1 ES|"
    r"Spanish translations|Spanish or other languages|Spanish filenames|"
    r"Legacy redirect|renamed to|English filename|"
    r"RFC Editor|editor approval|Lead editor|\*\*Editors\*\*|"
    r"Editorial|Editors MAY|Editors MUST|editorial/",
    re.I,
)

# Strong Spanish prose indicators (word boundaries).
SPANISH_PATTERNS = [
    re.compile(r"[¿¡]"),
    re.compile(r"\b(especificación|implementación|gobernanza|conformidad|requisitos?)\b", re.I),
    re.compile(r"\b(anexo|sección|capítulo|borrador|versión|descripción)\b", re.I),
    re.compile(r"\b(debe|debería|deben|deberían)\s+(ser|estar|implementar|publicar|cumplir)\b", re.I),
    re.compile(r"\b(este|esta|estos|estas)\s+(documento|especificación|sección|anexo|capítulo)\b", re.I),
    re.compile(r"\b(todos|todas)\s+los\b", re.I),
    re.compile(r"\b(según|también|además|mediante|durante)\s+la\b", re.I),
    re.compile(r"\b(introducción|resumen|objetivo|alcance|nota importante)\b", re.I),
    re.compile(r"\b(para el|para la|de la|de los|de las|en el|en la)\b", re.I),
    re.compile(r"\b(español|castellano)\b", re.I),
]

ACCENT_WORD = re.compile(r"\b\w*[áéíóúñÁÉÍÓÚÑ]\w*\b")


def load_exclude_globs() -> list[str]:
    text = MKDOCS.read_text(encoding="utf-8")
    block = text.split("exclude_docs: |", 1)[1].split("\nvalidation:", 1)[0]
    return [line.strip() for line in block.splitlines() if line.strip()]


def excluded(rel_posix: str, patterns: list[str]) -> bool:
    for pat in patterns:
        if fnmatch.fnmatch(rel_posix, pat):
            return True
        if fnmatch.fnmatch(Path(rel_posix).name, pat):
            return True
        # directory prefix patterns without glob
        if pat.endswith("/") and rel_posix.startswith(pat):
            return True
    return False


def site_markdown_files() -> list[Path]:
    patterns = load_exclude_globs()
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        if excluded(rel, patterns):
            continue
        files.append(path)
    return sorted(files)


def strip_inline_code_and_links(line: str) -> str:
    line = re.sub(r"`[^`]*`", " ", line)
    line = re.sub(r"\[[^\]]*\]\([^)]*\)", " ", line)
    line = re.sub(r"https?://\S+", " ", line)
    return line


def check_ascii_punctuation(text: str) -> list[str]:
    if "\u2014" in text or "\u2013" in text or "\u00a7" in text:
        return ["contains em dash, en dash, or section sign (use - and 'section N')"]
    return []


def check_file(path: Path) -> list[str]:
    issues: list[str] = []
    text = path.read_text(encoding="utf-8")
    for msg in check_ascii_punctuation(text):
        issues.append(f"{path.relative_to(ROOT)}: {msg}")
    for num, raw in enumerate(text.splitlines(), 1):
        if ALLOW_LINE.search(raw):
            continue
        line = strip_inline_code_and_links(raw)
        for pat in SPANISH_PATTERNS:
            if pat.search(line):
                issues.append(f"{path.relative_to(ROOT)}:{num}: {raw.strip()}")
                break
        else:
            for word in ACCENT_WORD.findall(line):
                if word not in {"Mérida"} and "Mérida" not in word:
                    issues.append(f"{path.relative_to(ROOT)}:{num}: accented token {word!r}")
                    break
    return issues


def main() -> int:
    files = site_markdown_files()
    all_issues: list[str] = []
    for path in files:
        all_issues.extend(check_file(path))

    if all_issues:
        print(f"FAIL - possible non-English prose in site Markdown ({len(all_issues)} hits):")
        for hit in all_issues[:40]:
            print(f"  - {hit}")
        if len(all_issues) > 40:
            print(f"  ... and {len(all_issues) - 40} more")
        return 1

    print(f"OK - English-only check passed ({len(files)} MkDocs Markdown files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
