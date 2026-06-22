# Conformance test: ODTIS-0328 - explicit consent before first release

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0328
**Profile:** core-identity

## Procedure

1. Register RP with custom attribute scopes.
2. Authenticate subject (first interaction with RP).
3. Before consent acceptance, call UserInfo or Verification API for custom attributes.
4. Assert attributes withheld or request blocked.
5. Accept consent prompt.
6. Repeat attribute request - assert release permitted.

## Pass criteria

No custom attribute release before explicit consent.
