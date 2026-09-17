# Full-tree hygiene scan notes

Condensed learnings from a real full-tree cron run on 2026-06-26.

## Practical classification rules

- If `wiki/reviews/_approval-log.md` exists and the action workflow references it, treat it as a **live workflow artifact**.
- If that file is not whitelisted in `wiki/meta/folder-structure.md`, report it as **`[SPEC CONFLICT]`**. Do not silently ignore it, and do not downgrade it to noise.
- In `wiki/drafts/`, `*.bak` files are usually cleanup leftovers. Report them as **WARNING / Orphan / Temporary file detected**.
- In `wiki/drafts/`, `.gitkeep` inside a non-empty folder is a **cleanup warning**, not a format or path error.
- Backup subfolders inside `wiki/drafts/` are still **ERROR / Path** because the zone is defined as flat.

## Reporting priorities under the daily 20-issue cap

Prioritize in this order:
1. Root-whitelist violations
2. Path violations in active content zones (`raw/`, `wiki/`, `context/`)
3. Spec/workflow conflicts
4. Naming errors that block structural correctness
5. Cleanup warnings (`.bak`, placeholder files)
6. INFO backlog such as review reports older than 30 days

## Expected INFO backlog pattern

A mature repo may accumulate many `wiki/reviews/YYYY-MM-DD_<type>-report.md` files older than 30 days.
These should show up as INFO archive candidates and can dominate the tail of a full-tree scan. That is normal; keep them below higher-severity issues in the report.
