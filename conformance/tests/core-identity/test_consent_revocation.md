# Conformance test: ODTIS-0330 - consent revocation

**Status:** pending implementation
**Requirement:** ODTIS-0330
**Profile:** core-identity

## Procedure

1. Grant consent for RP; verify attribute release works.
2. Revoke consent via citizen portal.
3. Invoke Verification API and OIDC UserInfo on subsequent request.
4. Assert restricted attributes denied.
5. Verify `consent.revoked` audit event emitted.

## Pass criteria

Revocation effective immediately for new requests.
