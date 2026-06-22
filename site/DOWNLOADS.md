---
title: ODTIS downloads and artifacts
description: Download OpenAPI bundles, requirement registry, event schemas, conformance manifests, and machine-readable ODTIS artifacts.
---

# Downloads & artifacts

<div class="odtis-hub-hero" markdown="1">

How to obtain ODTIS normative text, machine-readable registries, OpenAPI bundles, and offline snapshots.

<p class="odtis-hub-meta" markdown="1">
<strong>Version:</strong> <a href="/VERSION">0.9.0-draft</a> | 
<strong>License:</strong> <a href="/LICENSE">CC BY 4.0</a> | 
<strong>Project hub:</strong> [Project hub](../project/README.md)
</p>

</div>

!!! note "YAML/JSON not in HTML site"
    MkDocs excludes `.yaml`, `.json`, and `.openapi.yaml` for size and security. Clone the repository or download a release tarball for machine-readable files.

---

## Choose a format

| I need... | Get it from |
|-----------|-------------|
| Read online (HTML) | [odtis.org](https://odtis.org) (when deployed) or local `mkdocs serve` |
| Full source tree | Git clone (below) |
| Citable offline snapshot | Zenodo tarball (below) |
| OpenAPI, registry, conformance YAML | [Machine-readable artifacts](#machine-readable-artifacts) (below) |
| Citation metadata | [Citation metadata (CFF)](../publication/CITATION.cff), [How to cite](../publication/HOW-TO-CITE.md) |

---

## Git repository

Canonical open-source repository:

```bash
git clone https://github.com/odtis/core-spec.git
cd core-spec
```

VenID reference implementation (private until published): `github.com/odtis/core-impl`.

---

## Release tarball (Zenodo / offline)

```bash
cd odtis
./scripts/package-release.sh
```

| File | Location |
|------|----------|
| Archive | `publication/zenodo/snapshots/odtis-{version}-{date}.tar.gz` |
| SHA-256 | `publication/zenodo/snapshots/SHA256SUMS` |

Upload checklist: [Zenodo release checklist](../publication/zenodo/RELEASE-CHECKLIST.md).

!!! info "DOI pending"
    After Zenodo upload, the DOI will appear in [How to cite](../publication/HOW-TO-CITE.md). Prefer the DOI over the moving `main` branch for citations.

---

## Static HTML site

```bash
cd odtis
./scripts/build-site.sh
# output: build/odtis-spec-site/
mkdocs serve -f site/mkdocs.yml
```

CI uploads the artifact on push to `odtis/**`. Deploy: [Site deploy script](../scripts/deploy-site.sh) (CNAME: `odtis.org`).

---

## Machine-readable artifacts {#machine-readable-artifacts}

Registries and OpenAPI bundles referenced by the normative specification. Adoption context: [Adoption guide](../ADOPTION.md) section 2.

| I need... | Artifact |
|-----------|----------|
| REST API contracts (frozen) | Annex A OpenAPI (below) |
| Requirement IDs + test links | [Requirements registry](../registry/requirements.json) |
| Profile definitions | [Profile definitions](../registry/profiles.yaml) |
| Audit events | [Audit event catalog](../registry/events.yaml) + schemas |
| Terms and definitions | [Terminology registry](../registry/terminology.yaml) |
| RF traceability | `traceability/` (repo only) |

Browse on site: [Requirements index](REQUIREMENTS-INDEX.md) | [Glossary](GLOSSARY.md) | [Registry guide](../registry/README.md)

### OpenAPI (Annex A - frozen @ 0.9.0-draft)

| Bundle | ODTIS surface |
|--------|---------------|
| [VenID common schemas (OpenAPI)](../annexes/A-openapi-registry/venid-common.openapi.yaml) | Shared schemas |
| [Verification API (OpenAPI)](../annexes/A-openapi-registry/verification-api.openapi.yaml) | Core Identity S2 |
| [Citizen API (OpenAPI)](../annexes/A-openapi-registry/citizen-api.openapi.yaml) | Core Identity S3 |
| [Admin API (OpenAPI)](../annexes/A-openapi-registry/admin-api.openapi.yaml) | Operator S4/S5 |
| [Regulator API (OpenAPI)](../annexes/A-openapi-registry/regulator-api.openapi.yaml) | Operator S8 |
| [RP Reports API (OpenAPI)](../annexes/A-openapi-registry/reports-api.openapi.yaml) | Operator S6 |
| [Government API (OpenAPI)](../annexes/A-openapi-registry/gov-api.openapi.yaml) | Operator S7 |
| [Exchange gateway (OpenAPI)](../annexes/A-openapi-registry/exchange-gateway.openapi.yaml) | Trust Network |
| [Surface index (YAML)](../annexes/A-openapi-registry/INDEX.yaml) | All bundles |
| [OIDC discovery contract](../annexes/A-openapi-registry/oidc-discovery.md) | Core Identity S1 |

Freeze record: [Annex A freeze record](../annexes/A-openapi-registry/FREEZE.md)

### Traceability and conformance (repo)

| Artifact | Link |
|----------|------|
| RF traceability index | [RF traceability index](../traceability/rf-index.yaml) |
| Coverage report | [Coverage report](../traceability/coverage-report.yaml) |
| Conformance manifest | [Conformance manifest](../conformance/manifest.yaml) |
| Statement template | [Conformance statement template](../conformance/templates/conformance-statement.yaml) |

### Validate after download

```bash
cd odtis
python3 scripts/validate-registry.py
python3 scripts/validate-openapi.py
./conformance/run.sh
```

Optional OpenAPI lint: `npx @stoplight/spectral-cli lint annexes/A-openapi-registry/*.openapi.yaml`

---

## Tarball contents

Per [Release packaging script](../scripts/package-release.sh): full `odtis/` tree (spec, annexes, registry, conformance, governance, site source, publication metadata). Excludes `.venv-site/` and local report JSON.

---

<div class="odtis-hub-footer" markdown="1">

## Still stuck?

| Document | Purpose |
|----------|---------|
| [Project status](STATUS.md) | Maturity and blockers |
| [Getting started](GETTING-STARTED.md) | 15-minute implementer path |
| [Adoption guide](../ADOPTION.md) | Full adoption path |
| [Conformance overview](../conformance/README.md) | L1/L2/L3 verification |

</div>
