#!/usr/bin/env python3
"""Generate normative prose blocks in spec/11-reliance-profiles/SPEC.md from registry."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry/requirements.json"
ANNEX = ROOT / "annexes/E-reliance-profiles/sub-modules.yaml"
SPEC = ROOT / "spec/11-reliance-profiles/SPEC.md"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

REQ_TITLES: dict[str, str] = {
    "ODTIS-0701": "Relying party identification",
    "ODTIS-0702": "Purpose binding",
    "ODTIS-0703": "Assurance metadata",
    "ODTIS-0704": "Audit evidence reference",
    "ODTIS-0705": "Recourse path",
    "ODTIS-0706": "Revocation and step-up triggers",
    "ODTIS-0707": "No-weakening rule",
    "ODTIS-0708": "Conformance sub-module declaration",
    "ODTIS-0710": "Agent identifier resolution",
    "ODTIS-0711": "Signed agent mandate",
    "ODTIS-0712": "Mandate revocation freshness",
    "ODTIS-0713": "Human anchor for high-risk agent actions",
    "ODTIS-0715": "Long-lived credential algorithm profile",
    "ODTIS-0716": "Post-quantum acceptance criteria",
    "ODTIS-0717": "Cryptographic bill of materials",
    "ODTIS-0719": "Lifecycle revocation SLA",
    "ODTIS-0720": "Unified revocation evidence",
    "ODTIS-0721": "Orphan credential scanning",
    "ODTIS-0723": "Document capture mode declaration",
    "ODTIS-0724": "Capture-channel integrity evidence",
    "ODTIS-0725": "Provider validation disclosure",
    "ODTIS-0727": "Liveness decision metadata",
    "ODTIS-0728": "Liveness verdict reuse prohibition",
    "ODTIS-0729": "Accessible liveness fallback",
    "ODTIS-0731": "Audience-bound disclosure sets",
    "ODTIS-0732": "Offline verdict reconstruction",
    "ODTIS-0733": "Unauthorized disclosure refusal",
    "ODTIS-0735": "External standard maturity gate",
    "ODTIS-0736": "Capa B controls before production reliance",
    "ODTIS-0737": "Conformance lab before promotion",
    "ODTIS-0739": "Multi-eID acceptance matrix",
    "ODTIS-0740": "Authentication versus authorization",
    "ODTIS-0741": "Wrongful-rejection recourse",
    "ODTIS-0743": "Portable assurance metadata",
    "ODTIS-0744": "Step-up before assurance reuse",
    "ODTIS-0745": "Non-portable assurance re-verification",
    "ODTIS-0747": "Fraud decision trust-event chain",
    "ODTIS-0748": "Fraud liability and sharing basis",
    "ODTIS-0749": "Wrongful block recourse",
    "ODTIS-0751": "CIP reliance decision record",
    "ODTIS-0752": "Institutional CIP reliance certification",
    "ODTIS-0753": "Protocol-agnostic CIP presentation",
    "ODTIS-0755": "Travel touchpoint reliance declaration",
    "ODTIS-0756": "Journey-bound attribute reuse",
    "ODTIS-0757": "Cross-border travel recourse",
    "ODTIS-0759": "Supply-chain role attestation",
    "ODTIS-0760": "Active-exploit trust-event chain",
    "ODTIS-0761": "Post-market monitoring documentation",
    "ODTIS-0763": "DPI blast-radius authorization",
    "ODTIS-0764": "Trust Resilience Evidence Pack",
    "ODTIS-0765": "Transparent DPI incident reporting",
    "ODTIS-0767": "Sovereign chain accountability",
    "ODTIS-0768": "No institutional trust transfer",
    "ODTIS-0771": "Law-enforcement biometric decision record",
    "ODTIS-0772": "False-match mitigation and recourse",
}


def parse_modules(text: str) -> list[dict]:
    modules: list[dict] = []
    current: dict | None = None
    in_sub = False
    for line in text.splitlines():
        if line.strip() == "sub_modules:":
            in_sub = True
            continue
        if in_sub and line.strip().startswith("composition_rules:"):
            break
        if not in_sub:
            continue
        m_id = re.match(r"^- id: (R-[\w-]+)\s*$", line)
        if m_id:
            if current:
                modules.append(current)
            current = {"id": m_id.group(1), "title": "", "tier": 0, "min_phase": 1, "anchors": [], "requirements": []}
            continue
        if current is None:
            continue
        m_title = re.match(r"^\s+title: (.+)$", line)
        if m_title:
            current["title"] = m_title.group(1).strip()
            continue
        m_tier = re.match(r"^\s+tier: (\d+)$", line)
        if m_tier:
            current["tier"] = int(m_tier.group(1))
            continue
        m_phase = re.match(r"^\s+min_deployment_phase: (\d+)$", line)
        if m_phase:
            current["min_phase"] = int(m_phase.group(1))
            continue
        m_anchors = re.match(r"^\s+anchors: \[(.+)\]\s*$", line)
        if m_anchors:
            current["anchors"] = [a.strip() for a in m_anchors.group(1).split(",")]
            continue
        m_reqs = re.match(r"^\s+requirements: \[(.+)\]\s*$", line)
        if m_reqs:
            current["requirements"] = [r.strip() for r in m_reqs.group(1).split(",")]
    if current:
        modules.append(current)
    return modules


def bold_keyword(text: str, keyword: str) -> str:
    """Bold the RFC 2119 keyword once in the requirement sentence."""
    if keyword not in text:
        return text
    return text.replace(keyword, f"**{keyword}**", 1)


def req_block(req: dict, mod: dict) -> list[str]:
    rid = req["id"]
    title = REQ_TITLES.get(rid, rid)
    kw = req.get("keyword", "MUST")
    text = bold_keyword(req["text"], kw)
    trace = req.get("trace_informative", "").split(" (manuelmerida.io")[0]
    short = req["text"][:90].rstrip()
    return [
        f"### {rid} - {title}",
        "",
        text,
        "",
        f"**Trace (informative):** {trace}",
        f"**Sub-module:** {mod['id']} | **Min deployment phase:** {mod['min_phase']}",
        f"**Conformance test:** Exercise `{rid}` against declared reliance profile; record evidence that: {short}…",
        "",
        "---",
        "",
    ]


def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    reqs = [r for r in data["requirements"] if r.get("section") == "11-reliance-profiles"]
    by_id = {r["id"]: r for r in reqs}
    modules = parse_modules(ANNEX.read_text(encoding="utf-8"))

    lines = [
        "---",
        'title: "Section 11: Reliance Extensions (Capa B)"',
        "description: Normative Capa B governance overlays for relying-party decisions, assurance metadata, audit evidence, recourse, and revocation.",
        "---",
        "",
        "# 11 Reliance Extensions (Capa B)",
        "",
        '<div class="odtis-spec-meta" markdown="1">',
        "",
        "| Field | Value |",
        "|-------|-------|",
        "| **Status** | review draft - Phase 3.2 |",
        f"| **Spec version** | {VERSION} |",
        f"| **Registry IDs** | ODTIS-0701 - ODTIS-0772 ({len(reqs)} requirements) |",
        "| **Profile** | `reliance-extensions` |",
        "| **Domain** | ODTIS-0007 |",
        "| **Annex** | E-reliance-profiles |",
        "",
        "</div>",
        "",
        "---",
        "",
        "## 11.1 Scope",
        "",
        "Reliance Extensions are **optional Capa B governance overlays** on the two-layer ODTIS model. "
        "Where Core Identity, Trust Network, and Federation define *how* trust signals are produced and exchanged (Capa A), "
        "Reliance Extensions define *who may rely* on a signal, *for what purpose*, *with what assurance*, "
        "*with what audit evidence*, and *with what recourse*.",
        "",
        "Each sub-module specializes the **R-Base reliance schema** (`ODTIS-0701`-`ODTIS-0708`) and "
        "**MUST NOT weaken** any Core Identity, Trust Network, Federation, or Operator requirement (`ODTIS-0707`).",
        "",
        "Sub-modules are declared independently in conformance statements (`ODTIS-0708`). "
        "Phase gates: [Annex E activation matrix](/annexes/E-reliance-profiles/activation.yaml).",
        "",
        "---",
        "",
        "## 11.2 R-Base reliance schema",
        "",
        "Every Reliance Extension sub-module inherits the base schema below. "
        "These requirements apply whenever any Reliance Extension sub-module is claimed.",
        "",
    ]

    base = next(m for m in modules if m["id"] == "R-Base")
    for rid in base["requirements"]:
        lines.extend(req_block(by_id[rid], base))

    lines.extend(
        [
            "## 11.3 Reliance Extension sub-modules",
            "",
            "The following sub-modules extend R-Base for specific reliance contexts. "
            "Claiming a sub-module requires satisfying its requirements in addition to R-Base.",
            "",
        ]
    )

    for mod in modules:
        if mod["id"] == "R-Base":
            continue
        tier_label = {1: "Tier 1 (draft normative)", 2: "Tier 2 (preview)", 3: "Tier 3 (preview)"}.get(
            mod["tier"], f"Tier {mod['tier']}"
        )
        anchors = ", ".join(mod["anchors"][:4])
        if len(mod["anchors"]) > 4:
            anchors += ", …"
        lines.extend(
            [
                f"### 11.3.{mod['id']} - {mod['title']}",
                "",
                f"*{tier_label}; minimum deployment phase {mod['min_phase']}.* "
                f"External anchors (informative): {anchors}.",
                "",
                f"Catalog: [Annex E sub-modules](/annexes/E-reliance-profiles/sub-modules.yaml).",
                "",
            ]
        )
        for rid in mod["requirements"]:
            if rid in by_id:
                lines.extend(req_block(by_id[rid], mod))

    lines.extend(
        [
            "## 11.4 Sub-module activation matrix",
            "",
            "Reliance Extension sub-modules MUST NOT be claimed in production before their minimum deployment phase. "
            "Tier 2 and Tier 3 sub-modules are preview profiles intended for national-scale or sensitive deployments.",
            "",
            "| Sub-module | Tier | Min phase | Requirement IDs |",
            "|------------|------|-----------|-----------------|",
        ]
    )
    for mod in modules:
        if mod["id"] == "R-Base":
            continue
        ids = ", ".join(f"`{r}`" for r in mod["requirements"])
        lines.append(f"| {mod['id']} | {mod['tier']} | {mod['min_phase']} | {ids} |")

    lines.extend(
        [
            "",
            "Machine-readable rules: [Activation (YAML)](/annexes/E-reliance-profiles/activation.yaml).",
            "",
            "---",
            "",
            "## 11.5 Requirement index",
            "",
            "<!-- Placeholder: run generate-spec-section-indexes.py -->",
            "",
            "---",
            "",
            "## Document history",
            "",
            "| Version | Date | Change |",
            "|---------|------|--------|",
            f"| 0.9.0-draft | 2026-06-23 | Initial Reliance Extensions catalog ({len(reqs)} IDs) from DTI editorial analysis |",
            f"| {VERSION} | 2026-06-23 | Normative prose for all {len(reqs)} requirements; section 11 completeness gate |",
            "",
            "**Phase 3.2 review checklist (11).**",
            "",
            "- [x] R-Base reliance schema normative prose (ODTIS-0701-0708)",
            "- [x] 16 sub-modules with normative requirement blocks",
            "- [x] Requirement index matches registry",
            "- [x] Conformance test stub per ID",
            "- [ ] Annex C external-standard anchors merged",
            "- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))",
            "",
        ]
    )

    SPEC.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {SPEC.relative_to(ROOT)} ({len(reqs)} normative blocks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
