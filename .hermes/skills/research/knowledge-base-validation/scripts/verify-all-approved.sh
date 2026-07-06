#!/usr/bin/env bash
# verify-all-approved.sh — Global sweep: confirm NO pending reports or stale headers remain
# Usage: bash verify-all-approved.sh
#
# This is a GLOBAL check (unlike verify-approval.sh which is date-specific).
# Run after mass approval to catch:
#   1. Dashboard pending count != 0
#   2. Any residual "## Pending —" section headers (stale from prior rounds)
#   3. Any 📋 emoji (unapproved report marker)
#   4. All recent (last 7 days) report statuses are approved or applied

set -euo pipefail

KB_DIR="${KB_DIR:-/home/julius/knowledge-base}"
DASHBOARD="$KB_DIR/wiki/reviews/_action-required.md"
PASS=0
FAIL=0

green() { echo "  ✅ $1"; PASS=$((PASS + 1)); }
red()   { echo "  ❌ $1"; FAIL=$((FAIL + 1)); }

echo "=== Global Approval Verification ==="
echo "Dashboard: $DASHBOARD"
echo ""

if [ ! -f "$DASHBOARD" ]; then
    red "MISSING: _action-required.md"
    exit 1
fi

# 1. Dashboard pending count
PENDING_COUNT=$(grep -oP 'Pending reports awaiting review:\*\* \K\d+' "$DASHBOARD" || echo "MISSING")
if [ "$PENDING_COUNT" = "0" ]; then
    green "Dashboard pending count = 0"
elif [ "$PENDING_COUNT" = "MISSING" ]; then
    red "Dashboard: pending count line not found"
else
    red "Dashboard: $PENDING_COUNT pending report(s) remain"
fi

# 2. No "## Pending —" section headers ANYWHERE
STALE_HEADERS=$(grep -c "^## Pending —" "$DASHBOARD" || true)
if [ "$STALE_HEADERS" -eq 0 ]; then
    green "No stale 'Pending —' section headers"
else
    red "$STALE_HEADERS stale 'Pending —' section header(s) found:"
    grep "^## Pending —" "$DASHBOARD" | sed 's/^/      /'
fi

# 3. No 📋 emoji (unapproved marker)
STALE_EMOJI=$(grep -c "📋" "$DASHBOARD" || true)
if [ "$STALE_EMOJI" -eq 0 ]; then
    green "No 📋 stale pending markers"
else
    red "$STALE_EMOJI 📋 emoji still present (pending reports)"
fi

# 4. Last updated date
LAST_UPDATED=$(grep -oP '\*\*Last updated:\*\* \K.*' "$DASHBOARD" || echo "MISSING")
echo ""
echo "  Last updated: $LAST_UPDATED"

# 5. APPROVED count in Applied Reports section
APPROVED_COUNT=$(sed -n '/^## Applied Reports/,/^---/p' "$DASHBOARD" | grep -c "APPROVED" || true)
echo "  APPROVED entries in Applied: $APPROVED_COUNT"

# 6. All recent report files (last 10 days) have approved/applied status
echo ""
echo "  Recent report statuses:"
for report in "$KB_DIR/wiki/reviews/"????-??-??_*-report.md; do
    [ -f "$report" ] || continue
    fname=$(basename "$report")
    status=$(head -8 "$report" | grep -oP '\*\*Status:\*\* \K\w+' || echo "???")
    case "$status" in
        approved|applied|promote)
            echo "    ✅ $fname → $status"
            ;;
        pending)
            echo "    ⏳ $fname → $status ⚠️ STILL PENDING"
            FAIL=$((FAIL + 1))
            ;;
        *)
            echo "    ❓ $fname → $status"
            ;;
    esac
done

echo ""
echo "=== Result: $PASS passed, $FAIL failed ==="
if [ "$FAIL" -gt 0 ]; then
    exit 1
fi
