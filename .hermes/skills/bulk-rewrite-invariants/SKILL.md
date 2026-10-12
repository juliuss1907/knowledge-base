---
name: bulk-rewrite-invariants
description: Batch-rewrite many files without silent content loss.
---

# Bulk rewrite with invariants

When one edit touches many files, a partial write is silent: no error, no exception, just
missing content. Prove each step instead of trusting it.

## Sequence

1. **Inventory.** Enumerate the exact target set, persist it to disk (JSON), and print the count.
   Never derive targets from a glob at write time — the set can shift between planning and writing.
2. **Back up.** Copy every target to a dated directory preserving relative paths. The backup is
   the only source of truth for "what did this file look like before", and the only rollback.
3. **Apply transforms in memory.** Read bytes, compute the new content, write to a temp path.
4. **Verify the temp path**, not the live file. Invariants below.
5. **Write the live file**, then re-verify by reading back from disk.
6. **Prove nothing else moved** by replaying the intended transforms on the backup and asserting
   `current == expected`. This is the check that catches an edit that over-reached.

## Byte-level fidelity

Preserve trailing newlines by appending the missing byte, never by re-serializing:

```python
b = path.read_bytes()
if b and not b.endswith(b'\n'):
    path.write_bytes(b + b'\n')
```

`'\n'.join(text.splitlines()) + '\n'` normalizes every line ending and rewrites files that were
already correct. Only use it when you know the original ended with a newline.

Edits whose only intended change is a substitution (`[[a.md]]` → `[[a]]`, stripping quotes) should
be expressed as a regex over text, never as a line-by-line rebuild.

## Invariants that catch real drops

Arithmetic counts are not evidence — `len(new) == len(old) + N` passes while one original item was
dropped and one duplicate added. Prefer:

- **Set difference.** Compare a `Counter` of item identities (titles, paths) before and after.
  Assert nothing from the original is missing and each addition appears exactly once.
- **Region containment.** For every moved item, assert it sits in the intended region by locating
  a section boundary and counting items on each side. An item that exists but lands in the wrong
  region reads as "missing" to any whole-file count.
- **Byte growth bound.** `abs(len(new) - len(old))` should match the expected edit size roughly.
  A 250 KB file growing by <100 bytes when you moved three 5 KB blocks means they were not moved.
- **No glued neighbors.** When concatenating a heading with following content, assert the joined
  string contains the heading followed by a newline. `heading + block` without a separator keeps the
  item present but stops it matching any line-anchored pattern — the worst shape, because it looks
  like data loss and is actually one missing character.

## Duplicate-field trap

When the target already has the field you are setting (e.g. a status line at the top of each
report), replace it in place rather than inserting a second one. Then assert exactly one instance
survives — a leftover duplicate makes later `grep -c` checks double-count and hides real state.

## Distinguish `git diff --check` complaints

| Complaint | Cause | Action |
|---|---|---|
| `\ No newline at end of file` | batch tool dropped the trailing byte | append the byte |
| `new blank line at EOF` in generated files | generator removed an empty section | verify content, then leave alone |

For the second case, confirm what the run removed before editing:

```bash
git show HEAD:<path> | sed -n '/^## <section>$/,/^## /p'
```

If the removed block held only placeholders, the run removed empty structure and the complaint is a
consequence, not a defect. Fixing it in isolation cosmetics a correct rewrite.

Similarly, a `D` in `git status` on an auto-generated page is not automatically data loss: confirm
every entry it listed was re-parented elsewhere and nothing still references it before re-creating
the file, which would reintroduce drift the generator just cleaned up.

## Attribute before claiming a regression

A count of defective files is not a finding until it is split by membership in your own change set.
An absolute total invites the wrong fix and invites claiming other agents' pre-existing state as your
damage.

```python
mine = set(json.load(open('/tmp/sweep-targets.json'))['paths'])
defective_now = [p for p in files if not p.read_bytes().endswith(b'\n')]
caused_here = [p for p in defective_now if p in mine]
pre_existing = [p for p in defective_now if p not in mine]
```

Cross-check the pre-edit backup before calling anything a regression: if the backup copy already
lacked the byte, the batch did not introduce it. Report both numbers — "52 of the 101 are mine, 49
predate me" scopes the work; "101 files lack newlines" scopes nothing.

## When a check fails

Determine whether the artifact or the check is wrong before editing. Print the actual bytes at the
location, probe the assertion's pattern against them, then decide. Fixing an artifact to satisfy a
mis-specified check leaves the real defect in place and teaches the check nothing.

Measure the pre-existing baseline before acting on any failed assertion. Most failures in a batch
verify are wrong expectations rather than wrong data, and the usual suspects are:

| Failure shape | Likely cause |
|---|---|
| count off by the number of items just moved | one item glued to a neighbouring heading |
| a keep-set path reported as caught by a new filter | an older broad pattern already matched it |
| a keyword filter matching unrelated files | the search term is a substring of unrelated names |
| two counts of the same set disagreeing | one measurement ran against the pre-edit file |

Resolve each by measuring the baseline and classifying as data-vs-expectation. Only after that
classification is a content edit ever the right response.

Naive assertion patterns fail predictably — an anchored search misses a heading glued to its
neighbor, a word-boundary shortcut misreads bold markup. Probe a suspect pattern with a one-line
print before acting on its verdict.

Refactors that must preserve behavior get proven by differential comparison across all real files
plus synthetic edge cases, requiring identical output — not by asserting remembered expectations.
