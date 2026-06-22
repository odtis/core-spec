# Conformance test: Annex B - ODTIS-0523 liveness threat mapping

**Status:** pending implementation
**Requirement:** ODTIS-0523
**Profile:** core-identity
**Annex B:** `T-P07-005` (Presentation attack)

## Procedure

1. Load `annexes/B-threat-mitigations/threats.yaml`.
2. Confirm `T-P07-005` lists `ODTIS-0523` and `ODTIS-0312`.
3. Attempt High LoA proofing without liveness signal; implementation MUST reject or queue manual review.

## Pass criteria

Threat row maps to live control; High LoA cannot bypass liveness per ODTIS-0523.
