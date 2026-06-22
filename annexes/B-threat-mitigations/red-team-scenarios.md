# Annex B - Red-team scenario appendix (draft)

**Status:** review draft - operator acceptance scenarios @ 0.9.0-draft
**Source:** P07 Table 1, ODTIS-8.x reverse index

Scenarios below exercise Annex B threat rows against observable controls. They are **informative** acceptance tests; normative requirements remain in sections 8 and mapped ODTIS-8.x IDs.

---

## Scenario RT-01 - Stolen RP client credentials

| Field | Value |
|-------|-------|
| Threat | T-07 credential theft |
| Control | ODTIS-0315, ODTIS-0321, ODTIS-0521 |
| Steps | Exfiltrate RP client secret; attempt Verification API calls from foreign IP |
| Expected | 401/403; operator alert; optional RP suspension via ODTIS-0339 |

## Scenario RT-02 - Consent bypass via custom claims

| Field | Value |
|-------|-------|
| Threat | T-03 excessive attribute disclosure |
| Control | ODTIS-0307, ODTIS-0317, ODTIS-0331 |
| Steps | Request custom scopes without consent record |
| Expected | UserInfo/verify omit restricted attributes; `consent_denied` error code |

## Scenario RT-03 - Gateway direct backend access

| Field | Value |
|-------|-------|
| Threat | T-12 trust zone bypass |
| Control | ODTIS-0201, ODTIS-0203, ODTIS-0517 |
| Steps | Partner mTLS to internal service URL bypassing gateway |
| Expected | Connection refused or unrouted; exchange audit shows denial |

## Scenario RT-04 - Revoked partner certificate

| Field | Value |
|-------|-------|
| Threat | T-08 certificate compromise |
| Control | ODTIS-0205, ODTIS-0216, ODTIS-0509 |
| Steps | Use revoked partner cert on gateway |
| Expected | TLS or application-level rejection before backend |

## Scenario RT-05 - Account recovery abuse

| Field | Value |
|-------|-------|
| Threat | T-05 credential stuffing / recovery abuse |
| Control | ODTIS-0309, ODTIS-0326 |
| Steps | Automate recovery requests for victim identifier |
| Expected | Rate limit 429; no credential reset without verification |

---

## Review checklist

- [x] Initial scenario set aligned to 18 Annex B rows (subset above)
- [ ] Review with security white paper (O-1, Phase 2.9)
- [ ] Operator tabletop exercise record template

See [Threat mitigations catalog](threats.yaml) for full threat -> ODTIS-8.x mapping.
