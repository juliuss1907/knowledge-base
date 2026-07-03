# Common Non-Compliant Patterns

> Recurring hygiene violations observed in practice.
> Updated: 2026-07-03

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

- `RAW_BACKLOG.md` — leftover from manual tracking; should move to `wiki/drafts/` or `raw/articles/`
- `MEMORY.md` — agent memory file that leaked from `.hermes/` or `.openclaw/`
- `search/` — temporary search index; should be gitignored or removed
- `state/` — empty directory, **recurring** (flagged 06-25, resolved 06-27, recreated 07-02 10:28, still present 07-03). Not in root whitelist. If needed, move inside `.hermes/` or `.openclaw/`; otherwise `rmdir`.\n- `memory/` — old folder migrated to `.openclaw/memory/` in v1.2. **Recurring** — reappeared 2026-07-03 with a content file (`2026-07-03.md`) inside. The writing process is targeting `memory/` instead of `.openclaw/memory/`. Move file and rmdir; fix the process output path.
- `temp_content/` — scratch folder; should be removed after use
- `memory/` — old folder migrated to `.openclaw/memory/` in v1.2; should be removed

---

## Heartbeat artifacts

Agent heartbeat files that sometimes leak outside their home:

- `raw/.last_heartbeat` — should be in `.hermes/` or `.openclaw/`, not `raw/`
- `wiki/reviews/HEARTBEAT.md` — should be in `.hermes/` or root (if symlink), not `wiki/reviews/`

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
