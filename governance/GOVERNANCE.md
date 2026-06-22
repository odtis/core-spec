# ODTIS governance

**Status:** Foundation track A - operational process finalized in Phase 4 
**Editors:** [Maintainers](MAINTAINERS.md) 
**Index:** [Project hub](README.md) | **Project:** [Project hub](../project/README.md)

---

## Foundation documents

| Document | Purpose |
|----------|---------|
| [Foundation charter](FOUNDATION-CHARTER.md) | Mission and board (draft) |
| [IPR policy](IPR-POLICY.md) | Contributions and patents |
| [Spec lifecycle stages](SPEC-STAGES.md) | Draft -> Standard lifecycle |
| [Errata policy](ERRATA.md) | Post-publication corrections |
| [Certification program](CERTIFICATION.md) | L1/L2/L3 program |
| [IETF roadmap](IETF-ROADMAP.md) | Scoped IETF extraction |
| [OIDF positioning](liaison/OIDF-POSITIONING.md) | OpenID bindings |
| [Adoption guide](../ADOPTION.md) | Independent adoption guide |
| [How to cite](../publication/HOW-TO-CITE.md) | Citation |

---

## Stewardship

ODTIS is maintained by editors listed in [Maintainers](MAINTAINERS.md). Final authority for normative changes rests with the specification editors until the ODTIS Foundation board is incorporated.

## Change control (Phase 3)

| Change type | Process |
|-------------|---------|
| Editorial | Direct commit / PR with reviewer |
| New SHOULD/MAY | PR + 7-day review |
| New or changed MUST | PR + RFC issue + 14-day review |
| Profile definition change | RFC + implementer feedback |

## Change control (Phase 4 - post v1.0)

- **Errata:** patch release, no new requirements - [Errata policy](ERRATA.md)
- **Amendment:** minor release with CHANGELOG and migration guide
- **Major revision:** RFC, pilot re-validation, major semver bump

## Conformance certification

See [Certification program](CERTIFICATION.md) and [Self-certification guide](../conformance/certification/self-cert-guide.md).

| Level | Who validates | Output |
|-------|---------------|--------|
| L1 Laboratory | Self | `./conformance/run.sh` PASS |
| L2 Staging | Self + published results | conformance-statement.yaml + L2 JSON |
| L3 Production | Third-party auditor | Attestation letter + report |

## IP and licensing

Normative ODTIS text: [CC BY 4.0](../LICENSE). See [IPR policy](IPR-POLICY.md).

## Appeals and disputes

Disputes on requirement interpretation SHOULD be filed via [Feedback channels](FEEDBACK.md). Maintainers publish clarifications as non-normative errata unless a MUST change is required.
