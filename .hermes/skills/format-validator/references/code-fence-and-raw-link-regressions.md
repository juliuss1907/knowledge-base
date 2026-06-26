# Code fence and raw-link regressions

## When this matters

Use this note when a format report claims code-block language-tag errors or broken raw-file wikilinks, but spot checks suggest the files were already fixed.

## Regression 1 — closing fences counted as missing language tags

### Symptom
A concept or source file contains opening fences like:

```text
```text
...
```
```

Yet the validator still emits:

```text
ERROR|Markdown|<file>|Code block missing language tag
```

### Root cause
Regex patterns like `re.findall(r'```(\S*)', body)` see both:
- opening fence: ` ```text ` → suffix `text`
- closing fence: ` ``` ` → suffix ``

That empty suffix from the closing fence is misclassified as a missing language tag.

### Durable fix
Validate fences line-by-line with an `in_fence` toggle:
1. On an opening fence, require a language tag.
2. On a closing fence, do not validate language; just close the fence.

## Regression 2 — source-body raw wikilinks flagged as broken

### Symptom
A source file references its raw input in body content, usually inside `## Metadata`:

```text
- **Original file:** [[2026-06-17_dan-koe-workflow-analysis-markus]]
```

The validator emits a broken-wikilink warning even though the raw file exists under `raw/articles/`.

### Root cause
Source-body wikilink validation only checked `wiki/concepts/` and `wiki/sources/`, unlike `original` frontmatter validation which already searched raw subdirectories.

### Durable fix
Source-body broken-wikilink checks must also search raw subtype directories:
- `raw/articles/`
- `raw/posts/`
- `raw/videos/`
- `raw/papers/`
- `raw/websites/`
- `raw/repos/`

Accept both:
- exact path: `<subdir>/<target>.md`
- slug-suffixed path: `<subdir>/*_<target>.md`

## Verification pattern

When a report claims these issues:
1. Read one affected file directly.
2. Check whether the opening fence already has a language tag.
3. Check whether the supposedly broken raw target actually exists in a raw subtype directory.
4. If both are already correct, treat the validator as suspect and patch `scripts/validate.py` before trusting the report.

## Session anchor

Observed during verification of Kara's claimed fixes for the 2026-06-25 format report. The report's listed fixes were real, but the validator script still produced false positives until these two regressions were patched.
