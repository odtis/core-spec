# Conformance test: ODTIS-0535 - operator product requirement

**Status:** implemented (static + unit + live E2E smoke)
**Requirement:** ODTIS-0535
**Profile:** operator
**Trace:** Book 2 ch.3.7 rule 1, Book 1 D5

## Automation

```bash
cd core-impl && ./scripts/fail-closed-audit-e2e-check.sh
cd core-spec && ./conformance/run-fail-closed-audit-e2e-checks.sh
```

Evidence: `implementation/evidence/fail-closed-e2e/lab-notes.md`

## Procedure

1. Configure target per declared profile and operator policy.
2. Verify behavior required by: Auth, consent, and grant denial paths MUST fail closed without partial attribute release or implicit trust fallback
3. Record evidence (API traces, audit logs, policy documents, or configuration export).

## Pass criteria

Implementation satisfies ODTIS-0535 (MUST) as declared in ODTIS spec prose.

## VenID reference stack (informative)

Map to `ven-identity-core`, `ven-trust-network`, or Extended modules per `implementation/RI-MAP.yaml`.
