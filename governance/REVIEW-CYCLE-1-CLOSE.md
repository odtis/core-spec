# Review cycle 1 - close checklist

**Spec version:** `0.9.0-draft` 
**Comment period closes:** 2026-06-26 
**Target after close:** `0.9.1-draft` (stabilization) or documented deferrals

**Project hub:** [Project hub](../project/README.md) | **Parent:** [External review cycle 1](REVIEW-CYCLE-1.md) | **Decisions:** [Review Log (YAML)](REVIEW-LOG.yaml)

---

## Steward readiness (pre-close)

Work completed before external comment period ends. Does **not** close the cycle by itself.

| Item | Status | Evidence |
|------|--------|----------|
| Sections 2-10 structural review (C1-C7) | Done | [Section review matrix](SECTION-REVIEW.md); `validate-section-completeness.py` PASS |
| Section 1 meta review | Done | Phase 3.2 checklist in [Section 1 - Scope and conformance](../spec/01-scope-conformance/SPEC.md) |
| FB-001 scope enforcement (5.1.4) | Accepted | [FB-001 test linkage](review/clarify-001-5.1.4-test-linkage.md) |
| FB-002 federation depth | Accepted | 6 IDs; registry + tests updated |
| FB-003 HA boundary (section 10) | Accepted | Informative note in section 10.4 |
| FB-004 autodiscovery SHOULD (section 4) | Accepted | section 4.4.3 + Annex A note |
| FB-005 L2 report template | Accepted | [L2 report template](../conformance/sandbox/L2-REPORT-TEMPLATE.md) |
| L1 conformance | PASS | `./conformance/run.sh` (8/8) |
| Registry / Annex C | 149/149 | `validate-standards-mapping.py` |
| Annex A OpenAPI | Frozen | [Annex A freeze record](../annexes/A-openapi-registry/FREEZE.md) |

**Still open for external input:** live sandbox L2 reports, Book 2 MUST conflicts, new RFCs from adopters.

---

## At comment period close (maintainers)

Run in order:

### 1. Triage external feedback

- [ ] List all GitHub issues labeled `odtis` opened during the period
- [ ] Classify each: clarification | RFC | sandbox | defer
- [ ] Append new entries to [Review Log (YAML)](REVIEW-LOG.yaml)
- [ ] Accept / reject / defer each item with dated resolution

### 2. Apply accepted normative changes

- [ ] Update affected `spec/*/SPEC.md` prose
- [ ] Update [Requirements registry](../registry/requirements.json) if IDs added/changed
- [ ] Regenerate Annex C if registry changed: `python3 scripts/generate-standards-mapping.py`
- [ ] Add or update conformance test stubs; run `python3 scripts/build-conformance-manifest.py`
- [ ] Run `./conformance/run.sh` and fix any FAIL

### 3. Editorial and index sync

- [ ] Run `python3 scripts/generate-site-indexes.py`
- [ ] Update [Changelog](/CHANGELOG/) for accepted changes
- [ ] Update [Project status](../site/STATUS.md) blockers and exit criteria

### 4. Book 2 cross-review

- [ ] Re-read [Book 2 cross-review](BOOK2-CROSS-REVIEW.md) open rows (CR-02 operator UI, etc.)
- [ ] Mark external sign-off or log remaining informative-only gaps

### 5. Close the cycle in metadata

- [ ] Set `review_period_open: false` in [Review Log (YAML)](REVIEW-LOG.yaml)
- [ ] Set `Status: closed` in [External review cycle 1](REVIEW-CYCLE-1.md) with close date
- [ ] Bump [VERSION](/VERSION) to `0.9.1-draft` **if** any normative or registry change landed; otherwise document "no bump" rationale
- [ ] Run `python3 scripts/sync-spec-version.py` if version bumped

### 6. Mark section footers

In each `spec/*/SPEC.md` Phase 3.2 checklist, check:

```markdown
- [x] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))
```

Sections: 1, 2, 3, 4, 5, 7, 8, 9, 10 (and 6 if not already checked).

Update [Section review matrix](SECTION-REVIEW.md) section 1 row: External review cycle 1 -> Done.

---

## Deferral rules

| Outcome | Action |
|---------|--------|
| Clarification accepted, no MUST change | Spec note only; may stay on `0.9.0-draft` until next cycle |
| RFC accepted with new IDs | Bump minor draft (`0.9.1-draft`); full L1 regen |
| RFC rejected | Log in REVIEW-LOG; no spec change |
| Deferred to Phase 4 | Log with target phase; do not block 0.9.x stabilization if non-blocking |

---

## Out of scope for cycle 1 close

These tracks proceed independently:

- Zenodo DOI ([Zenodo release checklist](../publication/zenodo/RELEASE-CHECKLIST.md))
- `digitaltrustinfrastructure.org` deploy
- L2 executable automation (stubs remain valid for 0.9.x)
- Annex D merge into main registry (Phase 4)

---

## Quick validation before tagging

```bash
# from repository root
python3 scripts/validate-section-completeness.py
./conformance/run.sh
python3 scripts/generate-site-indexes.py
# Optional: mkdocs build
./scripts/build-site.sh
```

All must PASS before publishing a post-close snapshot.
