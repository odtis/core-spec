# ODTIS external feedback (Phase 3.2.4)

**Status:** open - [Review cycle 1](REVIEW-CYCLE-1.md) (**2026-06-12 -> 2026-06-26**) 
**Audience:** operators, RPs, integrators, regulators, auditors

**Governance hub:** [Project hub](README.md) | **Project:** [Project hub](../project/README.md)

!!! tip "Not sure which channel?"
    - **Wording unclear, no MUST change** -> clarification (below)
    - **New or changed MUST** -> RFC
    - **Ran sandbox L2** -> implementation experience report

---

## What to comment on

| Area | Examples |
|------|----------|
| Normative clarity | Untestable MUST, ambiguous scope |
| Annex A | Missing operations, schema fields |
| Conformance | Untestable or missing procedures |
| Profiles | Profile composition, deployment phase claims |
| Book 2 alignment | Descriptive gaps (informative) |

---

## How to submit

### 1. Clarification (non-normative)

Use the **ODTIS clarification** GitHub issue template (`.github/ISSUE_TEMPLATE/odtis-clarification.yml`) or email stewards with:

- Section / ODTIS ID / Annex A `operationId`
- Observed text
- Proposed clarification

Decisions are logged in [Review Log (YAML)](REVIEW-LOG.yaml). Steward seeds: [Review templates index](review/README.md).

### 2. Normative change (RFC)

Use [RFC template](RFC-TEMPLATE.md) and the **ODTIS RFC** issue template. Store drafts under [RFC drafts index](rfc/README.md) for:

- New MUST or changed MUST
- Profile definition changes
- Breaking Annex A changes

**Process:** publish RFC -> 14-day comment period -> maintainer decision -> registry + spec update + CHANGELOG.

### 3. Implementation experience

Sandbox operators SHOULD attach:

- `conformance-statement.yaml`
- L2 JSON report from [Run Sandbox Check script](../conformance/sandbox/run-sandbox-check.sh)
- Profile and phase declared

Use the **ODTIS sandbox conformance report** issue template or [L2 report template](../conformance/sandbox/L2-REPORT-TEMPLATE.md).

---

## Cycle 1 items (reference)

| ID | Type | Topic |
|----|------|-------|
| FB-001 | clarification | ODTIS-0331 test linkage |
| FB-002 | rfc | Federation depth |
| FB-003 | clarification | HA metrics boundary |
| FB-004 | clarification | Autodiscovery SHOULD |
| FB-005 | sandbox | L2 report template |

Close checklist (maintainers): [Review close checklist](REVIEW-CYCLE-1-CLOSE.md)

---

## Related

| Document | Purpose |
|----------|---------|
| [Contributing guide](CONTRIBUTING.md) | PR workflow |
| [Conformance FAQ](../conformance/FAQ.md) | Conformance questions |
| [Project status](../site/STATUS.md) | Review cycle status |
