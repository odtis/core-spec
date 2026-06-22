---
title: Getting started with ODTIS
description: 15-minute path to read the spec, pick a profile, run L1 validators, and plan an honest conformance claim.
---

# Getting started with ODTIS

<div class="odtis-hub-hero" markdown="1">

Fifteen-minute path for independent implementers.

<p class="odtis-hub-meta" markdown="1">
<strong>Spec index:</strong> [Specification index](../spec/INDEX.md) | 
<strong>Adoption:</strong> [Full adoption guide](../ADOPTION.md) | 
<strong>Conformance:</strong> [Conformance overview](../conformance/README.md) | 
<strong>Project hub:</strong> [Project hub](../project/README.md)
</p>

</div>

!!! tip "Conformance is not optional for claims"
    If you publish an ODTIS profile claim, you need a [Conformance statement template](../conformance/templates/conformance-statement.yaml) backed by L1 at minimum and L2 for staging/production behaviour. Start with [Conformance overview](../conformance/README.md).

---

## 1. Pick a profile

| If you build... | Declare | Deployment phase (typical) |
|-----------------|---------|--------------------------|
| Citizen IdP + verification API | **Core Identity** | Phase 1 |
| Partner gateway / exchange | Core Identity + **Trust Network** | Phase 2 |
| Cross-operator bilateral trust | + **Federation** | Phase 2+ |
| Platform operator duties (PKI, audit) | + **Operator** | Phase 3 |
| Wallet, webhooks, KYB, etc. | + **Extended** (sub-modules) | Phase 4 |

Always include **Reference Architecture** rules when publishing any claim ([`ODTIS-0001`](../spec/01-scope-conformance/SPEC.md) through [`ODTIS-0010`](../spec/01-scope-conformance/SPEC.md)).

Profile docs: [Profile comparison](PROFILES.md) | normative packs linked from each profile row

---

## 2. Read normative scope

1. [Section 1 - Scope and conformance](../spec/01-scope-conformance/SPEC.md) - levels, claims, keywords (section 1.9)
2. Mandatory sections for your profile(s) in [Profile definitions](../registry/profiles.yaml)
3. Section prose for each mandatory block (Specification tab)
4. Deployment phase rules: [Section 10 - Deployment](../spec/10-deployment-profiles/SPEC.md)

---

## 3. Bind machine-readable artifacts

| Artifact | Path |
|----------|------|
| OpenAPI (Annex A, frozen) | [Annex A - OpenAPI registry](../annexes/A-openapi-registry/README.md) |
| Requirement IDs | [Requirements registry](../registry/requirements.json) |
| OIDC binding notes | [OIDF positioning](../governance/liaison/OIDF-POSITIONING.md) |

Downloads: [Downloads & artifacts](DOWNLOADS.md)

---

## 4. Verify (L1 then L2)

### L1 - repository (no live stack required)

```bash
# from repository root
./conformance/run.sh
```

### L2 - live deployment (recommended before publishing)

```bash
export ODTIS_TARGET=https://your-idp/realms/your-realm
./conformance/sandbox/run-sandbox-check.sh
```

Reports land in `conformance/reports/`. Sandbox alignment map: [Sandbox alignment](../conformance/sandbox/README.md).

---

## 5. Publish your claim

1. Copy [Conformance statement template](../conformance/templates/conformance-statement.yaml).
2. Fill profiles, `deployment_phase`, `environment`, and `tests.report_path`.
3. Follow the [Self-certification guide](../conformance/certification/self-cert-guide.md).
4. Optional: file a sandbox report using the [L2 report template](../conformance/sandbox/L2-REPORT-TEMPLATE.md).

!!! warning "Trademark"
    L2 self-cert does **not** grant the **ODTIS Certified** mark. See [Trademark policy](../governance/TRADEMARK-POLICY.md).

---

## What level do I need?

| Your claim | Minimum level | Guide |
|------------|---------------|-------|
| "We track ODTIS draft" | L1 (internal) | [Conformance README](../conformance/README.md) |
| "Staging deployment meets profiles X" | L2 + published statement | [Self-cert](../conformance/certification/self-cert-guide.md) |
| "Production ODTIS Certified" | L3 third-party audit | [Auditor guide](../conformance/certification/auditor-guide.md) |

---

<div class="odtis-hub-footer" markdown="1">

## Still stuck?

| Goal | Document |
|------|----------|
| [Compare profiles](PROFILES.md) | Profile dependencies |
| [Conformance hub](../conformance/README.md) | L1/L2/L3 path |
| [Conformance FAQ](../conformance/FAQ.md) | Test and statement questions |
| [Project status](STATUS.md) | Live metrics |
| [Contribute](../governance/CONTRIBUTING.md) | PR workflow |

</div>
