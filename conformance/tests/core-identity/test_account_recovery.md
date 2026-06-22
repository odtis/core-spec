# Conformance test: ODTIS-0309 - Account recovery

**Status:** pending implementation
**Requirement:** ODTIS-0309
**Profile:** core-identity

## Procedure

1. Register test subject with verified contact channel.
2. Initiate password reset or MFA recovery flow.
3. Assert identity verification step required (OTP, proofing, or step-up MFA).
4. Complete recovery; assert new credentials work.
5. Exceed rate limit threshold on recovery endpoint - MUST return 429 per ODTIS-0326.
6. Verify audit events `identity.recovery.initiated` and `identity.recovery.completed` in export.

## Pass criteria

Recovery requires identity verification; rate limits enforced; auditable events emitted.
