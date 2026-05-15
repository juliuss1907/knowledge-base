# Folder Structure Whitelist — Knowledge Base V2

> Ground truth for allowed paths and folder hierarchy.
> Consumed by: Hermes Hygiene Inspector.
> Changes here directly affect hygiene validation.

**Version:** 1.0
**Last updated:** 2026-05-07

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
- Archives (`*-archive/`, `*-v1-backup/`) must be gitignored

---

## 3. Agent homes (depth 1)

### 3.1 `.openclaw/`

```
.openclaw/
├── IDENTITY.md   ✓ required
├── SOUL.md       ✓ required
├── MEMORY.md     ✓ required
├── HEARTBEAT.md  ✓ required
└── skills/       ✓ required
    ├── ingest-agent/
    ├── compile-agent/
    ├── index-agent/
    ├── fix-agent/
    └── */         ✓ allowed (additional skills)
```

**Rules:**
- Exactly 4 identity files at root
- `skills/` contains 4 core subfolders + additional skills allowed
- Runtime folders (`agents/`, `cron/`, `memory/`) allowed
- Runtime files (`.sqlite`, `.log`, `.tmp`) allowed

### 3.2 `.hermes/`

```
.hermes/
├── IDENTITY.md   ✓ required
├── SOUL.md       ✓ required
├── MEMORY.md     ✓ required
├── HEARTBEAT.md  ✓ required
└── skills/       ✓ required
    ├── output-validator/
    ├── format-validator/
    ├── hygiene-inspector/
    └── */         ✓ allowed (additional skills)
```

**Rules:**
- Exactly 4 identity files at root
- `skills/` contains 3 core subfolders + additional skills allowed
- Runtime folders (`sessions/`, `cron/`, `hermes-agent/`) allowed
- Runtime files (`.db`, `.log`, `.tmp`) allowed

---

## 4. Skills folders (depth 2)

Each skill folder must contain:

```
skills/<skill-name>/
├── SKILL.md       ✓ required (main skill file)
├── workflow.md    ✓ allowed (detailed workflow)
├── examples.md    ✓ allowed (sample inputs/outputs)
├── reference.md   ✓ allowed (specs, references)
└── *              ✗ forbidden (no other files)
```

**Rules:**
- `SKILL.md` is required
- Supporting files (`workflow.md`, `examples.md`, `reference.md`) are optional
- No subfolders
- No files with other names

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
├── meta/
│   ├── format-spec.md           ✓ required
│   ├── folder-structure.md      ✓ required (this file)
│   └── *                        ✗ forbidden
├── sources/
│   └── src_<slug>.md            ✓ allowed (many files)
├── concepts/
│   └── <concept-slug>.md        ✓ allowed (many files)
├── tag/
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
- `meta/` contains exactly 2 files (ground truth)
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
