# GitHub repository settings (manual)

If `scripts/set-github-repo-metadata.sh` cannot run (no `gh auth`), set these in GitHub: **Settings → General**.

## Description

```
Open Digital Trust Infrastructure Specification (ODTIS) - vendor-neutral digital identity, trust networks, and conformance (0.9.0-draft).
```

## Topics

```
odtis
open-specification
digital-identity
trust-network
digital-trust
conformance
oidc
openapi
identity-management
zero-trust
```

## Website

```
https://odtis.org
```

## Automated setup

```bash
gh auth login
cd core-spec && ./scripts/set-github-repo-metadata.sh
```
