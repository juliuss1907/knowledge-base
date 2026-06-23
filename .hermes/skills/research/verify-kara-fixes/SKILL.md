---
name: verify-kara-fixes
description: Systematically verify that Kara (Fix Agent) correctly applied all fixes from approved Hermes validation reports. Run after every `openclaw fix apply` cycle to catch silent failures.
when_to_use: After Kara responds "Fix apply completed" or "All reports resolved". Also use when Julius says "kiểm tra Kara fix đúng chưa", "verify fixes", "đã kiểm tra lại chưa", "kiểm tra lại", or any variant asking whether previously approved fixes were actually applied.
---

# Verify Kara Fixes

Kara's `fix apply` often fails silently — reports issues as "fixed" but files remain unchanged. This skill provides a systematic checklist to verify each fix was actually applied.

## Critical rules

- **Read-only**: Only read files and search patterns. NEVER modify wiki files.
- **Check evidence, not Kara's claims**: Kara says "fixed" — you verify by reading files.
- **Report findings to Julius**: List what was fixed vs. what wasn't.

## Quick re-check (đã kiểm tra lại chưa?)

When Julius asks "đã kiểm tra lại chưa" or "kiểm tra lại", he wants a fast status check — not the full systematic workflow. This is a condensed path:

### Step 1: Read the latest approved reports

Read `_action-required.md` to identify what was recently approved/applied. Focus on the most recent 1-2 batches.

### Step 2: Grep for each specific issue

Go directly to grepping. Do NOT re-run the full validators. Target only the issues listed in the approved reports:

```bash
# Example: check if "Ngưởi" typo was fixed
grep -rn "Ngưởi" wiki/concepts/ wiki/sources/

# Example: check if "thờigian" spacing typo was fixed
grep -rn "thờigian" wiki/concepts/ wiki/sources/
```

**Run all grep commands in parallel** — use separate `terminal` calls, not a loop. Each grep targets one specific string.

### Step 3: Report in table format

Present findings as a compact before/after table:

| Issue | Trước | Sau | Trạng thái |
|---|---|---|---|
| "Ngưởi" typo | 1 file còn lại | 0 | ✅ Đã fix |
| "thờigian" | 1 instance | 1 | ❌ Chưa fix |

Also note any new files compiled since the last report (check with `find -newer`).

### When to use quick re-check vs full workflow

| Trigger | Mode |
|---|---|
| "đã kiểm tra lại chưa", "kiểm tra lại" | Quick re-check (this section) |
| "kiểm tra Kara fix", "verify fixes đầy đủ" | Full workflow (below) |
| After `openclaw fix apply` just completed | Full workflow (below) |

---

## Full verification workflow

### Step 1: Identify all issues from approved reports

Read the latest `_action-required.md` to get the full list of recently applied reports with their issue counts.

### Step 2: Check ERROR-level fixes first (highest priority)

Common ERROR types and how to verify:

**Sub_tag classification (Pool A vs Pool B):**
```bash
# Check if 'economic' was removed from sub_tags
search_files pattern="sub_tags:.*economic" target="content" path="wiki/"
```

**Code block language tags:**
Read the specific file and check if ` ``` ` is now ` ```yaml ` or appropriate language.

### Step 3: Check WARNING-level fixes

**Section case (Key Ideas → Key ideas, Related Concepts → Related concepts):**
```bash
search_files pattern="^## Key Ideas" target="content" path="wiki/concepts"
search_files pattern="^## Related Concepts" target="content" path="wiki/concepts"
```
If matches found → NOT fixed.

**Deprecated date_ingested field:**
```bash
search_files pattern="^date_ingested:" target="content" path="wiki/sources" output_mode="count"
```
If count > 0 → NOT fixed. Kara must remove this field from all source files.

**Original field wikilink → bare path:**
```bash
search_files pattern='original:.*\[\[' target="content" path="wiki/sources" output_mode="count"
```
If count > 0 → NOT fixed. Kara must unwrap wikilinks to bare paths.

**Vietnamese typos:**
Read the specific file and search for the typo string (e.g., "tiếm").

### Step 4: Check INFO-level fixes

**Excess key points:** Read files, count bullets. If still 11+, not fixed.

**Empty sections:** Read files, check if `## Notes` or `## Original excerpts` sections still empty.

**Broken wikilinks:** Check if referenced concepts now exist:
```bash
search_files pattern="orphan-commit-attack" target="files" path="wiki/concepts"
```

### Step 5: Report findings

Clear summary to Julius:
- ✅ What was actually fixed
- ❌ What Kara failed to fix (with file paths + current state)
- 🔄 Whether this is a one-time fix failure or Compile Agent template issue

## Common failure patterns

| Pattern | Root cause | Fix |
|---|---|---|
| ALL issues unfixed | Kara doesn't have write permission to `wiki/` | Julius must check permissions |
| Section case unfixed | Compile Agent template uses Title Case | Fix in compile-agent SKILL.md |
| `date_ingested` unfixed | Compile Agent still emits deprecated field | Fix in compile-agent SKILL.md |
| `original` wikilink unfixed | Compile Agent wraps all paths | Fix in compile-agent SKILL.md |
| Individual typos unfixed | Kara missed specific file | Manual fix by Julius or re-run |

## Multi-report verification

When verifying fixes across multiple reports (Output + Format + Hygiene) simultaneously, use `execute_code` to batch all checks. Each validator type requires different methods:

**Format fixes (frontmatter + sections):**
```python
# Check frontmatter: sub_tags bracket syntax, legacy fields
for f in ["file1.md", "file2.md", "file3.md"]:
    r = terminal(f"sed -n '/^---$/,/^---$/p' /home/julius/knowledge-base/wiki/sources/{f}")
    print(f"--- {f} ---\n{r['output']}")

# Check section ordering: extra sections moved after Sources
r = terminal("grep -n '^## ' /home/julius/knowledge-base/wiki/concepts/cookie-fun-mcp.md")
```

**Output fixes (content quality):**
```python
# Check empty excerpts filled
r = terminal("grep -A 5 '## Original excerpts' /path/to/file.md")

# Verify broken wikilink concepts exist
r = terminal("test -f /home/julius/knowledge-base/wiki/concepts/orphan-commit-attack.md && echo 'EXISTS' || echo 'MISSING'")
```

**Hygiene fixes (filesystem):**
```python
# Check files/dirs removed
r = terminal("test -d /home/julius/knowledge-base/memory && echo 'EXISTS' || echo 'GONE'")
r = terminal("test -f /home/julius/knowledge-base/RAW_BACKLOG.md && echo 'EXISTS' || echo 'GONE'")
```

## User preferences to skip

- **Empty `## Notes` sections**: Intentional — Julius configured Compile Agent template to include them. Do NOT flag as issues. Output validator should skip empty Notes.

## Performance

- Typical verification: 30-60 seconds
- Read 5-10 files + 3-5 pattern searches
- Focus on the specific files listed in the report, not the entire KB
