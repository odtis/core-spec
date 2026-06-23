# Annex E - Reliance Extensions

| Field | Value |
|-------|-------|
| **Status** | review draft - Phase 3.2 |
| **Spec version** | 0.9.0-draft |
| **Source** | manuelmerida.io DTI editorial feed (The DTI problem) |
| **Profile** | `reliance-extensions` (optional; depends on Core Identity) |
| **Domain** | ODTIS-0007 |

---

## Purpose

Annex E defines **optional Capa B reliance overlays**: governance profiles that specify *who may rely on a trust signal, for what purpose, with what assurance, audit evidence, revocation/step-up, and recourse*. Each sub-module specializes the **R-Base** reliance schema (`ODTIS-0701..0708`) for a specific reliance context and **MUST NOT weaken** Core, Trust Network, Federation, or Operator requirements.

These overlays were derived from the DTI editorial analysis (see `analisis/status/09-PROFILES-EMERGENTES-ARTICULOS-DTI.md`). Status: **normative @ 0.9.0-draft** (optional profile; declare only active sub-modules in production).

---

## Sub-modules

| ID | Title | Tier | Min phase | Status |
|----|-------|------|-----------|--------|
| **R-Base** | Reliance Profile base schema | 0 | 1 | draft |
| **R-Agent-Authority** | Agent authority reliance (Capa B for AI agents) | 1 | 2 | draft |
| **R-Crypto-Agility** | Crypto-agility assurance (PQC / HNDL) | 1 | 2 | draft |
| **R-Lifecycle-Revocation** | Identity lifecycle revocation (workforce/passkeys) | 1 | 2 | draft |
| **R-Document-Capture** | Document capture reliance (deepfake/injection) | 1 | 2 | draft |
| **R-Liveness** | Liveness reliance (presence != trust) | 1 | 2 | draft |
| **R-Disclosure-Assurance** | Disclosure assurance (audience-bound audit) | 1 | 2 | draft |
| **R-Assurance-Portability** | Assurance portability (reusable KYC) | 1 | 2 | draft |
| **R-VC-Maturity-Gate** | VC standards maturity gate | 1 | 1 | draft |
| **R-Public-eID** | Public-sector eID reliance (multi-eID coexistence) | 1 | 2 | draft |
| **R-Fraud-Orchestration** | Fraud event orchestration (PSD3/PSR) | 2 | 3 | preview |
| **R-Stablecoin-CIP** | Stablecoin CIP reliance (GENIUS Act) | 2 | 3 | preview |
| **R-Travel** | Cross-border travel reliance (ICAO/IATA) | 2 | 3 | preview |
| **R-CRA-Resilience** | CRA trust-resilience (software supply chain) | 2 | 3 | preview |
| **R-DPI-Resilience** | DPI trust resilience (blast-radius control) | 2 | 3 | preview |
| **R-Sovereign-Chain-Interop** | Sovereign identity-chain interop (reference) | 3 | 4 | preview |
| **R-LE-Biometric** | Law-enforcement biometric reliance (sensitive) | 3 | 4 | preview |

Full catalog: [Sub Modules (YAML)](sub-modules.yaml) | requirements: [Reliance Requirements (YAML)](reliance-requirements.yaml) | index: [Surface index (YAML)](INDEX.yaml).

---

## Declaration rules

1. Conformance statements **MUST** list active reliance sub-modules and phase (**ODTIS-0708**).
2. Reliance Extensions **MUST NOT** weaken Core / Trust Network / Federation / Operator controls (**ODTIS-0707**).
3. Tier 2/3 sub-modules are **preview**; tier 1 are **draft** toward ODTIS 1.x.

---

## Validation

```bash
python3 scripts/validate-reliance-annex.py
```

---

## References

- DTI editorial feed: https://manuelmerida.io/feed.xml
- Analysis: `analisis/status/09-PROFILES-EMERGENTES-ARTICULOS-DTI.md`
- Base schema: `ODTIS-0701..0708` (section 11)
