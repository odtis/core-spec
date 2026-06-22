# Conformance FAQ

<div class="odtis-hub-hero" markdown="1">

Frequently asked questions about **proving** ODTIS conformance: levels, statements, tests, and common failures.

<p class="odtis-hub-meta" markdown="1">
<strong>Hub:</strong> [Conformance overview](README.md) | 
<strong>General FAQ:</strong> [Site FAQ](../site/FAQ.md) | 
<strong>Adoption:</strong> [Adoption guide](../ADOPTION.md)
</p>

</div>

!!! info "Scope"
    L1/L2/L3, conformance statements, and test procedures only. For downloads, profiles overview, or governance process, see the [Site FAQ](../site/FAQ.md).

---

## Levels and claims

### What is the difference between L1, L2, and L3?

| Level | Question it answers | Who runs it | Public claim? |
|-------|---------------------|-------------|---------------|
| **L1** | Is the spec package structurally sound? | You (CI/local) | Internal only |
| **L2** | Does my deployment behave per ODTIS checks? | You + published evidence | Yes - self-certified staging |
| **L3** | Has an independent party verified production maturity? | Third-party auditor | Yes - **ODTIS Certified** (with program) |

Details: [Certification program](../governance/CERTIFICATION.md) | guides: [Self-cert (L2)](certification/self-cert-guide.md) | [Auditor (L3)](certification/auditor-guide.md)

### Does L1 PASS mean my product conforms?

**No.** L1 means validators pass in the repository (registry links, annex integrity, test stubs exist). Product conformance requires **L2 evidence** against your deployment. L3 is required for the **ODTIS Certified** mark.

### Can I claim "ODTIS compatible" without a conformance statement?

**No meaningful public claim.** Publish [Conformance statement template](templates/conformance-statement.yaml) backed by L1 at minimum and L2 for behaviour claims. Normative basis: spec section 1.9 ([`ODTIS-0008`](../spec/01-scope-conformance/SPEC.md)).

### What is the difference between L2 self-cert and ODTIS Certified?

| | L2 self-cert | ODTIS Certified (L3) |
|---|--------------|----------------------|
| Validator | Operator | Independent auditor |
| Trademark | Not allowed | Allowed with program approval |
| Typical environment | Sandbox / staging | Production |
| Guide | [Self-cert guide](certification/self-cert-guide.md) | [Auditor guide](certification/auditor-guide.md) |

See [Trademark policy](../governance/TRADEMARK-POLICY.md).

---

## Profiles and deployment phases

### Which profiles must I declare?

Declare **every profile your public claim implies**, plus **reference-architecture** (layer and statement rules). List from [Profile definitions](../registry/profiles.yaml). Comparison: [Profile comparison](../site/PROFILES.md).

### What is deployment phase (1-4)?

Phase gates which profiles and Extended sub-modules you may claim ([`ODTIS-0532`](../spec/10-deployment-profiles/SPEC.md)):

| Phase | Typical scope |
|-------|---------------|
| 1 | Core Identity |
| 2 | + Trust Network, Federation |
| 3 | + Operator |
| 4 | + Extended (Annex D sub-modules) |

Your `conformance-statement.yaml` **deployment_phase** must match what you actually deploy. False phase claims fail validation and L3 audit.

### Do I need Federation if I only have one operator?

**No** - declare only profiles you implement. Federation applies to **bilateral cross-operator** trust (section 6). It is not OpenID Federation.

### Can I declare Extended at Phase 2?

**No** - Extended sub-modules are Phase 4 scope per spec section 10. You may implement code earlier, but the **conformance claim** must match phase rules.

---

## Running checks

### What should `ODTIS_TARGET` be?

For Core Identity L2 checks, set the **OIDC realm base URL**, for example:

```text
https://idp.example/realms/citizens
```

Not the admin console, not a single endpoint path. Wrong targets cause discovery FAIL. See [Sandbox alignment](sandbox/README.md).

### Do I need a running stack for L1?

**No.** L1 runs entirely from the repository:

```bash
./conformance/run.sh
```

### What is the fastest path to L2?

```bash
# from repository root
./conformance/run.sh
export ODTIS_TARGET=https://your-idp/realms/your-realm
./conformance/sandbox/run-sandbox-check.sh
```

Then complete your statement: [Self-cert guide](certification/self-cert-guide.md).

### What does `run-phase4-package.sh` do?

VenID reference stack only. It builds the **Phase 4 full-mandate** statement (all profiles + Extended), validates phase rules, and runs Extended/Federation smokes. See [L3 certification package](../implementation/L3-CERTIFICATION-PACKAGE.md).

Independent vendors use the same L1/L2 tools with their own statement - you are not required to run the Phase 4 package.

---

## Conformance statement

### Where is the statement template?

[Conformance statement template](templates/conformance-statement.yaml). Validate with:

```bash
python3 scripts/validate-conformance-statement.py path/to/conformance-statement.yaml
```

### When should `tests.status` be `partial` vs `pass`?

| Value | Use when |
|-------|----------|
| `partial` | L2 automated checks PASS but not all manual procedures executed |
| `pass` | Every declared profile procedure executed with recorded evidence |
| `fail` | Do not publish - fix implementation first |

Pending test stubs in the repo do **not** waive ODTIS MUST requirements.

### What fields are mandatory?

Minimum per [`ODTIS-0008`](../spec/01-scope-conformance/SPEC.md): `odtis_version`, `profiles`, `level`, `operator`, `environment`, `jurisdiction`, `deployment_phase`, `tests`, `date`, `contact`. Generator: `python3 scripts/generate-conformance-statement.py --help`.

### Where should I publish the statement?

| Channel | When |
|---------|------|
| Operator policy / docs site | Production operators |
| GitHub issue with [L2 template](sandbox/L2-REPORT-TEMPLATE.md) | Sandbox feedback, review cycle |
| Attached to procurement / audit pack | L3 engagements |

---

## Tests and coverage

### Why are there 159 procedures but only 81 "implemented"?

The suite links **every registry MUST** to a test procedure stub. `implemented` means this repository has smoke or L2 evidence for that procedure. **Pending** means you must still execute it against your system before claiming `tests.status: pass`.

Live counts: [Project status](../site/STATUS.md). Regenerate: `python3 scripts/sync-test-status-from-smokes.py`.

### Where are the test procedure files?

Under `conformance/tests/<profile>/` in the git repository. They are **not** rendered in the HTML site (size); browse via [Requirements registry](../registry/requirements.json) `conformance_test` links or profile manifests in `conformance/profiles/`.

### Do I need to run every manual stub for L2?

**Recommended honest practice:** run all stubs for declared profiles before `tests.status: pass`. Minimum for a useful L2 claim: automated L2 PASS + representative manual execution documented in your report.

L3 auditors expect full MUST coverage for declared profiles: [L3 checklist](certification/L3-AUDIT-CHECKLIST.md).

### What is stub coverage 100%?

Every registry requirement ID has a linked test **procedure** in the manifest. That is traceability coverage, not proof your deployment passes. Execution is separate.

---

## Common failures

### L2 OIDC discovery FAIL

| Cause | Fix |
|-------|-----|
| Wrong `ODTIS_TARGET` | Use realm root URL (`.../realms/name`) |
| IdP down or TLS error | Fix deployment; retry |
| Issuer mismatch | Realm issuer must match discovery `issuer` field |

### L2 PKCE FAIL

Realm must advertise S256 and reject authorization requests without `code_challenge`. Check Keycloak client/realm OIDC settings.

### Statement validation FAIL on phase

You declared Phase 4 profiles (e.g. `extended`) at `deployment_phase: 1`. Align statement with [Section 10 - Deployment](../spec/10-deployment-profiles/SPEC.md) or reduce declared profiles.

### Smoke PASS but manual stub not done

Normal for early L2. Keep `tests.status: partial` until manual procedures are executed and recorded.

### Gateway mTLS check FAIL or deferred

OpenAPI may declare mTLS while live bilateral handshake is not yet proven. VenID RI tracks this as `GAP-TN-0204`. Document as conditional in L3 audits: [Deferred production track](../implementation/gaps/DEFERRED-TRACK.md).

---

## VenID reference stack

### Do I need VenID code to conform?

**No.** VenID (`ven-identity-core`, `ven-trust-network`) is an **informative** reference implementation. Independent vendors implement ODTIS from the spec and Annex A OpenAPI.

Map: [Reference implementations overview](../implementation/README.md) | bindings: [Component bindings](../site/COMPONENT-BINDINGS.md)

### What is the Phase 4 statement example?

[Phase 4 conformance statement](../implementation/statements/venid-phase4-full/conformance-statement.md) - honest **staging L3-target** scope, not third-party certified.

### What are deferred production gaps?

Four items documented as not yet closable in sandbox (live mTLS, national TSA, IETF TEP track, third-party L3). They do not waive spec MUSTs; they document RI limits. Playbook: [Deferred production track](../implementation/gaps/DEFERRED-TRACK.md).

---

## Auditors and review

### I am an independent auditor - where do I start?

1. [Certification program](../governance/CERTIFICATION.md)
2. [Auditor guide](certification/auditor-guide.md)
3. [L3 audit checklist](certification/L3-AUDIT-CHECKLIST.md)
4. Operator's published statement + L2 JSON

### How do I file sandbox experience for stewards?

Use [L2 report template](sandbox/L2-REPORT-TEMPLATE.md) in a GitHub issue during [External review cycle 1](../governance/REVIEW-CYCLE-1.md).

### Can I suggest a spec clarification from a failed test?

Yes - [Feedback channels](../governance/FEEDBACK.md) for clarifications; [RFC template](../governance/RFC-TEMPLATE.md) for normative changes.

---

<div class="odtis-hub-footer" markdown="1">

## Still stuck?

| Goal | Document |
|------|----------|
| 15-minute implementer path | [Getting started](../site/GETTING-STARTED.md) |
| L2 step-by-step | [Self-cert guide](certification/self-cert-guide.md) |
| Live sandbox checks | [Sandbox README](sandbox/README.md) |
| All certification guides | [Certification guides](README.md#certification-guides) |
| Project status / metrics | [Project status](../site/STATUS.md) |
| Full adoption guide | [Adoption guide](../ADOPTION.md) |

</div>
