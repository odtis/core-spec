# ODTIS open-source layout

**Last updated:** 2026-06-22  
**Canonical specification:** [github.com/odtis/core-spec](https://github.com/odtis/core-spec) (public)  
**Reference implementation:** [github.com/odtis/core-impl](https://github.com/odtis/core-impl) (private during Phase 3.2)

---

## Repository model

| Piece | GitHub | Role |
|-------|--------|------|
| **core-spec** | [odtis/core-spec](https://github.com/odtis/core-spec) | Normative ODTIS text, registry, annexes, conformance tests, MkDocs sources |
| **core-impl** | [odtis/core-impl](https://github.com/odtis/core-impl) | VenID reference implementation (Java modules, smokes) |
| **odtis.org** | *(not a git repo)* | Static site built from `core-spec` and deployed to EC2 |

Recommended local layout for contributors running smokes:

```
odtis/
├── core-spec/
├── core-impl/
└── build/odtis-spec-site/    # gitignored MkDocs output
```

---

## Build and deploy (local)

```bash
cd core-spec
./scripts/build-site.sh

# One-time: copy and edit deploy config (gitignored)
cp scripts/odtis-deploy.env.example scripts/odtis-deploy.env

# Build + rsync to EC2
./scripts/deploy-ec2.sh
```

Deploy credentials live only in `scripts/odtis-deploy.env` on your machine (never committed).

Optional version bump before release:

```bash
python3 scripts/bump-spec-version.py --minor --write
python3 scripts/sync-spec-version.py
python3 scripts/sync-site-release-meta.py
./scripts/build-site.sh
./scripts/deploy-ec2.sh
```

---

## Release and versioning

- Single source: `VERSION` at repo root
- Site shows release badge, footer build metadata, and `/site/BUILD-META.json`
- Bump and deploy manually from local when ready

---

## Security

- Never commit SSH keys or `scripts/odtis-deploy.env`
- Report issues: [SECURITY.md](SECURITY.md)

---

## Related

- [README](README.md) - specification overview
- [ADOPTION.md](ADOPTION.md) - implementers and operators
- [DEPLOY-EC2-ODTIS-ORG.md](scripts/DEPLOY-EC2-ODTIS-ORG.md) - odtis.org hosting guide
