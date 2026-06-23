# ODTIS - Open Digital Trust Infrastructure Specification

[![Specification site](https://img.shields.io/badge/site-odtis.org-2563eb?style=flat-square)](https://odtis.org)
[![Version](https://img.shields.io/badge/version-0.9.0--draft-f59e0b?style=flat-square)](VERSION)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-16a34a?style=flat-square)](LICENSE)
[![Conformance](https://img.shields.io/badge/conformance-L1%20%7C%20L2%20%7C%20L3-7c3aed?style=flat-square)](conformance/README.md)

Vendor-neutral open specification for digital identity, institutional trust exchange, operator governance, and optional extended modules.

**Live site:** [odtis.org](https://odtis.org) · **Version:** [`0.9.0-draft`](VERSION) · **License:** [CC BY 4.0](LICENSE) · **Copyright:** FinnectOS, Inc.

ODTIS defines normative MUST/SHOULD/MAY requirements, **seven** adoptable conformance profiles, machine-readable annexes (OpenAPI, events, registry), and an L1/L2/L3 verification model. Implementations may be open source or proprietary; conformance is proven by tests and published statements, not by using any single vendor stack.

[VenID](https://github.com/odtis/core-impl) is the first reference implementation (separate repository). You do **not** need VenID code to implement ODTIS.

---

## Start here

| You are… | Start with |
|----------|------------|
| **New to ODTIS** | [Getting started](https://odtis.org/site/GETTING-STARTED/) on the spec site |
| **Implementing or procuring** | [Adoption guide](ADOPTION.md) |
| **Verifying conformance** | [Conformance overview](conformance/README.md) |
| **Citing or packaging** | [How to cite](publication/HOW-TO-CITE.md) |
| **Contributing** | [Contributing guide](governance/CONTRIBUTING.md) · [Review cycle 1](governance/REVIEW-CYCLE-1.md) (open until 2026-06-26) |

Authoritative specification text is **English only** ([Language policy](governance/LANGUAGE.md)).

---

## Status (`0.9.0-draft`)

| Item | State |
|------|--------|
| **Lifecycle** | Review draft ([Spec stages](governance/SPEC-STAGES.md)) - not ODTIS `1.0.0` |
| **Normative sections 1-11** | Review draft complete |
| **Annex A OpenAPI** | Frozen @ `0.9.0-draft` |
| **Registry** | 204 ODTIS requirement IDs |
| **Conformance suite** | 214 test procedures (see [Project status](https://odtis.org/site/STATUS/)) |
| **Public site** | [odtis.org](https://odtis.org) |
| **Steward** | FinnectOS, Inc. (interim; [Foundation charter](governance/FOUNDATION-CHARTER.md) draft) |

Full metrics: [Project status](https://odtis.org/site/STATUS/) · Roadmap: [Build plan](PLAN-PHASES.md)

---

## Ecosystem

| Resource | Role |
|----------|------|
| [odtis.org](https://odtis.org) | Specification website (built from this repo) |
| **This repository** | Normative source: `spec/`, `registry/`, `annexes/`, `conformance/` |
| [Core Impl](https://github.com/odtis/core-impl) | VenID reference implementation (private during Phase 3.2) |
| [digitaltrustinfrastructure.org](https://digitaltrustinfrastructure.org) | Research organization - informative books and papers (not vendored here) |

**Sibling layout** (optional, for RI smokes and local site build):

```
workspace/
├── core-spec/     # this repository
├── core-impl/     # VenID RI (optional)
└── build/         # gitignored MkDocs output (odtis-spec-site/)
```

---

## Repository layout

See [Repository map](STRUCTURE.md).

```
├── spec/            # Sections 1-11 + adoptable profiles
├── registry/        # Requirement IDs, terminology, events, profiles
├── annexes/         # A (OpenAPI, frozen) - E
├── conformance/     # L1/L2/L3 tests and certification guides
├── governance/      # IPR, stages, review, maintainers
├── publication/     # Citation, Zenodo packaging
├── implementation/  # RI map, gaps, conformance statements (informative)
├── traceability/    # RF ↔ ODTIS automation
├── scripts/         # Validators, site build, release tools
└── site/            # MkDocs sources → odtis.org
```

---

## Conformance profiles

| Profile | Sections | Tests | Smoke-evidenced | Req IDs |
|---------|----------|-------|-----------------|---------|
| Reference Architecture | 1 | 10 | 1 | 10 |
| Core Identity | 2, 3, 5 | 58 | 9 | 45 |
| Trust Network | 4 | 30 | 18 | 27 |
| Federation | 6 | 8 | 8 | 8 |
| Operator | 7-10 | 30 | 25 | 36 |
| Extended | Annex D | 23 | 20 | 25 |
| Reliance Extensions | 11 | 55 | 55 | 55 |
| **Total** | | **214** | **200** | **204** |

Details: [Profile definitions](registry/profiles.yaml) · [Profile comparison](https://odtis.org/site/PROFILES/)

---

## Validate locally

From this repository root:

```bash
python3 scripts/validate-registry.py
python3 scripts/sync-spec-version.py --check
./conformance/run.sh
```

With a live deployment target (L2):

```bash
export ODTIS_TARGET=https://your-staging.example/realms/your-realm
python3 scripts/run-conformance.py --level L2 --profile core-identity
```

---

## Build the spec site

```bash
./scripts/build-site.sh
source .venv-site/bin/activate   # created on first build
mkdocs serve -f site/mkdocs.yml  # http://127.0.0.1:8000
```

Maintainers: [Site overview](site/README.md) · [Deploy to odtis.org](scripts/DEPLOY-EC2-ODTIS-ORG.md) (local credentials, gitignored)

---

## Contributing

We welcome clarifications, editorial fixes, sandbox L2 reports, and RFC-track normative proposals.

1. Read [Contributing guide](governance/CONTRIBUTING.md) and [Code of conduct](CODE_OF_CONDUCT.md)
2. Check [Review cycle 1](governance/REVIEW-CYCLE-1.md) for open feedback items
3. Open an issue or PR against `main`

Normative contributions are published under [CC BY 4.0](LICENSE). Copyright holder: **FinnectOS, Inc.** See [IPR policy](governance/IPR-POLICY.md).

**Maintainers:** [GitHub setup guide](.github/GITHUB-SETUP.md) (public repo, Discussions, labels, branch protection).

---

## License and attribution

Specification text in this repository is licensed under **[Creative Commons Attribution 4.0 (CC BY 4.0)](LICENSE)**.

- **Copyright:** FinnectOS, Inc. (interim; intended transfer to ODTIS Foundation upon incorporation)
- **Trademarks** (ODTIS, ODTIS Certified, VenID, FinnectOS) are **not** granted by CC BY - see [Trademark policy](governance/TRADEMARK-POLICY.md)
- **Referenced papers/books** may use separate licenses (often on [digitaltrustinfrastructure.org](https://digitaltrustinfrastructure.org))

---

## Security

Report specification or site security concerns to **info@odtis.org**. Do not open public issues for undisclosed vulnerabilities. See [Security](SECURITY.md).

---

## Key documents

| Document | Description |
|----------|-------------|
| [Adoption guide](ADOPTION.md) | Profiles, certification, honest maturity claims |
| [Governance](governance/README.md) | Stages, IPR, certification program |
| [Certification](governance/CERTIFICATION.md) | L1 / L2 / L3 levels |
| [How to cite](publication/HOW-TO-CITE.md) | Academic and procurement citation |
| [Changelog](CHANGELOG.md) | Release history |
| [GitHub setup](.github/GITHUB-SETUP.md) | Publish checklist, Discussions, branch protection |
