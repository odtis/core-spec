# Conformance test: ODTIS-0521 - OWASP baseline

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0521
**Profile:** core-identity

## Procedure

1. Run OWASP-informed security assessment on citizen portal and public APIs.
2. Verify controls for injection, XSS, CSRF, auth flaws documented.
3. Critical open issues MUST have remediation plan for L2+.

## Pass criteria

No unmitigated critical web vulnerabilities in production scope.
