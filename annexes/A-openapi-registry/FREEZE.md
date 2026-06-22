# Annex A OpenAPI freeze - 0.9.0-draft

**Phase:** 3.2.2
**Date:** 2026-06-12
**ODTIS spec:** `0.9.0-draft`

Annex A OpenAPI bundles are **frozen for external review** at version **`0.9.0-draft`**. Breaking changes before ODTIS `1.0.0` require a minor bump (`0.9.x-draft`) and CHANGELOG entry.

---

## Frozen bundles

| File | Surface | `info.version` |
|------|---------|----------------|
| `venid-common.openapi.yaml` | Shared | 0.9.0-draft |
| `verification-api.openapi.yaml` | S2 | 0.9.0-draft |
| `citizen-api.openapi.yaml` | S3 | 0.9.0-draft |
| `admin-api.openapi.yaml` | S4, S5 | 0.9.0-draft |
| `reports-api.openapi.yaml` | S6 | 0.9.0-draft |
| `gov-api.openapi.yaml` | S7 | 0.9.0-draft |
| `regulator-api.openapi.yaml` | S8 | 0.9.0-draft |
| `exchange-gateway.openapi.yaml` | Gateway | 0.9.0-draft |
| `INDEX.yaml` | Index | spec_version 0.9.0-draft |
| `oidc-discovery.md` | S1 | informative (not OpenAPI) |

---

## Integrity

Regenerate checksums after any bundle edit:

```bash
python3 scripts/pin-annex-a-checksums.py --write
```

Verify:

```bash
python3 scripts/pin-annex-a-checksums.py
python3 scripts/validate-openapi.py
```

Checksum file: [CHECKSUMS.sha256](CHECKSUMS.sha256)

---

## Change policy (pre-1.0)

| Change type | Action |
|-------------|--------|
| Editorial / description | Patch in place; regenerate checksums |
| New optional field (backward compatible) | `0.9.x-draft` bump |
| New required field, path rename, auth change | New `/v2/` prefix + major bump; RFC required |

At ODTIS `1.0.0`, pin checksums in conformance statements (see Annex A README checklist).

---

## Related

- ODTIS versioning: [Versioning policy](/governance/VERSIONING/)
- Validation: [Validate Openapi script](/scripts/validate-openapi.py)
- Spectral: [.Spectral (YAML)](.spectral.yaml)
