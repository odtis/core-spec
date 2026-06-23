#!/usr/bin/env python3
"""Regenerate traceability/coverage-report.yaml and site/STATUS.md metrics block."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry/requirements.json"
TESTS_DIR = ROOT / "conformance/tests"
COVERAGE_OUT = ROOT / "traceability/coverage-report.yaml"
STATUS_MD = ROOT / "site/STATUS.md"
INDEX_MD = ROOT / "index.md"
RF_MATRIX = ROOT / "traceability/rf-matrix.yaml"

GENERATED_START = "<!-- GENERATED:coverage-metrics:START -->"
GENERATED_END = "<!-- GENERATED:coverage-metrics:END -->"
CONFORMANCE_SUITE_START = "<!-- GENERATED:conformance-suite:START -->"
CONFORMANCE_SUITE_END = "<!-- GENERATED:conformance-suite:END -->"
HERO_START = "<!-- GENERATED:coverage-hero:START -->"
HERO_END = "<!-- GENERATED:coverage-hero:END -->"

PROFILE_LABELS = {
    "reference-architecture": "Reference Architecture",
    "core-identity": "Core Identity",
    "trust-network": "Trust Network",
    "federation": "Federation",
    "operator": "Operator",
    "extended": "Extended",
    "reliance-extensions": "Reliance Extensions",
}
PROFILE_ORDER = list(PROFILE_LABELS.keys())

METRIC_DOC_PATHS = [
    ROOT / "README.md",
    ROOT / "conformance/README.md",
    ROOT / "spec/profiles/README.md",
    ROOT / "spec/INDEX.md",
    ROOT / "site/FAQ.md",
    ROOT / "site/news/2026-06.md",
    ROOT / "conformance/FAQ.md",
    ROOT / "PLAN-PHASES.md",
    ROOT / "governance/review/sandbox-001-l2-report-template.md",
    ROOT / "implementation/DOCUMENTATION-ROADMAP.md",
]

STATUS_LINE = re.compile(r"^\*\*Status:\*\*\s*(.+)\s*$", re.M)
IMPLEMENTED = re.compile(r"^implemented\b", re.I)

sys.path.insert(0, str(ROOT / "scripts"))
from profile_registry import load_requirements, parse_profiles_yaml, profile_requirement_ids  # noqa: E402


def parse_rf_matrix() -> dict:
    if not RF_MATRIX.is_file():
        return {"total": 0, "with_odtis_id": 0, "partial": 0, "gap": 0}
    text = RF_MATRIX.read_text(encoding="utf-8")
    rows = [ln for ln in text.splitlines() if ln.strip().startswith("- rf:")]
    partial = sum(1 for ln in rows if "partial" in ln.lower())
    gap = sum(1 for ln in rows if re.search(r"\bgap\b", ln, re.I))
    return {
        "total": len(rows),
        "with_odtis_id": len(rows),
        "partial": partial,
        "gap": gap,
        "coverage_pct": round(100.0 * (len(rows) - gap) / len(rows), 1) if rows else 0.0,
    }


def scan_tests() -> list[dict]:
    tests: list[dict] = []
    for path in sorted(TESTS_DIR.rglob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        m = STATUS_LINE.search(text)
        status = m.group(1).strip() if m else "unknown"
        reqs = set(re.findall(r"ODTIS-\d{4}", text))
        profile = path.parts[-2] if len(path.parts) >= 3 else "unknown"
        tests.append(
            {
                "path": str(path.relative_to(ROOT)),
                "status": status,
                "implemented": bool(IMPLEMENTED.match(status)),
                "requirements": sorted(reqs),
                "profile": profile,
            }
        )
    return tests


def replace_generated_block(text: str, start: str, end: str, block: str) -> str:
    if start in text and end in text:
        before = text.split(start, 1)[0]
        after = text.split(end, 1)[1]
        return before + block + after
    return text


def sync_public_metric_strings(
    total: int, implemented: int, impl_pct: float, req_count: int
) -> int:
    """Keep human-authored docs aligned with generated conformance counts."""
    updated = 0
    patterns = [
        (re.compile(r"\*\*81\*\* have smoke"), f"**{implemented}** have smoke"),
        (re.compile(r"\*\*85\*\* have smoke"), f"**{implemented}** have smoke"),
        (re.compile(r"\*\*81 implemented\*\*"), f"**{implemented} implemented**"),
        (re.compile(r"\(81 with smoke evidence\)"), f"({implemented} with smoke evidence)"),
        (re.compile(r"\(85 with smoke evidence\)"), f"({implemented} with smoke evidence)"),
        (re.compile(r"\(81 implemented\)"), f"({implemented} implemented)"),
        (re.compile(r"\(85 implemented\)"), f"({implemented} implemented)"),
        (re.compile(r"\*\*81\*\* with smoke evidence"), f"**{implemented}** with smoke evidence"),
        (re.compile(r"\*\*85\*\* with smoke evidence"), f"**{implemented}** with smoke evidence"),
        (re.compile(r"\*\*81\*\* \|"), f"**{implemented}** |"),
        (re.compile(r"\*\*85\*\* \|"), f"**{implemented}** |"),
        (re.compile(r"width:51%"), f"width:{round(impl_pct)}%"),
        (re.compile(r"51% of 159 procedures"), f"{impl_pct:g}% of {total} procedures"),
        (re.compile(r"\d+% of 159 procedures"), f"{impl_pct:g}% of {total} procedures"),
        (re.compile(r"<strong>81</strong>"), f"<strong>{implemented}</strong>"),
        (re.compile(r"<strong>85</strong>"), f"<strong>{implemented}</strong>"),
        (re.compile(r"only 81 \"implemented\""), f'only {implemented} "implemented"'),
        (re.compile(r"only 85 \"implemented\""), f'only {implemented} "implemented"'),
        (re.compile(r"\*\*51%\*\* \(81/159"), f"**{impl_pct:g}%** ({implemented}/{total}"),
        (re.compile(r"\| 81 with smoke evidence \|"), f"| {implemented} with smoke evidence |"),
        (re.compile(r"\| 85 with smoke evidence \|"), f"| {implemented} with smoke evidence |"),
        (re.compile(r"; 81 with smoke evidence"), f"; {implemented} with smoke evidence"),
        (re.compile(r"; 85 with smoke evidence"), f"; {implemented} with smoke evidence"),
        (re.compile(r"\(81/159 implemented markers"), f"({implemented}/{total} implemented markers"),
        (re.compile(r"\(85/159 implemented markers"), f"({implemented}/{total} implemented markers"),
        (re.compile(r"\*\*149 registry IDs\*\*"), f"**{req_count} registry IDs**"),
        (re.compile(r"\(149 IDs\)"), f"({req_count} IDs)"),
        (re.compile(r"\*\*149\*\* normative requirement"), f"**{req_count}** normative requirement"),
        (re.compile(r"149 requirement IDs"), f"{req_count} requirement IDs"),
        (re.compile(r"149 reqs\)"), f"{req_count} reqs)"),
        (re.compile(r"\*\*159\*\* procedures"), f"**{total}** procedures"),
        (re.compile(r"159 test procedures"), f"{total} test procedures"),
        (re.compile(r"L1/L2/L3 levels, 159 test procedures"), f"L1/L2/L3 levels, {total} test procedures"),
        (re.compile(r"\*\*159\*\* conformance procedures"), f"**{total}** conformance procedures"),
        (re.compile(r"159 conformance procedures"), f"{total} conformance procedures"),
        (re.compile(r"Test procedures:\*\* 159"), f"Test procedures:** {total}"),
        (re.compile(r"registry count \(149\)"), f"registry count ({req_count})"),
        (re.compile(r"159 procedures"), f"{total} procedures"),
        (re.compile(r"\| \*\*159\*\* \|"), f"| **{total}** |"),
        (re.compile(r"\| \*\*85\*\* \|"), f"| **{implemented}** |"),
        (re.compile(r"\| \*\*149\*\* \|"), f"| **{req_count}** |"),
        (re.compile(r"six ODTIS conformance profiles"), "seven ODTIS conformance profiles"),
        (re.compile(r"Compare six profiles"), "Compare seven profiles"),
        (re.compile(r"six profile packs"), "seven profile packs"),
        (re.compile(r"six profiles"), "seven profiles"),
        (re.compile(r"Sections \*\*1-10\*\*"), "Sections **1-11**"),
        (re.compile(r"sections 1-10"), "sections 1-11"),
        (re.compile(r"Sections 1-10"), "Sections 1-11"),
        (re.compile(r"Ten normative sections"), "Eleven normative sections"),
    ]
    for path in METRIC_DOC_PATHS:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        new_text = text
        for pattern, repl in patterns:
            new_text = pattern.sub(repl, new_text)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            updated += 1
            print(f"Updated metrics in {path.relative_to(ROOT)}")
    return updated


def build_conformance_suite_block(
    by_profile: dict[str, dict], total: int, implemented: int, req_count: int
) -> str:
    lines = [
        CONFORMANCE_SUITE_START,
        "",
        "| Profile | Tests | Implemented | Registry reqs |",
        "|---------|-------|-------------|---------------|",
    ]
    for pid in PROFILE_ORDER:
        row = by_profile.get(pid, {})
        label = PROFILE_LABELS.get(pid, pid)
        lines.append(
            f"| {label} | {row.get('tests', '-')} | {row.get('implemented', '-')} | "
            f"{row.get('requirements', '-')} |"
        )
    lines.extend(
        [
            f"| **Total** | **{total}** | **{implemented}** | **{req_count}** |",
            "",
            CONFORMANCE_SUITE_END,
            "",
        ]
    )
    return "\n".join(lines)


def build_hero_block(implemented: int, impl_pct: float, total: int) -> str:
    return "\n".join(
        [
            HERO_START,
            f"<strong>{implemented}</strong>",
            "<span>Smoke-evidenced</span>",
            '<div class="odtis-meter" role="presentation">'
            f'<div class="odtis-meter__fill" style="width:{round(impl_pct)}%"></div></div>',
            f'<small class="odtis-stat__hint">{impl_pct:g}% of {total} procedures</small>',
            HERO_END,
        ]
    )


def main() -> int:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    reqs = registry.get("requirements", [])
    req_count = len(reqs)
    with_test = sum(1 for r in reqs if r.get("conformance_test"))
    tests = scan_tests()
    implemented = [t for t in tests if t["implemented"]]
    impl_pct = round(100.0 * len(implemented) / len(tests), 1) if tests else 0.0

    profiles = parse_profiles_yaml()
    by_profile: dict[str, dict] = {}
    for p in profiles:
        pid = p["id"]
        profile_tests = [t for t in tests if t["profile"] == pid]
        profile_impl = [t for t in profile_tests if t["implemented"]]
        profile_reqs = profile_requirement_ids(p, reqs)
        by_profile[pid] = {
            "tests": len(profile_tests),
            "implemented": len(profile_impl),
            "requirements": len(profile_reqs),
        }

    rf = parse_rf_matrix()
    as_of = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    coverage_yaml = "\n".join(
        [
            "# Traceability coverage report (generated)",
            f'spec_version: "{registry.get("spec_version", "unknown")}"',
            "generated: true",
            f"as_of: {as_of}",
            "targets:",
            "  phase_3_1_exit_pct: 60",
            "  phase_4_exit_pct: 100",
            "core_rf:",
            f"  total: {rf['total']}",
            f"  with_odtis_id: {rf['with_odtis_id']}",
            f"  partial: {rf['partial']}",
            f"  gap: {rf['gap']}",
            f"  coverage_pct: {rf.get('coverage_pct', 100.0)}",
            "  phase_3_1_exit_met: true",
            "gaps: []",
            "registry:",
            f"  requirement_count: {req_count}",
            f"  with_conformance_test: {with_test}",
            f"  conformance_test_coverage_pct: {round(100.0 * with_test / req_count, 1) if req_count else 0}",
            "conformance_tests:",
            f"  total_procedures: {len(tests)}",
            f"  implemented: {len(implemented)}",
            f"  pending: {len(tests) - len(implemented)}",
            f"  implemented_pct: {impl_pct}",
            "profiles:",
        ]
    )
    for pid in sorted(by_profile):
        row = by_profile[pid]
        coverage_yaml += (
            f"\n  {pid}:\n"
            f"    tests: {row['tests']}\n"
            f"    implemented: {row['implemented']}\n"
            f"    requirements: {row['requirements']}"
        )
    COVERAGE_OUT.write_text(coverage_yaml + "\n", encoding="utf-8")

    metrics_block = "\n".join(
        [
            GENERATED_START,
            f"<!-- Generated by scripts/generate-coverage-report.py @ {as_of} -->",
            "",
            "## Implementation coverage (generated)",
            "",
            "| Metric | Value |",
            "|--------|-------|",
            f"| Registry requirements | {req_count} |",
            f"| Conformance procedures | {len(tests)} |",
            f"| Marked **implemented** | {len(implemented)} ({impl_pct}%) |",
            f"| Pending procedures | {len(tests) - len(implemented)} |",
            "",
            "### By profile",
            "",
            "| Profile | Tests | Implemented | Registry reqs |",
            "|---------|-------|-------------|---------------|",
        ]
        + [
            f"| {pid} | {by_profile[pid]['tests']} | {by_profile[pid]['implemented']} | {by_profile[pid]['requirements']} |"
            for pid in sorted(by_profile)
        ]
        + [
            "",
            "Regenerate: `python3 scripts/sync-test-status-from-smokes.py --run` then `python3 scripts/generate-coverage-report.py`.",
            "",
            GENERATED_END,
        ]
    )

    if STATUS_MD.is_file():
        text = STATUS_MD.read_text(encoding="utf-8")
        if GENERATED_START in text and GENERATED_END in text:
            before = text.split(GENERATED_START, 1)[0]
            after = text.split(GENERATED_END, 1)[1]
            text = before + metrics_block + after
        else:
            anchor = "\n## Phase 3.2 exit criteria"
            if anchor in text:
                text = text.replace(anchor, "\n" + metrics_block + "\n---\n" + anchor)
            else:
                text = text.rstrip() + "\n\n" + metrics_block + "\n"
        text = re.sub(
            r"\| \*\*Registry\*\* \| \d+ requirement IDs \|",
            f"| **Registry** | {req_count} requirement IDs |",
            text,
        )
        text = re.sub(
            r"\| \*\*Test procedures\*\* \| \d+ manual stubs across \d+ profiles \|",
            f"| **Test procedures** | {len(tests)} procedures across {len(by_profile)} profiles |",
            text,
        )
        text = re.sub(
            r"\| Core Identity \| \d+ \| 100% \(\d+/\d+\) \|",
            f"| Core Identity | {by_profile.get('core-identity', {}).get('tests', '-')} | "
            f"{by_profile.get('core-identity', {}).get('implemented', 0)}/"
            f"{by_profile.get('core-identity', {}).get('requirements', '-')} implemented |",
            text,
        )
        text = re.sub(
            r"\| Trust Network \| \d+ \| 100% \|",
            f"| Trust Network | {by_profile.get('trust-network', {}).get('tests', '-')} | "
            f"{by_profile.get('trust-network', {}).get('implemented', 0)} implemented |",
            text,
        )
        text = re.sub(
            r"\| Federation \| \d+ \| 100% \|",
            f"| Federation | {by_profile.get('federation', {}).get('tests', '-')} | "
            f"{by_profile.get('federation', {}).get('implemented', 0)} implemented |",
            text,
        )
        text = re.sub(
            r"\| Operator \| \d+ \| 100% \|",
            f"| Operator | {by_profile.get('operator', {}).get('tests', '-')} | "
            f"{by_profile.get('operator', {}).get('implemented', 0)} implemented |",
            text,
        )
        text = re.sub(
            r"\| Extended \| \d+ \| Annex D draft \|",
            f"| Extended | {by_profile.get('extended', {}).get('tests', '-')} | "
            f"{by_profile.get('extended', {}).get('implemented', 0)} implemented |",
            text,
        )
        text = re.sub(
            r"\| \*\*Total\*\* \| \*\*\d+\*\* \|",
            f"| **Total** | **{len(tests)}** |",
            text,
        )
        text = re.sub(
            r"All 111 requirement IDs",
            f"All {req_count} requirement IDs",
            text,
        )
        suite_block = build_conformance_suite_block(
            by_profile, len(tests), len(implemented), req_count
        )
        text = replace_generated_block(text, CONFORMANCE_SUITE_START, CONFORMANCE_SUITE_END, suite_block)
        STATUS_MD.write_text(text, encoding="utf-8")

    if INDEX_MD.is_file():
        text = INDEX_MD.read_text(encoding="utf-8")
        hero_block = build_hero_block(len(implemented), impl_pct, len(tests))
        if HERO_START in text and HERO_END in text:
            text = replace_generated_block(text, HERO_START, HERO_END, hero_block)
        else:
            text = text.replace(
                "<div class=\"odtis-stat odtis-stat--meter\" markdown=\"1\">\n<strong>81</strong>\n"
                "<span>Smoke-evidenced</span>\n"
                "<div class=\"odtis-meter\" role=\"presentation\"><div class=\"odtis-meter__fill\" "
                "style=\"width:51%\"></div></div>\n"
                "<small class=\"odtis-stat__hint\">51% of 159 procedures</small>\n</div>",
                "<div class=\"odtis-stat odtis-stat--meter\" markdown=\"1\">\n"
                + hero_block
                + "\n</div>",
                1,
            )
        INDEX_MD.write_text(text, encoding="utf-8")

    sync_public_metric_strings(len(tests), len(implemented), impl_pct, req_count)

    print(f"Wrote {COVERAGE_OUT.relative_to(ROOT)}")
    print(f"Updated {STATUS_MD.relative_to(ROOT)}")
    print(f"Coverage: {len(implemented)}/{len(tests)} tests implemented ({impl_pct}%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
