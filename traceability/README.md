# ODTIS traceability

Links functional requirements (RF) to ODTIS requirement IDs and spec sections.

---

## Authoritative matrix (workspace)

The master traceability matrix lives at:

**[Traceability Matrix](https://github.com/finnectos/venezuela/blob/main/docs/sources/papers/TRACEABILITY-MATRIX.md)**

Columns: RF/RNF -> Paper -> Book 2 chapter -> ODTIS ID -> Status

This directory holds ODTIS-local views and automation.

---

## Local files

| File | Purpose |
|------|---------|
| [RF traceability index](rf-index.yaml) | RF -> ODTIS ID index (generated) |
| [Rf Overrides (YAML)](rf-overrides.yaml) | Manual mappings not in registry `trace_informative` |
| [Section Coverage (YAML)](section-coverage.yaml) | Count of IDs per spec section (generated) |
| [Coverage report](coverage-report.yaml) | Phase 3.1 exit metrics (generated) |

---

## Sync workflow

```bash
# Regenerate rf-index from registry + overrides
python3 scripts/build-traceability-index.py
```

After adding ODTIS IDs:

1. Update `registry/requirements.json` `trace_informative` when possible
2. Add or adjust rows in `rf-overrides.yaml` for gaps or partial mappings
3. Run `build-traceability-index.py`
4. Update `TRACEABILITY-MATRIX.md` ODTIS ID column for major releases

---

## Coverage targets

| Milestone | RF with ODTIS ID |
|-----------|------------------|
| Phase 3.1 exit | ≥60 % |
| Phase 4 / v1.0 | 100 % |

**Current (generated):** see [Coverage report](coverage-report.yaml) - **30/30 core RF (100 %)**.

---

## Related

- Requirements: [Requirements registry](../registry/requirements.json)
- Plan task 3.1.17: [Build plan](../PLAN-PHASES.md)
