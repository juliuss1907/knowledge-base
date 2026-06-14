# Common Non-Compliant Patterns

> Recurring hygiene violations observed in practice.
> Updated: 2026-06-14

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
- `state/` — runtime state folder; should be inside `.hermes/` or `.openclaw/`
- `temp_content/` — scratch folder; should be removed after use
- `memory/` — old folder migrated to `.openclaw/memory/` in v1.2; should be removed

---

## Heartbeat artifacts

Agent heartbeat files that sometimes leak outside their home:

- `raw/.last_heartbeat` — should be in `.hermes/` or `.openclaw/`, not `raw/`
- `wiki/reviews/HEARTBEAT.md` — should be in `.hermes/` or root (if symlink), not `wiki/reviews/`

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
