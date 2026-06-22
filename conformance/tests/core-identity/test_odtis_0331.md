# Conformance test: ODTIS-0331 - Scope enforcement

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0331
**Profile:** core-identity

## Related requirements

| ID | Layer | Focus |
|----|-------|-------|
| ODTIS-0307 | OIDC IdP | Custom claims gated on active consent |
| ODTIS-0317 | Verification API | Attribute release gated on consent scopes |

Composite coverage: `test_consent_gated_claims.md` (3.1.7), `test_verification_consent_scope.md` (3.5.3).

## Procedure

1. Register subject with verified attributes; grant consent for scope set **A** only (exclude scope set **B**).
2. **Verification API:** request attributes in scope **B**; expect denial (403 or empty attributes with denial code).
3. **OIDC:** request token or userinfo for claims outside consented scopes; expect omission or denial per operator policy.
4. Inspect all denial payloads (HTTP body, OIDC error, Verification API error object) for restricted attribute values.

## Pass criteria

- No attributes outside active consented scopes are returned on any path.
- Denial payloads MUST NOT include restricted attribute values (names alone MAY appear; values MUST NOT).
