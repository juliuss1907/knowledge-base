# Hygiene Inspector — Examples

Sample hygiene validation reports and common folder structure issues with fixes.

---

## Overview

This document provides real-world examples of Hygiene Inspector reports and demonstrates how to fix common folder structure issues. Hygiene Inspector checks **folder structure only** (paths, naming, orphans), not file content.

---

## Example 1: Complete Validation Report

### Sample report structure

```markdown
# Hygiene Inspection — 2026-05-09

**Status:** pending
**Issues found:** 10 (4 ERROR, 4 WARNING, 2 INFO)
**Created:** 2026-05-09 23:00:15
**Validator:** hygiene-inspector

**Paths checked:** 342

---

## Issue 1: Path not in root whitelist

**Path:** NOTES.md
**Severity:** ERROR
**Category:** Path
**Issue:** Path not in root whitelist
**Current:** NOTES.md
**Expected:** Only allowed: AGENTS.md, TAGS.md, README.md, knowledge-base.md, .openclaw/, .hermes/, context/, raw/, wiki/
**Suggested fix:** Remove path or add to folder-structure.md whitelist

---

## Issue 2: Subfolder not allowed

**Path:** wiki/archive/
**Severity:** ERROR
**Category:** Path
**Issue:** Subfolder not allowed in wiki/
**Current:** archive
**Expected:** Only allowed: meta, sources, concepts, tag, topic, reviews, drafts
**Suggested fix:** Remove wiki/archive/ or add to folder-structure.md

---

## Issue 3: Folder name does not follow format

**Path:** wiki/Tag_Index/
**Severity:** WARNING
**Category:** Naming
**Issue:** Folder name does not follow lowercase-hyphen format
**Current:** Tag_Index
**Expected:** lowercase-hyphen-format
**Suggested fix:** Rename to lowercase with hyphens only

---

## Issue 4: Source file missing src_ prefix

**Path:** wiki/sources/anthropic-claude.md
**Severity:** ERROR
**Category:** Naming
**Issue:** Source file missing src_ prefix
**Current:** anthropic-claude.md
**Expected:** src_<slug>.md
**Suggested fix:** Rename to src_anthropic-claude.md

---

## Issue 5: Source file in wrong location

**Path:** wiki/concepts/src_rag-intro.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** Source file in wrong location
**Current:** wiki/concepts/src_rag-intro.md
**Expected:** wiki/sources/src_<slug>.md
**Suggested fix:** Move to wiki/sources/src_rag-intro.md

---

## Issue 6: Path contains spaces

**Path:** wiki/concepts/RAG System.md
**Severity:** ERROR
**Category:** Naming
**Issue:** Path contains spaces
**Current:** wiki/concepts/RAG System.md
**Expected:** Use hyphens instead of spaces
**Suggested fix:** Rename path to remove spaces

---

## Issue 7: Temporary file detected

**Path:** wiki/concepts/embedding.md.bak
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary file detected
**Current:** wiki/concepts/embedding.md.bak
**Expected:** Temporary files should be cleaned up
**Suggested fix:** Delete temporary file

---

## Issue 8: Empty folder detected

**Path:** wiki/experiments/
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty folder detected
**Current:** Folder contains no files
**Expected:** Folders should contain files or be removed
**Suggested fix:** Remove empty folder or add files

---

## Issue 9: Old review report

**Path:** wiki/reviews/2026-04-01_output-report.md
**Severity:** INFO
**Category:** Orphan
**Issue:** Old review report (38 days old)
**Current:** wiki/reviews/2026-04-01_output-report.md
**Expected:** Reports older than 30 days should be archived
**Suggested fix:** Move to wiki/reviews/archive/2026-04/

---

## Issue 10: Temporary folder at root

**Path:** .tmp-experiments/
**Severity:** WARNING
**Category:** Path
**Issue:** Temporary folder at root (should be deleted when done)
**Current:** .tmp-experiments/
**Expected:** Temporary folders should use .tmp- prefix and be deleted
**Suggested fix:** Delete when testing complete or promote to permanent
```

---

## Example 2: Path Whitelist Issues

### Issue 2.1: File at root not in whitelist

**Before (ERROR):**
```
knowledge-base/
├── AGENTS.md
├── TAGS.md
├── README.md
├── NOTES.md          ← ERROR: not in whitelist
└── wiki/
```

**After (FIXED):**

**Option A: Remove file**
```bash
rm NOTES.md
```

**Option B: Add to whitelist**
```bash
# 1. Edit folder-structure.md
vim wiki/meta/folder-structure.md
# Add NOTES.md to root whitelist

# 2. Commit
git add wiki/meta/folder-structure.md
git commit -m "feat: add NOTES.md to root whitelist"

# 3. Next hygiene run → OK
```

---

### Issue 2.2: Folder at root not in whitelist

**Before (ERROR):**
```
knowledge-base/
├── AGENTS.md
├── experiments/      ← ERROR: not in whitelist
└── wiki/
```

**After (FIXED):**

**Option A: Remove folder**
```bash
rm -rf experiments/
```

**Option B: Move to wiki/**
```bash
mv experiments/ wiki/experiments/

# Then update folder-structure.md to allow wiki/experiments/
```

**Option C: Use temporary prefix**
```bash
mv experiments/ .tmp-experiments/
# Hygiene Inspector will report WARNING (not ERROR)
```

---

### Issue 2.3: Subfolder not allowed

**Before (ERROR):**
```
wiki/
├── sources/
├── concepts/
├── archive/          ← ERROR: not in wiki/ whitelist
└── meta/
```

**After (FIXED):**

**Option A: Remove folder**
```bash
rm -rf wiki/archive/
```

**Option B: Add to whitelist**
```bash
# 1. Edit folder-structure.md
vim wiki/meta/folder-structure.md
# Add archive/ to wiki/ subfolders

# 2. Commit changes
git add wiki/meta/folder-structure.md
git commit -m "feat: add wiki/archive/ to structure"

# 3. Next hygiene run → OK
```

---

## Example 3: Naming Convention Issues

### Issue 3.1: Folder uses uppercase

**Before (WARNING):**
```
wiki/
├── Sources/          ← WARNING: should be lowercase
├── Concepts/         ← WARNING: should be lowercase
└── meta/
```

**After (FIXED):**
```bash
# Rename folders
git mv wiki/Sources/ wiki/sources/
git mv wiki/Concepts/ wiki/concepts/

# Commit
git add wiki/
git commit -m "fix: rename folders to lowercase"
```

---

### Issue 3.2: Folder uses underscores

**Before (WARNING):**
```
wiki/
├── tag_index/        ← WARNING: should use hyphens
└── topic_index/      ← WARNING: should use hyphens
```

**After (FIXED):**
```bash
# Rename folders
git mv wiki/tag_index/ wiki/tag-index/
git mv wiki/topic_index/ wiki/topic-index/

# Update folder-structure.md if needed
# Commit changes
```

---

### Issue 3.3: Source file missing src_ prefix

**Before (ERROR):**
```
wiki/sources/
├── anthropic-claude.md    ← ERROR: missing src_ prefix
├── src_openai-gpt.md
└── src_google-gemini.md
```

**After (FIXED):**
```bash
# Rename file
git mv wiki/sources/anthropic-claude.md wiki/sources/src_anthropic-claude.md

# Commit
git add wiki/sources/
git commit -m "fix: add src_ prefix to source file"
```

---

### Issue 3.4: Concept file uses uppercase

**Before (ERROR):**
```
wiki/concepts/
├── RAG-System.md     ← ERROR: should be lowercase
├── Embedding.md      ← ERROR: should be lowercase
└── vector-db.md
```

**After (FIXED):**
```bash
# Rename files
git mv wiki/concepts/RAG-System.md wiki/concepts/rag-system.md
git mv wiki/concepts/Embedding.md wiki/concepts/embedding.md

# Commit
git add wiki/concepts/
git commit -m "fix: rename concept files to lowercase"
```

---

### Issue 3.5: Path contains spaces

**Before (ERROR):**
```
wiki/concepts/
├── RAG System.md     ← ERROR: contains spaces
└── Vector Database.md ← ERROR: contains spaces
```

**After (FIXED):**
```bash
# Rename files
git mv "wiki/concepts/RAG System.md" wiki/concepts/rag-system.md
git mv "wiki/concepts/Vector Database.md" wiki/concepts/vector-database.md

# Commit
git add wiki/concepts/
git commit -m "fix: remove spaces from filenames"
```

---

## Example 4: Orphan Detection Issues

### Issue 4.1: Source file in wrong folder

**Before (ERROR):**
```
wiki/
├── sources/
│   └── src_openai-gpt.md
└── concepts/
    └── src_anthropic-claude.md  ← ERROR: source in concepts/
```

**After (FIXED):**
```bash
# Move file to correct location
git mv wiki/concepts/src_anthropic-claude.md wiki/sources/src_anthropic-claude.md

# Commit
git add wiki/
git commit -m "fix: move source file to correct folder"
```

---

### Issue 4.2: Concept file in wrong folder

**Before (ERROR):**
```
wiki/
├── sources/
│   ├── src_openai-gpt.md
│   └── embedding.md          ← ERROR: concept in sources/
└── concepts/
    └── rag-system.md
```

**After (FIXED):**
```bash
# Move file to correct location
git mv wiki/sources/embedding.md wiki/concepts/embedding.md

# Commit
git add wiki/
git commit -m "fix: move concept file to correct folder"
```

---

### Issue 4.3: Empty folder

**Before (INFO):**
```
wiki/
├── sources/
├── concepts/
└── experiments/      ← INFO: empty folder
```

**After (FIXED):**

**Option A: Remove empty folder**
```bash
rmdir wiki/experiments/
```

**Option B: Add files to folder**
```bash
# Add content
touch wiki/experiments/test-concept.md

# Or move existing files
mv wiki/drafts/some-file.md wiki/experiments/
```

---

### Issue 4.4: Temporary files left behind

**Before (WARNING):**
```
wiki/concepts/
├── rag-system.md
├── rag-system.md.bak     ← WARNING: backup file
├── embedding.md
└── embedding.md~         ← WARNING: temp file
```

**After (FIXED):**
```bash
# Remove temporary files
rm wiki/concepts/*.bak
rm wiki/concepts/*~

# Or use find
find wiki/ -name "*.bak" -delete
find wiki/ -name "*~" -delete
```

---

### Issue 4.5: Old review reports

**Before (INFO):**
```
wiki/reviews/
├── 2026-03-01_output-report.md   ← INFO: 69 days old
├── 2026-03-15_format-report.md   ← INFO: 55 days old
├── 2026-05-01_output-report.md
└── 2026-05-09_hygiene-report.md
```

**After (FIXED):**
```bash
# Create archive folder
mkdir -p wiki/reviews/archive/2026-03/

# Move old reports
mv wiki/reviews/2026-03-*.md wiki/reviews/archive/2026-03/

# Commit
git add wiki/reviews/
git commit -m "chore: archive old review reports"
```

---

## Example 5: Structure Change Scenarios

### Scenario 5.1: Adding new folder

**Step 1: Update folder-structure.md**
```bash
vim wiki/meta/folder-structure.md
# Add: wiki/experiments/ — Testing new concepts
```

**Step 2: Commit changes**
```bash
git add wiki/meta/folder-structure.md
git commit -m "feat: add wiki/experiments/ to structure"
```

**Step 3: Create folder**
```bash
mkdir wiki/experiments/
```

**Step 4: Next hygiene run**
```
✓ No issues found for wiki/experiments/
```

---

### Scenario 5.2: Removing folder

**Step 1: Backup if needed**
```bash
cp -r wiki/drafts/ wiki-drafts-backup/
```

**Step 2: Update folder-structure.md**
```bash
vim wiki/meta/folder-structure.md
# Remove: wiki/drafts/
```

**Step 3: Update agent skills**
```bash
vim .openclaw/skills/compile-agent/SKILL.md
# Remove references to wiki/drafts/
```

**Step 4: Commit changes**
```bash
git add wiki/meta/folder-structure.md .openclaw/skills/
git commit -m "refactor: remove wiki/drafts/ folder"
```

**Step 5: Delete folder**
```bash
rm -rf wiki/drafts/
```

**Step 6: Next hygiene run**
```
✓ No issues found
```

---

### Scenario 5.3: Using temporary folder

**Create temporary folder for testing:**
```bash
mkdir .tmp-experiments/
```

**Hygiene Inspector report:**
```markdown
## Issue: Temporary folder at root

**Path:** .tmp-experiments/
**Severity:** WARNING
**Category:** Path
**Issue:** Temporary folder at root (should be deleted when done)
**Suggested fix:** Delete when testing complete or promote to permanent
```

**Cleanup after testing:**
```bash
# Option A: Delete
rm -rf .tmp-experiments/

# Option B: Promote to permanent
mv .tmp-experiments/ wiki/experiments/
# Then update folder-structure.md
```

---

### Scenario 5.4: Emergency folder creation

**Julius needs folder urgently:**
```bash
# Create folder without updating folder-structure.md
mkdir wiki/experiments/
```

**Hygiene Inspector report:**
```markdown
## Issue: Subfolder not allowed

**Path:** wiki/experiments/
**Severity:** ERROR
**Category:** Path
**Issue:** Subfolder not allowed in wiki/
**Suggested fix:** Remove wiki/experiments/ or add to folder-structure.md
```

**Julius approves via Telegram:**
```
approve hygiene
Note: Intentional, will update folder-structure.md within 24h
```

**Update folder-structure.md:**
```bash
vim wiki/meta/folder-structure.md
# Add: wiki/experiments/

git add wiki/meta/folder-structure.md
git commit -m "feat: add wiki/experiments/ to structure"
```

**Next hygiene run:**
```
✓ No issues found
```

---

## Example 6: Multi-Category Issues

### Complex case: Multiple issues in one path

**Before (3 ERROR, 2 WARNING):**

```
knowledge-base/
├── NOTES.md                          ← ERROR: not in root whitelist
├── wiki/
│   ├── Archive/                      ← ERROR: not allowed + WARNING: uppercase
│   │   └── old_concepts/             ← WARNING: underscore
│   │       └── RAG System.md         ← ERROR: spaces
│   └── sources/
│       └── anthropic-claude.md       ← ERROR: missing src_ prefix
```

**Issues found:**
1. ERROR (Path): NOTES.md not in root whitelist
2. ERROR (Path): wiki/Archive/ not allowed
3. WARNING (Naming): Archive uses uppercase
4. WARNING (Naming): old_concepts uses underscore
5. ERROR (Naming): RAG System.md contains spaces
6. ERROR (Naming): anthropic-claude.md missing src_ prefix

---

**After (FIXED):**

```
knowledge-base/
├── AGENTS.md
├── TAGS.md
├── README.md
└── wiki/
    ├── sources/
    │   ├── src_anthropic-claude.md   ← Fixed: added src_ prefix
    │   └── src_openai-gpt.md
    └── concepts/
        └── rag-system.md             ← Fixed: moved, renamed
```

**Fix commands:**
```bash
# 1. Remove NOTES.md
rm NOTES.md

# 2. Rename and move files
git mv "wiki/Archive/old_concepts/RAG System.md" wiki/concepts/rag-system.md
git mv wiki/sources/anthropic-claude.md wiki/sources/src_anthropic-claude.md

# 3. Remove empty folders
rm -rf wiki/Archive/

# 4. Commit
git add .
git commit -m "fix: resolve multiple hygiene issues"
```

---

## Example 7: Systematic Issues

### Pattern: Multiple files with same issue

**Detected pattern:**
```
15 source files missing src_ prefix
Likely cause: Compile Agent not following naming convention
```

**Report includes:**
```markdown
[SYSTEMATIC ISSUE]
Pattern: 15 source files missing src_ prefix
Files affected: anthropic-claude.md, openai-gpt.md, google-gemini.md, ...
Likely cause: Compile Agent not following naming convention
Recommendation: Update compile-agent/SKILL.md to enforce src_ prefix
```

**Bulk fix:**
```bash
# Rename all source files without src_ prefix
cd wiki/sources/
for file in *.md; do
    if [[ ! $file =~ ^src_ ]]; then
        git mv "$file" "src_$file"
    fi
done

# Commit
git add .
git commit -m "fix: add src_ prefix to all source files"
```

---

## Example 8: Report Actions

### Julius approves report

**Telegram command:**
```
approve hygiene
```

**Result:**
- Report status: pending → approved
- Entry moves to "Recently Applied" in _action-required.md
- Fix Agent can now apply fixes

---

### Julius rejects report

**Telegram command:**
```
reject hygiene
```

**Result:**
- Report status: pending → rejected
- Entry removed from _action-required.md
- Report archived to wiki/reviews/archive/

---

### Julius requests details

**Telegram command:**
```
show hygiene
```

**Result:**
- Full report sent to Telegram
- Or link to wiki/reviews/2026-05-09_hygiene-report.md

---

## Example 9: Edge Cases

### Case 9.1: Vietnamese diacritics in path (allowed)

**Valid:**
```
wiki/concepts/tối-ưu-hóa-context.md
```

This is **allowed** per folder-structure.md naming rules.

---

### Case 9.2: Agent home folders (exception)

**Valid:**
```
.openclaw/
.hermes/
.git/
.obsidian/
```

These folders can use dots and are exceptions to lowercase-hyphen rule.

---

### Case 9.3: Temporary folder with .tmp- prefix

**Valid (WARNING, not ERROR):**
```
.tmp-experiments/
.tmp-testing/
```

Hygiene Inspector reports WARNING (should be deleted when done), not ERROR.

---

## Related Documentation

- [SKILL.md](SKILL.md) — Hygiene Inspector overview
- [workflow.md](workflow.md) — Step-by-step validation process
- [wiki/meta/folder-structure.md](../../wiki/meta/folder-structure.md) — Ground truth folder rules

---

**End of examples.md**
