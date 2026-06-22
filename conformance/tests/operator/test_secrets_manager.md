# Conformance test: ODTIS-0519 - secrets manager

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0519
**Profile:** operator

## Procedure

1. Review deployment manifests and repos for RP secrets and PKI keys.
2. Verify secrets referenced from secrets manager or HSM, not plaintext env.
3. Document secrets rotation procedure.

## Pass criteria

No plaintext secrets at rest in code or config.
