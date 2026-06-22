# Conformance test: ODTIS-0307 - consent-gated custom claims

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0307, ODTIS-0331
**Profile:** core-identity

## Procedure

1. Register RP with custom scope requiring extended attributes.
2. Authenticate subject without granting consent for custom scope.
3. Request UserInfo or token with custom scope.
4. Assert custom attributes absent or request denied; error payload MUST NOT leak restricted values (ODTIS-0331).
5. Grant consent; repeat request; assert attributes released.

## Pass criteria

Custom attributes never released without active consent.
