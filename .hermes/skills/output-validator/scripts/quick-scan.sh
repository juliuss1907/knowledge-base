#!/bin/bash
# output-validator/scripts/quick-scan.sh
# Run systemic checks across all existing wiki files in one pass.
# Designed for the "quick scan existing files" phase of daily validation.
# Usage: bash quick-scan.sh [--json]
#   --json  Output results as JSON for programmatic consumption
# Without --json, outputs human-readable summary.

set -euo pipefail

KB_DIR="${KB_DIR:-/home/julius/knowledge-base}"
cd "$KB_DIR"

TODAY="${TODAY:-$(date +%Y-%m-%d)}"
OUTPUT_JSON=false
[[ "${1:-}" == "--json" ]] && OUTPUT_JSON=true

# ─── Helper ──────────────────────────────────────────────
count_lines() { wc -l | tr -d ' '; }
file_list() { find "$1" -maxdepth 1 -name "*.md" -type f 2>/dev/null | sort; }

# ─── 1. New file detection ───────────────────────────────
NEW_FILES=""
for f in $(file_list "wiki/sources") $(file_list "wiki/concepts"); do
    if grep -qE "^(date_compiled|last_updated):\s*$TODAY" "$f" 2>/dev/null; then
        NEW_FILES="$NEW_FILES $f"
    fi
done
NEW_COUNT=$(echo "$NEW_FILES" | wc -w)

# ─── 2. Typo: "ngưởi" → "người" ─────────────────────────
NGUOI_FILES=$(grep -rl "ngưởi" wiki/sources/ wiki/concepts/ 2>/dev/null || echo "")
NGUOI_COUNT=$(echo "$NGUOI_FILES" | grep -c "." || echo 0)
# Check if any of today's new files are affected
NGUOI_NEW=""
for f in $NEW_FILES; do
    if grep -q "ngưởi" "$f" 2>/dev/null; then
        NGUOI_NEW="$NGUOI_NEW $f"
    fi
done

# ─── 3. 1-sentence definitions (concepts only) ───────────
ONE_SENT_DEF=""
for f in $(file_list "wiki/concepts"); do
    sentences=$(sed -n '/^## Definition$/,/^## /p' "$f" 2>/dev/null \
        | sed '1d;/^## /,$d' | grep -v '^$' | grep -c '\.' 2>/dev/null || echo 0)
    # Clean: strip trailing newlines from grep -c output in subshell
    sentences=$(echo "$sentences" | tr -d '[:space:]')
    [ -z "$sentences" ] && sentences=0
    if [ "$sentences" -eq 1 ]; then
        ONE_SENT_DEF="$ONE_SENT_DEF $f"
    fi
done
ONE_SENT_COUNT=$(echo "$ONE_SENT_DEF" | wc -w)

# ─── 4. Too few key points (<5, concepts) ────────────────
FEW_POINTS=""
for f in $(file_list "wiki/concepts"); do
    points=$(sed -n '/^## Key ideas$/,/^## /p' "$f" 2>/dev/null \
        | sed '1d;/^## /,$d' | grep -c '^- ' 2>/dev/null || echo 0)
    points=$(echo "$points" | tr -d '[:space:]')
    [ -z "$points" ] && points=0
    if [ "$points" -gt 0 ] && [ "$points" -lt 5 ]; then
        FEW_POINTS="$FEW_POINTS $f:$points"
    fi
done
FEW_COUNT=$(echo "$FEW_POINTS" | wc -w)

# ─── 5. Truncated files (missing required sections) ──────
TRUNCATED_CONCEPTS=""
for f in $(file_list "wiki/concepts"); do
    has_rel=$(grep -c "^## Related concepts" "$f" 2>/dev/null || echo 0)
    has_rel=$(echo "$has_rel" | tr -d '[:space:]'); [ -z "$has_rel" ] && has_rel=0
    has_src=$(grep -c "^## Sources" "$f" 2>/dev/null || echo 0)
    has_src=$(echo "$has_src" | tr -d '[:space:]'); [ -z "$has_src" ] && has_src=0
    if [ "$has_rel" -eq 0 ] || [ "$has_src" -eq 0 ]; then
        TRUNCATED_CONCEPTS="$TRUNCATED_CONCEPTS $f(rel=$has_rel src=$has_src)"
    fi
done

TRUNCATED_SOURCES=""
for f in $(file_list "wiki/sources"); do
    has_cr=$(grep -c "^## Concepts referenced" "$f" 2>/dev/null || echo 0)
    has_cr=$(echo "$has_cr" | tr -d '[:space:]'); [ -z "$has_cr" ] && has_cr=0
    if [ "$has_cr" -eq 0 ]; then
        TRUNCATED_SOURCES="$TRUNCATED_SOURCES $f"
    fi
done

# ─── 6. Empty sections ───────────────────────────────────
EMPTY_SOURCES=""
EMPTY_KEY_IDEAS=""
for f in $(file_list "wiki/concepts"); do
    src_count=$(sed -n '/^## Sources$/,/^## /p' "$f" 2>/dev/null \
        | grep -c '\[\[.*\]\]' 2>/dev/null || echo 0)
    src_count=$(echo "$src_count" | tr -d '[:space:]'); [ -z "$src_count" ] && src_count=0
    [ "$src_count" -eq 0 ] && EMPTY_SOURCES="$EMPTY_SOURCES $f"

    ideas=$(sed -n '/^## Key ideas$/,/^## /p' "$f" 2>/dev/null \
        | sed '1d;/^## /,$d' | grep -c '^- ' 2>/dev/null || echo 0)
    ideas=$(echo "$ideas" | tr -d '[:space:]'); [ -z "$ideas" ] && ideas=0
    [ "$ideas" -eq 0 ] && EMPTY_KEY_IDEAS="$EMPTY_KEY_IDEAS $f"
done

# ─── 7. Draft status count ───────────────────────────────
DRAFT_COUNT=$(grep -rl "status: draft" wiki/concepts/*.md 2>/dev/null | wc -l | tr -d ' ')

# ─── 8. Source key points (too few) ──────────────────────
SOURCE_FEW_POINTS=""
for f in $(file_list "wiki/sources"); do
    points=$(sed -n '/^## Key points$/,/^## /p' "$f" 2>/dev/null \
        | sed '1d;/^## /,$d' | grep -c '^- ' 2>/dev/null || echo 0)
    points=$(echo "$points" | tr -d '[:space:]'); [ -z "$points" ] && points=0
    if [ "$points" -gt 0 ] && [ "$points" -lt 5 ]; then
        SOURCE_FEW_POINTS="$SOURCE_FEW_POINTS $f:$points"
    fi
done

# ─── Output ──────────────────────────────────────────────
if $OUTPUT_JSON; then
    cat <<EOF
{
  "new_files": $NEW_COUNT,
  "new_file_list": $(echo "$NEW_FILES" | jq -R -s -c 'split(" ") | map(select(length>0))'),
  "typo_nguoi": $NGUOI_COUNT,
  "typo_nguoi_new": $(echo "$NGUOI_NEW" | wc -w),
  "one_sentence_defs": $ONE_SENT_COUNT,
  "few_key_points": $FEW_COUNT,
  "few_key_points_detail": $(echo "$FEW_POINTS" | jq -R -s -c 'split(" ") | map(select(length>0))'),
  "truncated_concepts": $(echo "$TRUNCATED_CONCEPTS" | grep -c "." || echo 0),
  "truncated_sources": $(echo "$TRUNCATED_SOURCES" | grep -c "." || echo 0),
  "empty_sources": $(echo "$EMPTY_SOURCES" | grep -c "." || echo 0),
  "empty_key_ideas": $(echo "$EMPTY_KEY_IDEAS" | grep -c "." || echo 0),
  "draft_concepts": $DRAFT_COUNT
}
EOF
else
    echo "=== Output Validator Quick Scan — $TODAY ==="
    echo ""
    echo "📁 New files today: $NEW_COUNT"
    for f in $NEW_FILES; do echo "   $f"; done
    echo ""
    echo "🔤 Typo 'ngưởi': $NGUOI_COUNT files (new: $(echo "$NGUOI_NEW" | wc -w))"
    echo "📝 1-sentence definitions: $ONE_SENT_COUNT concepts"
    echo "📊 Too few key points (<5): $FEW_COUNT"
    for fp in $FEW_POINTS; do echo "   $fp"; done
    echo "✂️  Truncated concepts (missing sections): $(echo "$TRUNCATED_CONCEPTS" | grep -c "." || echo 0)"
    for tc in $TRUNCATED_CONCEPTS; do echo "   $tc"; done
    echo "✂️  Truncated sources (missing Concepts referenced): $(echo "$TRUNCATED_SOURCES" | grep -c "." || echo 0)"
    echo "📭 Empty Key ideas: $(echo "$EMPTY_KEY_IDEAS" | grep -c "." || echo 0)"
    echo "📭 Empty Sources: $(echo "$EMPTY_SOURCES" | grep -c "." || echo 0)"
    echo "🏷️  Draft concepts: $DRAFT_COUNT"
    echo ""
    echo "Total sources: $(file_list 'wiki/sources' | wc -l)"
    echo "Total concepts: $(file_list 'wiki/concepts' | wc -l)"
fi
