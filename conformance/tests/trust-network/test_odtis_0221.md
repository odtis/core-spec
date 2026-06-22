# Conformance test: ODTIS-0221

**Status:** implemented (static + unit/live smoke)
**Requirement:** ODTIS-0221 
**Profile:** trust-network

## Procedure

1. Configure target deployment per conformance statement.
2. Verify published gateway SLA doc maps NIST SP 800-207 principles to VenID controls (continuous verification, least privilege, micro-segmentation).
3. Run `./scripts/exchange-audit-check.sh` (or conformance `run-exchange-sla-checks.sh`).

## Pass criteria

Implementation satisfies ODTIS-0221 MUST/SHOULD as declared in spec prose.
