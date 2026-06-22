# Contributing to ODTIS

Thank you for helping build the Open Digital Trust Infrastructure Specification.

**Governance hub:** [Project hub](README.md) | **Project:** [Project hub](../project/README.md) | **Feedback:** [Feedback channels](FEEDBACK.md) | **Community:** [Code of conduct](../site/CODE-OF-CONDUCT.md)

---

## Choose your contribution type

| Change type | Path | Review |
|-------------|------|--------|
| Clarification (no MUST change) | [Feedback channels](FEEDBACK.md) | Stewards + `REVIEW-LOG.yaml` |
| Normative MUST/SHOULD change | [RFC template](RFC-TEMPLATE.md) | RFC comment period |
| Editorial / typo in spec | PR to `spec/` | Maintainer review |
| Conformance test stub | `conformance/tests/` | + registry link |
| Sandbox L2 experience | [L2 report template](../conformance/sandbox/L2-REPORT-TEMPLATE.md) | Review cycle |

---

## Before you start

1. Read [Project hub](../) and [Build plan](/PLAN-PHASES/)
2. Understand normative keywords (RFC 2119) in [Section 1 - Scope and conformance](../spec/01-scope-conformance/SPEC.md)
3. Check [Versioning policy](VERSIONING.md) and [Spec lifecycle stages](SPEC-STAGES.md) for release stage

---

## What to edit where

| Change | Edit | Do not edit |
|--------|------|-------------|
| Normative MUST/SHOULD text | `spec/*/SPEC.md` | P18 (after migration complete) |
| Requirement ID metadata | `registry/requirements.json` | Auto-only without PR review |
| OpenAPI contracts | `annexes/A-openapi-registry/` | Informal docs in Book 3 |
| RF traceability | `traceability/` + upstream matrix | - |
| Site pages | `site/`, `governance/`, `conformance/*.md` | Generated blocks marked `GENERATED` |

---

## Workflow

1. Open an issue describing the gap (reference RF-xx or ODTIS ID if applicable)
2. Branch from `main`
3. Edit spec + registry + [Changelog](/CHANGELOG/) under `[Unreleased]`
4. Run validation:

```bash
cd odtis
python3 scripts/validate-registry.py
python3 scripts/validate-section-completeness.py
./conformance/run.sh
```

5. Open PR with:
    - Summary of normative impact
 - List of affected ODTIS IDs
 - Checklist item from relevant `spec/*/SPEC.md`

---

## Style

- **English only** for normative and governance text - see [Language policy](LANGUAGE.md)
- One requirement per ODTIS ID
- Use MUST/SHOULD/MAY consistently
- Cross-reference Annexes and Book 2 as **informative** unless elevating to MUST
- Use ASCII hyphens in site markdown (no em dash) per [Language policy](LANGUAGE.md)

---

## Language policy

ODTIS is an international open standard; **English is the canonical language** for specification prose, registry metadata, OpenAPI descriptions, conformance tests, and governance docs. Narrative translations (Book 1 ES, jurisdiction playbooks) live outside `odtis/` and do not override normative MUST text.

---

## Related

| Document | Purpose |
|----------|---------|
| [Maintainers](MAINTAINERS.md) | Editors and escalation |
| [External review cycle 1](REVIEW-CYCLE-1.md) | Active external review |
| [Getting started](../site/GETTING-STARTED.md) | Implementer path (read-only contributors) |
