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

## Lesson

When tracing systemic format errors, check ALL agent configs in the pipeline, not just Compile/Ingest Agent. Index Agent runs **after** Compile Agent and can regress previously-fixed files by regenerating them from scratch. Multiple duplicate script implementations (5 copies of the same logic) mean the fix must be applied in ALL copies.
