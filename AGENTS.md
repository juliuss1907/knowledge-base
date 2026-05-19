# AGENTS.md — Knowledge Base V2

> Global rules for any agent operating on this Knowledge Base.
> This file is the entry point. Detailed instructions live in per-skill SKILL.md files.

**Version:** 2.0
**Last updated:** 2026-05-04

---

## 1. What this KB is

A dual-layer knowledge system for Julius:

- **`raw/`** — ingested source material (articles, posts, videos, papers, repos, websites)
- **`wiki/`** — compiled, structured, cross-linked knowledge (concepts + sources + indexes)

Knowledge lives in `wiki/` permanently. There is no "promote to permanent" step — personal vault has been moved to the separate `julius-workspace` repo.

---

## 2. Pipeline

```
NGUỒN ──► INGEST ──► COMPILE ──► INDEX ──► VALIDATION
         (OpenClaw)  (OpenClaw)  (OpenClaw)  (Hermes-VPS)
```

| Stage | Owner | Skill | Output |
|---|---|---|---|
| Ingest | OpenClaw | `knowledge-base/.openclaw/skills/ingest-agent/` | New file in `raw/<type>/` |
| Compile | OpenClaw | `knowledge-base/.openclaw/skills/compile-agent` | `wiki/sources/` + `wiki/concepts/` |
| Index | OpenClaw | `knowledge-base/.openclaw/skills/index-agent/` | `wiki/tag/` + `wiki/topic/` |
| Validation | Hermes-VPS | `knowledge-base/.hermes/skills/{output,format,hygiene}/` | `wiki/reviews/<type>-report.md` |
| Fix (post-validation) | OpenClaw | `knowledge-base/.openclaw/skills/fix-agent/` | Updated files based on approved reports |

---

## 3. Stack

| Tool | Role |
|---|---|
| Obsidian | Frontend for browsing KB (graph view, tag explorer) |
| OpenClaw | Automation runtime — owns 4 skills above |
| Hermes-VPS | 3 read-only validators (Output / Format / Hygiene) |

Hermes-local on Julius's main machine is a separate consumer (RAG search) and operates KB **read-only**.

---

## 4. Hard constraints

These rules apply to every agent. Skill-level SKILL.md may add more, but cannot override these.

### 4.1 Write zones (whitelist)

| Agent                       | May write to                                                           |
| --------------------------- | ---------------------------------------------------------------------- |
| OpenClaw Ingest             | `raw/<type>/` only + Stats/Items sections in `raw/<type>/<type>.md`    |
| OpenClaw Compile            | `wiki/sources/`, `wiki/concepts/`, `wiki/drafts/`                      |
| OpenClaw Index              | `wiki/tag/`, `wiki/topic/` + Stats/Items sections in `wiki/tag/tag.md` |
| OpenClaw Fix                | Files explicitly listed in approved Hermes report                      |
| Hermes (any role)           | `wiki/reviews/` only                                                   |
| Hermes-local (main machine) | Nothing — read-only                                                    |
|                             |                                                                        |

Anything not listed above is forbidden territory.

### 4.2 Read-only zones (no agent may modify)

- `AGENTS.md` (this file)
- `TAGS.md`
- `wiki/meta/format-spec.md`
- `wiki/meta/folder-structure.md`
- `wiki/meta/index-spec.md`
- `context/USER.md`
- `context/context.md`
- `raw/raw.md`
- `wiki/wiki.md`
- `.openclaw/IDENTITY.md`, `.openclaw/SOUL.md`
- `.hermes/IDENTITY.md`, `.hermes/SOUL.md`


Changes to these files are made by Julius only.

### 4.3 Append-only files

These files may be added to but never have entries removed or rewritten:

- `.openclaw/MEMORY.md`
- `.hermes/MEMORY.md`
- `TAGS.md` (tag taxonomy)

### 4.4 Forbidden actions

- ❌ No agent may create new top-level folders
- ❌ No agent may delete files in `raw/`
- ❌ No agent may move files between `wiki/concepts/` and `wiki/sources/`
- ❌ No agent may use nested tag syntax (`#ai/tools`) — flat tags only
- ❌ No agent may add tags not present in `TAGS.md` without going through proposal flow
- ❌ Hermes may never auto-fix issues — report only, OpenClaw fixes after Julius approves

---

## 5. Tag system

Defined in detail in `TAGS.md`. Summary:

- **Pool A — main-tags:** broad categories, exactly 1 per file (required)
- **Pool B — sub-tags:** cross-cutting attributes, 1–3 per file
- **topic:** free-form slug (not a tag), used for `wiki/topic/<topic>.md` index

New tags require Julius approval via the proposal channel before being added.

---

## 6. Where to look for details

When invoked for a specific task, an agent loads the relevant SKILL.md only. SKILL.md files use progressive disclosure: overview + navigation in SKILL.md, full details in supporting files within the same folder.

| Task type | Skill location |
|---|---|
| Ingest new source | `knowledge-base/.openclaw/skills/ingest-agent/SKILL.md` |
| Compile raw → wiki | `knowledge-base/.openclaw/skills/compile-agent/SKILL.md` |
| Maintain tag/topic indexes | `knowledge-base/.openclaw/skills/index-agent/SKILL.md` |
| Apply approved Hermes fixes | `knowledge-base/.openclaw/skills/fix-agent/SKILL.md` |
| Quality-check wiki content | `knowledge-base/.hermes/skills/output-validator/SKILL.md` |
| Format-check wiki files | `knowledge-base/.hermes/skills/format-validator/SKILL.md` |
| Folder-structure check | `knowledge-base/.hermes/skills/hygiene-inspector/SKILL.md` |

Ground-truth references used by skills:

- `wiki/meta/format-spec.md` — file format rules (frontmatter, sections, naming)
- `wiki/meta/folder-structure.md` — allowed paths whitelist
- `TAGS.md` — tag taxonomy

---

## 7. Escalation to Julius

Any agent must escalate (via the agreed channel — Telegram / report file) when:

- A new tag is needed that isn't in `TAGS.md`
- A Hermes finding requires destructive action (delete / move outside whitelist)
- Source type cannot be classified into existing `raw/` subfolders
- Format/hygiene rules conflict with a real-world case not covered by spec

Default behavior on ambiguity: **stop and ask**, do not guess.
