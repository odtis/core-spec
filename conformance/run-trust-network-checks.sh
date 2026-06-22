#!/usr/bin/env bash
# P2-E01: Trust Network L2 smoke (exchange-gateway) + spec checks.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

GATEWAY="${ODTIS_EXCHANGE_GATEWAY:-}"
TN_SCRIPT="../core-impl/ven-trust-network/scripts/exchange-gateway-check.sh"

echo "== Trust Network spec checks =="
python3 conformance/l2/run_l2.py --output /tmp/odtis-tn-l2-spec.json >/dev/null
python3 - <<'PY'
import json
from pathlib import Path
report = json.loads(Path("/tmp/odtis-tn-l2-spec.json").read_text())
mtls = next(r for r in report["results"] if r["id"] == "l2-gateway-mtls-spec")
assert mtls["ok"], mtls["detail"]
print("OK: exchange-gateway OpenAPI declares partnerMutualTLS (ODTIS-0204 spec)")
PY

if [[ -n "$GATEWAY" ]] || curl -sf "http://localhost:9080/exchange/health" >/dev/null 2>&1; then
  echo "== Live exchange-gateway smoke =="
  if [[ -x "$TN_SCRIPT" ]]; then
    ODTIS_EXCHANGE_GATEWAY="${GATEWAY:-http://localhost:9080}" bash "$TN_SCRIPT"
  else
    echo "WARN: ${TN_SCRIPT} not found or not executable"
  fi
else
  echo "WARN: ODTIS_EXCHANGE_GATEWAY not set and localhost:9080 unreachable  -  spec-only PASS"
fi

CATALOG_SCRIPT="../core-impl/ven-trust-network/scripts/service-catalog-check.sh"
if [[ -x "$CATALOG_SCRIPT" ]] && { curl -sf "http://localhost:8096/actuator/health" >/dev/null 2>&1 \
  || curl -sf "http://localhost:9080/exchange/health" >/dev/null 2>&1; }; then
  echo "== Live service catalog smoke =="
  bash "$CATALOG_SCRIPT"
elif [[ -x "$CATALOG_SCRIPT" ]]; then
  echo "WARN: trust-service/gateway unreachable  -  skip catalog smoke"
fi

GRANTS_SCRIPT="../core-impl/ven-trust-network/scripts/service-grants-check.sh"
if [[ -x "$GRANTS_SCRIPT" ]] && curl -sf "http://localhost:8096/actuator/health" >/dev/null 2>&1; then
  echo "== Live service grants smoke =="
  bash "$GRANTS_SCRIPT"
elif [[ -x "$GRANTS_SCRIPT" ]]; then
  echo "WARN: trust-service unreachable  -  skip grants smoke"
fi

SENDER_SCRIPT="../core-impl/ven-trust-network/scripts/sender-routing-check.sh"
if [[ -x "$SENDER_SCRIPT" ]] && curl -sf "http://localhost:9080/exchange/health" >/dev/null 2>&1; then
  echo "== Live sender routing smoke =="
  bash "$SENDER_SCRIPT"
elif [[ -x "$SENDER_SCRIPT" ]]; then
  echo "WARN: exchange-gateway unreachable  -  skip sender routing smoke"
fi

METADATA_SCRIPT="../core-impl/ven-trust-network/scripts/metadata-only-check.sh"
if [[ -x "$METADATA_SCRIPT" ]] && curl -sf "http://localhost:8084/actuator/health" >/dev/null 2>&1; then
  echo "== Live metadata-only exchange smoke =="
  bash "$METADATA_SCRIPT"
elif [[ -x "$METADATA_SCRIPT" ]]; then
  echo "WARN: audit-service unreachable  -  skip metadata-only smoke"
fi

PKI_SCRIPT="../core-impl/ven-trust-network/scripts/trust-pki-check.sh"
if [[ -x "$PKI_SCRIPT" ]] && curl -sf "http://localhost:8098/actuator/health" >/dev/null 2>&1; then
  echo "== Live Trust PKI smoke =="
  bash "$PKI_SCRIPT"
elif [[ -x "$PKI_SCRIPT" ]]; then
  echo "WARN: trust-authority unreachable  -  skip PKI smoke"
fi

AUDIT_SCRIPT="../core-impl/ven-trust-network/scripts/exchange-audit-check.sh"
if [[ -x "$AUDIT_SCRIPT" ]] && curl -sf "http://localhost:9080/exchange/health" >/dev/null 2>&1 \
  && curl -sf "http://localhost:8084/actuator/health" >/dev/null 2>&1; then
  echo "== Live exchange audit and SLA smoke =="
  bash "$AUDIT_SCRIPT"
elif [[ -x "$AUDIT_SCRIPT" ]]; then
  echo "WARN: exchange-gateway or audit-service unreachable  -  skip audit smoke"
fi

FAL_SCRIPT="../core-impl/ven-trust-network/scripts/fal-controls-check.sh"
if [[ -x "$FAL_SCRIPT" ]]; then
  echo "== FAL controls smoke (ODTIS-0106) =="
  bash "$FAL_SCRIPT"
fi

echo ""
echo "Trust Network checks: PASS"
