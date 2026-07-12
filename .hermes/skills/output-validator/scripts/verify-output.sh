#!/bin/bash
# verify-output.sh — Post-validation structural integrity check
# Run after each output-validator execution to confirm all 3 output files are well-formed.
#
# Usage: bash scripts/verify-output.sh [KB_DIR]
#   KB_DIR defaults to /home/julius/knowledge-base
#
# Checks:
#   1. _action-required.md — pending count, status line, section uniqueness, no corruption
#   2. YYYY-MM-DD_output-report.md — exists, all 5 required sections present
#   3. .hermes/MEMORY.md — today's log entry present with contextual references

set -euo pipefail

KB_DIR="${1:-/home/julius/knowledge-base}"
TODAY=$(date +%Y-%m-%d)
PASS=0
FAIL=0

# ── Helpers ──────────────────────────────────────────────
check() {
  local desc="$1"; shift
  if "$@"; then
    echo "  ✅ $desc"
    PASS=$((PASS+1))
  else
    echo "  ❌ $desc"
    FAIL=$((FAIL+1))
  fi
}

# ── _action-required.md ──────────────────────────────────
echo "=== _action-required.md ==="

ACT="$KB_DIR/wiki/reviews/_action-required.md"
[ -f "$ACT" ] || { echo "  ❌ _action-required.md not found"; exit 1; }

check "Pending count = 1" \
  grep -q '\*\*Pending reports awaiting review:\*\* 1' "$ACT"

check "Output Validation entry for today present" \
  grep -qF "Output Validation — ${TODAY}" "$ACT"

check "Pending Reports section header exists" \
  grep -qF "## Pending Reports" "$ACT"

check "Applied Reports section intact" \
  grep -qF "## Applied Reports" "$ACT"

# Check Pending Reports section is unique (not duplicated)
PC=$(grep -cF "## Pending Reports" "$ACT" || echo 0)
PC=$(echo "$PC" | tr -d '[:space:]')
[ "$PC" = "1" ] && { echo "  ✅ Pending section unique ($PC)"; PASS=$((PASS+1)); } \
  || { echo "  ❌ Pending section appears $PC times (expected 1)"; FAIL=$((FAIL+1)); }

# ── Output report ────────────────────────────────────────
echo ""
echo "=== ${TODAY}_output-report.md ==="

RPT="$KB_DIR/wiki/reviews/${TODAY}_output-report.md"
[ -f "$RPT" ] || { echo "  ❌ Report not found: $RPT"; exit 1; }
[ -s "$RPT" ] || { echo "  ❌ Report is empty: $RPT"; exit 1; }
echo "  ✅ Report exists and non-empty ($(wc -l < "$RPT") lines)"
PASS=$((PASS+1))

for section in "Output Validator Report" "Summary" "New files validated" "Systemic issues" "Actions"; do
  check "Section '$section' present" \
    grep -qF "$section" "$RPT"
done

# ── MEMORY.md ────────────────────────────────────────────
echo ""
echo "=== .hermes/MEMORY.md ==="

MEM="$KB_DIR/.hermes/MEMORY.md"
[ -f "$MEM" ] || { echo "  ❌ MEMORY.md not found"; exit 1; }

check "Today's log entry present" \
  grep -qF "## ${TODAY}" "$MEM"

# Verify the entry is not empty (has at least a report path)
check "Log entry has report reference" \
  grep -qF "${TODAY}_output-report.md" "$MEM"

# ── Summary ──────────────────────────────────────────────
echo ""
echo "=== Results: $PASS passed, $FAIL failed ==="
[ "$FAIL" -eq 0 ] || exit 1
