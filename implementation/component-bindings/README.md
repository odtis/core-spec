# Component normative bindings

Per-component **informative** bindings between VenID code, ODTIS requirement IDs, conformance tests, and L2/L3 evidence.

| Artifact | Role |
|----------|------|
| [RI surface map](../RI-MAP.yaml) | Machine-readable RI map (`binding_doc` per surface) |
| `*.yaml` in this directory | Deep binding for high-traffic / Phase 4 components |
| [Component bindings](/site/COMPONENT-BINDINGS/) | Generated site page (MkDocs) |

## Components (R3)

| Binding | Profile | Epic |
|---------|---------|------|
| `verification-api.yaml` | core-identity | P1-E04 |
| `gov-api.yaml` | core-identity | deferred (#29) |
| `exchange-gateway.yaml` | trust-network | P2-E01 |
| `exchange-client-sdk.yaml` | trust-network | P2-E04 |
| `ven-partner-sdk.yaml` | trust-network | P2-E04 |
| `partner-node-kit.yaml` | operator | P3-E03 |
| `federation-runtime.yaml` | federation | P4-E01 |
| `eregistry-adapter.yaml` | extended | P3-E07 |
| `wallet-service.yaml` | extended | P4-E02 |
| `inclusion-service.yaml` | extended | P4-E03 |
| `ewebhook-delivery.yaml` | extended | P4-E04 |
| `signature-service.yaml` | extended | P4-E05 |
| `kyb-service.yaml` | extended | P4-E06 |

## Workflow

1. Copy [Template (YAML)](TEMPLATE.yaml) to `<component-id>.yaml`.
2. List `odtis_ids` from [Requirements registry](/registry/requirements.json).
3. Link smoke scripts and evidence under `implementation/statements/` or `implementation/evidence/`.
4. Set `binding_doc` on the RI-MAP surface.
5. Regenerate:

```bash
python3 scripts/validate-component-bindings.py
python3 scripts/generate-component-bindings-docs.py
```

Bindings do **not** replace normative spec prose or profile manifests; they document how the reference implementation satisfies requirements.
