# ODTIS - Open Digital Trust Infrastructure Specification

**Status:** `0.9.0-draft` - Sections 1-10 review draft; Annex A frozen; Phase 3.2 + Foundation track A  
**Navigation:** [Repository map](STRUCTURE.md)  
**Citation:** [How to cite](publication/HOW-TO-CITE.md)  
**Site:** [https://odtis.org](https://odtis.org)  
**License:** [CC BY 4.0](LICENSE)  
**Reference implementation:** [Core Impl](https://github.com/odtis/core-impl) (private during Phase 3.2)

ODTIS is the open normative specification for digital trust infrastructure. [VenID](https://github.com/odtis/core-impl) is the first reference implementation. It defines conformance profiles, MUST/SHOULD/MAY requirements, machine-readable annexes, and a test suite for implementations.

**Adoption:** independent vendors and operators SHOULD read [Adoption guide](ADOPTION.md) first (profiles, certification, IETF track).

**Language:** all authoritative ODTIS text is **English only** ([Language policy](governance/LANGUAGE.md)).

---

## Related repositories and sites

| Resource | Role |
|----------|------|
| [odtis.org](https://odtis.org) | ODTIS specification site (this repo) |
| [digitaltrustinfrastructure.org](https://digitaltrustinfrastructure.org) | Parent research org (informative books and papers) |
| [core-spec](https://github.com/odtis/core-spec) | Normative spec, registry, conformance, MkDocs sources |
| [core-impl](https://github.com/odtis/core-impl) | VenID reference implementation; clone as sibling for smokes |

Local layout for RI smokes and site build:

```
odtis/
├── core-spec/          # this repository
├── core-impl/          # reference implementation (optional)
└── build/odtis-spec-site/   # gitignored MkDocs output
```

Informative books and papers (Book 2, Book 3, P18) are **not** vendored here; see [Adoption guide](ADOPTION.md) and [digitaltrustinfrastructure.org](https://digitaltrustinfrastructure.org) when published.

---

## Repository structure

See [Repository map](STRUCTURE.md). Top level:

```
├── VERSION                 # single semver source
├── spec/                   # sections 1-10 + adoptable profiles
├── registry/               # requirement IDs, events, terminology
├── annexes/                # A (frozen) - D
├── conformance/            # L1/L2 tests + certification
├── publication/            # citation, Zenodo releases
├── governance/             # stages, IPR, review, liaison
├── ietf/                   # scoped Internet-Draft working copies
├── implementation/         # RI map, gaps, conformance statements
├── traceability/           # RF ↔ ODTIS automation
├── scripts/                # validate, sync, build, deploy (local)
└── site/                   # MkDocs sources
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

## Validate and test

```bash
python3 scripts/validate-registry.py
python3 scripts/sync-spec-version.py --check
./conformance/run.sh    # L1 + L2 structural suite
```

---

## Build site and deploy (local)

```bash
./scripts/build-site.sh   # -> ../build/odtis-spec-site/
source .venv-site/bin/activate   # after first build
mkdocs serve -f site/mkdocs.yml  # http://127.0.0.1:8000

cp scripts/odtis-deploy.env.example scripts/odtis-deploy.env   # once, gitignored
./scripts/deploy-ec2.sh
```

Optional release version bump:

```bash
python3 scripts/bump-spec-version.py --minor --write
python3 scripts/sync-spec-version.py
python3 scripts/sync-site-release-meta.py
```

See [Site overview](site/README.md) and [Deploy Ec2 Odtis Org](scripts/DEPLOY-EC2-ODTIS-ORG.md).

---

## Foundation and publication

| Doc | Path |
|-----|------|
| Adoption guide | [Adoption guide](ADOPTION.md) |
| Repository map | [Repository map](STRUCTURE.md) |
| How to cite | [How to cite](publication/HOW-TO-CITE.md) |
| Governance | [Governance overview](governance/README.md) |
| Certification | [Certification program](governance/CERTIFICATION.md) |
| Build plan | [Build plan](PLAN-PHASES.md) |

```bash
python3 scripts/sync-spec-version.py
./scripts/package-release.sh   # Zenodo tarball
./scripts/audit-before-publish.sh   # pre-public repo check
```

## Contributing

Read [Contributing guide](governance/CONTRIBUTING.md) and [Versioning policy](governance/VERSIONING.md).
