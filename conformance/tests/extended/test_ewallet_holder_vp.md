# Extended: E-Wallet - holder-signed VP

**Status:** implemented (static + unit smoke)
**Sub-module:** E-Wallet
**Requirements:** ODTIS-0340, ODTIS-0524
**Profile:** extended

## Procedure

Present VC without holder-signed VP; Verification Gateway MUST reject. Valid OID4VP with holder signature MUST succeed when issuer is trusted (ODTIS-0346).

## Pass criteria

VC-only copy attack fails; signed VP passes per Annex B T-P07-011.
