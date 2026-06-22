# Annex A - OpenAPI registry

| Field | Value |
|-------|-------|
| **Status** | frozen - see FREEZE.md |
| **Spec version** | 0.9.0-draft |
| **Source** | P14 10, ODTIS 3.11 |
| **Format** | OpenAPI 3.1 |

**Annexes hub:** [Project hub](../README.md) | **Spec index:** [Specification index](../../spec/INDEX.md) | **Conformance:** [Conformance overview](/conformance/)

---

## Purpose

Annex A is the **machine-readable API registry** for ODTIS Core Identity and operator REST surfaces. Conformance tests reference **`operationId`** values defined here, not prose section numbers (P14 10.4).

OIDC Surface **S1** is **not** duplicated in VenID OpenAPI files; use IdP discovery - see [OIDC discovery contract](oidc-discovery.md).

**Trust Network autodiscovery** (`@VenPartnerService`, ODTIS-0214) is **not** in Annex A for `0.9.0-draft`. Catalog sync and exchange-gateway OpenAPI cover federated exchange; partner-side autodiscovery remains a manual conformance stub until Book 2 ch.9 defines a discovery well-known URI (FB-004).

---

## Registry layout

```
A-openapi-registry/
├── README.md
├── INDEX.yaml <- Surface -> file -> ODTIS IDs
├── oidc-discovery.md <- S1 informative contract
├── venid-common.openapi.yaml
├── verification-api.openapi.yaml <- S2 (Core)
├── citizen-api.openapi.yaml <- S3 (Core)
├── admin-api.openapi.yaml <- S4/S5
├── regulator-api.openapi.yaml <- S8 (Operator)
├── reports-api.openapi.yaml <- S6
├── gov-api.openapi.yaml <- S7
└── exchange-gateway.openapi.yaml <- Trust Network gateway
```

---

## Surface catalog

| Surface | OpenAPI bundle | Base path | ODTIS | Status |
|---------|----------------|-----------|-------|--------|
| S1 OIDC | (discovery) | `/.well-known/...` | 3.3 | informative |
| S2 Verification | `verification-api.openapi.yaml` | `/v1` | 3.5 | ✅ draft |
| S3 Citizen | `citizen-api.openapi.yaml` | `/v1/citizen` | 3.7-3.8 | ✅ draft |
| S4 RP clients | `admin-api.openapi.yaml` | `/v1/admin/clients` | 3.6 | ✅ draft |
| S5 Operator admin | `admin-api.openapi.yaml` | `/v1/admin` | 7 | partial |
| S8 Regulator | `regulator-api.openapi.yaml` | `/v1/regulator` | 7.5, 9.4 | ✅ draft |
| S6 Reports | `reports-api.openapi.yaml` | `/v1/rp/reports` | 3.5, 9.2 | ✅ draft |
| S7 Government | `gov-api.openapi.yaml` | `/v1/gov` | 3.4, 3.5 | ✅ draft |
| Exchange GW | `exchange-gateway.openapi.yaml` | `/v1/exchange` | 4 | ✅ draft |

Full index: [Surface index (YAML)](INDEX.yaml).

---

## Versioning rules (normative summary)

| Rule | Specification |
|------|---------------|
| URL version | `/v1/` prefix on REST resources |
| Document version | `info.version` in each OpenAPI file (semver) |
| Breaking change | New `/v2/` URL **and** major OpenAPI version |
| Operation IDs | `{service}.{resource}.{action}` |
| Shared schemas | Import `venid-common.openapi.yaml` |

Source: P14 10.2, ODTIS 3.11.

---

## Core Identity conformance minimum

Implementations claiming **Core Identity API conformance** MUST expose:

1. **S1** - OIDC Authorization Code + PKCE (public clients)
2. **S2** - Verification API with `VerifyResponse` schema
3. **S3** - Citizen registration/consent endpoints (or equivalent contract)
4. **Error envelope** - `ErrorResponse` on REST surfaces
5. **Published OpenAPI** - bundles in this annex or equivalent URLs with checksums in conformance statement

Source: P14 11.3.

---

## Validation

```bash
python3 ../../scripts/validate-openapi.py
```

Optional (if Spectral installed):

```bash
spectral lint *.openapi.yaml
```

---

## Publication target

| Artifact | Location |
|----------|----------|
| Git registry | `odtis/annexes/A-openapi-registry/` |
| Public site | `https://odtis.org/annexes/A-openapi-registry/` |

---

## Checklist

- [x] Shared components (`venid-common.openapi.yaml`)
- [x] Core bundles S2, S3, S4, S8
- [x] `INDEX.yaml` with ODTIS requirement cross-refs
- [x] Validation script
- [x] reports-api, gov-api, exchange-gateway
- [x] Spectral rules (`.spectral.yaml`; CI optional)
- [x] Pin checksums at ODTIS v0.9.0-draft freeze - [CHECKSUMS.sha256](CHECKSUMS.sha256), [Annex A freeze record](FREEZE.md)

**Phase 3.2 review (A).**

- [x] Core + gateway bundles validated
- [x] FB-004 autodiscovery documented out of scope
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))
