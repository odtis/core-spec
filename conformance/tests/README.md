# Manual conformance test stubs

Each `.md` file describes a **manual or future automated** procedure. The runner indexes these files via `scripts/build-conformance-manifest.py`.

**Naming:** `test_<topic>.md` under the profile directory matching `registry/profiles.yaml`.

**Front matter (required lines):**

```markdown
**Status:** pending implementation
**Requirement:** ODTIS-x.x.x
**Profile:** core-identity
```

Add executable tests as `.py` / `.sh` alongside stubs when implementing L2.
