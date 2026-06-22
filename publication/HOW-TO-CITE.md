---
title: How to cite ODTIS
description: Citation formats for the ODTIS working draft, Zenodo DOI, and profile-specific conformance references.
---

# How to cite ODTIS

**Current version:** see [Version](/VERSION) (`0.9.0-draft`) 
**License:** [CC BY 4.0](../LICENSE)

**Project hub:** [Project hub](../project/README.md) | **Downloads:** [Downloads](../site/DOWNLOADS.md)

!!! tip "Cite version + profile"
    ODTIS is published from [Core Spec](https://github.com/odtis/core-spec). For implementation conformance, cite the **exact ODTIS version and declared profile(s)**.

---

## Working draft (0.9.x-draft)

Use when citing the evolving specification before ODTIS `1.0.0`:

> Merida Oliveros, M. (2026). *Open Digital Trust Infrastructure Specification (ODTIS)*, version 0.9.0-draft. Copyright FinnectOS, Inc. Licensed CC BY 4.0. https://odtis.org (working draft).

After Zenodo upload, **prefer the DOI**:

> Merida Oliveros, M. (2026). *Open Digital Trust Infrastructure Specification (ODTIS)*, version 0.9.0-draft. https://doi.org/10.5281/zenodo.TBD

---

## Frozen standard (1.0.0 - future)

> Merida Oliveros, M. (YYYY). *Open Digital Trust Infrastructure Specification (ODTIS)*, version 1.0.0. Copyright ODTIS Foundation (or successor). https://doi.org/...

---

## What to cite for what purpose

| Purpose | Cite |
|---------|------|
| Normative MUST/SHOULD for implementation | **ODTIS** + exact version + profile ([Adoption guide](../ADOPTION.md)) |
| Conformance claim evidence | `conformance-statement.yaml` + ODTIS version |
| Academic alignment evidence | **P18** ([Annex C standards mapping](/annexes/C-standards-mapping/)) |
| Policy narrative | Book 1 (informative) |
| Architecture monograph | Book 2 (informative) |
| OIDC / OAuth behaviour | [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html) + ODTIS Core Identity profile deltas |
| Protocol extraction | IETF drafts in [IETF working drafts overview](../ietf/README.md) (informative until published) |

---

## Machine-readable

| File | Format |
|------|--------|
| [Citation metadata (CFF)](CITATION.cff) | GitHub / Zenodo metadata |
| [BIBLIOGRAPHY.bib](BIBLIOGRAPHY.bib) | BibTeX |

Release packaging: [Zenodo release checklist](zenodo/RELEASE-CHECKLIST.md)

---

## Related

| Document | Purpose |
|----------|---------|
| [Spec lifecycle stages](../governance/SPEC-STAGES.md) | Draft vs standard lifecycle |
| [Changelog](/CHANGELOG/) | Version history |
| [Project status](../site/STATUS.md) | DOI / Zenodo status |
