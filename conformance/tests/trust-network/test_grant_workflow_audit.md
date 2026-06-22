# Conformance test: ODTIS-0226 - trust-network product requirement

**Status:** implemented (static + unit smoke; live grant audit when stack up)
**Requirement:** ODTIS-0226
**Profile:** trust-network
**Trace:** platform ANALISIS catalog/grants, P04

## Procedure

1. Configure target per declared profile and operator policy.
2. Run `portal-trust-check.sh` and `service-grants-check.sh` (or conformance `run-portal-trust-checks.sh`).
3. Verify grant request, approve, reject, and revoke workflows emit auditable events when audit-service is wired.

## Pass criteria

Implementation satisfies ODTIS-0226 (MUST) as declared in ODTIS spec prose.
