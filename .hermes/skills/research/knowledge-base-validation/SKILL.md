---
name: knowledge-base-validation
description: Review wiki concept files and write review results to wiki/reviews/. Updates _pending.md and reviews_index.md.
tools:
  - read_file
  - write_file
  - search_files
  - execute_code
  - terminal
---

# Knowledge Base Validation

Review wiki/concepts/ files with status draft or ready_review. Write structured review files to wiki/reviews/ and update _pending.md.

## Workspace

`~/knowledge-base/knowledge-base-agent/`

## Filtering

- Read files in `wiki/concepts/` with `status: draft` or `status: ready_review`
- Skip files with `status: revising`
- Do NOT read `raw/`, `Context/`, or OpenClaw memory

## Output Files

- Individual reviews: `wiki/reviews/YYYY-MM-DD_[concept-name]-review.md`
- Queue: `wiki/reviews/_pending.md`
- Index: `wiki/indexes/reviews_index.md`

## Verdicts

- **PROMOTE**: Well-structured, deep content, specific examples, proper references
- **REVISE**: Usable but has issues (wrong tags, missing sections, generic content)
- **REJECT**: Fundamentally broken (empty content, single-sentence descriptions)

Do NOT promote anything yourself. Wait for Julius to confirm.

## Review Criteria

1. Frontmatter completeness (type, status, tags, sources, date/date_created)
2. Structure (Mô tả/Tóm tắt, Chi tiết/Nội dung chi tiết, Liên quan, Nguồn tham khảo sections)
3. Content quality (depth, specific examples, insights beyond docs)
4. Tag validity (approved: ai, llm, crypto, web3, business, marketing, content, productivity, health, coding, research, finance, mindset, keyboard, website-hay, nature)
5. Source references must exist in wiki/sources/
6. Cross-references in Liên quan (flag if concepts don't exist)
7. Language consistency (flag all-English when others are Vietnamese)

### Tag Parsing

Tags in frontmatter use format `tags: [#tag1, #tag2, #tag3]` — strip the `#` prefix before comparing to the approved list. Common invalid tags and recommended replacements:
- `#tech` → use `#coding` or `#research`
- `#design` → use `#business` or `#content`
- `#security` → use `#coding` or `#crypto`

### Section Detection

Use **flexible regex matching** for sections — files use variant headers:
- **Mô tả**: also `## Tóm tắt` (summary)
- **Chi tiết**: also `## Nội dung chi tiết`, `## Nội dung`, `## Chi Tiết`
- **Nguồn tham khảo**: also `## Nguồn`, `## Source`, `## References`

### Verdict Thresholds

- **REJECT** if: content < 50 words, OR missing 3+ required sections
- **REVISE** if: any structural issue (missing sections, invalid tags, missing examples, no date) but content has substance (>100 words)
- **PROMOTE** only if: all 4 sections present, all tags valid, has specific examples, date field exists, word count > 200, source refs verified
- In practice, almost no draft concepts achieve PROMOTE on first review — most lack the Chi tiết section

## Review File Frontmatter

```yaml
type: review
concept: [name]
status: [same as concept status]
reviewer: hermes
date: YYYY-MM-DD
verdict: PROMOTE | REVISE | REJECT
```

## _pending.md Contents

1. Instructions for Julius (PROMOTE = copy to archive, REVISE = fix and resubmit, REJECT = move to drafts)
2. Tables grouped by verdict with concept name and reason
3. Statistics (total, by verdict count)
4. Common issues section

## Process

1. Scan wiki/concepts/ for .md files using `os.listdir()` — `search_files` may return 0 results on this directory
2. Parse frontmatter with regex, filter by status (draft/ready_review)
3. For tag parsing: strip `#` prefix, split by `,`, trim whitespace. Format is `tags: [#tag1, #tag2]`
4. Read each qualifying file fully
5. Verify source files exist in wiki/sources/ — source filenames use `src_` prefix pattern. Match `src_XXXX.md` in the sources directory.
6. For cross-reference validation: check if referenced concept names exist as filenames (minus .md extension) in wiki/concepts/
7. Evaluate against criteria using the verdict thresholds above
8. Write review files to wiki/reviews/ with proper frontmatter
9. Write _pending.md with verdict tables, statistics, common issues, and guidance for Compile Agent
10. Update reviews_index.md in wiki/indexes/

### Implementation Pattern

Use `execute_code` with Python for all file operations (reading concepts, parsing frontmatter, writing reviews, computing statistics). This is much faster than individual tool calls for 50+ files. Key steps:
- Load all concept files at once, parse YAML frontmatter with regex
- Batch-validate tags, sections, sources, cross-references in a single pass
- Generate all review files + _pending.md + reviews_index.md in one or two scripts
- Save intermediate JSON to `/tmp/` if needed between execute_code calls

## Promote Procedure (after Julius approves)

When Julius confirms PROMOTE for specific concepts:

1. **Copy** each promoted concept to `knowledge-base-personal/Content_Archive/[concept].md` (original status preserved)
2. **Update** the original in `wiki/concepts/`: change `status: draft` → `status: published`
3. **Keep originals** in wiki/concepts/ — do NOT delete them (Julius preference)

```python
# Promote logic (execute_code)
archive_dir = os.path.join(workspace, "knowledge-base-personal/Content_Archive")
# Copy to archive (original content)
# Update original: status: draft/ready_review → status: published
```

### What happens to REVISE and REJECT
- Julius delegates these to other agents (e.g., Kara). Not Hermes responsibility.
- Do NOT modify REVISE or REJECT files unless Julius explicitly asks.

## Pitfalls

- Workspace is ~/knowledge-base/knowledge-base-agent/ not hermes-agent project
- Tags have a strict approved whitelist — `#tech`, `#design`, `#security` are NOT in the list
- Tags in frontmatter have `#` prefix — must strip before comparing: `tags: [#business, #ai]`→ parse as `['business', 'ai']`
- Verify wiki/sources/ file references actually exist — filenames follow `src_XXXX.md` pattern
- Flag nonexistent concepts referenced in Liên quan sections — most cross-refs point to concepts that don't exist yet
- Avoid unicode/emoji in execute_code Python scripts (causes SyntaxError)
- When promoting: KEEP originals in wiki/concepts/, only update status field — Julius prefers both copies to exist
- `search_files` returns 0 results for `wiki/concepts/` — use `os.listdir()` in `execute_code` instead
- Most concepts lack the "Chi tiết" section — this is the #1 most common issue flagged as REVISE
- The "date" field may appear as either `date:` or `date_created:` — check for both
- Concepts with Vietnamese titles but English-only content should be flagged