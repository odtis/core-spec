#!/usr/bin/env python3
"""L2 automated conformance checks against a live --target deployment."""

from __future__ import annotations

import argparse
import json
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]

REQUIRED_DISCOVERY_FIELDS = (
    "issuer",
    "authorization_endpoint",
    "token_endpoint",
    "userinfo_endpoint",
    "jwks_uri",
    "response_types_supported",
    "grant_types_supported",
    "id_token_signing_alg_values_supported",
    "scopes_supported",
    "subject_types_supported",
)


def read_version() -> str:
    version_file = ROOT / "VERSION"
    if version_file.is_file():
        return version_file.read_text(encoding="utf-8").strip()
    return "unknown"


def fetch(url: str, timeout: int = 15) -> tuple[int, str]:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return exc.code, body


def discovery_url(target: str) -> str:
    return urllib.parse.urljoin(target.rstrip("/") + "/", ".well-known/openid-configuration")


def load_discovery(target: str) -> tuple[int, dict[str, Any] | None, str]:
    status, body = fetch(discovery_url(target))
    if status != 200:
        return status, None, body
    try:
        return status, json.loads(body), body
    except json.JSONDecodeError:
        return status, None, body


def test_oidc_discovery_reachable(target: str) -> dict:
    url = discovery_url(target)
    status, doc, _ = load_discovery(target)
    ok = status == 200 and doc is not None
    return {
        "id": "l2-oidc-discovery",
        "requirement": "ODTIS-0301",
        "ok": ok,
        "detail": f"GET {url} -> {status}",
    }


def test_discovery_required_fields(target: str) -> dict:
    status, doc, _ = load_discovery(target)
    if status != 200 or not doc:
        return {
            "id": "l2-discovery-fields",
            "requirement": "ODTIS-0301",
            "ok": False,
            "detail": f"Discovery unavailable ({status})",
        }

    missing = [field for field in REQUIRED_DISCOVERY_FIELDS if field not in doc]
    checks: list[str] = []

    if "code" not in doc.get("response_types_supported", []):
        checks.append("response_types_supported missing 'code'")
    if "authorization_code" not in doc.get("grant_types_supported", []):
        checks.append("grant_types_supported missing 'authorization_code'")
    if "openid" not in doc.get("scopes_supported", []):
        checks.append("scopes_supported missing 'openid'")
    methods = doc.get("code_challenge_methods_supported", [])
    if methods and "S256" not in methods:
        checks.append("code_challenge_methods_supported missing 'S256'")

    ok = not missing and not checks
    detail_parts: list[str] = []
    if missing:
        detail_parts.append("missing fields: " + ", ".join(missing))
    detail_parts.extend(checks)
    detail = "; ".join(detail_parts) if detail_parts else "All required discovery fields present"
    return {
        "id": "l2-discovery-fields",
        "requirement": "ODTIS-0301",
        "ok": ok,
        "detail": detail,
    }


def test_jwks_reachable(target: str) -> dict:
    status, doc, _ = load_discovery(target)
    if status != 200 or not doc:
        return {
            "id": "l2-jwks",
            "requirement": "ODTIS-0301",
            "ok": False,
            "detail": "Cannot read jwks_uri from discovery",
        }

    jwks_uri = doc.get("jwks_uri")
    if not jwks_uri:
        return {
            "id": "l2-jwks",
            "requirement": "ODTIS-0301",
            "ok": False,
            "detail": "jwks_uri not advertised",
        }

    jwks_status, jwks_body = fetch(jwks_uri)
    ok = jwks_status == 200 and "keys" in jwks_body
    return {
        "id": "l2-jwks",
        "requirement": "ODTIS-0301",
        "ok": ok,
        "detail": f"GET {jwks_uri} -> {jwks_status}",
    }


def test_pkce_s256(target: str) -> dict:
    status, doc, _ = load_discovery(target)
    if status != 200 or not doc:
        return {
            "id": "l2-pkce-discovery",
            "requirement": "ODTIS-0302",
            "ok": False,
            "detail": f"Discovery unavailable ({status})",
        }

    methods = doc.get("code_challenge_methods_supported", [])
    ok = "S256" in methods
    detail = (
        "code_challenge_methods_supported includes S256"
        if ok
        else "code_challenge_methods_supported MUST include S256 for public clients"
    )
    return {
        "id": "l2-pkce-discovery",
        "requirement": "ODTIS-0302",
        "ok": ok,
        "detail": detail,
    }


def test_logout_endpoint(target: str) -> dict:
    status, doc, _ = load_discovery(target)
    if status != 200 or not doc:
        return {
            "id": "l2-logout-endpoint",
            "requirement": "ODTIS-0308",
            "ok": False,
            "detail": f"Discovery unavailable ({status})",
        }

    endpoint = doc.get("end_session_endpoint")
    ok = bool(endpoint)
    return {
        "id": "l2-logout-endpoint",
        "requirement": "ODTIS-0308",
        "ok": ok,
        "detail": "end_session_endpoint advertised"
        if ok
        else "end_session_endpoint not advertised",
    }


def test_revocation_endpoint(target: str) -> dict:
    status, doc, _ = load_discovery(target)
    if status != 200 or not doc:
        return {
            "id": "l2-revocation-endpoint",
            "requirement": "ODTIS-0303",
            "ok": False,
            "detail": f"Discovery unavailable ({status})",
        }
    endpoint = doc.get("revocation_endpoint")
    ok = bool(endpoint)
    return {
        "id": "l2-revocation-endpoint",
        "requirement": "ODTIS-0303",
        "ok": ok,
        "detail": "revocation_endpoint advertised" if ok else "revocation_endpoint missing",
    }


def _auth_probe(target: str, params: dict[str, str]) -> tuple[int, str]:
    status, doc, _ = load_discovery(target)
    if status != 200 or not doc:
        return status, ""
    auth = doc.get("authorization_endpoint")
    if not auth:
        return 0, ""
    query = urllib.parse.urlencode(params)
    url = f"{auth}?{query}"
    return fetch(url)


def test_pkce_enforced(target: str, client_id: str = "portal-ciudadano") -> dict:
    status, body = _auth_probe(
        target,
        {
            "client_id": client_id,
            "redirect_uri": "http://localhost:5173/",
            "response_type": "code",
            "scope": "openid",
            "state": "l2-pkce-test",
        },
    )
    if status == 0:
        return {
            "id": "l2-pkce-enforced",
            "requirement": "ODTIS-0302",
            "ok": False,
            "detail": "authorization_endpoint unavailable",
        }
    rejected = status == 400 or "code_challenge" in body.lower() or "pkce" in body.lower()
    return {
        "id": "l2-pkce-enforced",
        "requirement": "ODTIS-0302",
        "ok": rejected,
        "detail": "Public client auth without PKCE rejected"
        if rejected
        else f"Authorization without PKCE may be accepted (HTTP {status})",
    }


def test_redirect_uri_validation(target: str, client_id: str = "portal-ciudadano") -> dict:
    status, body = _auth_probe(
        target,
        {
            "client_id": client_id,
            "redirect_uri": "https://evil.example/callback",
            "response_type": "code",
            "scope": "openid",
            "code_challenge": "l2-test-challenge",
            "code_challenge_method": "S256",
            "state": "l2-redirect-test",
        },
    )
    if status == 0:
        return {
            "id": "l2-redirect-uri",
            "requirement": "ODTIS-0305",
            "ok": False,
            "detail": "authorization_endpoint unavailable",
        }
    rejected = "redirect" in body.lower() and ("invalid" in body.lower() or "not allowed" in body.lower())
    rejected = rejected or status == 400
    return {
        "id": "l2-redirect-uri",
        "requirement": "ODTIS-0305",
        "ok": rejected,
        "detail": "Unregistered redirect_uri rejected"
        if rejected
        else f"Unregistered redirect_uri may be accepted (HTTP {status})",
    }


def test_loa_in_verify_schema(_target: str) -> dict:
    common = ROOT / "annexes/A-openapi-registry/venid-common.openapi.yaml"
    text = common.read_text(encoding="utf-8")
    ok = (
        "assurance_level" in text
        and "AssuranceLevel" in text
        and "verified" in text
    )
    return {
        "id": "l2-loa-schema",
        "requirement": "ODTIS-0316",
        "ok": ok,
        "detail": "Annex A VerifyResponse includes verified, assurance_level (live API: verification-api-check.sh)",
    }


def test_gateway_mtls_required() -> dict:
    spec = ROOT / "annexes/A-openapi-registry/exchange-gateway.openapi.yaml"
    text = spec.read_text(encoding="utf-8")
    ok = "partnerMutualTLS" in text and "mutualTLS" in text
    return {
        "id": "l2-gateway-mtls-spec",
        "requirement": "ODTIS-0204",
        "ok": ok,
        "detail": "Exchange gateway OpenAPI declares partnerMutualTLS (live mTLS handshake requires certs)",
    }


def _human_summary(report: dict) -> str:
    lines = [f"ODTIS L2 automated: {report['status']} ({report['passed']}/{report['total']})"]
    for result in report["results"]:
        if result.get("informational") and result["ok"]:
            mark = "OK"
        elif result.get("informational"):
            mark = "INFO"
        else:
            mark = "OK" if result["ok"] else "FAIL"
        lines.append(f"  [{mark}] {result['id']}: {result['detail']}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="ODTIS L2 automated checks")
    parser.add_argument("--target", help="Base IdP URL (e.g. https://idp.example/realms/venid)")
    parser.add_argument("--json", action="store_true", help="Print report JSON to stdout")
    parser.add_argument("--output", help="Write report JSON to file")
    args = parser.parse_args()

    results: list[dict] = [test_loa_in_verify_schema(args.target or ""), test_gateway_mtls_required()]
    if args.target:
        results = [
            test_oidc_discovery_reachable(args.target),
            test_discovery_required_fields(args.target),
            test_jwks_reachable(args.target),
            test_pkce_s256(args.target),
            test_pkce_enforced(args.target),
            test_redirect_uri_validation(args.target),
            test_logout_endpoint(args.target),
            test_revocation_endpoint(args.target),
            *results,
        ]
    else:
        results.insert(
            0,
            {
                "id": "l2-target-skipped",
                "requirement": "-",
                "ok": True,
                "detail": "Pass --target for live OIDC/PKCE/JWKS checks",
            },
        )

    failed = [r for r in results if not r["ok"] and not r.get("informational")]
    report = {
        "level": "L2",
        "odtis_version": read_version(),
        "target": args.target,
        "results": results,
        "status": "PASS" if not failed else "FAIL",
        "passed": len(results) - len(failed),
        "total": len(results),
    }

    payload = json.dumps(report, indent=2)
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(payload + "\n", encoding="utf-8")

    if args.json or not args.output:
        print(payload if args.json else _human_summary(report))

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
