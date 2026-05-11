# Ingest Agent — Frontmatter Field Reference

Complete definitions for all frontmatter fields used in raw/ files.

---

## Required Fields

These fields must be present in every raw file. Ingestion fails if any are missing.

### `type`

**Type:** String (enum)

**Required:** Yes

**Valid values:** `article`, `post`, `video`, `paper`, `repo`, `website`

**Description:** Content type determines which folder the file goes into and how it's processed during compilation.

**Examples:**
```yaml
type: article
type: post
type: video
```

**Validation:**
- Must be exactly one of the 6 allowed values
- Case-sensitive (lowercase only)
- No plurals (use `article` not `articles`)

**Error handling:**
- If invalid value → ask Julius which type to use
- If ambiguous → default to `website` and flag for review

---

### `title`

**Type:** String

**Required:** Yes

**Max length:** 200 characters (recommended: under 100)

**Description:** Original title of the content. Used to generate slug and display in wiki.

**Examples:**
```yaml
title: The SKILL.md Pattern: How to Write AI Agent Skills That Actually Work
title: Anthropic announces Extended Thinking for Claude
title: Intro to Large Language Models
```

**Extraction sources:**
- HTML `<title>` tag
- `<h1>` heading
- `<meta property="og:title">` tag
- First line of content if no title found

**Validation:**
- Must be non-empty string
- Strip leading/trailing whitespace
- Remove newlines (replace with space)
- Escape special YAML characters: `:`, `#`, `|`, `>`

**Fallback:**
- If missing → use first 50 characters of content
- If still empty → use `Untitled-YYYY-MM-DD`

---

### `date_ingested`

**Type:** Date (YYYY-MM-DD format)

**Required:** Yes

**Description:** Date when content was added to the KB. Always set to today's date.

**Examples:**
```yaml
date_ingested: 2026-05-07
date_ingested: 2026-12-31
```

**Generation:**
```bash
date +%Y-%m-%d
```

**Validation:**
- Must be valid date in ISO 8601 format (YYYY-MM-DD)
- Cannot be in the future
- Must have leading zeros (e.g., `2026-05-07` not `2026-5-7`)

**Error handling:**
- If invalid format → reject and ask Julius
- If future date → use today's date and warn

---

### `status`

**Type:** String (enum)

**Required:** Yes

**Valid values:** `unprocessed`, `processed`, `archived`

**Description:** Processing status. Always set to `unprocessed` when ingesting. Compile Agent changes to `processed` after compilation.

**Examples:**
```yaml
status: unprocessed
```

**Lifecycle:**
1. Ingest Agent creates file → `status: unprocessed`
2. Compile Agent processes → `status: processed`
3. Manual archive (rare) → `status: archived`

**Validation:**
- Must be exactly `unprocessed` when ingesting
- Case-sensitive (lowercase only)

**Error handling:**
- If set to anything else → override to `unprocessed` and warn

---

## Optional but Recommended Fields

These fields should be included when available. Missing values use fallbacks.

### `url`

**Type:** String (URL)

**Required:** No (but strongly recommended)

**Description:** Original source URL. Used for attribution and re-fetching if needed.

**Examples:**
```yaml
url: https://bibek-poudel.medium.com/the-skill-md-pattern-72a3169dd7ee
url: https://x.com/AnthropicAI/status/1234567890
url: https://www.youtube.com/watch?v=zjkBMFhNj_g
```

**Validation:**
- Must be valid HTTP/HTTPS URL
- Strip tracking parameters if possible (e.g., `?utm_source=...`)
- Preserve fragment identifiers (e.g., `#section`)

**Fallback:**
- If missing → omit field entirely (don't use placeholder)

**Special cases:**
- For threads: use URL of first tweet
- For repos: use main repo URL (not specific file)
- For papers: prefer DOI URL over PDF URL

---

### `author`

**Type:** String

**Required:** No

**Description:** Content creator. Can be person name, username, or organization.

**Examples:**
```yaml
author: Bibek Poudel
author: @AnthropicAI
author: Andrej Karpathy
author: Ashish Vaswani, Noam Shazeer, Niki Parmar, et al.
```

**Extraction sources:**
- `<meta name="author">` tag
- Byline in article
- @username for social posts
- Author list for papers
- Organization name for repos

**Validation:**
- Strip leading/trailing whitespace
- Preserve @mentions as-is for social posts
- For multiple authors: comma-separated list or "et al." if >5

**Fallback:**
- If missing → use `[unknown]`
- If organization → use org name (e.g., `Anthropic`, `OpenAI`)

---

### `date_published`

**Type:** Date (YYYY-MM-DD format)

**Required:** No

**Description:** Original publication date. Used for chronological sorting and filename.

**Examples:**
```yaml
date_published: 2026-02-26
date_published: 2023-11-22
date_published: 2017-06-12
```

**Extraction sources:**
- `<meta property="article:published_time">` tag
- Date in URL path (e.g., `/2026/05/07/title`)
- Timestamp in social post
- Publication date for papers

**Parsing:**
- Try ISO 8601 first: `YYYY-MM-DD`
- Parse common formats:
  - `May 7, 2026` → `2026-05-07`
  - `07/05/2026` → `2026-05-07` (assume MM/DD/YYYY for US sources)
  - `2026-05-07T10:30:00Z` → `2026-05-07` (strip time)

**Validation:**
- Must be valid date
- Can be in the past (even years ago)
- Cannot be in the future (if so, use `date_ingested`)

**Fallback:**
- If missing or unparseable → use `date_ingested`

**Usage:**
- Filename uses `date_published` if available, else `date_ingested`
- Chronological sorting prefers `date_published`

---

### `source`

**Type:** String

**Required:** No

**Description:** Platform or domain name. Used for grouping and attribution.

**Examples:**
```yaml
source: medium.com
source: x.com
source: youtube.com
source: arxiv.org
source: github.com
```

**Extraction:**
- Extract domain from URL: `https://example.com/path` → `example.com`
- Strip `www.` prefix
- Keep subdomain if meaningful (e.g., `blog.anthropic.com`)

**Validation:**
- Lowercase only
- No protocol (no `https://`)
- No path (no `/page`)

**Fallback:**
- If missing → extract from `url` field
- If `url` also missing → use `[unknown]`

**Special cases:**
- Twitter/X: always use `x.com` (not `twitter.com`)
- YouTube: use `youtube.com` (not `youtu.be`)
- GitHub: use `github.com` (not `raw.githubusercontent.com`)

---

## Optional Fields (Edge Cases)

These fields are used only in specific situations.

### `language`

**Type:** String (ISO 639-1 code)

**Required:** No

**Description:** Content language if not English or Vietnamese. Used to flag for translation.

**Examples:**
```yaml
language: zh
language: ja
language: es
language: fr
```

**When to use:**
- Content is primarily in a language other than English or Vietnamese
- Omit if content is English or Vietnamese (default assumption)

**Valid values:**
- ISO 639-1 two-letter codes: `zh`, `ja`, `es`, `fr`, `de`, `ko`, etc.
- Use lowercase

**Validation:**
- Must be valid ISO 639-1 code
- If invalid → omit field and warn

**Compile Agent behavior:**
- If `language` present → attempt translation or flag for manual review
- If omitted → assume English/Vietnamese, no translation needed

---

### `duration`

**Type:** String (HH:MM:SS or MM:SS format)

**Required:** No (videos only)

**Description:** Video length. Used for time estimates.

**Examples:**
```yaml
duration: 1:00:15
duration: 45:30
duration: 3:22
```

**When to use:**
- Only for `type: video`
- Omit for other content types

**Extraction:**
- From video metadata API
- From page HTML (e.g., `<meta property="video:duration">`)

**Validation:**
- Format: `HH:MM:SS` or `MM:SS`
- Must be valid time (e.g., not `90:00` for minutes)

**Fallback:**
- If missing → omit field (not critical)

---

### `doi`

**Type:** String

**Required:** No (papers only)

**Description:** Digital Object Identifier for academic papers.

**Examples:**
```yaml
doi: 10.48550/arXiv.1706.03762
doi: 10.1145/3290605.3300233
```

**When to use:**
- Only for `type: paper`
- Omit for other content types

**Extraction:**
- From paper metadata
- From URL (e.g., `https://doi.org/10.1234/example`)

**Validation:**
- Format: `10.XXXX/...`
- Must start with `10.`

**Fallback:**
- If missing → omit field (not critical)

---

### `arxiv_id`

**Type:** String

**Required:** No (papers only)

**Description:** arXiv identifier for preprints.

**Examples:**
```yaml
arxiv_id: 1706.03762
arxiv_id: 2001.08361
```

**When to use:**
- Only for `type: paper` from arXiv
- Omit for published papers or other content types

**Extraction:**
- From arXiv URL: `https://arxiv.org/abs/1706.03762` → `1706.03762`

**Validation:**
- Format: `YYMM.NNNNN` or `YYMM.NNNNNN`
- Must be numeric with optional dot

**Fallback:**
- If missing → omit field

---

### `stars`

**Type:** Integer

**Required:** No (repos only)

**Description:** GitHub star count. Used for popularity ranking.

**Examples:**
```yaml
stars: 1234
stars: 50000
```

**When to use:**
- Only for `type: repo`
- Omit for other content types

**Extraction:**
- From GitHub API: `/repos/{owner}/{repo}`
- From page HTML (e.g., star count badge)

**Validation:**
- Must be non-negative integer
- No commas or formatting (use `1234` not `1,234`)

**Fallback:**
- If missing → omit field

**Note:** Star count is snapshot at ingestion time, not live.

---

### `license`

**Type:** String

**Required:** No (repos only)

**Description:** Repository license (e.g., MIT, Apache-2.0, GPL-3.0).

**Examples:**
```yaml
license: MIT
license: Apache-2.0
license: GPL-3.0
```

**When to use:**
- Only for `type: repo`
- Omit for other content types

**Extraction:**
- From GitHub API: `license.spdx_id`
- From LICENSE file in repo

**Validation:**
- Use SPDX identifier if possible
- Common values: `MIT`, `Apache-2.0`, `GPL-3.0`, `BSD-3-Clause`, `Unlicense`

**Fallback:**
- If missing → omit field

---

## Field Order

Always use this order in frontmatter for consistency:

```yaml
---
type: <value>
title: <value>
url: <value>
author: <value>
date_published: <value>
date_ingested: <value>
status: <value>
source: <value>
# Optional fields below (if present)
language: <value>
duration: <value>
doi: <value>
arxiv_id: <value>
stars: <value>
license: <value>
---
```

**Rationale:**
- Required fields first
- Optional but common fields next
- Edge case fields last
- Alphabetical within each group

---

## Validation Rules Summary

Before writing any raw file, verify:

| Check | Rule |
|---|---|
| Required fields | `type`, `title`, `date_ingested`, `status` present |
| Type value | One of 6 allowed types |
| Status value | Exactly `unprocessed` |
| Date format | All dates are `YYYY-MM-DD` |
| Date validity | No future dates, valid calendar dates |
| URL format | Valid HTTP/HTTPS if present |
| Author fallback | Use `[unknown]` if missing |
| Source extraction | Extract from URL if not provided |
| Field order | Matches standard order above |
| YAML syntax | Valid YAML (no unescaped colons in values) |

---

## Common Mistakes

### Mistake 1: Wrong type value

```yaml
# ❌ Wrong
type: articles

# ✅ Correct
type: article
```

### Mistake 2: Future date

```yaml
# ❌ Wrong (if today is 2026-05-07)
date_ingested: 2026-05-08

# ✅ Correct
date_ingested: 2026-05-07
```

### Mistake 3: Wrong status

```yaml
# ❌ Wrong
status: pending

# ✅ Correct
status: unprocessed
```

### Mistake 4: Unescaped colon in title

```yaml
# ❌ Wrong (YAML parse error)
title: AI: The Future of Computing

# ✅ Correct
title: "AI: The Future of Computing"
```

### Mistake 5: Wrong date format

```yaml
# ❌ Wrong
date_published: 05/07/2026

# ✅ Correct
date_published: 2026-05-07
```

### Mistake 6: Including protocol in source

```yaml
# ❌ Wrong
source: https://medium.com

# ✅ Correct
source: medium.com
```

---

## YAML Escaping Rules

Certain characters require escaping or quoting in YAML:

| Character | Rule | Example |
|---|---|---|
| `:` (colon) | Quote if in value | `title: "AI: The Future"` |
| `#` (hash) | Quote if at start | `title: "#1 Trending Topic"` |
| `\|` (pipe) | Quote if in value | `title: "A \| B Comparison"` |
| `>` (greater) | Quote if in value | `title: "A > B"` |
| `[` `]` (brackets) | Quote if in value | `title: "[Draft] Article"` |
| `{` `}` (braces) | Quote if in value | `title: "{Urgent} Update"` |

**Safe approach:** When in doubt, quote the entire value:

```yaml
title: "Any title with: special, characters!"
```

---

## Field Usage by Content Type

Not all fields are relevant for all content types:

| Field | article | post | video | paper | repo | website |
|---|---|---|---|---|---|---|
| `type` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `title` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `url` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `author` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `date_published` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `date_ingested` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `status` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `source` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `language` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `duration` | — | — | ✓ | — | — | — |
| `doi` | — | — | — | ✓ | — | — |
| `arxiv_id` | — | — | — | ✓ | — | — |
| `stars` | — | — | — | — | ✓ | — |
| `license` | — | — | — | — | ✓ | — |

**Legend:**
- ✓ = Recommended to include if available
- — = Not applicable for this content type

---

## Frontmatter Templates

Copy-paste templates for each content type:

### Article template

```yaml
---
type: article
title: 
url: 
author: 
date_published: 
date_ingested: 
status: unprocessed
source: 
---
```

### Post template

```yaml
---
type: post
title: 
url: 
author: 
date_published: 
date_ingested: 
status: unprocessed
source: 
---
```

### Video template

```yaml
---
type: video
title: 
url: 
author: 
date_published: 
date_ingested: 
status: unprocessed
source: 
duration: 
---
```

### Paper template

```yaml
---
type: paper
title: 
url: 
author: 
date_published: 
date_ingested: 
status: unprocessed
source: 
doi: 
arxiv_id: 
---
```

### Repo template

```yaml
---
type: repo
title: 
url: 
author: 
date_published: 
date_ingested: 
status: unprocessed
source: 
stars: 
license: 
---
```

### Website template

```yaml
---
type: website
title: 
url: 
author: 
date_published: 
date_ingested: 
status: unprocessed
source: 
---
```

---

## Related Documentation

- [SKILL.md](SKILL.md) — Ingest Agent overview
- [workflow.md](workflow.md) — Step-by-step ingestion process
- [examples.md](examples.md) — Sample raw files for each type
- `wiki/meta/format-spec.md` — Format rules for compiled wiki files (different schema)
