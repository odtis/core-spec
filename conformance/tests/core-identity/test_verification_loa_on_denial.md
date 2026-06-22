# Conformance test: ODTIS-0108 - Verification API LoA on denial

**Status:** pending implementation
**Requirement:** ODTIS-0108
**Profile:** core-identity

## Procedure

1. Proof subject to Medium LoA.
2. Invoke Verification API with RP context where attribute release is denied (consent withheld or scope insufficient).
3. Assert response includes denial reason.
4. Assert response includes `assurance_level` = `medium`.

## Pass criteria

LoA returned on denied attribute release.
