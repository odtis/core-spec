# Extended: E-Registry - National LoA

**Status:** implemented (unit + staging overlay smoke)
**Sub-module:** E-Registry
**Requirements:** ODTIS-0344, ODTIS-0350 (draft)
**Profile:** extended
**Min phase:** 3

## Procedure

1. Run `eregistry-adapter-check.sh` (NationalLoaUpgradeServiceTest + ERegistryVerificationServiceTest).
2. Optional staging: `./scripts/eregistry-staging-up.sh` with sandbox bilateral agreement mounted.
3. High LoA without registry match MUST NOT yield National LoA; sandbox match MAY upgrade.

## Pass criteria

National LoA gated on E-Registry declaration, adapter activation, and successful verification.
