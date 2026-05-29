# Format Validation Report — Wikilink Quoting Check

**Date:** 2026-05-28  
**Validator:** Hermes Format Validator  
**Rule tested:** Format spec v2.2 — wikilinks in frontmatter must use quoted format `"[[...]]"`

---

## Summary

| Check | Result |
|---|---|
| Format spec rule | ✅ Quoted wikilink format `"[[...]]"` required in frontmatter |
| Sources scanned | 36 files in `wiki/sources/` |
| Concepts scanned | 163 files in `wiki/concepts/` |
| **Violations found** | **0** |

All frontmatter wikilinks correctly use the quoted `"[[...]]"` format.

---

## Rule Reference (format-spec.md v2.2)

From section 2.2 (concept frontmatter) and section 3.2 (source frontmatter):

```
# Concept — sources field:
sources:
  - "[[src_<slug-1>]]"
  - "[[src_<slug-2>]]"

# Source — original field:
original: "[[YYYY-MM-DD_<slug>]]"
```

From section 9, note:
> Wikilinks in frontmatter fields (`original`, `sources`) use quoted format `"[[...]]"` for Obsidian compatibility.

---

## Verification Results

### Sources (`wiki/sources/`)

All 36 source files have `original:` field with quoted wikilinks:

```
original: "[[YYYY-MM-DD_slug]]"  ✅
```

**No unquoted wikilinks found in any `original:` field.**

### Concepts (`wiki/concepts/`)

All 163 concept files have `sources:` field with correctly quoted array items:

```
sources:
  - "[[src_<slug>]]"  ✅
```

**No unquoted wikilinks found in any `sources:` array items.**

---

## Notes

- Wikilinks in body content (e.g., in "## Related concepts" sections) use bare format `[[...]]` — this is correct per spec section 4.
- The 50 matches found by `^- \[\[` were body content links, not frontmatter violations.
- The 36 matches for `original:.*\[\[` and 171 matches for `"\[\[src_` all show properly quoted format.

---

## Conclusion

✅ **All wiki files pass validation.**  
No files contain unquoted `[[...]]` wikilinks in frontmatter `original:` or `sources:` fields.