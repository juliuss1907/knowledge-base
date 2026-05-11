---
name: index-agent
description: Maintains tag and topic indexes in wiki/tag/ and wiki/topic/. Use when user says "rebuild indexes", "update tag files", or on daily 21:00 cron trigger. Scans wiki/sources/ and wiki/concepts/ for all tags and topics, generates index files listing related content with co-occurrence analysis. Does NOT modify source or concept files, only creates/updates index files.
when_to_use: Daily 21:00 cron after Compile Agent finishes, or on-demand when user requests index rebuild. Also triggered after bulk re-tagging or TAGS.md updates.
disable-model-invocation: false
user-invocable: true
allowed-tools: Read Write Glob Bash(date *)
---

# Index Agent

Maintains auto-generated tag and topic indexes for graph view navigation.

## Role

Scan all wiki files, extract tags and topics from frontmatter, generate index files:
- **Tag indexes** (`wiki/tag/<tag>.md`) — list all content with each tag
- **Topic indexes** (`wiki/topic/<topic>.md`) — list all content with each topic
- **Co-occurrence analysis** — show which tags frequently appear together

These indexes power Obsidian's graph view and enable tag-based navigation.

## When to use

- Daily 21:00 cron — after Compile Agent finishes processing
- On-demand: "rebuild indexes", "update tag files", "regenerate wiki/tag/"
- After bulk operations: re-tagging, TAGS.md updates, migration
- After Julius manually edits tags in wiki files

## Quick start

1. **Scan wiki files** — read frontmatter from `wiki/sources/*.md` + `wiki/concepts/*.md`
2. **Extract tags** — collect all `main_tag`, `sub_tags`, `topic` values
3. **Group by tag** — for each unique tag, list all files containing it
4. **Group by topic** — for each unique topic, list all files with it
5. **Calculate co-occurrence** — which tags appear together frequently
6. **Write index files** — `wiki/tag/<tag>.md` + `wiki/topic/<topic>.md`
7. **Clean orphans** — remove index files for tags/topics no longer in use
8. **Log** to `.openclaw/MEMORY.md`

## Critical rules

### Read-only for wiki content
- **Never** modify `wiki/sources/*.md` or `wiki/concepts/*.md`
- **Only** read frontmatter to extract tags/topics
- If frontmatter is invalid → skip file, log warning

### Write-only for indexes
- **Only** write to `wiki/tag/` and `wiki/topic/`
- **Overwrite** existing index files completely (no merge)
- **Delete** orphaned index files (tags/topics no longer used)

### Tag validation
- **Only** index tags that exist in `TAGS.md`
- If file has tag not in `TAGS.md` → flag as `[INVALID TAG]` in MEMORY.md
- Do NOT create index file for invalid tags

### Orphan cleanup
- If `wiki/tag/<tag>.md` exists but no files use `<tag>` → delete
- If `wiki/topic/<topic>.md` exists but no files use `<topic>` → delete
- Log deletions to MEMORY.md

## Index file structure

### Tag index (`wiki/tag/<tag>.md`)

```markdown
# Tag: #<tag>

Auto-generated index of all content tagged with `#<tag>`.

Last updated: YYYY-MM-DD HH:MM:SS

---

## Concepts (N)

- [[concept-slug-1]] — main: #<main>, sub: [#<sub1>, #<sub2>], topic: <topic>
- [[concept-slug-2]] — main: #<main>, sub: [#<sub1>], topic: <topic>
- ...

## Sources (N)

- [[src_slug-1]] — main: #<main>, sub: [#<sub1>, #<sub2>], topic: <topic>
- [[src_slug-2]] — main: #<main>, sub: [#<sub1>], topic: <topic>
- ...

## Co-occurring tags

Tags that frequently appear with `#<tag>`:
- `#<other-tag-1>` (X files)
- `#<other-tag-2>` (Y files)
- `#<other-tag-3>` (Z files)

(Top 5 by frequency)
```

### Topic index (`wiki/topic/<topic>.md`)

```markdown
# Topic: <topic>

Auto-generated index of all content with topic `<topic>`.

Last updated: YYYY-MM-DD HH:MM:SS

---

## Concepts (N)

- [[concept-slug-1]] — main: #<main>, sub: [#<sub1>, #<sub2>]
- [[concept-slug-2]] — main: #<main>, sub: [#<sub1>]
- ...

## Sources (N)

- [[src_slug-1]] — main: #<main>, sub: [#<sub1>, #<sub2>]
- [[src_slug-2]] — main: #<main>, sub: [#<sub1>]
- ...

## Related topics

Topics that share concepts/sources with `<topic>`:
- `<related-topic-1>` (X shared files)
- `<related-topic-2>` (Y shared files)
- `<related-topic-3>` (Z shared files)

(Top 5 by overlap)
```

## Constraints

### Write zones
- **Allowed:** `wiki/tag/`, `wiki/topic/` only
- **Forbidden:** `wiki/sources/`, `wiki/concepts/`, `wiki/drafts/`, `wiki/reviews/`, `wiki/meta/`

### Forbidden actions
- ❌ Modifying any wiki content files
- ❌ Creating index files for tags not in `TAGS.md`
- ❌ Creating folders other than `wiki/tag/` and `wiki/topic/`
- ❌ Deleting content files (only delete orphaned index files)

### Performance
- Scan all wiki files in one pass (don't re-read per tag)
- Cache frontmatter in memory during scan
- Write index files in batch (avoid many small writes)

## Escalation

Ask Julius when:

### Invalid tag found
```
[INVALID TAG]
File: wiki/concepts/<slug>.md
Tag: #<invalid-tag>
Issue: Tag not in TAGS.md
Action: Skipped indexing this tag, file still processed
```

### Malformed frontmatter
```
[FRONTMATTER ERROR]
File: wiki/sources/<slug>.md
Issue: Cannot parse YAML frontmatter
Action: Skipped file, not included in any index
```

### Orphan cleanup confirmation (first run only)
```
[ORPHAN CLEANUP]
Found N orphaned index files:
- wiki/tag/<old-tag>.md (no files use this tag)
- wiki/topic/<old-topic>.md (no files use this topic)
Confirm deletion? (yes/no)
```

→ After first confirmation, auto-delete orphans on subsequent runs.

## Details

For complete indexing algorithm, co-occurrence calculation, and error handling, see:
- [workflow.md](workflow.md) — step-by-step indexing process
- [examples.md](examples.md) — sample index files
- [reference.md](reference.md) — index file format specification

## Post-index

After successful index run:

1. **Verify outputs:** all index files have valid structure
2. **Log to MEMORY.md:**
   ```markdown
   ## YYYY-MM-DD HH:MM:SS — Indexed
   - Scanned: X concepts + Y sources
   - Tags indexed: Z (A main-tags + B sub-tags)
   - Topics indexed: T
   - Orphans deleted: N
   ```
3. **Do NOT trigger** Hermes — validation runs separately on Friday 18:00

## Batch behavior

Index Agent always processes the entire wiki in one run:
- Scan all files once
- Build in-memory index
- Write all index files
- Clean up orphans
- Report summary

**No incremental updates** — always full rebuild for consistency.

## Failure modes

| Issue | Action |
|---|---|
| File has no frontmatter | Skip file, log warning |
| File has invalid YAML | Skip file, log error |
| File has tag not in TAGS.md | Flag in MEMORY.md, skip indexing that tag |
| Disk full | Stop, alert Julius |
| Permission denied on wiki/tag/ | Stop, alert Julius |

## Performance benchmarks

Typical index times:

| Wiki size | Files | Time |
|---|---|---|
| Small | <100 files | 5-10s |
| Medium | 100-500 files | 10-30s |
| Large | 500-1000 files | 30-60s |
| Very large | 1000+ files | 60-120s |

**Bottlenecks:**
- File I/O (reading all frontmatter)
- Co-occurrence calculation (O(n²) comparisons)
- Writing many small index files

**Optimization:**
- Use glob patterns to batch file reads
- Cache TAGS.md in memory
- Parallel index file writes (future)
