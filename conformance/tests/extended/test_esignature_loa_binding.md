# Extended: E-Signature - LoA binding

**Status:** implemented (static + unit smoke)
**Sub-module:** E-Signature
**Requirements:** ODTIS-0361 (draft)
**Profile:** extended
**Min phase:** 3

## Procedure

Attempt signature operation with subject below RP minimum LoA; MUST fail. Repeat with sufficient LoA; signature record MUST link subject_id and client_id in audit.

## Pass criteria

Signatures bound to verified identity and LoA policy.
