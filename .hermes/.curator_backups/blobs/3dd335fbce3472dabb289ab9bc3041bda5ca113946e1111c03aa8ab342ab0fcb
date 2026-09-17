# Adding a New Pool B Tag — 3-File Sync

When Julius approves a new tag for Pool B, these 3 files must be updated. Missing any one causes the format validator to reject the tag.

## Files to update (in order)

### 1. TAGS.md
- Add `| #<tag> | <description> |` to Pool B table
- Update `**Total:** N sub-tags` (increment)
- Update `**Version:**` and `**Last updated:**`
- Add changelog entry: `| YYYY-MM-DD | Approved: #<tag> → Pool B (Julius) | Connor |`

### 2. validate.py
Path: `.hermes/skills/format-validator/scripts/validate.py`
- Add `'<tag>'` to `POOL_B` set (lines 24-26)
- Update version comment: `v1.3` → `v1.4`

### 3. knowledge-base-validation/SKILL.md
Path: `.hermes/skills/research/knowledge-base-validation/SKILL.md`
- Update Pool B count in the "Pool B tags are defined in TAGS.md" paragraph (e.g., `19 tags as of 2026-06-19` → `20 tags as of 2026-08-06`)
- Add `<tag>` to the comma-separated list
- Update Criteria Quick Reference at bottom — same count + list

## Verification after sync

```bash
# Confirm TAGS.md has the tag
grep "#<tag>" ~/knowledge-base/TAGS.md

# Confirm validate.py has the tag
grep "'<tag>'" ~/knowledge-base/.hermes/skills/format-validator/scripts/validate.py

# Re-run format validator — should show 0 ERRORs for that tag
cd ~/knowledge-base && python3 .hermes/skills/format-validator/scripts/validate.py 2>&1 | head -8
```

## Example: Adding #strategy (2026-08-06)

1. TAGS.md: `| #strategy | Strategic thinking, decision frameworks, competitive positioning, game theory |`
2. validate.py POOL_B: added `'strategy'` to set
3. SKILL.md: `19 tags` → `20 tags`, added `strategy` to list

**Pitfall discovered:** TAGS.md was updated first but validator still flagged `strategy` as invalid. Root cause: validate.py POOL_B was still at v1.3 with 19 tags. Required troubleshooting with `grep -n POOL_B validate.py` to find the hardcoded set.
