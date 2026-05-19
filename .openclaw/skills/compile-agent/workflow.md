# Compile Agent — Complete Workflow

Detailed step-by-step process for compiling raw content into wiki knowledge.

---

## Overview

This workflow transforms one raw file into structured wiki outputs:
- **Input:** `raw/<type>/YYYY-MM-DD_<slug>.md` (status: unprocessed)
- **Output 1:** `wiki/sources/src_<slug>.md` (source note)
- **Output 2:** `wiki/concepts/<concept>.md` × 1-5 files (concept notes)
- **Side effect:** Update raw frontmatter (status: processed)

Total time per file: 30-90 seconds depending on content length and concept count.

---

## Step 1: Find Unprocessed Files

### Scan raw/ for candidates

```bash
# Find all files with status: unprocessed
grep -r "status: unprocessed" raw/ | cut -d: -f1
```

**Filter criteria:**
- File must be in `raw/<type>/` (one of 6 allowed types)
- Frontmatter must contain `status: unprocessed`
- File must have valid YAML frontmatter (opening and closing `---`)

**Sort order:**
- By `date_ingested` (oldest first)
- If same date, alphabetical by filename

**Batch size:**
- On-demand: process specified files only
- Daily cron: process all unprocessed (no limit)
- Migration: process in batches of 50, report progress

---

## Step 2: Read and Validate Raw File

For each candidate file:

### 2.1 Read frontmatter

```bash
# Extract frontmatter
sed -n '/^---$/,/^---$/p' raw/<type>/<filename>
```

**Required fields check:**
- `type` — must be one of 6 allowed values
- `title` — must be non-empty
- `date_ingested` — must be valid YYYY-MM-DD
- `status` — must be exactly `unprocessed`

**If validation fails:**
```markdown
[VALIDATION ERROR]
File: raw/<type>/<filename>
Issue: Missing required field '<field>' or invalid value
Action: Skipped, logged to MEMORY.md, flagged for Julius
```

### 2.2 Read body content

```bash
# Extract body (everything after second ---)
sed '1,/^---$/d; /^---$/d' raw/<type>/<filename>
```

**Content check:**
- Body must be non-empty (at least 100 characters)
- Must be valid markdown (no binary content)

**If body too short:**
- Flag as `[INSUFFICIENT CONTENT]` in MEMORY.md
- Skip compilation, keep status `unprocessed`

---

## Step 3: Summarize Content

### 3.1 Generate summary (3-5 sentences)

**Prompt template:**
```
Summarize the following content in 3-5 sentences. Keep the same language as the original content. Focus on the main thesis and key takeaways.

Content:
<raw file body>
```

**Output format:**
```
<3-5 sentence summary in original language>
```

**Quality criteria:**
- Captures main thesis
- Mentions key findings or arguments
- Avoids trivial details
- Same language as source (no translation)

### 3.2 Extract key points (5-10 bullets)

**Prompt template:**
```
Extract 5-10 key points from the following content as a bullet list. Keep the same language as the original. Each point should be one sentence.

Content:
<raw file body>
```

**Output format:**
```
- Key point 1
- Key point 2
- ...
- Key point N (5-10 total)
```

**Quality criteria:**
- Each point is self-contained (readable without context)
- Points are ordered by importance
- Avoid redundancy between points
- Technical terms preserved in English

### 3.3 Extract original excerpts (optional)

If content contains notable quotes, code snippets, or data worth preserving verbatim:

**Selection criteria:**
- Quotes that define key concepts
- Code examples demonstrating techniques
- Data/statistics supporting claims
- Author's unique phrasing worth citing

**Format:**
```markdown
## Original excerpts

> "Quote text here"
> — Author name

```code-block
code example
```

**Data:** 40% improvement on benchmark X
```

**Limit:** Max 3-5 excerpts per source note (avoid copying entire article)

---

## Step 4: Extract Concepts

### 4.1 Identify concept candidates

**Prompt template:**
```
Identify 1-5 knowledge atoms from this content that warrant their own concept files. A concept should be:
- A technical term or methodology with depth
- A tool, product, or system worth tracking
- A pattern or practice with reusable knowledge

Do NOT extract:
- Generic terms (AI, blockchain)
- Trivial mentions without explanation
- Author names or organizations (unless they are the subject)

Content:
<raw file body>

Output format:
1. <concept-name-1>: <1 sentence why it's a concept>
2. <concept-name-2>: <1 sentence why it's a concept>
...
```

**Example output:**
```
1. progressive-disclosure: Context engineering technique for Agent Skills, reduces token cost
2. skill-description-pattern: How to write skill descriptions that trigger correctly
3. three-level-loading: Metadata → Instructions → Supporting files loading hierarchy
```

### 4.2 Validate concept candidates

For each candidate, check:

**Depth test:**
- Does the content explain this concept in ≥2 paragraphs?
- Are there actionable details or examples?
- Would this concept be useful to reference from other sources?

**Uniqueness test:**
- Is this distinct from existing concepts? (check `wiki/concepts/` for similar slugs)
- If similar concept exists, should we merge or create separate?

**Naming test:**
- Slug is lowercase-hyphen
- Max 50 characters
- Descriptive enough to understand without context

**If concept fails tests:**
- Skip creation
- Mention in source note's "Key points" instead
- Log decision in MEMORY.md

### 4.3 Check for existing concepts

For each validated candidate:

```bash
# Check if concept file already exists
test -f "wiki/concepts/<concept-slug>.md"
```

**If exists:**
- Mark for **merge** (Step 6.2)
- Read existing file to understand current content

**If not exists:**
- Mark for **create** (Step 6.1)

---

## Step 5: Assign Tags

### 5.1 Read current taxonomy

```bash
# Load TAGS.md to know available tags
cat TAGS.md
```

**Parse:**
- Pool A (main-tags): 7 tags
- Pool B (sub-tags): 12 tags
- Rules: 1 main + 1-3 sub + 1 topic

### 5.2 Select main-tag (Pool A)

**Prompt template:**
```
Given this content, select exactly ONE main-tag from Pool A that best categorizes it:

Pool A: #ai, #crypto, #tech, #productivity, #system, #economic, #politic

Content summary:
<summary from Step 3.1>

Output: <one-tag-from-pool-a>
```

**Decision logic:**
- If content is about AI/ML/LLM → `#ai`
- If content is about blockchain/DeFi/crypto → `#crypto`
- If content is about software/dev tools → `#tech`
- If content is about workflows/methods → `#productivity`
- If content is about architecture/design → `#system`
- If content is about markets/finance → `#economic`
- If content is about policy/regulation → `#politic`

**If ambiguous (e.g., AI + crypto):**
- Choose primary focus (what is 60%+ of content about?)
- Secondary focus goes into sub-tags

### 5.3 Select sub-tags (Pool B, 1-3 tags)

**Prompt template:**
```
Given this content, select 1-3 sub-tags from Pool B that describe cross-cutting attributes:

Pool B: #hack, #tools, #automation, #vibecode, #research, #tutorial, #opinion, #news, #defi, #perpdex, #layer1, #layer2

Content summary:
<summary from Step 3.1>

Output: <1-to-3-tags-from-pool-b>
```

**Decision logic:**
- `#hack` — if about exploits, vulnerabilities, attacks
- `#tools` — if about specific software/products
- `#automation` — if about bots, scripts, workflows
- `#vibecode` — if about AI-assisted development
- `#research` — if academic paper or deep analysis
- `#tutorial` — if how-to guide or walkthrough
- `#opinion` — if personal take or commentary
- `#news` — if recent event or announcement
- `#defi` — if about DeFi protocols (crypto-specific)
- `#perpdex` — if about perpetual exchanges (crypto-specific)
- `#layer1` — if about base-layer blockchains (crypto-specific)
- `#layer2` — if about scaling solutions (crypto-specific)

**Constraints:**
- Minimum 1 sub-tag
- Maximum 3 sub-tags
- If content fits 4+ sub-tags, pick the 3 most relevant

### 5.4 Generate topic (free-form slug)

**Prompt template:**
```
Generate a topic slug (lowercase-hyphen, max 50 chars) that describes the specific subject of this content. This is NOT a tag, but a grouping label.

Examples:
- "claude-code-workflow"
- "defi-hack-curve-pool"
- "progressive-disclosure-pattern"

Content title: <title>
Content summary: <summary>

Output: <topic-slug>
```

**Rules:**
- Lowercase only
- Hyphens for spaces
- Max 50 characters
- Specific enough to group related content
- Not a duplicate of existing tags

### 5.5 Handle missing tags

If content needs a tag not in TAGS.md:

**Stop compilation** and propose:
```
[TAG PROPOSAL]
Pool: A (main-tag) | B (sub-tag)
Proposed: #<new-tag>
Reason: Content is about <X> which doesn't fit existing tags
File context: raw/<type>/<filename>
Closest existing tag: <fallback-tag>
```

**Move file to `wiki/drafts/`** until Julius approves or rejects.

**If approved:**
- Julius updates TAGS.md
- Re-run compilation with new tag

**If rejected:**
- Use fallback tag
- Resume compilation

---

## Step 6: Write Wiki Outputs

### 6.1 Write source note

**File path:**
```
wiki/sources/src_<slug>.md
```

Where `<slug>` is derived from raw filename (strip date prefix and `.md` extension).

**Frontmatter:**
```yaml
---
type: source
original: [[raw/<type>/YYYY-MM-DD_<slug>.md]]
main_tag: <from-step-5.2>
sub_tags: [<from-step-5.3>]
topic: <from-step-5.4>
date_ingested: <from-raw-frontmatter>
date_compiled: <today-YYYY-MM-DD>
url: <from-raw-frontmatter-if-present>
author: <from-raw-frontmatter-if-present>
---
```

**Body structure:**
```markdown
# <Original title from raw>

## Metadata

- **Author:** <author or [unknown]>
- **Published:** <date_published or date_ingested>
- **Source:** <source domain>
- **URL:** <url or N/A>
- **Type:** <article|post|video|paper|repo|website>

## Summary

<3-5 sentence summary from Step 3.1>

## Key points

<5-10 bullet points from Step 3.2>

## Concepts referenced

<wikilinks to concept files from Step 4>
- [[concept-slug-1]]
- [[concept-slug-2]]
- ...

## Original excerpts

<optional, from Step 3.3>
```

**Write operation:**
```bash
cat > "wiki/sources/src_<slug>.md" << 'EOF'
<full content above>
EOF
```

**Verify:**
```bash
# Check file exists
test -f "wiki/sources/src_<slug>.md" && echo "✓ Source note created"

# Check frontmatter valid
head -n 20 "wiki/sources/src_<slug>.md" | grep -q "^---$" && echo "✓ Frontmatter valid"
```

### 6.2 Write/update concept notes

For each concept identified in Step 4:

#### Case A: New concept (file doesn't exist)

**File path:**
```
wiki/concepts/<concept-slug>.md
```

**Frontmatter:**
```yaml
---
type: concept
status: draft
main_tag: <same-as-source-note>
sub_tags: [<same-as-source-note>]
topic: <same-as-source-note>
sources:
  - [[wiki/sources/src_<slug>]]
last_updated: <today-YYYY-MM-DD>
---
```

**Body structure:**
```markdown
# <Concept name>

## Definition

<2-3 sentence definition in same language as source>

## Key ideas

<main points about this concept, extracted from source>
- Idea 1
- Idea 2
- ...

## Related concepts

<wikilinks to other concepts mentioned in source>
- [[related-concept-1]]
- [[related-concept-2]]

## Sources

<auto-maintained list, matches frontmatter>
- [[wiki/sources/src_<slug>]]

## Notes

<empty section for Julius's annotations>
```

**Write operation:**
```bash
cat > "wiki/concepts/<concept-slug>.md" << 'EOF'
<full content above>
EOF
```

#### Case B: Existing concept (file exists)

**Read existing file:**
```bash
cat "wiki/concepts/<concept-slug>.md"
```

**Merge logic:**

1. **Frontmatter:**
   - Append new source to `sources:` list
   - Update `last_updated` to today
   - Keep existing `main_tag`, `sub_tags`, `topic` (do NOT change)

2. **Body sections:**
   - `## Definition` — keep existing (do NOT rewrite)
   - `## Key ideas` — append new ideas, dedupe if similar
   - `## Related concepts` — append new links, dedupe
   - `## Sources` — append new source link
   - `## Notes` — **preserve completely** (Julius's annotations)

**Deduplication logic:**
- Compare new key idea with existing ideas
- If semantic similarity >80% → skip (already covered)
- If new angle or detail → append

**Update operation:**
```bash
# Read existing content
existing=$(cat "wiki/concepts/<concept-slug>.md")

# Parse sections
# Append new source to frontmatter sources: list
# Append new ideas to ## Key ideas
# Preserve ## Notes section

# Write updated content
cat > "wiki/concepts/<concept-slug>.md" << 'EOF'
<merged content>
EOF
```

**Conflict handling:**

If merge is ambiguous (e.g., contradictory definitions):
```bash
# Save new version to drafts
cp "wiki/concepts/<concept-slug>.md" "wiki/drafts/<concept-slug>-merge.md"

# Alert Julius
echo "[MERGE CONFLICT] wiki/concepts/<concept-slug>.md — see drafts/ for new version"
```

---

## Step 7: Update Raw File Status

### 7.1 Edit frontmatter only

**Add fields:**
```yaml
status: processed
compiled_at: YYYY-MM-DD
compiled_to: [[wiki/sources/src_<slug>]]
```

**Edit operation:**
```bash
sed -i 's/^status: unprocessed$/status: processed/' raw/<type>/<filename>
sed -i '/^status: processed$/a compiled_at: $(date +%Y-%m-%d)' raw/<type>/<filename>
sed -i "/^compiled_at:/a compiled_to: [[wiki/sources/src_${slug}]]" raw/<type>/<filename>
```

**Verify:**
```bash
grep -q "status: processed" raw/<type>/<filename> && echo "✓ Status updated"
grep -q "compiled_at:" raw/<type>/<filename> && echo "✓ Compiled date added"
grep -q "compiled_to:" raw/<type>/<filename> && echo "✓ Compiled link added"
```

**Do NOT modify body:**
- Raw file body remains unchanged
- Only frontmatter fields updated

### 7.2 Update raw index file Stats

After updating raw file status, update `raw/<type>/<type>.md` Stats section:

```bash
type_folder="raw/${type}"
total=$(find "${type_folder}/" -name "*.md" -not -name "${type}.md" | wc -l)
processed=$(grep -l "status: processed" ${type_folder}/*.md 2>/dev/null | wc -l)
unprocessed=$((total - processed))
this_week=$(find "${type_folder}/" -name "*.md" -mtime -7 -not -name "${type}.md" | wc -l)
this_month=$(find "${type_folder}/" -name "*.md" -mtime -30 -not -name "${type}.md" | wc -l)

index_file="${type_folder}/${type}.md"

cat > temp_stats << EOF
## Stats

- Total: ${total} files
- By status: ${processed} processed, ${unprocessed} unprocessed
- By date: ${this_week} this week, ${this_month} this month
- Last updated: $(date +%Y-%m-%d)
EOF

sed -i '/^## Stats$/,/^## Items$/{//!d}' "${index_file}"
sed -i '/^## Stats$/r temp_stats' "${index_file}"
rm temp_stats
```

**Note:** Reflects new processed count after compilation.

## Step 8: Log to Memory

### 8.1 Append to MEMORY.md

```markdown
## YYYY-MM-DD HH:MM:SS — Compiled

- **Raw:** raw/<type>/YYYY-MM-DD_<slug>.md
- **Source note:** wiki/sources/src_<slug>.md
- **Concepts:** [<concept-1>, <concept-2>, ...]
- **Tags applied:** main=#<x>, sub=[#<y>, #<z>], topic=<t>
- **Action:** <created|updated> N concept files
```

**Example:**
```markdown
## 2026-05-07 14:30:15 — Compiled

- **Raw:** raw/articles/2026-05-04_claude-code-skills-guide.md
- **Source note:** wiki/sources/src_claude-code-skills-guide.md
- **Concepts:** [progressive-disclosure, skill-description-pattern, three-level-loading]
- **Tags applied:** main=#ai, sub=[#tools, #automation], topic=agent-skills
- **Action:** created 3 concept files
```

### 8.2 Do NOT trigger Index Agent

Index Agent runs separately at 21:00 daily. Do not invoke it after each compilation.

---

## Batch Processing

When compiling multiple files:

### Sequential processing

```bash
for file in $(find raw/ -name "*.md" -exec grep -l "status: unprocessed" {} \;); do
  compile_single_file "$file"
  sleep 1  # Avoid race conditions on shared concept files
done
```

### Progress reporting

Every 10 files:
```
Compiled 10/50: 3 concepts created, 7 updated
Compiled 20/50: 5 concepts created, 15 updated
...
```

### Error handling

On error:
1. Log error to MEMORY.md
2. Skip file (keep status `unprocessed`)
3. Continue with next file
4. Report failed files at end

### Final summary

```
Compilation complete:
- Processed: 48/50 files
- Failed: 2 files (see MEMORY.md)
- Concepts created: 15
- Concepts updated: 33
- Tag proposals: 2 (pending Julius approval)
```

---

## Error Handling

### Missing required frontmatter

```
[ERROR] raw/articles/2026-05-04_file.md
Issue: Missing required field 'title'
Action: Skipped, flagged for Julius
```

### Tag not in TAGS.md

```
[TAG PROPOSAL]
Pool: B (sub-tag)
Proposed: #mcp
Reason: Content is about Model Context Protocol, not covered by existing tags
File context: raw/articles/2026-05-05_mcp-guide.md
Closest existing tag: #tools
```

→ Move to `wiki/drafts/`, wait for Julius approval.

### Concept merge conflict

```
[MERGE CONFLICT] wiki/concepts/progressive-disclosure.md
Issue: New source contradicts existing definition
Action: Saved new version to wiki/drafts/progressive-disclosure-merge.md
```

→ Julius reviews both versions, decides which to keep.

### Disk full

```
[FATAL ERROR] Disk full
Action: Stop batch, alert Julius
```

→ Do not continue, risk data loss.

---

## Validation Checklist

Before marking compilation complete:

- [ ] Source note exists in `wiki/sources/`
- [ ] Source note has valid frontmatter (all required fields)
- [ ] All concept files exist in `wiki/concepts/`
- [ ] All concept files have valid frontmatter
- [ ] Raw file status updated to `processed`
- [ ] Raw file has `compiled_at` field
- [ ] MEMORY.md entry added
- [ ] No files written outside allowed zones

---

## Performance Benchmarks

Typical compilation times:

| Content type | Length | Time |
|---|---|---|
| Short post | <500 words | 15-30s |
| Medium article | 500-2000 words | 30-60s |
| Long article | 2000-5000 words | 60-90s |
| Video transcript | 5000+ words | 90-120s |
| Paper | 10000+ words | 120-180s |

**Bottlenecks:**
- Concept extraction (LLM call)
- Existing concept file reads (I/O)
- Merge deduplication (text comparison)

**Optimization:**
- Cache TAGS.md in memory (read once per batch)
- Batch concept existence checks (single glob)
- Parallel processing (future, requires locking)

---

## Related Documentation

- [SKILL.md](SKILL.md) — Compile Agent overview
- [tagging-rules.md](tagging-rules.md) — detailed tag assignment logic
- [examples.md](examples.md) — sample transformations
- [reference.md](reference.md) — frontmatter schemas

