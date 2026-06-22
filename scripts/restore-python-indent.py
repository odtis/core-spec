#!/usr/bin/env python3
"""Restore Python indentation after accidental leading-space strip."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TARGETS = [
    ROOT / "scripts/pin-annex-a-checksums.py",
    ROOT / "scripts/validate-threats.py",
    ROOT / "scripts/sync-spec-version.py",
    ROOT / "scripts/generate-standards-mapping.py",
    ROOT / "scripts/validate-registry.py",
    ROOT / "scripts/build-traceability-index.py",
    ROOT / "scripts/validate-standards-mapping.py",
    ROOT / "scripts/normalize-coherence.py",
    ROOT / "scripts/validate-extended-annex.py",
    ROOT / "scripts/build-conformance-manifest.py",
    ROOT / "scripts/validate-openapi.py",
    ROOT / "conformance/l2/run_l2.py",
]

MODULE_LEVEL = (
    "def ",
    "class ",
    "import ",
    "from ",
    "if __name__",
    "@",
)


def is_dedent_keyword(stripped: str) -> bool:
    if stripped.startswith(("elif ", "elif:", "else:", "except ", "except:", "finally:", "finally ")):
        return True
    return False


def is_module_level(stripped: str) -> bool:
    return any(stripped.startswith(p) for p in MODULE_LEVEL)


def reindent_source(source: str) -> str:
    out: list[str] = []
    stack = [0]

    for raw in source.splitlines():
        stripped = raw.strip()
        if not stripped:
            out.append("")
            continue

        if is_module_level(stripped):
            while len(stack) > 1:
                stack.pop()

        if is_dedent_keyword(stripped) and len(stack) > 1:
            stack.pop()

        out.append(" " * stack[-1] + stripped)

        if stripped.endswith(":") and not stripped.startswith("#"):
            stack.append(stack[-1] + 4)

    return "\n".join(out) + ("\n" if source.endswith("\n") else "")


def main() -> int:
    failed: list[str] = []
    for path in TARGETS:
        text = path.read_text(encoding="utf-8")
        fixed = reindent_source(text)
        path.write_text(fixed, encoding="utf-8")
        try:
            compile(fixed, str(path), "exec")
        except SyntaxError as exc:
            failed.append(f"{path.relative_to(ROOT)}: {exc}")

    if failed:
        print("FAIL - could not restore indentation:")
        for item in failed:
            print(f"  - {item}")
        return 1

    print(f"Restored indentation in {len(TARGETS)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
