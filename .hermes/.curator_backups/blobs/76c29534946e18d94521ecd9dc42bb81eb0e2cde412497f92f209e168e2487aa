#!/bin/bash
# verify-approval-batch.sh — Batch verification after approving reports
# Usage: bash scripts/verify-approval-batch.sh 2026-07-09 2026-07-10
# Without args: scans all *_report.md files with approved status
#
# Reusable across sessions. Satisfies the hermes-verify- gate.
# NO set -e (avoid ((var++)) exit-on-zero pitfall).

# Resolve to absolute knowledge-base root regardless of how script is invoked.
# Script lives at: .hermes/skills/research/knowledge-base-validation/scripts/verify-approval-batch.sh
# So we need 5 levels up from scripts/ to reach the root.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/../../../../.." || exit 1  # cd to knowledge-base root

pass=0
fail=0

echo "=== verify-approval-batch ==="
echo ""

# If dates provided, verify only those; otherwise all approved reports
if [ $# -gt 0 ]; then
  files=""
  for date in "$@"; do
    files="$files wiki/reviews/${date}_*-report.md"
  done
else
  files=$(grep -l '^[*][*]Status:[*][*] approved' wiki/reviews/*_report.md 2>/dev/null)
fi

# 1. Each report has approved status
echo "--- Report status ---"
for f in $files; do
  if grep -q '^[*][*]Status:[*][*] approved' "$f" 2>/dev/null; then
    echo "  ✅ $(basename "$f")"
    pass=$((pass+1))
  else
    echo "  ❌ $(basename "$f") — NOT approved"
    fail=$((fail+1))
  fi
done

# 2. Dashboard pending count
echo ""
echo "--- Dashboard ---"
if grep -q 'Pending reports.*0$' wiki/reviews/_action-required.md 2>/dev/null; then
  echo "  ✅ pending=0"
  pass=$((pass+1))
else
  echo "  ❌ pending count not zero"
  fail=$((fail+1))
fi

# 3. No stale ## Pending headers
if grep -q '^## Pending' wiki/reviews/_action-required.md 2>/dev/null; then
  echo "  ❌ Stale '## Pending' headers found"
  fail=$((fail+1))
else
  echo "  ✅ No stale Pending headers"
  pass=$((pass+1))
fi

# 4. Approved section exists
if grep -q '^## Approved' wiki/reviews/_action-required.md 2>/dev/null; then
  echo "  ✅ Approved section present"
  pass=$((pass+1))
else
  echo "  ❌ Missing Approved section"
  fail=$((fail+1))
fi

echo ""
echo "Results: $pass passed, $fail failed"
if [ "$fail" -eq 0 ]; then
  echo "✅ ALL CHECKS PASSED"
  exit 0
else
  echo "❌ $fail FAILURES"
  exit 1
fi
