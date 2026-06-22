# Zenodo release checklist (ODTIS snapshot)

Publish a **citable offline snapshot** without requiring a public site deploy.

**Maintainers:** [Maintainers](/governance/MAINTAINERS/) | **Cite guide:** [How to cite](../HOW-TO-CITE.md) | **Project:** [Project hub](/project/)

!!! info "DOI status"
    Zenodo DOI is **pending** @ `0.9.0-draft`. Track on [Project status](/site/STATUS/).

---

## Before upload

| Step | Action |
|------|--------|
| 1 | Confirm [Version](../../VERSION) matches release tag |
| 2 | Run validators (below) |
| 3 | Build tarball: `./scripts/package-release.sh` |
| 4 | Verify SHA-256 in `publication/zenodo/snapshots/SHA256SUMS` |

```bash
cd odtis
python3 scripts/sync-spec-version.py --check
./conformance/run.sh
python3 scripts/pin-annex-a-checksums.py
./scripts/package-release.sh
```

---

## Zenodo metadata (suggested)

| Field | Value |
|-------|-------|
| Title | Open Digital Trust Infrastructure Specification (ODTIS) |
| Version | `0.9.0-draft` |
| License | CC BY 4.0 |
| Upload type | Software / Other |
| Description | Normative open specification for digital trust infrastructure (Core Identity, Trust Network, Federation, Operator, Extended profiles). |
| Related identifier | P18 DOI (when available) - *Is supplement to* |

---

## After upload

1. Update `publication/BIBLIOGRAPHY.bib` with real DOI
2. Update `publication/CITATION.cff` `doi` field
3. Add entry to [Changelog](../../CHANGELOG.md)
4. Update [Review Log (YAML)](/governance/REVIEW-LOG.yaml) if release closes a review cycle
5. Update [How to cite](../HOW-TO-CITE.md) citation strings

---

## Tarball contents

Per [Release packaging script](/scripts/package-release.sh):

| Included | Excluded |
|----------|----------|
| Full `odtis/` tree (spec, registry, conformance, governance, site) | `.venv-site/` |
| | Local `conformance/reports/*.json` |
| | `.DS_Store` |

Download guide: [Downloads](/site/DOWNLOADS/)

---

## Related

| Document | Purpose |
|----------|---------|
| [Machine-readable artifacts](/site/DOWNLOADS/#machine-readable-artifacts) | Machine-readable file index |
| [Versioning policy](/governance/VERSIONING/) | Semver rules |
