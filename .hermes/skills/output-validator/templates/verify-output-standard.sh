#!/bin/bash
# Full-run verification for Output Validation reports (cron post-edit evidence).
# Copy + customize via env vars, then run:
#   TODAY=2026-08-24 ISSUES=3 SEV='0 ERROR, 2 WARNING, 1 INFO' \
#   ACT_SUM='3 (0E+2W+1I)' MEM_HEADING='2026-08-24 23:06:38' NEWFILES=4 \
#   bash .hermes/skills/output-validator/templates/verify-output-standard.sh
# NOTE: SEV must match the report's "**Issues found:** N (...)" wording exactly.
set -u
: "${TODAY:?export TODAY=YYYY-MM-DD}"
: "${ISSUES:?export ISSUES=N}"
: "${SEV:?export SEV='X ERROR, Y WARNING, Z INFO'}"
: "${ACT_SUM:?export ACT_SUM='XE+YW+ZI'}"
: "${MEM_HEADING:?export MEM_HEADING='YYYY-MM-DD HH:MM:SS'}"
NEWFILES="${NEWFILES:-}"

KB="/home/julius/knowledge-base"
R="$KB/wiki/reviews/${TODAY}_output-report.md"
A="$KB/wiki/reviews/_action-required.md"
M="$KB/.hermes/MEMORY.md"
DD="${TODAY#20*-}"   # 2026-08-24 -> 08-24 (table row date format)

PASS=0; FAIL=0
check() { local desc="$1"; shift
  if "$@" >/dev/null 2>&1; then echo "[OK]   $desc"; PASS=$((PASS+1))
  else echo "[FAIL] $desc"; FAIL=$((FAIL+1)); fi; }

# --- Report file ---
# Escape regex metacharacters in ACT_SUM ('+' etc.) before ERE use (found 2026-08-25:
# '3 (0E+2W+1I)' as bare ERE treats '+' as quantifier -> table-row check never matches).
ACT_SUM_RE=$(printf '%s' "$ACT_SUM" | sed 's/[][\.*^$()+?{|}\\]/\\&/g')
check "report exists non-empty" test -s "$R"
check "report Status=pending (** both sides)" grep -q 'Status:\*\* pending' "$R"
check "report Issues found = $ISSUES ($SEV)" grep -q "Issues found:\*\* $ISSUES ($SEV)" "$R"
check "report Created field present" grep -q 'Created:\*\*' "$R"
check "issue headers == $ISSUES" bash -c "test \"\$(grep -c '^## Issue [0-9]' \"\$1\")\" -eq $ISSUES" _ "$R"

# --- _action-required.md ---
echo "[INFO] $(grep '\*\*Pending reports awaiting review:\*\*' "$A")"
check "'Output Validation — $TODAY' heading unique" bash -c "test \"\$(grep -c \"Output Validation — $TODAY\" \"\$1\")\" -eq 1" _ "$A"
check "new entry Status=pending (-A 10 window)" bash -c "grep -F -A 10 \"Output Validation — $TODAY\" \"\$1\" | grep -q 'Status:\*\* pending'" _ "$A"
check "summary table row present ($DD)" grep -qE "\| PENDING \| $DD \| Output \| $ACT_SUM_RE" "$A"
check "no ||| table corruption" bash -c "test \"\$(grep -c '|||' \"\$1\")\" -eq 0" _ "$A"
check "Pending Reports section unique" bash -c "test \"\$(grep -c '^## Pending Reports' \"\$1\")\" -eq 1" _ "$A"

# --- MEMORY.md ---
MEM_LINE=$(grep -n "$MEM_HEADING — Output validation" "$M" | head -1 | cut -d: -f1)
[ -n "$MEM_LINE" ] && echo "[INFO] memory entry at line $MEM_LINE"
check "memory entry exists" test -n "$MEM_LINE"
check "memory entry references report" grep -q "wiki/reviews/${TODAY}_output-report.md" "$M"

# --- Cross-file consistency ---
check "issues count agrees report<->action" bash -c "grep -q \"Issues found:\\*\\* $ISSUES ($SEV)\" \"\$1\" && grep -qF \"$ACT_SUM\" \"\$2\"" _ "$R" "$A"
if [ -n "$NEWFILES" ]; then
  check "new-files count agrees memory<->action" bash -c "grep -q \"New files:\\*\\* $NEWFILES\" \"\$1\" && grep -q \"$NEWFILES\" \"\$2\"" _ "$M" "$A"
fi

echo ""
echo "RESULT: $PASS passed, $FAIL failed"
exit $FAIL
