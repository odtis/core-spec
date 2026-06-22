# Conformance test: ODTIS-0302 - PKCE for public clients

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0302
**Profile:** core-identity

## Procedure

1. Register public OAuth client (no client secret).
2. Start Authorization Code flow without PKCE parameters.
3. Assert authorization endpoint rejects request.
4. Repeat with valid `code_challenge` / `code_verifier`.
5. Complete flow and obtain tokens.

## Pass criteria

Public client cannot authorize without PKCE.
