# Conformance test: Annex C - NIST LoA mapping disclosure

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0105
**Profile:** core-identity, operator
**Annex C:** `loa-matrix.yaml`, `mapping.yaml`

## Procedure

1. Request operator conformance statement and published LoA policy.
2. Verify document maps VenID Low/Medium/High/National to NIST IAL/AAL equivalents.
3. Cross-check mapping against `loa-matrix.yaml` informative crosswalk.

## Pass criteria

Operator publishes NIST mapping; High LoA aligns with biometric proofing per ODTIS-0103.
