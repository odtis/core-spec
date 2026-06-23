# Conformance test: ODTIS-0532 - phase declaration

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0532
**Profile:** operator

## Procedure

1. Obtain conformance statement for production environment.
2. Verify deployment phase field present (1-4).
3. Verify Extended sub-modules list matches production feature set.
4. Verify Reliance Extension sub-modules list (`reliance_extensions`) matches production when `reliance-extensions` profile is claimed.
5. Cross-check with live config and Annex E activation matrix.

## Pass criteria

Phase, Extended modules, and Reliance Extension modules accurately declared.
