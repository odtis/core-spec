# Conformance test: ODTIS-0512

**Status:** implemented (static + kit verification smoke)
**Requirement:** ODTIS-0512 
**Profile:** operator

## Automation

```bash
cd core-impl/ven-trust-network && ./scripts/partner-node-kit-check.sh
cd core-spec && ./conformance/run-partner-node-kit-checks.sh
```

Evidence: `implementation/evidence/partner-node-kit/lab-notes.md`

## Procedure

1. Configure target deployment per conformance statement.
2. Exercise behavior required by: Operator MUST define partner onboarding, certification, and pricing transparency...
3. Record evidence (request/response, logs, or policy document as applicable).

## Pass criteria

Implementation satisfies ODTIS-0512 MUST/SHOULD as declared in spec prose.
