# Conformance test: ODTIS-0504 - Operator subject administration

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0504
**Profile:** operator

## Procedure

1. Authenticate as operator admin (Annex A `admin.subjects.suspend`).
2. Suspend test subject with documented reason and ticket ID.
3. Assert subject cannot complete OIDC login or Verification API access.
4. Invoke `admin.subjects.reverify` and complete proofing path.
5. Export audit log - MUST contain operator ID, reason, and subject_id.

## Pass criteria

Administrative actions are audited and enforce account restrictions without bypassing consent rules.
