# Folder Structure Whitelist — Knowledge Base V2

> Ground truth for allowed paths and folder hierarchy.
> Consumed by: Hermes Hygiene Inspector.
> Changes here directly affect hygiene validation.

**Version:** 1.2
**Last updated:** 2026-05-17
---

## 1. Purpose

This file defines:
- Which folders and files are allowed at each level
- Naming conventions for folders and files
- Forbidden patterns that indicate structural issues

Hygiene Inspector uses this as the single source of truth. Any path not explicitly allowed here is flagged.

---

## 2. Root level (depth 0)

```
knowledge-base/
├── AGENTS.md          ✓ required
├── TAGS.md            ✓ required
├── README.md          ✓ required
├── knowledge-base.md  ✓ required
├── HEARTBEAT.md       ✓ allowed (symlink to .openclaw/HEARTBEAT.md)
├── IDENTITY.md        ✓ allowed (symlink to .openclaw/IDENTITY.md)
├── SOUL.md            ✓ allowed (symlink to .openclaw/SOUL.md)
├── TOOLS.md           ✓ allowed (symlink to .openclaw/TOOLS.md)
├── USER.md            ✓ allowed (symlink to .openclaw/USER.md)
├── .gitignore         ✓ required
├── .git/              ✓ required (git internals)
├── .obsidian/         ✓ allowed (Obsidian config)
├── .openclaw/         ✓ required (OpenClaw agent home)
├── .hermes/           ✓ required (Hermes agent home)
├── context/           ✓ required
├── raw/               ✓ required
├── wiki/              ✓ required
├── scripts/           ✓ allowed (utility scripts)
└── *                  ✗ forbidden (no other files/folders)

**Rules:**
- No loose `.md` files except the 4 required ones + 5 allowed symlinks
- Symlinks to agent identity files allowed at root (for convenience)
- No folders starting with uppercase (except `.git`, `.obsidian`)
- Archives (`*-archive/`, `*-v1-backup/`) must be gitignored

---

## 3. Agent homes (depth 1)

### 3.1. `.openclaw/` — OpenClaw Agent Home

This is OpenClaw's runtime workspace. The agent owns this folder entirely.

**Required core files:**
- `IDENTITY.md`
- `SOUL.md`
- `MEMORY.md`
- `HEARTBEAT.md`
- `skills/` (folder containing skill definitions)

**Runtime folders/files:**
Any files and folders created by the OpenClaw runtime are allowed inside `.openclaw/`. The Hygiene Inspector only flags content that clearly does not belong (e.g., user content files like articles or notes mistakenly placed here).

**Forbidden in this folder:**
- User-generated content (articles, notes, sources)
- Files belonging to `wiki/`, `raw/`, or `context/` layers

### 3.2. `.hermes/` — Hermes Agent Home

This is Hermes's runtime workspace. The agent owns this folder entirely.

**Required core files:**
- `IDENTITY.md`
- `SOUL.md`
- `MEMORY.md`
- `HEARTBEAT.md`
- `skills/` (folder containing skill definitions)

**Runtime folders/files:**
Any files and folders created by the Hermes runtime are allowed inside `.hermes/`. The Hygiene Inspector only flags content that clearly does not belong.

**Forbidden in this folder:**
- User-generated content
- Files belonging to `wiki/`, `raw/`, or `context/` layers
---

## 4. Skills folders (depth 2)

Each skill folder must contain:

```
skills/<skill-name>/
├── SKILL.md                ✓ required (main skill file)
├── workflow.md             ✓ allowed (detailed workflow)
├── examples.md             ✓ allowed (sample inputs/outputs)
├── reference.md            ✓ allowed (specs, references)
├── validation-criteria.md  ✓ allowed (validation rules)
└── *.md                    ✓ allowed (additional documentation)
```

**Rules:**
- `SKILL.md` is required
- Supporting markdown files allowed (no limit on names)
- No subfolders
- No non-markdown files (except `.gitkeep`)

---

## 5. Context folder

```
context/
├── context.md  ✓ required (index)
├── USER.md     ✓ required (Julius profile)
└── *           ✗ forbidden
```

**Rules:**
- Exactly 2 files
- No subfolders

---

## 6. Raw layer

```
raw/
├── raw.md                          ✓ required (level 1 index)
├── articles/
│   ├── articles.md              ✓ required (index)
│   └── YYYY-MM-DD_<slug>.md     ✓ allowed (content files)
├── posts/
│   ├── posts.md                 ✓ required
│   └── YYYY-MM-DD_<slug>.md     ✓ allowed
├── websites/
│   ├── websites.md              ✓ required
│   └── YYYY-MM-DD_<slug>.md     ✓ allowed
├── videos/
│   ├── videos.md                ✓ required
│   └── YYYY-MM-DD_<slug>.md     ✓ allowed
├── papers/
│   ├── papers.md                ✓ required
│   └── YYYY-MM-DD_<author>_<title>.md  ✓ allowed
├── repos/
│   ├── repos.md                 ✓ required
│   └── YYYY-MM-DD_<owner>_<repo>.md    ✓ allowed
└── *                            ✗ forbidden (no other subfolders)
```

**Rules:**
- Exactly 6 subfolders (content types)
- Each subfolder has 1 index file (`<type>.md`)
- Content files follow naming convention: `YYYY-MM-DD_<slug>.md`
- No files at `raw/` root level
- No subfolders inside content type folders

---

## 7. Wiki layer

```
wiki/
├── wiki.md                               ✓ required (level 1 index)
├── meta/
│   ├── format-spec.md           ✓ required
│   ├── folder-structure.md      ✓ required (this file)
│   └── *                        ✗ forbidden
├── sources/
│   └── src_<slug>.md            ✓ allowed (many files)
├── concepts/
│   └── <concept-slug>.md        ✓ allowed (many files)
├── tag/
│ ├── tag.md                        ✓ required (level 2 index)
│   └── <tag>.md                 ✓ allowed (auto-generated)
├── topic/
│   └── <topic>.md               ✓ allowed (auto-generated)
├── drafts/
│   └── <slug>.md                ✓ allowed (rejected files)
└── reviews/
    ├── _action-required.md      ✓ required
    ├── YYYY-MM-DD_output-report.md     ✓ allowed
    ├── YYYY-MM-DD_format-report.md     ✓ allowed
    ├── YYYY-MM-DD_hygiene-report.md    ✓ allowed
    └── archive/
        └── YYYY-MM/             ✓ allowed (archived reports)
```

**Rules:**
- `meta/` contains exactly 3 files: `format-spec.md`, `folder-structure.md`, `index-spec.md`
- `sources/` files must start with `src_`
- `concepts/` files use lowercase-hyphen slugs
- `tag/` and `topic/` files auto-generated by Index Agent
- `drafts/` contains files awaiting Julius review
- `reviews/` contains Hermes outputs only
- No files at `wiki/` root level

---

## 8. Naming conventions

### 8.1 File names

| Pattern | Where | Example |
|---|---|---|
| `YYYY-MM-DD_<slug>.md` | `raw/` content | `2026-05-07_anthropic-claude-code.md` |
| `src_<slug>.md` | `wiki/sources/` | `src_anthropic-claude-code.md` |
| `<concept-slug>.md` | `wiki/concepts/` | `claude-code-workflow.md` |
| `<tag>.md` | `wiki/tag/` | `ai.md`, `tools.md` |
| `<topic>.md` | `wiki/topic/` | `claude-code-intro.md` |
| `YYYY-MM-DD_<type>-report.md` | `wiki/reviews/` | `2026-05-07_format-report.md` |

**Slug rules:**
- Lowercase only
- Hyphens for word separation (no underscores or spaces)
- Vietnamese diacritics allowed
- Max 80 characters
- No special characters except hyphens

### 8.2 Folder names

- Lowercase only
- Hyphens for multi-word names
- No spaces, underscores, or special characters
- Agent homes start with `.` (`.openclaw`, `.hermes`)

---

## 9. Forbidden patterns

Hygiene Inspector flags these as errors:

| Pattern | Reason |
|---|---|
| Files at `wiki/` root | Content must be in subfolders |
| Files at `raw/` root | Content must be in type subfolders |
| Uppercase folder names | Violates naming convention |
| Nested folders in `raw/<type>/` | Raw content is flat |
| Files in `wiki/tag/` not matching tag list | Orphaned index files |
| Folders not in whitelist | Structural drift |
| `.DS_Store`, `Thumbs.db` | OS artifacts (should be gitignored) |

---

## 10. Hygiene validation workflow

When Hygiene Inspector runs:

1. Scan entire KB folder structure
2. For each path:
   - Check if allowed by this whitelist
   - Verify naming convention
   - Check for forbidden patterns
3. Generate report: `wiki/reviews/YYYY-MM-DD_hygiene-report.md`
4. Append summary to `wiki/reviews/_action-required.md`

Hygiene Inspector never modifies structure — only reports issues.

---

## 11. Structure evolution

This whitelist is versioned. When structure changes:

1. Bump version number in header
2. Add entry to change log below
3. Update Hygiene Inspector skill to handle transition
4. Announce to Julius via report

### Change log

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-05-07 | Initial structure whitelist for V2 |
| 1.1 | 2026-05-17 | Added index files to whitelist: raw.md, wiki.md, wiki/tag/tag.md. Added runtime artifacts for .openclaw/ and .hermes/. |
| 1.2 | 2026-05-17 | - Simplified `.openclaw/` and `.hermes/` whitelist to use catch-all clause for runtime folders (avoids maintenance burden when agents update)
- Updated `meta/` count from 2 to 3 (added `index-spec.md`)
- Migrated `memory/` from root to `.openclaw/memory/` (OpenClaw-owned)
- Fixed version header (was 1.0, now 1.2) |

---

## 12. Quick reference

**Allowed top-level folders:**
`.git`, `.obsidian`, `.openclaw`, `.hermes`, `context`, `raw`, `wiki`, `scripts`

**Allowed `raw/` subfolders:**
`articles`, `posts`, `websites`, `videos`, `papers`, `repos`

**Allowed `wiki/` subfolders:**
`meta`, `sources`, `concepts`, `tag`, `topic`, `drafts`, `reviews`

**Agent skill folders:**
`.openclaw/skills/{ingest-agent, compile-agent, index-agent, fix-agent}`
`.hermes/skills/{output-validator, format-validator, hygiene-inspector}`
