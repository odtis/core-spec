# L3 certification package (VenID reference stack)

**Status:** internal dry-run complete; third-party attestation pending (`GAP-CERT-L3-ATT`) 
**ODTIS version:** `0.9.0-draft` 
**Audience:** operators, internal audit, independent L3 auditors

This page is the **single entry point** for reproducing the VenID Phase 4 L3-target conformance package on the ODTIS project site.

!!! warning "Not an ODTIS Certified claim"
    This package supports **honest Phase 4 staging L3-target self-assessment**. The **ODTIS Certified** mark requires third-party attestation ([GAP-CERT-L3-ATT](gaps/DEFERRED-TRACK.md#gap-cert-l3-att-third-party-l3)).

!!! tip "Independent auditors"
    Start with [Auditor guide](../conformance/certification/auditor-guide.md) and [L3 audit checklist](../conformance/certification/L3-AUDIT-CHECKLIST.md), then use this page for artefacts and reproduce commands.

**Conformance hub:** [Overview](../conformance/README.md) | **Program:** [Certification program](../governance/CERTIFICATION.md)

---

## What this package proves

| Level | What is demonstrated | What is not claimed |
|-------|----------------------|---------------------|
| L1 | Registry, manifests, spec completeness | Live deployment behaviour |
| L2 | Automated checks + smoke scripts against staging | Third-party audit |
| L3 (target) | Full profile scope + Extended modules declared + anti-weakening | **ODTIS Certified** mark without external attestation |

Honest claim today: **Phase 4 staging L3-target self-assessment** with internal tabletop dry-run. See [Deferred production track](gaps/DEFERRED-TRACK.md).

---

## Artefacts

| Artefact | Path |
|----------|------|
| Conformance statement (YAML) | [Conformance statement template](/implementation/statements/venid-phase4-full/conformance-statement.yaml) |
| Human-readable statement | [Phase 4 conformance statement](/implementation/statements/venid-phase4-full/conformance-statement/) |
| L2 automated report | [L2 Report](/implementation/statements/venid-phase4-full/l2-report/) |
| L3 internal dry-run | [L3 Audit Dry Run 2026 Q2 (YAML)](evidence/phase4-conformance/l3-audit-dry-run-2026-Q2.yaml) |
| Extended anti-weakening | [Extended No Weakening 2026 (YAML)](evidence/phase4-conformance/extended-no-weakening-2026.yaml) |
| Gap closure (L2 sandbox) | [Closure Report 2026 Q2 (YAML)](evidence/gap-closure/closure-report-2026-Q2.yaml) |
| RI traceability | [RI surface map](RI-MAP.yaml) |
| Component bindings | [Component bindings](../site/COMPONENT-BINDINGS.md) |
| Deferred production gaps | [Deferred production track](gaps/DEFERRED-TRACK.md) |

---

## Reproduce the package

From repository root (`odtis/`):

```bash
# Full Phase 4 package (statement + L2 + smokes)
./conformance/run-phase4-package.sh

# Optional: live L2 against deployment
ODTIS_TARGET=https://YOUR_REALM ./conformance/run-phase4-package.sh

# Gap closure regression (L2 sandbox evidence)
./conformance/run-gap-closure-checks.sh

# Documentation gates
python3 scripts/validate-section-completeness.py
python3 scripts/validate-component-bindings.py
python3 scripts/sync-test-status-from-smokes.py --assume-pass
python3 scripts/generate-coverage-report.py
```

Expected: statement validates; L2 spec checks PASS; smokes PASS or WARN if live stack down (unit/static fallback).

---

## Profiles and requirements in scope

| Profile | Registry reqs | Key sections |
|---------|---------------|--------------|
| reference-architecture | 10 | 1 |
| core-identity | 45 | 2, 3, 5 |
| trust-network | 26 | 4 |
| federation | 8 | 6 |
| operator | 36 | 7-10 |
| extended | 24 | 5.6-5.7, Annex D |

**Extended modules declared:** E-Wallet, E-Registry, E-Inclusion, E-Webhook, E-Signature, E-KYB (sandbox partial; `venid.*.active=false` by default).

---

## Auditor workflow

1. Read [Auditor guide](../conformance/certification/auditor-guide.md).
2. Execute [L3 audit checklist](../conformance/certification/L3-AUDIT-CHECKLIST.md).
3. Review **deferred** items - do not treat as PASS without evidence:
    - GAP-TN-0204 (live mTLS)
 - GAP-TN-0217 (TSA, if operator policy requires)
 - GAP-CERT-L3-ATT (this engagement)
4. Publish attestation letter + findings register per auditor guide section 5.

---

## Phase statements (historical)

| Phase | Statement |
|-------|-------------|
| Phase 1 | [Venid Phase1 Core](/implementation/statements/venid-phase1-core/) |
| Phase 2 | [Venid Phase2 Trust](/implementation/statements/venid-phase2-trust/) |
| Phase 3 | [Venid Phase3 Operator](/implementation/statements/venid-phase3-operator/) |
| Phase 4 | [Venid Phase4 Full](/implementation/statements/venid-phase4-full/) |

---

## Related

- Certification program: [Certification program](../governance/CERTIFICATION.md)
- Adoption: [Adoption guide](../ADOPTION.md)
- Documentation roadmap: [Documentation roadmap](DOCUMENTATION-ROADMAP.md) (R4)
