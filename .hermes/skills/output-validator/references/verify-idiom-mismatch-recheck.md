# Verify-script idiom mismatch — check each file in its own idiom (2026-10-04 reinforcement)

A first verify run on the 10-04 output validation returned `PASS=29 FAIL=1`. Applying
the standing rule ("verify FAILs are script bugs until proven otherwise"), the whole
diagnosis was one command per file:

```bash
grep -cF '848 (221 sources + 627 concepts)'            wiki/reviews/_action-required.md   # 0
grep -cF '848 files (221 sources + 627 concepts)'      wiki/reviews/_action-required.md   # 3
grep -cF '848 (221 sources + 627 concepts)'            wiki/reviews/2026-10-04_output-report.md  # 1
```

The numbers agreed everywhere. Only the **idiom** differed: the report writes
`**Files checked:** 848 (221 sources + 627 concepts)`, the action file writes
`848 files (221 sources + 627 concepts)` in its summary row.

## The twist worth internalising

This is the 09-30 Class-2 idiom mismatch, but with a different resolution. There, two
files could have been reconciled and one was arguably stale. **Here both idioms are
correct by design** — the action file has always prefixed its counts with "files", and
several sibling Format/Hygiene rows in the same table use the same shape. No file is
wrong. Fix the check, not the files.

Had the check "won", it would have pushed a cross-file edit that made one file
inconsistent with its own table neighbours.

## Rules

1. When a cross-file assertion FAILs, grep the literal against **each** file separately
   before touching anything. Print the counts.
2. If both files carry the right number in different wording, **split the single
   cross-file assertion into one assertion per file**. A future divergence then shows
   up as two named checks instead of one unexplained FAIL.
3. Never normalise a wording difference by editing the file that is internally
   consistent with its neighbours.

## Re-run after editing the script

After fixing the check, the script was re-run end to end: `PASS=31 FAIL=0`.

Always re-run the **full** script after editing it and report the final count in the
run log. A partial re-run, or quoting the first run's count as the result, is worse
than no verification evidence at all — the numbers will not match the file the reader
is looking at.