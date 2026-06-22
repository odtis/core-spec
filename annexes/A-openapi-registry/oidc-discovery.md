# Surface S1 - OIDC discovery (normative contract summary)

ODTIS Annex A does **not** ship a VenID OpenAPI document for Surface **S1**. The authoritative contract is the IdP **OpenID Connect Discovery** document per [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html).

## Normative endpoints

| Endpoint | ODTIS |
|----------|-------|
| `/.well-known/openid-configuration` | ODTIS-0301 |
| `/protocol/openid-connect/certs` (JWKS) | ODTIS-0301 |
| `/protocol/openid-connect/auth` | ODTIS-0302 |
| `/protocol/openid-connect/token` | ODTIS-0303 |
| `/protocol/openid-connect/userinfo` | ODTIS-0306, ODTIS-0307 |
| `/protocol/openid-connect/logout` or `end_session_endpoint` | ODTIS-0308 |

Paths are realm-scoped in Keycloak deployments (e.g. `/realms/{realm}/protocol/openid-connect/...`).

## Required discovery fields (ODTIS-0301)

Implementations **MUST** publish at minimum:

| Field | Requirement |
|-------|-------------|
| `issuer` | HTTPS issuer identifier matching token `iss` |
| `authorization_endpoint` | Authorization Code entry point |
| `token_endpoint` | Token issuance |
| `userinfo_endpoint` | UserInfo when enabled |
| `jwks_uri` | JWKS for signature verification |
| `response_types_supported` | MUST include `code` |
| `grant_types_supported` | MUST include `authorization_code` |
| `code_challenge_methods_supported` | MUST include `S256` when public clients used |
| `id_token_signing_alg_values_supported` | MUST document algs in use (e.g. `RS256`) |
| `scopes_supported` | MUST include `openid`; SHOULD list custom LoA scopes |
| `subject_types_supported` | MUST document (typically `public`) |
| `end_session_endpoint` | SHOULD when ODTIS-0308 logout enabled |

## Conformance notes

- Public clients **MUST** use PKCE (`S256`) per ODTIS-0302
- Custom claims **MUST** derive from identity-core (ODTIS-0306)
- Custom attributes **MUST NOT** release without consent (ODTIS-0307)
- Logout **MUST** terminate IdP session when `end_session_endpoint` is published (ODTIS-0308)

## Reference

P14 4, ODTIS 3.3.
