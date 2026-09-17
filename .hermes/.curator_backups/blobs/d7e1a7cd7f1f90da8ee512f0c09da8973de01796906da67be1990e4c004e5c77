# Index Agent Frontmatter Regression — Fixed 2026-07-01

## Symptom

Format Validator reports 311 broken wikilinks every run. Root cause: topic files in `wiki/topic/*.md` missing YAML frontmatter, so Obsidian can't resolve wikilinks.

## Root Cause

Index Agent (`gemma-4-31b`, runs daily 21:00 via OpenClaw pipeline) regenerates all topic index files. **5 Python scripts** all wrote topic files starting with bare `# Topic: <slug>` — no `---` YAML frontmatter block.

Tag files (`wiki/tag/*.md`) had frontmatter in 4/5 scripts (only `build_index.py` was missing it). Topic files had frontmatter in **0/5 scripts**.

## Affected Scripts

All in `.openclaw/skills/index-agent/`:

| Script | Tag frontmatter | Topic frontmatter | Fixed |
|--------|:-:|:-:|:-:|
| `build_index.py` | ❌ | ❌ | ✅ |
| `index_run.py` | ✅ | ❌ | ✅ |
| `run_index.py` | ✅ | ❌ | ✅ |
| `indexer.py` | ✅ | ❌ | ✅ |
| `index_helper.py` | ✅ | ❌ | ✅ |
| `SKILL.md` (template) | ❌ | ❌ | ✅ |
| `workflow.md` (pseudocode) | ✅ | ❌ | ✅ |

## Correct Frontmatter Format

### Topic files (`wiki/topic/<slug>.md`)

```yaml
---
type: index
scope: topic
parent: "[[topic]]"
topic: <slug>
auto_generated: true
last_updated: YYYY-MM-DD
---
```

### Tag files (`wiki/tag/<tag>.md`)

```yaml
---
type: index
level: 3
scope: tag
parent: "[[tag]]"
tag: <tag>
auto_generated: true
last_updated: YYYY-MM-DD
---
```

## Verification

```bash
cd /home/julius/knowledge-base/.openclaw/skills/index-agent
for f in build_index.py index_run.py run_index.py indexer.py index_helper.py; do
  grep -c "scope: topic" "$f"
done
# Expected: 1 for each script
```

## Regression #2: Parent field quoting (Fixed 2026-07-05)

### Symptom

Format Validator 2026-07-04: 24 WARNING — `wiki/tag/*.md` files had `parent: [[tag]]` (unquoted) instead of `parent: "[[tag]]"` (quoted). These were resolved on 07-03, then **reappeared** on 07-04 — Index Agent regenerated with old unquoted format.

### Root Cause

The 06-30 frontmatter fix added the `parent` field to all tag index templates, but 5/7 files used **unquoted** format. Only `build_index.py` and `SKILL.md` had the correct `parent: "[[tag]]"` (quoted). When any of the wrong scripts ran, they wrote unquoted format → Format Validator flagged them → Index Agent ran again with a different script → format seemed "resolved" → then a wrong script ran again and regressed.

### Affected (2026-07-05 fix)

| File | Was | Fixed to |
|------|-----|----------|
| `indexer.py:163` | `parent: [[tag]]` | `parent: "[[tag]]"` |
| `index_helper.py:206` | `parent: [[tag]]` | `parent: "[[tag]]"` |
| `index_run.py:183` | `parent: [[tag]]` (in f-string) | `parent: \"[[tag]]\"` |
| `run_index.py:210` | `parent: [[tag]]` | `parent: "[[tag]]"` |
| `workflow.md:343` | `parent: [[tag]]` | `parent: "[[tag]]"` |
| `build_index.py:214` | Already correct | — |
| `SKILL.md:72` | Already correct | — |

### Disk fix

23 tag files on disk also fixed: `sed -i 's/^parent: \[\[tag\]\]$/parent: "[[tag]]"/' wiki/tag/*.md`

### Verification pitfall: grep `[[` regex

`grep 'parent: "[[tag]]"'` without `-F` flag returns 0 matches because `[[` is interpreted as a regex character class. **Always use `grep -F` (fixed strings) or escape with `\[\[`** when searching for wikilinks.

## Lesson

When tracing systemic format errors, check ALL agent configs in the pipeline, not just Compile/Ingest Agent. Index Agent runs **after** Compile Agent and can regress previously-fixed files by regenerating them from scratch. Multiple duplicate script implementations (5 copies of the same logic) mean the fix must be applied in ALL copies — and every field in those copies must match exactly, not just be "present."
