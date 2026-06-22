# Conformance test: ODTIS-0405 - transitive route rejection

**Status:** implemented (static + unit smoke)
**Requirement:** ODTIS-0405
**Profile:** federation

## Procedure

1. Configure federation agreements A↔B and B↔C without A↔C.
2. Configure catalog or routing so a service on C could be reached from A via B.
3. Send federated request from A targeting C (direct or implied multi-hop).
4. Assert sender gateway rejects before establishing federated exchange with C.

## Pass criteria

Sender gateway denies federated routing without direct bilateral agreement, independent of intermediary connectivity.
