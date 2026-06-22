# ODTIS review cycle 1 - `0.9.0-draft`

**Status:** open 
**Opened:** 2026-06-12 
**Comment period closes:** 2026-06-26 (14 days) 
**Target version after close:** `0.9.x-draft` stabilization

**Submit feedback:** [Feedback channels](FEEDBACK.md) | **Governance:** [Project hub](README.md) | **Project:** [Project hub](../project/README.md)

---

## Purpose

Collect external feedback on ODTIS `0.9.0-draft` before promoting to stabilized `0.9.x-draft` and Phase 4 (`1.0.0` track).

**In scope:** normative clarity, Annex A completeness, conformance testability, profile claims, sandbox L2 experience.
**Out of scope:** Book 2 redaction (informative only), production deploy to `odtis.org` (separate track).

---

## How to participate

| Channel | Use for |
|---------|---------|
| GitHub **ODTIS clarification** | Editorial / non-normative fixes |
| GitHub **ODTIS RFC** | MUST/SHOULD changes |
| GitHub **ODTIS sandbox report** | L1/L2 against live `--target` |
| Email stewards | If GitHub unavailable (see [Feedback channels](FEEDBACK.md)) |

Decisions are recorded in [Review Log (YAML)](REVIEW-LOG.yaml).

---

## Steward-seeded items (comment welcome)

These items open the cycle; external reviewers may add new issues.

| ID | Type | Topic | File |
|----|------|-------|------|
| FB-001 | clarification | ODTIS-0331 test linkage | [FB-001 test linkage](review/clarify-001-5.1.4-test-linkage.md) |
| FB-002 | rfc | Federation depth (IG-02) | [Federation interoperability RFC](rfc/2026-06-12-federation-interoperability.md) |
| FB-003 | clarification | HA metrics boundary (IG-03) | [FB-003 HA boundary](review/clarify-002-ha-informative-boundary.md) |
| FB-004 | clarification | Autodiscovery SHOULD (ODTIS-4.6.1) | [FB-004 autodiscovery](review/clarify-003-autodiscovery-should.md) |
| FB-005 | sandbox | L2 report template (accepted; live reports welcome) | [L2 report template](../conformance/sandbox/L2-REPORT-TEMPLATE.md) |

All steward-seeded items **accepted** as of 2026-06-12. External comments may still add new issues until close.

**Close procedure:** [Review close checklist](REVIEW-CYCLE-1-CLOSE.md)

---

## Steward readiness (internal)

| Track | Status |
|-------|--------|
| Section completeness 2-10 | Done ([Section review matrix](SECTION-REVIEW.md)) |
| FB-001 .. FB-005 | Accepted ([Review Log (YAML)](REVIEW-LOG.yaml)) |
| L1 conformance | PASS |
| Live sandbox L2 reports | Awaiting operators |

---

## Review checklist (maintainers)

At comment period close (see [Review close checklist](REVIEW-CYCLE-1-CLOSE.md)):

- [ ] Triage all `odtis` labeled issues
- [ ] Accept / reject / defer each RFC in `REVIEW-LOG.yaml`
- [ ] Update registry + spec for accepted normative changes
- [ ] Bump to `0.9.1-draft` or document deferrals
- [ ] Mark Book 2 cross-review external sign-off if no open MUST conflicts
- [ ] Check External review cycle 1 in all spec footers
- [ ] Set `review_period_open: false` in `REVIEW-LOG.yaml`

---

## Open issues on GitHub

When the repo is pushed and `gh` is available:

```bash
./scripts/open-review-issues.sh --dry-run # preview
./scripts/open-review-issues.sh # create issues
```

Until then, copy bodies from [Review](../review/) into GitHub manually.

---

## Related

- [Feedback channels](FEEDBACK.md)
- [Book 2 cross-review](BOOK2-CROSS-REVIEW.md)
- [Build plan](../PLAN-PHASES.md) Phase 3.2
