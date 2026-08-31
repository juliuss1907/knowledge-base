# Cross-Spec Conflicts — Format Validator

> Known conflicts between `format-spec.md` and `index-spec.md` that require escalation.

## 1. Unquoted wikilinks in index frontmatter (resolved 2026-08-31)

**Discovered:** 2026-06-17
**Resolved:** 2026-08-31 — All 24 tag files regenerated with quoted `parent: "[[tag]]"` (Index Agent 22:04 run). No longer produces WARNINGs. Escalation closed.

**History:** 08-28 through 08-30 saw 24 unquoted-parent WARNINGs per day after Index Agent regenerated tag files. Between 08-30 23:15 and 08-31 22:04 the tag files were re-quoted to `parent: "[[tag]]"`, matching format-spec.md §9. Resolution: 24 WARNINGs → 0. If Index Agent regenerates unquoted parent again, escalate as a recurrence.

**Spec A (format-spec.md §9):** "Wikilinks in frontmatter fields (original, sources) use quoted format `"...[[...]]..."` for Obsidian compatibility."

**Spec B (index-spec.md §4.2, §5.2):** Shows `parent: [[<tầng-1-slug>]]` — unquoted, bare wikilink.

**YAML behavior:** Unquoted `[[tag]]` is parsed by `yaml.safe_load` as nested list `[['tag']]`, not string `'[[tag]]'`.

**Files affected:** All `wiki/tag/*.md` files (20+). Also `wiki/tag/tag.md`.

**Validator handling:**
- Detect both `isinstance(val, str)` (quoted) and `isinstance(val, list)` (unquoted, YAML-parsed)
- Report as WARNING (not ERROR) — file works in Obsidian, just ambiguous YAML
- Escalate as `[SPEC CONFLICT]` in report

**Resolution recommendation:**
1. Update `index-spec.md` to show quoted format: `parent: "[[<tầng-1-slug>]]"`
2. Update Index Agent to write quoted format
3. Fix Agent can quote all 20 tag files' parent fields istrivially

## 2. tag.md level mismatch (active)

**Discovered:** 2026-06-17

**Spec:** `index-spec.md` §4.1 lists `wiki/tag/tag.md` as Tầng 2 (level 2) with scope `tags` and parent `[[wiki]]`.

**Reality:** `wiki/tag/tag.md` has `level: 1` and `scope: tag`.

**Validator handling:**
- Report as ERROR: level=1 requires scope raw/wiki/context
- Escalate as `[FORMAT UNCERTAINTY]`
- Julius decides: keep as level 1 or fix to level 2 per spec

## 3. Topic files: type=index but no level (resolved)

**Discovered:** 2026-06-18
**Resolved:** 2026-06-18

**Issue:** `wiki/topic/*.md` files have `type: index, scope: topic` but NO `level` field. When dispatched to `validate_index()`, all 108 topic files generated false ERRORs for "missing level field."

**Spec:** `index-spec.md` §5.1 explicitly excludes topic files: "Topic files have their own format (defined in Index Agent skill), separate from this spec."

**Resolution:** Detect topic files by `scope: topic` OR path prefix `wiki/topic/`. Route to light topic validation (check `topic` matches filename, `auto_generated: true`, valid date, H1 present). Do NOT validate as indexes.

**Validator fix applied:** 2026-06-18 — added dispatch check before `type: index` routing. See `references/topic-file-dispatch.md` for implementation.

## Resolution log

| Date | Conflict | Resolution |
|---|---|---|
| 2026-06-18 | Topic file dispatch | Fixed — detect by scope:topic, route to validate_topic |
| 2026-06-17 | Unquoted wikilinks | RESOLVED 2026-08-31 — tag files re-quoted to `parent: "[[tag]]"`; escalation closed |
| 2026-06-17 | tag.md level | Pending Julius review |
