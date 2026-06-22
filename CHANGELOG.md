# Changelog - ODTIS

Format based on [Keep a Changelog](https://keepachangelog.com/). Versioning: [VERSION](/VERSION) | policy: [Versioning policy](/governance/VERSIONING/)

**Project hub:** [Project hub](/project/) | **Status:** [Project status](/site/STATUS/)

---

## [Unreleased]

### Added

- **Project site hub** - [Project hub](/project/); Conformance and Project section UX alignment
- **Conformance FAQ** - [Conformance FAQ](/conformance/FAQ/)
- **L3 certification package** - [L3 certification package](/implementation/L3-CERTIFICATION-PACKAGE/), audit checklist, deferred track
- **Book 1 domains (site)** - [Book 1 domain map](/registry/BOOK1-DOMAINS/)
- **Component bindings** - 9 YAML bindings + [Component bindings](/site/COMPONENT-BINDINGS/) generator
- **Documentation roadmap R0-R4** - [Documentation roadmap](/implementation/DOCUMENTATION-ROADMAP/)

### Changed

- **Domain and contact alignment** - `odtis.org` spec site; `digitaltrustinfrastructure.org` research org; VenID links to `core-impl`; `info@odtis.org` / `conformance@odtis.org`
- **Open-source publication prep** - removed stale `docs/sources/` paths; local deploy docs; audit script; README and adoption alignment
- **Registry** - 149 requirement IDs; section index sync; ID alignment (0104, 0340-0343)
- **Conformance suite** - 159 test procedures; 81 with smoke evidence; 6 profiles including reference-architecture
- **Section review FB-004** - autodiscovery SHOULD scope in section 4.4.3 + Annex A README
- **Section review FB-002 / FB-003** - Federation depth; HA boundary note in section 10.4
- **Spec site** - STATUS, DOWNLOADS, FAQ, GETTING-STARTED, PROFILES, governance and RI hub pages

## [0.9.0-draft] - 2026-06-12

### Phase 3.2 - Review and stabilization

- **Foundation track A** - `publication/`, governance foundation docs, `ietf/`, `implementation/`, `conformance/certification/`, adoptable `spec/profiles/`, `sync-spec-version.py`, `package-release.sh`; spec section 1 Abstract/Status/Security/References

- **Book 2 cross-review (3.2.1)** - Full matrix in `governance/BOOK2-CROSS-REVIEW.md`; CR-01..03 resolved; Book 2 ch.4 and ch.8 updated
- **Annex A freeze (3.2.2)** - All bundles `info.version: 0.9.0-draft`; `FREEZE.md`, `CHECKSUMS.sha256`, `scripts/pin-annex-a-checksums.py`
- **Sandbox RI map (3.2.3)** - `conformance/sandbox/README.md` aligned to Book 3 C1-C4
- **External feedback (3.2.4)** - Review cycle 1 (`REVIEW-CYCLE-1.md`, `REVIEW-LOG.yaml`, steward items FB-001..005, `open-review-issues.sh`)
- **FB-001 accepted** - ODTIS-0331 linked in consent scope test stubs (100% core-identity coverage)
- **Site deploy prep (3.1.16)** - `scripts/deploy-ec2.sh`, `scripts/build-site.sh`, CNAME for `odtis.org`
- **L2 enhancements** - Discovery field checks, JWKS, PKCE S256, `--output` JSON; `conformance/sandbox/run-sandbox-check.sh`
- **Version bump** - ODTIS `0.9.0-draft` (registry, traceability, Annex A INDEX)

## [0.1.0-draft] - 2026-06-12 (superseded by 0.9.0-draft)

### Added

- Full ODTIS repository scaffold (`spec/`, `annexes/`, `registry/`, `conformance/`, `governance/`, `traceability/`, `scripts/`, `site/`)
- Registry of 103 `ODTIS-x.x.x` requirements extracted from P18 v1.0 (`registry/requirements.json`)
- Draft conformance profiles (`registry/profiles.yaml`)
- Draft event catalog (`registry/events.yaml`)
- ODTIS phase plan aligned with PLAN-EJECUCION-FASES Phase 3-4
- Scripts `extract-requirements.py` and `validate-registry.py`
- **Sections 1-10** - normative prose Phase 3.1 (105 numbered IDs)
- **Annexes A-D** - OpenAPI, threats, standards mapping, extended profiles
- **Conformance suite L1** - `conformance/run.sh`, manifest builder, initial manual stubs
- **MkDocs site** - `site/requirements.txt`, `scripts/build-site.sh`

### Phase 3.1 expansion (same release line, before 0.9.0-draft)

- Traceability automation - `build-traceability-index.py`, 30/30 RF synced
- ODTIS-0308 / ODTIS-0309 - logout and account recovery
- ODTIS-0504 - operator subject administration (RF-27)
- Annex A - exchange-gateway, reports-api, gov-api bundles; normative `ErrorCode` enum
- Event JSON Schemas - `registry/events/schemas/` (16 schemas); `generate-event-schemas.py`
- Conformance - 125 test stubs; L2 runner; 100% registry coverage for Core/Trust/Federation/Operator
- Spectral - `.spectral.yaml` for Annex A lint rules

### Notes

- Normative text for sections 1-10 was draft v0.5 prose label; superseded by semver `0.9.0-draft`
- P18 remains complementary academic reference
- Spec license: CC BY 4.0 (distinct from papers CC BY-NC-ND)
