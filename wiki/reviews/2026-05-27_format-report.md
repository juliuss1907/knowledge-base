# Format Validation — 2026-05-27

**Status:** approved 2026-05-27
**Issues found:** 20 (14 ERROR + 6 WARNING)
**Files checked:** 123 (99 concepts + 24 sources)
**Created:** 2026-05-27 07:43:00
**Validator:** format-validator

---

## Issue 1: Invalid status 'stub' × 5 files (SYSTEMATIC)

**File:** wiki/concepts/ai-powered-discovery.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `status: stub` is not a valid status
**Current:** stub
**Expected:** `draft` | `reviewed` | `needs-revision`
**Suggested fix:** Replace `status: stub` with `status: draft` in all 5 files

**Affected files:**
- `wiki/concepts/ai-powered-discovery.md`
- `wiki/concepts/ai-productivity.md`
- `wiki/concepts/conversational-website.md`
- `wiki/concepts/generative-ai-seo.md`
- `wiki/concepts/human-judgment-ai.md`

---

## Issue 2: Missing 'Key ideas' section × 5 files

**File:** wiki/concepts/ai-powered-discovery.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Required section `## Key ideas` is missing
**Current:** `['Definition', 'Related concepts', 'Sources', 'Backlinks', 'Notes']`
**Expected:** `['Definition', 'Key ideas', 'Related concepts', 'Sources']`
**Suggested fix:** Add `## Key ideas` section after `## Definition`

**Affected files:**
- `wiki/concepts/ai-powered-discovery.md`
- `wiki/concepts/ai-productivity.md`
- `wiki/concepts/conversational-website.md`
- `wiki/concepts/generative-ai-seo.md`
- `wiki/concepts/human-judgment-ai.md`

---

## Issue 3: Empty sources array × 4 files

**File:** wiki/concepts/ai-powered-discovery.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `sources: []` — empty sources array
**Current:** `[]`
**Expected:** At least 1 source wikilink
**Suggested fix:** Add source wikilinks (at minimum, the source that spawned this concept)

**Affected files:**
- `wiki/concepts/ai-powered-discovery.md`
- `wiki/concepts/conversational-website.md`
- `wiki/concepts/generative-ai-seo.md`
- `wiki/concepts/human-judgment-ai.md`

---

## Issue 4: Invalid sub_tag 'productivity'

**File:** wiki/concepts/ai-productivity.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sub_tags: [tools, productivity]` — 'productivity' is a Pool A tag, not Pool B
**Current:** `productivity`
**Expected:** One of Pool B: `automation, coding, defi, hack, law, layer1, layer2, news, opinion, perpdex, research, tools, tutorial, vibecode`
**Suggested fix:** Replace 'productivity' with a valid Pool B sub-tag (e.g., `opinion` or `research`)

---

## Issue 5: Invalid sub_tag 'marketing'

**File:** wiki/concepts/generative-ai-seo.md
**Severity:** ERROR
**Category:** Frontmatter
**Issue:** `sub_tags: [tools, marketing]` — 'marketing' is not in TAGS.md
**Current:** `marketing`
**Expected:** One of Pool B: `automation, coding, defi, hack, law, layer1, layer2, news, opinion, perpdex, research, tools, tutorial, vibecode`
**Suggested fix:** Either propose `#marketing` as new sub-tag to Julius, or replace with closest existing tag (e.g., `opinion` or `news`)

---

## Issue 6: Missing 'Related concepts' section

**File:** wiki/concepts/static-website-blind-spot.md
**Severity:** ERROR
**Category:** Sections
**Issue:** Section header uses `## Related Concepts` (capital C) instead of `## Related concepts`
**Current:** `['Definition', 'Key ideas', 'Opportunity', 'Related Concepts', 'Sources', 'Backlinks', 'Notes']`
**Expected:** `['Definition', 'Key ideas', 'Related concepts', 'Sources']`
**Suggested fix:** Rename `## Related Concepts` → `## Related concepts`; also note extra sections (`Opportunity`, `Backlinks`, `Notes`) — consider keeping `## Notes` as optional per spec

---

## Issue 7: Code block missing language tag

**File:** wiki/concepts/x-search-tool.md
**Severity:** ERROR
**Category:** Markdown
**Issue:** Code block(s) use bare ` ``` ` without language tag
**Current:** ` ``` ` with no language specifier
**Expected:** Language-tagged code block (e.g., ` ```yaml`)
**Suggested fix:** Add language identifier to code blocks

---

## Issue 8: Field order incorrect (2 source files)

**File:** wiki/sources/src_ai-trillion-dollar-blind-spot.md
**Severity:** WARNING
**Category:** Frontmatter
**Issue:** `author` field appears before `main_tag`, `date_compiled` appears before `topic`
**Current:** `['type', 'original', 'author', 'date_compiled', 'main_tag', 'sub_tags', 'topic']`
**Expected:** `['type', 'original', 'main_tag', 'sub_tags', 'topic', 'date_compiled', 'url', 'author']`
**Suggested fix:** Reorder: move `main_tag, sub_tags, topic` before `date_compiled`, move `author` after `date_compiled`

**Affected files:**
- `wiki/sources/src_ai-trillion-dollar-blind-spot.md`
- `wiki/sources/src_will-ai-replace-systems-thinking.md`

---

## Summary by category

| Category | ERROR | WARNING | INFO |
|---|---|---|---|
| Frontmatter | 7 | 6 | 0 |
| Sections | 6 | 0 | 0 |
| Markdown | 1 | 0 | 0 |
| Naming | 0 | 0 | 0 |
| **Total** | **14** | **6** | **0** |

## Top violation patterns

1. **Invalid status 'stub'** — 5 files use `status: stub` (not in enum)
2. **Missing 'Key ideas' section** — 5 stub concepts lack the required section
3. **Empty sources** — 4 stub concepts have `sources: []`
4. **Invalid sub-tags** — 2 files use tags not in Pool B (`productivity`, `marketing`)
5. **Field order** — 2 source files have `author` and `date_compiled` out of order

## Systematic issue: Stub concepts with incomplete format

5 concept files share a pattern: `status: stub`, missing `## Key ideas` section, and most have empty sources. These appear to be placeholder concepts created during compilation of new source material but never completed. Compile Agent should ensure all concept files meet minimum format requirements even in draft state:

- `status` must be `draft` (not `stub`)
- All required sections must be present
- At least 1 source wikilink required
