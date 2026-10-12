# Stale hand-written raw sub-index (2026-10-04)

The 09-28 scan (`status: processed` + missing `compiled_to` → report as a backlink
defect) returned **0** on 10-04: the raw layer was clean. Yet
`raw/websites/websites.md` still listed 2 files as `(unprocessed)` when both were
`status: processed`, carried valid `compiled_to`, and had sources in `wiki/sources/`.

This is the **inverse** of the 09-28 blind spot. There, a misspelled key hid a real
defect from the grep. Here, correct per-file frontmatter let stale index prose hide
behind a clean sweep.

Cause: the file carries `auto_generated: false`. It refreshes only when someone edits
it by hand — and nobody did after the 09-30 compile.

## Rule

A clean `compiled_to` sweep does NOT certify the raw layer. Check the index text too.

```bash
# 1. Items the index claims are still backlog
grep -rn '(unprocessed)' raw/*/*.md

# 2. Cross-check each against its own frontmatter
grep -n '^status:' raw/websites/<file>.md

# 3. Verify the Stats arithmetic
grep -n 'By status:' raw/*/*.md
```

On 10-04: `By status: 5 processed, 2 unprocessed` while all 7 items were `processed`
and all 7 had sources.

Same logic applies to any `wiki/topic/*` index carrying `auto_generated: false`.

## Orphan sub-index check

A sub-index that nothing links to is invisible to every other scan. Two checks:

```bash
# 1. Every [[x]] listed under "Sub-indexes" must resolve to a real file
for t in <each slug from raw/raw.md>; do
  [ -f "raw/$t/$t.md" ] || [ -f "raw/$t.md" ] || echo "DANGLING: [[$t]]"
done

# 2. Is anything actually pointing at the sub-index files themselves?
grep -rn '<sub-index-slug>' raw/ wiki/ | grep -v 'raw/<cat>/<cat>.md:' || echo "ORPHAN"
```

## Case found 2026-10-04

Three defects, one cause:

| Finding | Evidence |
|---|---|
| `raw/raw.md:23` lists `[[tools]]` with **no target anywhere** | `raw/tools/tools.md`, `raw/websites/tools.md`, `wiki/concepts/tools.md` all MISS. (`wiki/tag/tools.md` exists but is a different namespace — a tag, not a sub-index.) |
| `raw/websites/2026-07-25_tools.md` has **0 inbound refs** | `grep -rn '2026-07-25_tools' raw/ wiki/` → 0 hits |
| It sits in `websites/` despite declaring `scope: tools` | Both its items (`2026-07-25_introducing-backsearch-gr-inc`, `2026-07-25_monid-ai-agent-tool-platform`) are in `raw/websites/` |

First added in commit `70cb2887` (2026-08-06) — **standing ~2 months** before being
caught. Being in the wrong directory is what let it stay invisible.

## Suggested fixes (either ending is acceptable)

(a) Build `raw/tools/tools.md` per the `raw/<category>/<category>.md` convention and
move the 2 tool raws into `raw/tools/`; or
(b) Drop the `tools` sub-index line from `raw/raw.md:23` and delete the orphan file.

Outside the Output Validator write zone — route to Ingest or Hygiene Inspector.