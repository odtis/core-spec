#!/usr/bin/env bash
# ODTIS-0006: Extended sub-modules must not weaken base profile controls.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
IC_ROOT="$(cd "$ROOT/../core-impl/ven-identity-core" 2>/dev/null && pwd || true)"
fail() { echo "FAIL: $1" >&2; exit 1; }

echo "== Extended activation gates (fail-closed defaults) =="
[[ -n "$IC_ROOT" ]] || fail "ven-identity-core not found"

for policy in \
  WalletActivationPolicy \
  ERegistryActivationPolicy \
  InclusionActivationPolicy \
  WebhookActivationPolicy \
  ESignatureActivationPolicy \
  KybActivationPolicy
do
  grep -rq "class ${policy}" "$IC_ROOT/shared/shared-lib/src/main/java" \
    || fail "missing activation policy: ${policy}"
done
echo "OK: Extended activation policies present"

echo ""
echo "== LoA / consent binding (no Extended bypass) =="
for policy in \
  WalletLoaPolicy \
  SignatureLoaPolicy \
  InclusionLoaPolicy \
  LegalEntityVerificationPolicy \
  KybRepresentativeLinkPolicy
do
  find "$IC_ROOT/shared/shared-lib/src/main/java" -name "${policy}.java" | grep -q . \
    || fail "missing anti-weakening policy: ${policy}"
done
grep -q 'assertNationalAllowed' "$IC_ROOT/shared/shared-lib/src/main/java/ve/venid/shared/constants/AssuranceLevelPolicy.java" \
  || fail "missing national LoA gate in AssuranceLevelPolicy"
echo "OK: LoA and representative linkage policies present"

echo ""
echo "== Sandbox inactive defaults =="
for pattern in \
  'venid.wallet.active:false' \
  'venid.eregistry.active:false' \
  'venid.inclusion.active:false' \
  'venid.webhook.active:false' \
  'venid.esignature.active:false' \
  'venid.kyb.active:false'
do
  grep -rq "$pattern" "$IC_ROOT/services" \
    || fail "missing inactive default: $pattern"
done
echo "OK: Extended services default inactive"

echo ""
echo "== Annex D composition rule evidence =="
ANNEX="$ROOT/annexes/D-extended-profiles/sub-modules.yaml"
grep -q 'MUST NOT weaken Core' "$ANNEX" || fail "missing composition rule in sub-modules.yaml"
EVIDENCE="$ROOT/implementation/evidence/phase4-conformance/extended-no-weakening-2026.yaml"
[[ -f "$EVIDENCE" ]] || fail "missing evidence: $EVIDENCE"
echo "OK: composition rules and evidence present"

echo ""
echo "Extended no-weakening checks: PASS"
