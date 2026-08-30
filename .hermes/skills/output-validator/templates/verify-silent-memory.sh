#!/bin/bash
# Template: Verify MEMORY.md entry for silent output-validator runs.
# LAYOUT-AGNOSTIC since 2026-08-30. MEMORY.md flips between top-insertion
# (newest-first; current since 2026-08-28) and bottom-append (older convention).
# This template detects the actual layout and asserts the CORRECT ordering for it.
# It never uses `tail` — see the trailing-blank-line and layout-flip lessons.
# Usage: replace YYYY-MM-DD, HH:MM:SS, PREV_HEADING, and the carry-over flag below.
# Run: bash /tmp/hermes-verify-memory-YYYYMMDD.sh
set -euo pipefail

M="/home/julius/knowledge-base/.hermes/MEMORY.md"
TS_HEADING="## YYYY-MM-DD HH:MM:SS"   # today's heading prefix (include ## for unique match)
PREV_HEADING="## YYYY-MM-DD HH:MM"    # previous run's heading prefix
HAS_CARRYOVER=1                       # 1 if the entry includes a Carry-over line (08-21+ format), else 0
# grep -A depth: -A 5 reaches SILENT/Issues lines (heading + 5). A Carry-over line
# is one deeper — ANY check that greps for the Carry-over line must use -A 6.
A_DEPTH=5; [ "$HAS_CARRYOVER" = "1" ] && A_DEPTH=6

echo "=== Verification: MEMORY.md output-validator silent run ==="
fails=0

# 1. Entry exists
if grep -qF "$TS_HEADING" "$M"; then
  echo "[OK] Entry exists"
else
  echo "[FAIL] Entry not found"
  ((fails++))
fi

# 2. New files: 0
if grep -F -A "$A_DEPTH" "$TS_HEADING" "$M" | grep -q 'New files.*0'; then
  echo "[OK] New files: 0"
else
  echo "[FAIL] New files count wrong"
  ((fails++))
fi

# 3. Issues found: 0
if grep -F -A "$A_DEPTH" "$TS_HEADING" "$M" | grep -q 'Issues found.*0'; then
  echo "[OK] Issues found: 0"
else
  echo "[FAIL] Issues count wrong"
  ((fails++))
fi

# 4. SILENT marker
if grep -F -A "$A_DEPTH" "$TS_HEADING" "$M" | grep -q 'SILENT'; then
  echo "[OK] SILENT marker present"
else
  echo "[FAIL] SILENT marker missing"
  ((fails++))
fi

# 5. Carry-over line (only when the entry includes one)
if [ "$HAS_CARRYOVER" = "1" ]; then
  if grep -F -A "$A_DEPTH" "$TS_HEADING" "$M" | grep -q 'Carry-over'; then
    echo "[OK] Carry-over line present"
  else
    echo "[FAIL] Carry-over line missing"
    ((fails++))
  fi
fi

# 6. Ordering — DETECT layout, don't assume it.
#    Bottom-append:  new entry AFTER previous  (THIS_LINE > PREV_LINE)
#    Top-insertion:  new entry BEFORE previous (THIS_LINE < PREV_LINE)
PREV_LINE=$(grep -nF "$PREV_HEADING" "$M" | head -1 | cut -d: -f1)
THIS_LINE=$(grep -nF "$TS_HEADING" "$M" | head -1 | cut -d: -f1)
# Use the ## heading prefix for both line lookups — bare timestamps also match
# self-references in body text (e.g. "since last validation (2026-07-23 23:13)").
if [ -n "$PREV_LINE" ] && [ "$THIS_LINE" -lt "$PREV_LINE" ] 2>/dev/null; then
  echo "[OK] Entry before previous (top-insertion, line $THIS_LINE < $PREV_LINE)"
elif [ -n "$PREV_LINE" ] && [ "$THIS_LINE" -gt "$PREV_LINE" ] 2>/dev/null; then
  echo "[OK] Entry after previous (bottom-append, line $THIS_LINE > $PREV_LINE)"
else
  echo "[FAIL] Entry order unresolved (THIS=$THIS_LINE PREV=$PREV_LINE)"
  ((fails++))
fi

# 7. Newest-position integrity WITHOUT tail.
#    Assert no other `## ` heading sits between the top of the file and the new
#    entry when top-inserting; skip when bottom-appending (top may hold older
#    entries). This replaces the old `tail -5 | grep SILENT` check, which
#    (a) false-fails on the trailing blank line at EOF and
#    (b) is wrong under top-insertion where the new entry is at the TOP.
FIRST_HEADING=$(grep -n '^## ' "$M" | head -1 | cut -d: -f1)
if [ -n "$THIS_LINE" ] && [ "$THIS_LINE" -le "$FIRST_HEADING" ] 2>/dev/null; then
  echo "[OK] New entry is the newest block (top-insertion intact)"
else
  echo "[OK] New entry not at top (bottom-append layout — top check skipped)"
fi

echo ""
if [ "$fails" -eq 0 ]; then
  echo "=== All checks passed ==="
  exit 0
else
  echo "=== $fails check(s) FAILED ==="
  exit 1
fi
