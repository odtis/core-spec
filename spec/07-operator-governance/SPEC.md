---
title: "Section 7: Operator governance"
description: DTI operator model, published service scope, SLA metrics, PKI stewardship, and regulator API requirements.
---

# 7 Operator governance

<div class="odtis-spec-meta" markdown="1">

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Derived from** | P18 8, P10, P08, Book 1 ch. 13 |
| **Registry IDs** | ODTIS-0501 - ODTIS-0516, ODTIS-0536 (17 requirements) |
| **Profile** | Operator (requires Core Identity; independent of Trust Network) |

</div>

---

## 7.1 Scope

This section normatively defines **DTI operator** obligations: organizational governance, PKI stewardship, service levels, partner onboarding, regulator access, incident response, and **documented liability allocation**.

Operator profile conformance **requires** Core Identity (1.6.4). Operators claiming Trust Network or Federation MUST also satisfy 4 and 6 operator duties cross-referenced here.

The operator **does not replace** civil registry authority, sector regulators, or national certification bodies (1.14). ODTIS documents **operational and technical duties**, not statutory liability outcomes.

---

## 7.2 Operator role and mandate

!!! note "Requirement ID numbering"
    Registry IDs **`ODTIS-7.1.x`** appear in this section (7.2). **`ODTIS-7.2.x`** appear in 7.3 (deployment phase), **`ODTIS-7.3.x`** in 7.4 (PKI), **`ODTIS-7.4.x`** in 7.5 (SLA), and **`ODTIS-7.5.x`** in 7.6 (regulator and liability). Section **7.8** indexes all 16 IDs.

A **DTI operator** runs identity platform and/or trust network infrastructure under mandate, contract, enterprise charter, or public-private arrangement.

### 7.2.1 Responsibilities (informative summary)

| Area | Operator duty |
|------|----------------|
| Platform | Operate declared ODTIS profiles with conformance statement |
| Policy | Publish operator policy, privacy policy, RP admission criteria |
| PKI | Steward partner and service CA hierarchy when Trust Network claimed |
| Audit | Maintain auditable events and regulator export paths (9) |
| Ecosystem | Onboard partners and RPs under documented rules |
| Incident | Execute documented incident response and escalation |

---

### ODTIS-0501 - Published service scope

The operator **MUST** publish the **scope of services** corresponding to declared ODTIS profiles:

- Core Identity;
- Trust Network;
- Federation; and
- Extended sub-modules (E-Wallet, E-Registry, etc.).

Publication MUST appear in the conformance statement (1.9) and operator-facing service catalog or policy site.

**Trace (informative):** P10
**Conformance test:** Compare live deployment capabilities to published scope; undeclared profiles MUST NOT be implied.

---

### ODTIS-0502 - Documented governance structure

The operator **MUST** maintain **documented governance** covering at minimum:

| Unit | Scope |
|------|-------|
| **Technology** | Architecture, security, PKI, change management |
| **Institutional** | Partner and RP relations, sector policy |
| **Operations** | SOC, runbooks, on-call, DR |
| **Commercial** | Pricing transparency, contracts, billing (where applicable) |

Documentation MUST identify accountable roles (named or role-based) and review cadence.

**Trace (informative):** P10 4
**Conformance test:** Review governance document set; all four units addressed.

---

### ODTIS-0503 - Delegated operator models

**National-scale deployments SHOULD** follow **delegated-operator** or **public-private partnership (PPP)** models with **audit rights for the state** or supervising authority where applicable.

This is a SHOULD for jurisdictional fit; deviations MUST be documented in operator policy with rationale.

**Trace (informative):** P10 5
**Conformance test:** National deployments (L2+): review mandate or PPP agreement for audit rights clause.

---

### ODTIS-0504 - Operator subject administration

The operator **MUST** provide **controlled administration** of subject identities for exceptional cases, including at minimum:

- **suspend** or **unsuspend** a subject account;
- **force re-verification** when fraud or data quality issues are suspected; and
- **audit** every administrative action with operator identity, reason, and ticket reference.

Administrative actions MUST NOT bypass consent or LoA rules for attribute release without documented legal basis in operator policy.

**Trace (informative):** RF-27, P14 7 (Book 2 ch.4 admin API alignment, informative)
**Conformance test:** Suspend test subject via admin API; verify audit event and blocked login.

---

## 7.3 Deployment phase and maturity

Operator maturity MUST align with **deployment phase** (10) and MUST NOT be misrepresented in conformance claims.

**Table 7-1 - Phase-appropriate capabilities (informative)**

| Capability | Phase 1-2 (pilot) | Phase 3-4 (national operator) |
|------------|-------------------|-------------------------------|
| PKI | Software CA, CRL | HSM hierarchy, OCSP, TSA, CPS |
| Security operations | Monitored stack, core runbooks | 24/7 SOC, DR site |
| Certifications | Documented roadmap | ISO 27001/22301, WebTrust/ETSI where applicable |
| Federation | Single-hub topology | Bilateral agreements operational |

---

### ODTIS-0505 - Phase-appropriate maturity in conformance statement

The operator **MUST** document **phase-appropriate PKI and SOC maturity** in the **conformance statement**, including:

- current deployment phase (10);
- PKI tier (software CA vs HSM);
- SOC coverage (hours, monitoring scope); and
- planned maturity roadmap if below Phase 4 targets.

**Trace (informative):** P10 6, P08
**Conformance test:** Conformance statement contains PKI and SOC maturity subsection matching observed deployment.

---

### ODTIS-0506 - No false Phase 4 claims

The operator **MUST NOT** claim **Phase 4 certification targets** (for example, ISO 27001 certified, qualified trust service equivalence) while operating **Phase 1-2 profile only**.

Roadmap references to future certification MUST be labeled as planned, not achieved.

**Trace (informative):** P10
**Conformance test:** Audit conformance statement and marketing materials for prohibited forward claims presented as current state.

---

## 7.4 PKI stewardship

Requirements in this subsection apply when **Trust Network** profile is claimed. Cross-reference 4.7 for technical exchange controls.

### ODTIS-0507 - CP/CPS

The operator **MUST** maintain a **Certificate Policy (CP)** and **Certification Practice Statement (CPS)** for network PKI covering partner and service certificates.

CP/CPS MUST define issuance, renewal, revocation, and key sizes aligned with ODTIS-0215.

**Trace (informative):** P08 7
**Conformance test:** Published CP/CPS version referenced in conformance statement; partner certs conform to policy.

---

### ODTIS-0508 - Key ceremonies

**Root and issuing key ceremonies MUST** be **documented** with **dual control** where **HSM** or equivalent hardware key storage is used.

Ceremony records MUST be retained per operator retention policy and SHOULD emit `operator.pki.ceremony` audit events (9).

**Trace (informative):** P08
**Conformance test:** Review ceremony log sample; dual control attestation for last root rotation.

---

### ODTIS-0509 - CRL or OCSP

The operator **MUST** operate **CRL or OCSP publication** for partner certificates (consistent with ODTIS-0216).

Revocation infrastructure MUST be available to gateway verification paths with documented freshness SLA.

**Trace (informative):** P08 4
**Conformance test:** Fetch CRL/OCSP for sample partner cert; gateway rejects revoked cert.

---

### ODTIS-0510 - PKI disaster recovery

**PKI backup, restore, and disaster recovery MUST** be **tested** on a **documented schedule** with results retained for audit.

Tests MUST cover at minimum: CA key backup integrity, CRL/OCSP continuity, and certificate re-issuance procedure.

**Trace (informative):** P08, RNF-08
**Conformance test:** Review last DR test report and schedule; evidence of successful restore exercise.

---

## 7.5 Service levels and ecosystem rules

### ODTIS-0511 - Core Identity availability

When **Core Identity** is claimed, the operator **MUST** publish **availability targets** for **IdP** and **Verification API**.

Design target: **≥99.5%** monthly availability unless operator policy documents a different measured target with rationale (RNF-07).

Trust Network gateway SLA is separately required by ODTIS-0220 when both profiles are claimed.

**Trace (informative):** P10, RNF-07
**Conformance test:** Operator SLA document lists IdP and Verification API availability metrics.

---

### ODTIS-0512 - Partner onboarding and transparency

The operator **MUST** define rules for:

- **partner onboarding** (Trust Network);
- **partner certification** or technical accreditation; and
- **pricing transparency** for ecosystem participants where commercial fees apply.

Rules MUST be published before production onboarding.

**Trace (informative):** P10 9
**Conformance test:** Published partner handbook or policy covers onboarding, certification, and fee schedule (if any).

---

### ODTIS-0513 - Ecosystem metrics

The operator **SHOULD** publish **product and business metrics** for ecosystem health, such as:

- registrations and verifications volume;
- error rates and manual review backlog; and
- service availability summaries.

Aggregation MUST avoid unnecessary PII exposure (RNF-25).

**Trace (informative):** P10, RNF-25
**Conformance test:** Public or regulator dashboard with aggregated metrics (L2+ SHOULD).

---

## 7.6 Regulator access, incidents, and liability

### ODTIS-0514 - Regulator export path

The operator **MUST** provide a **regulator API** or **documented export path** for **aggregated audit metrics** without unnecessary PII exposure in log bodies (cross-ref ODTIS-0530, ODTIS-0528).

Export MUST support correlation ID tracing for supervised investigations without bulk citizen PII dumps.

**Trace (informative):** RNF-17, RNF-25, P14 8
**Conformance test:** Execute regulator export; verify aggregated fields and PII minimization.

---

### ODTIS-0515 - Incident response

The operator **MUST** support **incident response procedures** with **documented escalation** paths covering:

- security incidents;
- fraud and impersonation spikes; and
- platform outages affecting Core Identity or Trust Network.

Procedures MUST reference roles, communication channels, and regulatory notification triggers per applicable law (documented in operator policy).

**Trace (informative):** P07, RNF-06
**Conformance test:** Review incident response runbook; table-top exercise record (L2+).

---

### ODTIS-0516 - Liability documentation

**Liability allocation** between **operator**, **Relying Parties**, and **citizens** **MUST** be **documented** in:

- operator terms of service or equivalent; and
- **RP contracts** (cross-ref ODTIS-0338).

Documentation MUST address at minimum: data handling duties, breach notification responsibilities, and limitation of operator liability for RP misuse after consented attribute release.

Legal enforceability is jurisdiction-specific; ODTIS requires **documentation existence and publication**, not adjudication of legal outcomes.

**Trace (informative):** Book 1 ch. 13, G-25
**Conformance test:** Review operator terms and sample RP contract for liability clauses.

---

### ODTIS-0536 - Reference implementation traceability map

When claiming **VenID-class** or multi-component ODTIS deployments at **L2+**, the operator **MUST** maintain a **reference implementation map** (or equivalent component-to-profile trace) that links:

- declared ODTIS profiles and Extended sub-modules;
- deployable components or services; and
- primary `ODTIS-xxxx` IDs satisfied by each surface.

The map MUST be available to auditors and conformance reviewers. A machine-readable example lives in [RI surface map](/implementation/RI-MAP.yaml) (informative template).

**Trace (informative):** ADOPTION.md, Book 2 ch. 3, implementation backlog
**Conformance test:** Review RI map; every declared profile has at least one mapped component or documented gap.

---

## 7.7 Cross-references

| Topic | Section |
|-------|---------|
| RP admission and suspension | ODTIS-0337, 5.3.3 |
| Privacy policy | ODTIS-0333 |
| PKI exchange controls | 4.7 |
| Gateway SLA | ODTIS-0220 |
| Audit events and export | 9 |
| Deployment phases | 10 |
| Conformance statement | 1.9 |

---

## 7.8 Requirement index

<!-- GENERATED:section-index:START -->
<!-- Generated by scripts/generate-spec-section-indexes.py @ 0.9.0-draft -->

**Table 7-* - Requirement index (17 IDs)**

| ID | Keyword | Summary |
|----|---------|---------|
| ODTIS-0501 | MUST | Operator MUST publish scope of services (Core, Trust Network, Extended … |
| ODTIS-0502 | MUST | Operator MUST maintain documented governance: technology, institutional… |
| ODTIS-0503 | SHOULD | National-scale deployments SHOULD follow delegated-operator or PPP mode… |
| ODTIS-0504 | MUST | Operator MUST provide audited subject administration (suspend, force re… |
| ODTIS-0505 | MUST | Operator MUST document phase-appropriate PKI and SOC maturity in confor… |
| ODTIS-0506 | MUST NOT | Operator MUST NOT claim Phase 4 certification targets while operating P… |
| ODTIS-0507 | MUST | Operator MUST maintain Certificate Policy and Certification Practice St… |
| ODTIS-0508 | MUST | Root and issuing key ceremonies MUST be documented with dual control wh… |
| ODTIS-0509 | MUST | Operator MUST operate CRL or OCSP publication for partner certificates |
| ODTIS-0510 | MUST | PKI backup, restore, and disaster recovery MUST be tested on a document… |
| ODTIS-0511 | MUST | Operator MUST publish availability targets for IdP and verification API… |
| ODTIS-0512 | MUST | Operator MUST define partner onboarding, certification, and pricing tra… |
| ODTIS-0513 | SHOULD | Operator SHOULD publish product and business metrics for ecosystem heal… |
| ODTIS-0514 | MUST | Operator MUST provide regulator API or export path for aggregated audit… |
| ODTIS-0515 | MUST | Operator MUST support incident response procedures with documented esca… |
| ODTIS-0516 | MUST | Liability allocation between operator, RPs, and citizens MUST be docume… |
| ODTIS-0536 | MUST | Operator MUST maintain a reference implementation map or equivalent com… |

<!-- GENERATED:section-index:END -->

---

## Document history

| Version | Date | Change |
|---------|------|--------|
| stub | 2026-06-12 | Scaffold Phase 3.0 |
| draft v0.5 | 2026-06-12 | 7.1-7.8 normative prose; 16 IDs |
| 0.9.0-draft | 2026-06-12 | Phase 3.2 section review; ID numbering note; index table fix |

**Phase 3.1 checklist (7).**

- [x] Operator role, governance, phase maturity
- [x] PKI stewardship (CP/CPS, ceremonies, CRL/OCSP, DR)
- [x] SLA, partner rules, regulator access
- [x] Incident response and liability documentation


**Phase 3.2 review checklist (7).**

- [x] Registry IDs cited in normative prose
- [x] Requirement index matches registry
- [x] Conformance test stub per ID
- [ ] External review cycle 1 ([Section review matrix](/governance/SECTION-REVIEW/))
