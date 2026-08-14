#!/bin/bash
# Template: Verify MEMORY.md append for silent output-validator runs
# Usage: replace YYYYMMDD, HH:MM:SS, and previous-run timestamp below
# Run: bash /tmp/hermes-verify-memory-YYYYMMDD.sh
set -euo pipefail

M="/home/julius/knowledge-base/.hermes/MEMORY.md"
TS_HEADING="## YYYY-MM-DD HH:MM:SS"   # today's heading prefix (include ## for unique match)
PREV_HEADING="## YYYY-MM-DD HH:MM"    # previous run's heading prefix

echo "=== Verification: MEMORY.md output-validator silent run ==="
fails=0

# 1. Entry exists
if grep -qF "$TS_HEADING" "$M"; then
  echo "[OK] Entry exists"
else
  echo "[FAIL] Entry not found"
  ((fails++))
fi

# 2. New files: 0 (need -A 5 because SILENT marker is on line 5)
if grep -F -A 5 "$TS_HEADING" "$M" | grep -q 'New files.*0'; then
  echo "[OK] New files: 0"
else
  echo "[FAIL] New files count wrong"
  ((fails++))
fi

# 3. Issues found: 0
if grep -F -A 5 "$TS_HEADING" "$M" | grep -q 'Issues found.*0'; then
  echo "[OK] Issues found: 0"
else
  echo "[FAIL] Issues count wrong"
  ((fails++))
fi

# 4. SILENT marker (line 5 after heading)
if grep -F -A 5 "$TS_HEADING" "$M" | grep -q 'SILENT'; then
  echo "[OK] SILENT marker present"
else
  echo "[FAIL] SILENT marker missing"
  ((fails++))
fi

# 5. Append-only order — use ## heading prefix, NOT bare timestamp.
#    Bare timestamps also match self-references in body text (e.g. "since last
#    validation (2026-07-23 23:13)"), which can appear AFTER today's heading
#    and cause a false FAIL. The ## prefix matches only the heading line.
PREV_LINE=$(grep -nF "$PREV_HEADING" "$M" | head -1 | cut -d: -f1)
THIS_LINE=$(grep -nF "$TS_HEADING" "$M" | head -1 | cut -d: -f1)
if [ "$THIS_LINE" -gt "$PREV_LINE" ] 2>/dev/null; then
  echo "[OK] Entry after previous (append-only, line $THIS_LINE > $PREV_LINE)"
else
  echo "[FAIL] Entry order wrong ($THIS_LINE <= $PREV_LINE)"
  ((fails++))
fi

# 6. File integrity: run's final data line appears in the tail window.
#    Do NOT use `tail -1 | grep -qF 'SILENT'` — appends via patch/write_file leave
#    a trailing blank line at EOF, so tail -1 returns empty and false-fails.
#    Assert the last entry is intact by matching its last data line in the tail instead.
THIS_HEADING="$(grep -nF "$TS_HEADING" "$M" | head -1 | cut -d: -f1)"
if [ -n "$THIS_HEADING" ] && tail -5 "$M" | grep -qF 'Carry-over'; then
  echo "[OK] File ends with SILENT entry (append successful)"
else
  echo "[FAIL] File tail unexpected; last entry not the terminal block"
  ((fails++))
fi

echo ""
if [ "$fails" -eq 0 ]; then
  echo "=== All 6 checks passed ==="
  exit 0
else
  echo "=== $fails check(s) FAILED ==="
  exit 1
fi
