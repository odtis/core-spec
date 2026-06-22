# Conformance test: ODTIS-0305 - redirect URI validation

**Status:** pending implementation
**Requirement:** ODTIS-0305
**Profile:** core-identity

## Procedure

1. Register RP client with redirect URI `https://rp.example/callback`.
2. Initiate authorization with matching redirect - MUST succeed.
3. Repeat with `https://evil.example/callback` - MUST fail.

## Pass criteria

Only registered redirect URIs accepted.
