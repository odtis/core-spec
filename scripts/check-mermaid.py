#!/usr/bin/env python3
"""Fail if Mermaid blocks use syntax that breaks Mermaid 11 (e.g. | inside node labels)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".venv-site", "build", ".git"}

# Unquoted node labels: [..|..] or [(..|..)]  -  pipe is a shape token in flowcharts.
PIPE_IN_NODE = re.compile(
    r"(?:\[[^\]\"]*\|[^\]\"]*\]|\[\([^\)]\"]*\|[^\)]\"]*\)\])"
)


def iter_md() -> list[Path]:
    out: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if any(p in SKIP for p in path.parts):
            continue
        out.append(path)
    return sorted(out)


def main() -> int:
    issues: list[str] = []
    for path in iter_md():
        text = path.read_text(encoding="utf-8")
        for i, m in enumerate(re.finditer(r"```mermaid\n([\s\S]*?)```", text), 1):
            code = m.group(1)
            for line_no, line in enumerate(code.splitlines(), 1):
                if "|" in line and PIPE_IN_NODE.search(line):
                    rel = path.relative_to(ROOT)
                    issues.append(f"{rel} diagram #{i} line {line_no}: unquoted | in node label")
    if issues:
        print("FAIL - Mermaid syntax hazards (use / or commas, or quote labels):")
        for item in issues:
            print(f"  - {item}")
        return 1
    print("OK - no known Mermaid 11 pipe-in-label issues")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
