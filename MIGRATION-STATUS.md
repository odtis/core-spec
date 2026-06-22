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

## Build and deploy

```bash
cd core-spec
./scripts/build-site.sh
# Manual deploy (local credentials, gitignored):
cp scripts/odtis-deploy.env.example scripts/odtis-deploy.env
./scripts/deploy-ec2.sh
```

**CI auto-deploy:** every merge to `main` runs `.github/workflows/release-deploy.yml` (minor version bump, build, EC2 rsync).  
GitHub Actions secrets: see [GITHUB-DEPLOY-SECRETS.md](scripts/GITHUB-DEPLOY-SECRETS.md).

---

## Release and versioning

- Single source: `VERSION` at repo root
- Site shows release badge, footer build metadata, and `/site/BUILD-META.json`
- Release commits use prefix `chore(release):` and do not re-trigger deploy

---

## Security

- Never commit SSH keys, `odtis-deploy.env`, or host-specific infrastructure values
- CI runs `scripts/check-deploy-safety.py` on pull requests
- Report issues: [SECURITY.md](SECURITY.md)

---

## Related

- [README](README.md) - specification overview
- [ADOPTION.md](ADOPTION.md) - implementers and operators
- [DEPLOY-EC2-ODTIS-ORG.md](scripts/DEPLOY-EC2-ODTIS-ORG.md) - odtis.org hosting guide
