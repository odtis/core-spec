# ODTIS versioning policy

**Applies to:** `odtis/` normative specification 
**Current version:** see [Version](/VERSION)

**Project hub:** [Project hub](../project/README.md) | **Lifecycle:** [Spec lifecycle stages](SPEC-STAGES.md)

---

## Semantic versioning

| Component | Rule |
|-----------|------|
| **MAJOR** | Breaking change to MUST requirements or profile definitions |
| **MINOR** | New SHOULD/MAY, new optional modules, backward-compatible MUST clarifications |
| **PATCH** | Editorial fixes, typo, non-normative clarifications |

Pre-1.0 versions use suffix `-draft` (e.g. `0.9.0-draft`). Requirement IDs (`ODTIS-x.x.x`) are stable across 0.x; new IDs MAY be added in minor 0.x releases.

## Release stages

| Stage | VERSION example | Meaning |
|-------|-----------------|---------|
| Scaffold | `0.1.0-draft` | Structure only; P18 extract |
| Working draft | `0.5.x-draft` | 1-11 prose in progress |
| Review draft | `0.9.x-draft` | Feature-complete for external review |
| Standard | `1.0.0` | Frozen after pilot metrics (Phase 4) |

## Branches and tags

- `main` - latest draft acceptable for implementers experimenting
- `v1.0.0` tag - frozen normative text at Phase 4
- Release branches `release/0.9.x` optional during stabilization

## Registry synchronization

On each release:

1. Run `python3 scripts/extract-requirements.py` if P18 changed (transitional)
2. Run `python3 scripts/validate-registry.py`
3. Update `CHANGELOG.md` and `VERSION`
4. Bump `registry/*.yaml` `spec_version` field

## Relationship to papers

| Document | Versioning |
|----------|------------|
| P18 | Zenodo DOI version; informative after ODTIS 1.0 |
| Book 2 | Monograph edition; sync review with ODTIS minor |
| Annex A OpenAPI | Independent semver until ODTIS 1.0, then aligned major |
