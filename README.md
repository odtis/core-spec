# ODTIS - Open Digital Trust Infrastructure Specification

**Status:** `0.9.0-draft` - Sections 1-10 review draft; Annex A frozen; Phase 3.2 + Foundation track A
**Navigation:** [Repository map](STRUCTURE.md) - full repository map
**Citation:** [How to cite](publication/HOW-TO-CITE.md)
**Target URL:** [https://odtis.org](https://odtis.org)
**Normative text license:** [CC BY 4.0](LICENSE)
**Open-source migration:** [Migration status & checklist](MIGRATION-STATUS.md)

ODTIS is the open normative specification for VenID / FinnectOS. It defines conformance profiles, MUST/SHOULD/MAY requirements, machine-readable annexes, and a test suite for digital trust infrastructure implementations.

**Adoption:** independent vendors and operators SHOULD read [Adoption guide](ADOPTION.md) first (profiles, certification, Book 2 relationship, IETF track).

**Language:** all authoritative ODTIS text is **English only** ([Language policy](governance/LANGUAGE.md)).

---

## Relationship to the workspace

| Artifact | Role | Path |
|----------|------|------|
| **P18** | Academic bridge; draft baseline (~103 IDs) | `docs/sources/papers/18-standards-alignment-odtis/` |
| **P13 / P14** | Data model and APIs that ODTIS normativizes | `docs/sources/papers/13-...`, `14-...` |
| **Book 2** | Reference Architecture (Vol. II) - descriptive source before ODTIS freeze | `docs/sources/books/02-platform-specification-monograph/` |
| **Book 3** | Implementation Guide (Vol. III) - non-normative | `docs/sources/books/03-implementation-guide/` |
| **RF matrix** | RF -> paper -> Book 2 -> ODTIS traceability | `docs/sources/papers/TRACEABILITY-MATRIX.md` |
| **Master plan** | Phase 0-4 sequence | `docs/sources/papers/PLAN-EJECUCION-FASES.md` |

P18 does **not** replace ODTIS v1.0: it is the standards-alignment paper. This repository is the **normative source of truth** evolving toward v1.0 in Phase 4.

---

## Repository structure

See [Repository map](STRUCTURE.md) for the full map. Top level:

```
odtis/
├── VERSION <- single semver source
├── spec/ <- sections 1-10 + adoptable profiles
├── registry/ <- 149 requirement IDs, events, terminology
├── annexes/ <- A (frozen) - D
├── conformance/ <- L1/L2 tests (159 procedures) + certification
├── publication/ <- citation, Zenodo releases
├── governance/ <- stages, IPR, review, liaison
├── ietf/ <- scoped Internet-Draft working copies
├── implementation/ <- RI map (ven-*), known gaps
├── traceability/ <- RF ↔ ODTIS automation
├── scripts/ <- validate, sync, release
└── site/ <- MkDocs -> build/odtis-spec-site/
```

---

## Conformance profiles (`0.9.0-draft`)

| Profile | Main sections | Tests | Implemented (smoke) | Req coverage |
|---------|---------------|-------|---------------------|--------------|
| **Reference Architecture** | 1 | 10 | 1 | 100% (10/10) |
| **Core Identity** | 2, 3, 5 | 58 | 9 | 100% (45/45) |
| **Trust Network** | 4 | 30 | 18 | 100% (27/27) |
| **Federation** | 6 | 8 | 8 | 100% (8/8) |
| **Operator** | 7-10 | 30 | 25 | 100% (36/36) |
| **Extended** | Annex D | 23 | 20 | 100% (25/25) |
| **Total** | - | **159** | **81** | **149** IDs |

Details: [Profile definitions](registry/profiles.yaml), [Conformance overview](conformance/README.md), [Profile comparison](site/PROFILES.md).

---

## Requirements registry

**149** `ODTIS-x.x.x` IDs in [Requirements registry](registry/requirements.json) (P18 baseline + federation depth FB-002, operator RF-27, and Phase 3.2 additions).

```bash
python3 scripts/extract-requirements.py # regenerate from P18
python3 scripts/validate-registry.py # validate integrity
./conformance/run.sh # L1 + L2 structural suite
```

---

## Phased build

See [Build plan](PLAN-PHASES.md). Summary:

| Workspace phase | ODTIS deliverable |
|-----------------|-------------------|
| **Phase 3** (current) | Sections 1-10 @ `0.9.0-draft`; Annex A frozen; L1+L2 conformance; review cycle 1 |
| **Phase 4** | Frozen ODTIS v1.0 + certification + DOI/Zenodo |

**Dependency:** Book 2 stable (≥90% chapters) before promoting requirements from `draft` to stable `normative`.

---

## Site and build

```bash
./scripts/build-site.sh # -> ../build/odtis-spec-site/
source .venv-site/bin/activate # after first build
mkdocs serve -f site/mkdocs.yml # http://127.0.0.1:8000
```

See [Site overview](site/README.md). CI artifact: `.github/workflows/odtis-spec.yml`.

---

## Foundation & publication

| Doc | Path |
|-----|------|
| **Adoption guide** | [Adoption guide](ADOPTION.md) |
| Repository map | [Repository map](STRUCTURE.md) |
| How to cite | [How to cite](publication/HOW-TO-CITE.md) |
| Governance index | [Governance overview](governance/README.md) |
| Spec stages | [Spec lifecycle stages](governance/SPEC-STAGES.md) |
| OIDF positioning | [OIDF positioning](governance/liaison/OIDF-POSITIONING.md) |
| IETF roadmap | [IETF roadmap](governance/IETF-ROADMAP.md) |
| Certification | [Certification program](governance/CERTIFICATION.md) |

Version and status hygiene:

```bash
python3 scripts/sync-spec-version.py
python3 scripts/normalize-coherence.py
python3 scripts/sync-spec-version.py --check # CI
./scripts/package-release.sh # Zenodo tarball
```

## Contributing

Read [Contributing guide](governance/CONTRIBUTING.md) and [Versioning policy](governance/VERSIONING.md).
