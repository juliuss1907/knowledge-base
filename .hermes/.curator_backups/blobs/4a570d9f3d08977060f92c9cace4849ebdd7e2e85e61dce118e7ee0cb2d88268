#!/usr/bin/env bash
# verify-approval.sh — Confirm all approval changes landed correctly
# Usage: bash verify-approval.sh YYYY-MM-DD
# Example: bash verify-approval.sh 2026-06-29
#
# Checks:
#   1. All 3 report files have "**Status:** approved" and approved-by line
#   2. Dashboard pending count is 0
#   3. Dashboard has ✅ APPROVED badges (not 🔲 PENDING)
#   4. Section heading renamed Pending → Approved
#   5. No residual pending/pending badges for the date

set -euo pipefail

DATE="${1:?Usage: $0 YYYY-MM-DD}"
KB_DIR="/home/julius/knowledge-base"
REVIEWS="$KB_DIR/wiki/reviews"
PASS=0
FAIL=0

green() { echo "  ✅ $1"; PASS=$((PASS + 1)); }
red()   { echo "  ❌ $1"; FAIL=$((FAIL + 1)); }

echo "=== Verifying approval for $DATE ==="
echo ""

# 1. Report files: status + approved-by
for validator in output format hygiene; do
    report="${REVIEWS}/${DATE}_${validator}-report.md"
    if [ ! -f "$report" ]; then
        red "MISSING: ${DATE}_${validator}-report.md"
        continue
    fi
    if grep -q "Status.*approved" "$report"; then
        green "${validator}-report: status=approved"
    else
        red "${validator}-report: missing 'Status: approved'"
    fi
    if grep -q "Approved by.*Julius" "$report"; then
        green "${validator}-report: approved_by present"
    else
        red "${validator}-report: missing 'Approved by: Julius'"
    fi
done

echo ""

# 2. Dashboard checks
dashboard="${REVIEWS}/_action-required.md"
if [ ! -f "$dashboard" ]; then
    red "MISSING: _action-required.md"
else
    # Pending count
    if grep -q "Pending reports awaiting review:.*0" "$dashboard"; then
        green "dashboard: pending count = 0"
    else
        red "dashboard: pending count NOT zero"
    fi

    # ✓ badges for the date
    output_ok=$(grep -c "✅ Output Validator.*${DATE}.*APPROVED" "$dashboard" || true)
    format_ok=$(grep -c "✅ Format Validator.*${DATE}.*APPROVED" "$dashboard" || true)
    hygiene_ok=$(grep -c "✅ Hygiene Inspector.*${DATE}.*APPROVED" "$dashboard" || true)
    if [ "$output_ok" -ge 1 ]; then green "dashboard: Output ${DATE} → APPROVED"; else red "dashboard: Output ${DATE} NOT approved"; fi
    if [ "$format_ok" -ge 1 ]; then green "dashboard: Format ${DATE} → APPROVED"; else red "dashboard: Format ${DATE} NOT approved"; fi
    if [ "$hygiene_ok" -ge 1 ]; then green "dashboard: Hygiene ${DATE} → APPROVED"; else red "dashboard: Hygiene ${DATE} NOT approved"; fi

    # Section heading renamed
    if grep -q "^## Approved.*${DATE}" "$dashboard"; then
        green "dashboard: section heading '## Approved — ${DATE}'"
    else
        red "dashboard: section heading NOT renamed to Approved"
    fi

    # No residual 🔲
    residue=$(grep -c "🔲.*${DATE}" "$dashboard" || true)
    if [ "$residue" -eq 0 ]; then
        green "dashboard: no residual 🔲 for ${DATE}"
    else
        red "dashboard: $residue residual 🔲 badge(s) for ${DATE}"
    fi
fi

echo ""
echo "=== Result: $PASS passed, $FAIL failed ==="
if [ "$FAIL" -gt 0 ]; then
    exit 1
fi
