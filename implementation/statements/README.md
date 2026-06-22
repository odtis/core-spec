# Published conformance statements

Dual-format statements (YAML + Markdown) per ODTIS `0534` and field rules `0008`.

| Environment | Path | Phase | Profiles | Level |
|-------------|------|-------|----------|-------|
| VenID lab | [Venid Sandbox](/implementation/statements/venid-sandbox/) | 1 | reference-architecture | L1 |
| VenID Phase 2 staging | [Venid Phase2 Trust](/implementation/statements/venid-phase2-trust/) | 2 | core-identity, trust-network | L2 |
| VenID Phase 3 operator | [Venid Phase3 Operator](/implementation/statements/venid-phase3-operator/) | 3 | core-identity, trust-network, operator | L2 |

## Commands

```bash
# Regenerate from registry (after profile/manifest changes)
python3 scripts/build-conformance-manifest.py
python3 scripts/generate-conformance-statement.py

# Validate machine + human parity
python3 scripts/validate-conformance-statement.py

# Custom profile set
python3 scripts/generate-conformance-statement.py \
 --profile reference-architecture \
 --profile core-identity \
 --level L2 \
 --environment sandbox \
 --out-dir implementation/statements/venid-staging
```

CI runs `validate-conformance-statement.py` on every ODTIS workflow.
