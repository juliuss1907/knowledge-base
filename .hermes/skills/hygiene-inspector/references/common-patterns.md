# Common Non-Compliant Patterns

> Recurring hygiene violations observed in practice.
> Updated: 2026-08-16

---

## Review file naming (wiki/reviews/)

The canonical format is `YYYY-MM-DD_<type>-report.md` where `<type>` is `format`, `output`, or `hygiene`.

Observed bad patterns and their fixes:

| Bad | Good | Fix action |
|---|---|---|
| `format-report-2026-05-30.md` | `2026-05-30_format-report.md` | Rename |
| `output-report-2026-06-14.md` | `2026-06-14_output-report.md` | Rename |
| `hygiene-report-2026-06-14.md` | `2026-06-14_hygiene-report.md` | Rename |
| `2026-05-28_validation-check.md` | `2026-05-28_output-report.md` | Rename |
| `2026-06-01_format-report-v2.md` | `2026-06-01_format-report.md` | Merge or overwrite |

**Systemic note:** Multiple historical reports accumulate with wrong naming. A bulk rename or archive pass is recommended once per quarter.

---

## Draft file naming (wiki/drafts/)

Slugs must use lowercase and hyphens only. Underscores are the most common violation.

| Bad | Good |
|---|---|
| `analysis_2026-advice.md` | `analysis-2026-advice.md` |
| `my_draft_file.md` | `my-draft-file.md` |

---

## Root-level orphans

Files and folders that frequently appear at root but are not in the whitelist:

- `openclaw-workspace-state.json` — **recurring since 2026-08-22; 3rd consecutive run flagged 08-24.** OpenClaw runtime workspace state (`version 1, setupCompletedAt 2026-05-12`), 69 bytes. Applied inline 08-23 morning (git rm → ~/.openclaw/) — runtime recreated <12h and ~10-min git auto-commit (`vault backup`) re-tracked it. Applied again 08-24 morning (removal commit `b568979f` 09:52 + `.gitignore` guard lines 88–89) — runtime recreated **10:00 SAME DAY: recycle < 1h, accelerating**. Gitignore guard now holds the REPO clean (file untracked + ignored; `git ls-files --error-unmatch` fails, `git check-ignore` hits) — only the disk-level orphan persists, and history retains pre-09:52 committed copies (cosmetic only; do NOT rewrite history). Writer still active on OpenClaw 2026.7.1-2; expected to end with the SQLite workspace-state refactor update. **08-24 verdict: STOP re-deleting (4th deletion changes nothing) — fix is either redirect the writer output path OR wait for the update.** **08-25: 4th consecutive run flagged (1E, only issue; 55,860 paths). Root cause CONFIRMED in vendor source (SKILL.md v1.21 pitfall #9: any dir containing AGENTS.md = workspace; state path CWD-relative by design, `dist/workspace-DkQ7irPD.js`). Disk file persisted all day (mtime 08-24 10:00, no fresh write on 08-25); git-level clean (untracked + `.gitignore:88` guard verified via `git check-ignore -v`). Per-run ERROR listing of this file remains correct and expected; do NOT re-escalate [SYSTEMATIC VIOLATION], do NOT recommend deletion-only fixes — reference SKILL.md pitfall #9 instead.**

- `RAW_BACKLOG.md` — leftover from manual tracking; should move to `wiki/drafts/` or `raw/articles/`
- `MEMORY.md` — agent memory file that leaked from `.hermes/` or `.openclaw/`
- `search/` — temporary search index; should be gitignored or removed
- `state/` — empty directory, **resolved since 07-20** (absent 07-20 through 07-22). Was recurring since 06-25. If it reappears, move inside `.hermes/` or `.openclaw/`; otherwise `rmdir`.
- `memory/` — old folder migrated to `.openclaw/memory/` in v1.2. **Resolved since 07-21** — absent 07-21 and 07-22 after Fix Agent bulk apply removed the folder and moved contents. Previously recurred 10 times (07-03 through 07-20). If it reappears, the writing process targets `memory/` instead of `.openclaw/memory/` — fix the process output path.
- `temp_content/` — scratch folder; should be removed after use

**Update 2026-07-22 — `memory/` and `state/` resolution confirmed:** Second consecutive clean run (51,944 paths) with zero root orphans. Both folders absent from 07-21 and 07-22 hygiene runs. Resolution appears permanent after Fix Agent bulk apply (07-20). If either reappears, escalate to process-level fix — do not treat as another file deletion.

**Update 2026-08-14 — `memory/` and `state/` RESURFACED after 4 clean runs (08-11 -> 08-13).** Hygiene 08-14 run (53,559 paths) found `memory/` (containing `memory/2026-08-14-0153.md`, an OpenClaw session log created 08:54) and an empty `state/`. The session-log file confirms the memory-log writer is emitting to KB root `memory/` instead of `.openclaw/memory/`. This is a process-level leak — file deletion is a stopgap; the writing process output path must be corrected. Escalated as [SYSTEMATIC VIOLATION] in the 08-14 report. 3-consecutive-clean streak broken.

**Update 2026-08-17 — `memory/` AND `state/` both resurfaced (4th consecutive run, 08-14→08-17).** Hygiene 08-17 run (53,578 paths) found `memory/` holding **6 files, all created 08-17**: 3 OpenClaw session logs (`2026-08-17-1325/1327/1329.md`, agent:main:main), `heartbeat-ok.md`, `heartbeat-poll.md`, and `fetch-status.md`. All 6 are **git-tracked** (`git ls-files memory/` confirmed) — they reach commits via the ~10-min auto `vault backup`, so filesystem deletion only removes the working copy and the committed copy resurrects on next checkout/sync. The writer runs multiple times daily. Fix MUST be root-cause (redirect the session/heartbeat/fetch writer output path from `memory/` → `.openclaw/memory/`) plus a committable removal (`git rm -r memory/` + commit). `state/` persists as an empty untracked phantom dir. Escalated as [SYSTEMATIC VIOLATION] in the 08-17 report. 08-11→08-13 clean streak remains broken.

**Update 2026-08-29 — `openclaw-workspace-state.json` 8th consecutive run flagged (08-22 → 08-29).** Hygiene 08-29 run (55,940 paths) — same status as 08-28: disk orphan persists (69 bytes, mtime 08-24 10:00, NO fresh write in 5 days), git-level clean (untracked + `.gitignore` guard via `git check-ignore`). Root cause CONFIRMED (SKILL.md v1.21 pitfall #9: OpenClaw treats any dir with AGENTS.md as workspace; state path CWD-relative by design). Per-pitfall ERROR listing remains correct; do NOT re-escalate [SYSTEMATIC VIOLATION], do NOT recommend deletion-only fixes. `wiki/HEARTBEAT.md` symlink also flagged 4th consecutive run (08-26 → 08-29, created 08-26 17:01); untracked + gitignored, same process-level leak — some sync tool mirrors the root `HEARTBEAT.md → .openclaw/HEARTBEAT.md` symlink into `wiki/`. `memory/` + `state/` clean 7th consecutive run.

---

## Heartbeat artifacts

Agent heartbeat files that sometimes leak outside their home:

- `raw/.last_heartbeat` — should be in `.hermes/` or `.openclaw/`, not `raw/`
- `wiki/HEARTBEAT.md` — **new variant (2026-08-10):** leaked to wiki/ root level, distinct from the wiki/reviews/ leak. Caught by wiki-root-level check before 08-10; now has dedicated HEARTBEAT_LEAK_PATHS classification.
- `wiki/reviews/HEARTBEAT.md` — should be in `.hermes/` or root (if symlink), not `wiki/reviews/`

**Recurring note (2026-08-10):** `wiki/HEARTBEAT.md` has been flagged every run since 08-07 (4th consecutive). This is a **process-level leak** — a runtime process writes HEARTBEAT.md to `wiki/` root instead of the agent home. The scan script now detects this specifically (added to `HEARTBEAT_LEAK_PATHS` 2026-08-10).

**Recurring note (2026-06-27):** `wiki/reviews/HEARTBEAT.md` has been flagged every run since 06-25. Fix Agent deleted it 2026-06-27 09:34 but it reappeared by 23:30. This is a **process-level leak** — a runtime process writes HEARTBEAT.md to `wiki/reviews/` instead of the agent home. File deletion alone will not resolve it; the writing process must be identified and its output path corrected.

**Resolution (2026-06-28):** The HEARTBEAT leak was resolved. The 2026-06-28 hygiene run (23:30) scanned 51,528 paths and found zero HEARTBEAT artifacts in `wiki/reviews/` or `raw/`. The root-level symlink `HEARTBEAT.md → .openclaw/HEARTBEAT.md` is correctly placed. If the leak recurs, flag as ERROR and escalate to process-level fix.

---

## Raw content naming — papers vs standard types

`raw/papers/` uses a different naming convention from other raw types:

| Type | Pattern | Example |
|---|---|---|
| Standard (`articles`, `posts`, etc.) | `YYYY-MM-DD_<slug>.md` | `2026-05-07_anthropic-claude-code.md` |
| Papers | `YYYY-MM-DD_<author>_<title>.md` | `2026-05-22_ning-et-al_code-as-agent-harness.md` |

**Pitfall:** A single `RE_RAW_CONTENT` regex that matches `YYYY-MM-DD_<slug>.md` will false-positive on papers. The scan script must check for `RE_RAW_PAPERS` before falling through to `RE_RAW_CONTENT` when processing `raw/papers/`.

---

## Scan script false-positive traps

Three patterns that caused false positives in the 2026-06-27 run:

1. **Archive regex prefix** — `RE_REVIEW_ARCHIVE` must use `^wiki/reviews/archive/` not `^archive/`. `os.walk` relative paths start from the repo root, so the full `wiki/reviews/archive/` prefix is needed.

2. **Papers naming** — `raw/papers/` uses `YYYY-MM-DD_<author>_<title>.md` (two slug segments separated by underscore). A single `RE_RAW_CONTENT` will flag every paper as non-compliant. Must add `RE_RAW_PAPERS` and check it first.

3. **Whitelisted files with uppercase** — `context/USER.md` is explicitly whitelisted by name but fails a generic lowercase-hyphen naming check. Skip the naming check for files that appear by name in an explicit whitelist (`CONTEXT_FILES`, `WIKI_META_FILES`). Only apply naming rules to content files (concepts, sources, tags, topics, drafts).

---

## Agent home content confusion

`.hermes/` and `.openclaw/` contain agent runtime files. The Hygiene Inspector should NOT flag deep internals as orphans. However, user content (e.g., `src_*.md`, `YYYY-MM-DD_*.md`, or article-like files) placed at the first level inside these agent homes IS a real orphan.

**Example real orphan:**
- `.openclaw/memory/2026-05-26.md` — user content inside agent home

**Example false positive (do NOT flag):**
- `.hermes/hermes-agent/agent/tool_executor.py` — runtime code
- `.hermes/cron/output/284427e7c7fa/2026-05-12_23-30-01.md` — cron output
- `.hermes/skills/creative/touchdesigner-mcp/references/particles.md` — skill reference

**Rule:** Skip `.hermes/` and `.openclaw/` at depth > 1 for orphan checks.
