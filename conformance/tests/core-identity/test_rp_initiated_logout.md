# Conformance test: ODTIS-0308 - RP-initiated logout

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0308
**Profile:** core-identity

## Procedure

1. Complete Authorization Code + PKCE login for a public RP client.
2. Obtain refresh token if issued.
3. Invoke RP-Initiated Logout (`end_session_endpoint`) or equivalent user logout UI.
4. Attempt token refresh with prior refresh token - MUST fail.
5. Start new authorization without re-authentication - MUST require login if session terminated.

## Pass criteria

IdP session terminated; refresh tokens invalidated; optional front/back-channel logout propagated when enabled.
