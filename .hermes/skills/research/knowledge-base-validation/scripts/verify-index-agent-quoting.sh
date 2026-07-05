#!/bin/bash
# Verify Index Agent tag file parent field has quoted wikilinks
# Run from knowledge-base root. Exits 0 if clean, 1 if issues found.
set -euo pipefail
BASE=".openclaw/skills/index-agent"
KB="."
FAIL=0

echo "=== Index Agent Quoting Verification ==="

# 1. Scripts — must use parent: "[[tag]]"
for f in indexer.py index_helper.py run_index.py build_index.py SKILL.md workflow.md; do
  if grep -qF 'parent: "[[tag]]"' "$BASE/$f" 2>/dev/null; then
    echo "  OK: $f"
  else
    echo "  FAIL: $f missing quoted parent"
    FAIL=1
  fi
done

# index_run.py uses f-string: parent: \"[[tag]]\"
if grep -q 'parent: \\"\[\[tag\]\]\\"' "$BASE/index_run.py" 2>/dev/null; then
  echo "  OK: index_run.py (f-string)"
else
  echo "  FAIL: index_run.py"
  FAIL=1
fi

# 2. Disk — zero unquoted tag files
DISK_BAD=$(grep -rFl 'parent: [[tag]]' "$KB"/wiki/tag/*.md 2>/dev/null | wc -l)
if [ "$DISK_BAD" -eq 0 ]; then
  echo "  OK: 0 unquoted tag files on disk"
else
  echo "  FAIL: $DISK_BAD unquoted tag files on disk"
  FAIL=1
fi

if [ $FAIL -eq 0 ]; then echo "PASS"; else echo "FAIL"; fi
exit $FAIL
