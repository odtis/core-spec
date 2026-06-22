# ODTIS L3 auditor guide (draft)

**Status:** `0.9.0-draft` - program finalized in Phase 4.3 
**Audience:** independent auditors, accredited test labs, national conformity bodies

This guide defines the **intended** L3 attestation scope. The certification program is not yet operational until the ODTIS Foundation launches; use this document for scoping engagements today.

!!! warning "L3 is required for the ODTIS Certified mark"
    L2 self-certification alone does not satisfy [Trademark policy](/governance/TRADEMARK-POLICY/). L3 validates production maturity with evidence beyond operator self-assertion.

**Executable checklist:** [L3 audit checklist](L3-AUDIT-CHECKLIST.md) 
**Program rules:** [Certification program](/governance/CERTIFICATION/) 
**VenID reference package:** [L3 certification package](/implementation/L3-CERTIFICATION-PACKAGE/)

---

## 1. Purpose

L3 validates that a deployment satisfies **all MUST requirements** for declared profile(s) in a **production** (or production-equivalent) environment.

| Question | L2 answer | L3 answer |
|----------|-----------|-----------|
| Did automated checks pass? | Yes (self-run) | Yes (verified by auditor) |
| Were manual procedures executed? | Optional | Required with signed lab notes |
| Who attests? | Operator | Independent third party |
| Trademark eligible? | No | Yes (with program approval) |

---

## 2. Prerequisites

Before fieldwork, confirm the operator provides:

| Item | Evidence |
|------|----------|
| ODTIS version pinned | Exact semver in scope document and statement |
| L2 PASS | Published `conformance-statement.yaml` + L2 JSON report |
| Profile scope | Matches [Profile definitions](/registry/profiles.yaml) |
| Deployment phase | Honest per [Section 10 - Deployment](../../spec/10-deployment-profiles/SPEC.md) |
| Extended sub-modules | Listed only if implemented ([`ODTIS-0532`](../../spec/10-deployment-profiles/SPEC.md)) |
| Environment label | `staging` vs `production` clearly stated |

Reject engagements where phase claims exceed deployment reality (e.g. Phase 4 Extended without implemented sub-modules).

---

## 3. Audit scope (per profile)

### Reference Architecture

- Layer dependencies ([`ODTIS-0001`](../../spec/01-scope-conformance/SPEC.md), [`ODTIS-0002`](../../spec/01-scope-conformance/SPEC.md))
- Statement minimum fields ([`ODTIS-0008`](../../spec/01-scope-conformance/SPEC.md))
- Prohibited claims ([`ODTIS-0007`](../../spec/01-scope-conformance/SPEC.md))
- Extended anti-weakening if Extended declared ([`ODTIS-0006`](../../spec/01-scope-conformance/SPEC.md))

### Core Identity

- OIDC discovery, authorization code + PKCE, token and UserInfo behavior
- Verification API (Annex A S2) including LoA claims and client authentication
- Consent grant, revocation, and audit events (sections 5, 9)
- Sample MUST requirements from [Requirements registry](/registry/requirements.json) (sections 2, 3, 5)

### Trust Network

- Exchange gateway mTLS, routing, service grants (section 4, gateway OpenAPI)
- Trust registry validation and certificate revocation behavior
- **Note:** live bilateral mTLS may be deferred - see [Deferred production track](/implementation/gaps/DEFERRED-TRACK/) (`GAP-TN-0204`)

### Federation

- Bilateral agreement configuration, non-transitivity (section 6)
- Suspension and expiry routing policies
- Normative depth expanding via [Federation interoperability RFC](/governance/rfc/2026-06-12-federation-interoperability/)

### Operator

- PKI/CPS publication, regulator export, liability documentation (sections 7-10)
- Security baseline and audit retention samples
- Phase declaration accuracy

### Extended

- Only declared Annex D sub-modules
- Each sub-module: activation policy, fail-closed paths, no weakening of Core/Trust/Federation MUSTs
- Draft registry IDs until v1.0 merge - document as residual risk if applicable

Component bindings (VenID RI): [Component bindings](/site/COMPONENT-BINDINGS/)

---

## 4. Evidence types

| Type | Examples | Weight |
|------|----------|--------|
| **Automated** | L1 `./conformance/run.sh`, L2 `conformance/l2/run_l2.py --target` | Necessary, not sufficient |
| **Manual procedures** | Executed stubs from [Test procedures hub](../tests/README.md) with signed lab notes | Required for L3 |
| **Policy** | CP/CPS, privacy notices, phase declaration documents | Required for Operator |
| **Architecture** | Book 2 alignment (informative only) | Supplementary |

Auditors SHOULD sample across automated PASS and high-risk MUSTs (consent denial, grant fail-closed, federation non-transitivity).

---

## 5. Attestation output

Publish at minimum:

1. **Attestation letter** - profiles, ODTIS version, environment, date, auditor identity
2. **Findings register** - requirement ID, pass/fail/conditional, evidence reference
3. **Residual risks** - SHOULD gaps, deferred production track items, informative Book 2 items not tested

Submit summary for public listing via PR to [Certified Products (YAML)](certified-products.yaml) after program approval.

### Outcome labels

| Outcome | When |
|---------|------|
| **PASS** | All declared MUSTs evidenced; no blocking deferred items |
| **CONDITIONAL PASS** | MUSTs met; documented residual risks (e.g. TSA policy N/A) |
| **FAIL** | MUST not met or false phase/profile claims |

---

## 6. VenID reference stack (Phase 4 L3 package)

For the FinnectOS VenID reference implementation:

| Document | Purpose |
|----------|---------|
| [L3 certification package](/implementation/L3-CERTIFICATION-PACKAGE/) | Artefacts, reproduce commands, profile scope |
| [L3 audit checklist](L3-AUDIT-CHECKLIST.md) | Step-by-step checklist (sections A-F) |
| [Phase 4 conformance statement](/implementation/statements/venid-phase4-full/conformance-statement/) | Declared Phase 4 L3-target statement |
| [L3 Audit Dry Run 2026 Q2 (YAML)](/implementation/evidence/phase4-conformance/l3-audit-dry-run-2026-Q2.yaml) | Internal tabletop (not third-party) |
| [Deferred production track](/implementation/gaps/DEFERRED-TRACK/) | Production gaps to disclose |

**Reproduce automated package:**

```bash
cd odtis
./conformance/run-phase4-package.sh
# Optional live L2:
ODTIS_TARGET=https://YOUR_REALM ./conformance/run-phase4-package.sh
```

**Conditional items:** live mTLS (`GAP-TN-0204`), national TSA if operator policy requires (`GAP-TN-0217`), and this engagement itself (`GAP-CERT-L3-ATT`). Do not issue an unconditional ODTIS Certified attestation until deferred track items are resolved or explicitly documented as residual risk.

---

## 7. Related

- Self-cert L2: [Self-certification guide](self-cert-guide.md)
- Certification index: [Project hub](README.md)
- Adoption path: [Adoption guide](/ADOPTION/)
- Conformance hub: [Project hub](../README.md)
