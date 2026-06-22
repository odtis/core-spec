# ODTIS open-source migration - status & checklist

**Last updated:** 2026-06-22  
**Workspace:** `odtis/` (sibling `core-spec` + `core-impl`)  
**Model:** two repos (`core-spec` + `core-impl`); **no** separate `site` repo - odtis.org is generated and deployed from `core-spec`.

---

## Architecture (target)

| Piece | Location | GitHub | Public |
|-------|----------|--------|--------|
| ODTIS specification | `core-spec/` | [Core Spec](https://github.com/odtis/core-spec) | Yes |
| VenID reference impl | `core-impl/` | [Core Impl](https://github.com/odtis/core-impl) | No (planned) |
| odtis.org HTML | `../build/odtis-spec-site/` | - (artifact, not a repo) | Via EC2 deploy |
| Legacy `odtis/site` repo | - | [Site](https://github.com/odtis/site) | Archived / unused |
| Editorial (books, papers) | `../venezuela/docs/` | Private monorepo | Zenodo / DTI.org later |

**Sibling layout** (required for smoke / L2 scripts):

```
odtis/
├── core-spec/          ← normative spec + MkDocs sources + scripts
├── core-impl/          <- ven-identity-core, ven-trust-network, ...
└── build/              ← gitignored; MkDocs output → odtis.org
    └── odtis-spec-site/
```

**Source monorepo (unchanged):** `../venezuela/` - copy only, not deleted yet.

---

## Decisions locked in

- [x] Two repos only: `core-spec` + `core-impl` (no `site` repo)
- [x] odtis.org = build artifact + EC2 rsync (not versioned in git)
- [x] Deploy: keep EC2 + Cloudflare Flexible (`scripts/DEPLOY-EC2-ODTIS-ORG.md`)
- [x] `core-impl` private for now; public release later
- [x] `odtis/site` GitHub repo: do nothing for now
- [x] Do not delete `venezuela/` until migration verified

---

## Completed

### Migration & workspace

- [x] Copy `venezuela/odtis/` → `core-spec/` (excl. `.venv-site`, `conformance/reports/`, `odtis-deploy.env`)
- [x] Copy `venezuela/ven-{cloud-stack,identity-core,trust-network,trust-network-web,infra-core}/` + `pom.xml` → `core-impl/`
- [x] Workspace README at `odtis/README.md`
- [x] **Do not delete** `venezuela/` sources (still authoritative for parallel dev until decided)

### Git & GitHub

- [x] Initial commit + push → `github.com/odtis/core-spec` (`main`)
- [x] Initial commit + push → `github.com/odtis/core-impl` (`main`, private)
- [x] Local branch `setup/local-workspace` tracks `origin/main` in both repos
- [x] Issue templates in `core-spec/.github/ISSUE_TEMPLATE/` (RFC, clarification, sandbox)
- [x] CI workflow `core-spec/.github/workflows/odtis.yml` (validate + build site artifact)
- [x] CI workflow `core-impl/.github/workflows/ci.yml` (Maven `-DskipDocker=true`)

### Paths & URLs

- [x] Canonical repo URL: `github.com/odtis/core-spec` (was `odtis/site`, `venid/odtis`)
- [x] Smoke script paths: `../core-impl/ven-*` (was `../ven-*` in monorepo)
- [x] MkDocs `site_dir`: `../../build/odtis-spec-site` (outside `docs_dir`; workspace `odtis/build/`)
- [x] Root community files excluded from MkDocs build (`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`)

### Build & quality

- [x] `./scripts/build-site.sh` passes locally (~16 MB → `odtis/build/odtis-spec-site/`)
- [x] Link check (`check-site-links.py`) passes after exclusions
- [x] `sync-spec-version --check` + `validate-registry.py` pass

### `.gitignore`

- [x] `core-spec/.gitignore` hardened (venv, secrets, Zenodo tarballs, reports, IDE)
- [x] `core-impl/.gitignore` aligned with monorepo patterns
- [x] Per-module ignores: `ven-cloud-stack/`, `ven-trust-network/`, `portal-trust/`, front portals
- [x] Removed from git: embedded `node/` binaries (~85 MB each) + `portal-trust/dist/`
- [x] Workspace `odtis/.gitignore` for `build/`

---

## Checklist - resume here

### P1 - Operate & unblock CI (this week)

- [ ] **Fix conformance L1** - `./conformance/run.sh` currently **FAIL (6/10)**
  - Errors: ODTIS-0517-0536 missing in annex B threat mappings / `odtis_8_coverage`
  - Files: `registry/requirements.json`, `annexes/B-threat-mitigations/`, validators in `scripts/`
  - **Blocks:** GitHub Actions green on `core-spec`
- [ ] **Deploy odtis.org**
  - [x] `scripts/odtis-deploy.env` configured (copied from monorepo; gitignored)
  - [x] `./scripts/deploy-ec2.sh` - deployed 2026-06-22
  - [x] https://odtis.org returns HTTP 200 (Cloudflare)
  - [x] Auto-deploy on merge to `main` via `.github/workflows/release-deploy.yml` (minor version bump + visible site version)
  - [ ] Add GitHub secrets `ODTIS_EC2_HOST` + `ODTIS_SSH_KEY` (see `scripts/GITHUB-DEPLOY-SECRETS.md`)
- [ ] **Review cycle 1** - comment period closes **2026-06-26**
  - [ ] Triage issues on `github.com/odtis/core-spec`
  - [ ] Update `governance/REVIEW-LOG.yaml`, `CHANGELOG.md`
  - [ ] Run `governance/REVIEW-CYCLE-1-CLOSE.md` checklist or extend cycle with record

### P2 - Consolidate migration

- [ ] **Choose canonical edit path** (pick one):
  - [ ] **A)** GitHub `core-spec` = source of truth; `venezuela/odtis` → stub README redirect
  - [ ] **B)** Keep developing in `venezuela/` + mirror/sync script to GitHub until cutover
- [x] **Commit this doc** into `core-spec` (`MIGRATION-STATUS.md`)
- [ ] **Rename local branch** `setup/local-workspace` → `main` (optional hygiene) `setup/local-workspace` → `main` (optional hygiene)
- [ ] **Archive `odtis/site` repo** on GitHub with README redirect to `core-spec` (when ready)
- [ ] **Remove duplicates** from `venezuela/` monorepo (only after canonical path + deploy verified):
  - [ ] `venezuela/odtis/`
  - [ ] `venezuela/ven-*` moved to `core-impl` only
  - [ ] Update `dti-core` / monorepo README

### P3 - Ecosystem & links

- [ ] Update [digitaltrustinfrastructure.org](https://digitaltrustinfrastructure.org) → `core-spec`, odtis.org, `core-impl` (when public)
- [ ] Update [manuelmerida.io](https://manuelmerida.io) Vol. III → odtis.org
- [ ] Review **informative links** still pointing to private monorepo:
  - `finnectos/venezuela` in `traceability/README.md`, `PLAN-PHASES.md`, Book 2 cross-refs
  - Scripts: `generate-phased-backlog.py`, `fix-deep-relative-links.py`, `normalize-site-markdown-links.py`
  - **Options:** Zenodo DOI, public docs repo, or remove broken links for external readers
- [ ] Fix stale path in `scripts/DEPLOY-EC2-ODTIS-ORG.md` (`odtis/site/mkdocs.yml` → `core-spec/site/mkdocs.yml`)
- [ ] GitHub org `odtis`: profile README, topics, branch protection on `main`, CODEOWNERS for `spec/`, `registry/`, `annexes/A-*`

### P4 - Publication & spec maturity (Phase 3.2 → 4)

- [ ] **Zenodo snapshot** @ `v0.9.0-draft`
  - [ ] `./scripts/package-release.sh`
  - [ ] Upload + DOI → update `publication/CITATION.cff`, `HOW-TO-CITE.md`, `BIBLIOGRAPHY.bib`
  - [ ] GitHub ↔ Zenodo integration
- [ ] Raise smoke evidence: **85/159** tests implemented (~53%); target 100% for v1.0
- [ ] Close **4 deferred RI gaps** (`implementation/gaps/DEFERRED-TRACK.md`): mTLS interop, TSA, IETF TEP, L3 attestation
- [ ] IETF drafts: markdown in `ietf/` → xml2rfc → submission (`governance/IETF-ROADMAP.md`)
- [ ] **ODTIS v1.0** per `PLAN-PHASES.md` Phase 4 (freeze, certification program, 100% RF traceability)

### P5 - `core-impl` (when opening publicly)

- [ ] Confirm `mvn clean install -DskipTests` locally and on GitHub Actions
- [ ] Add `CITATION.cff` (link to P12 / Zenodo)
- [ ] Make repo public on `github.com/odtis/core-impl`
- [ ] Regenerate `core-spec/implementation/RI-MAP.yaml` + `site/COMPONENT-BINDINGS.md` with public URLs
- [ ] L2 sandbox smoke documented in `conformance/sandbox/README.md` against live `--target`
- [ ] Consider Git LFS if large assets reappear (embedded `node/` must stay gitignored)

### P6 - Foundation & governance (medium term)

- [ ] ODTIS Foundation incorporation (`governance/FOUNDATION-CHARTER.md`)
- [ ] Trademark + formal L3 auditor program (`governance/CERTIFICATION.md`)
- [ ] Working groups activation (`governance/working-groups/`)
- [ ] Stewardship transition FinnectOS → multi-stakeholder board

---

## Known non-blockers

| Item | Notes |
|------|-------|
| MkDocs anchor warnings | `KNOWN-GAPS.md` → `PHASED-BACKLOG.md` missing anchors; build still passes |
| MkDocs 2.0 warning | Material team advisory; no action required now |
| `MIGRATION-STATUS.md` in repo | Versioned in `core-spec`; workspace copy at `../MIGRATION-STATUS.md` |
| Review draft status | Spec is `0.9.0-draft`, not `1.0.0`; Annex A frozen @ 0.9.0-draft |
| `brain/`, `docs/`, `ven-development-stack/` | Stay in private monorepo; not part of OSS split |

---

## Quick commands

```bash
# Workspace
cd odtis

# Validate spec
cd core-spec
python3 scripts/sync-spec-version.py --check
python3 scripts/validate-registry.py
./conformance/run.sh                    # target: all green

# Build site (output outside repo)
./scripts/build-site.sh
open ../build/odtis-spec-site/index.html

# Deploy odtis.org (needs odtis-deploy.env)
./scripts/deploy-ec2.sh

# Package for Zenodo
./scripts/package-release.sh

# VenID build
cd ../core-impl
mvn clean install -DskipTests
# CI-style: mvn clean install -DskipTests -DskipDocker=true

# Git status
cd ../core-spec && git status && git log -1 --oneline
cd ../core-impl && git status && git log -1 --oneline
```

---

## Remote state (last known)

| Repo | URL | Branch | Latest theme |
|------|-----|--------|--------------|
| core-spec | https://github.com/odtis/core-spec | `main` | Spec import + `.gitignore` hardening |
| core-impl | https://github.com/odtis/core-impl | `main` (private) | RI import + removed node/dist artifacts |

---

## Related docs (inside `core-spec`)

| Doc | Path |
|-----|------|
| Phased build plan | `core-spec/PLAN-PHASES.md` |
| Deploy guide | `core-spec/scripts/DEPLOY-EC2-ODTIS-ORG.md` |
| Review cycle 1 | `core-spec/governance/REVIEW-CYCLE-1.md` |
| Adoption | `core-spec/ADOPTION.md` |
| Zenodo checklist | `core-spec/publication/zenodo/RELEASE-CHECKLIST.md` |

---

*Retomar desde **Checklist - resume here → P1**.*
