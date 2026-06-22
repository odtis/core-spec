# Conformance test: ODTIS-0102 - expose active LoA

**Status:** pending implementation
**Requirement:** ODTIS-0102
**Profile:** core-identity

## Procedure

1. Proof subject to Medium LoA.
2. Complete OIDC Authorization Code flow with `openid` scope.
3. Assert ID Token or UserInfo contains `assurance_level` = `medium`.
4. Call Verification API for same subject.
5. Assert response contains matching LoA field.

## Pass criteria

LoA present and consistent across OIDC and Verification API.
