# Conformance test: Annex A - VerifyResponse schema

**Status:** pending implementation
**Requirement:** ODTIS-0316, ODTIS-0317
**Profile:** core-identity
**OpenAPI:** `verification-api.openapi.yaml` - `verification.verify.post`

## Procedure

1. Load OpenAPI bundle from Annex A registry path.
2. Assert `VerifyResponse` requires `verified`.
3. Call live `POST /v1/verify` with valid RP credentials.
4. Validate response against schema; assert `assurance_level` on success or denial per ODTIS-0108.

## Pass criteria

OpenAPI schema matches runtime VerifyResponse behavior.
