# Defect D — intra-file claim conflict (observed 2026-10-03)

## The invariant

A concept compiled from 2+ sources can end up asserting two mutually exclusive numbers for the **same entity**, because the new source's figure is pasted in without checking the text already present. Unlike Defect B (duplication *across* files), the conflict lives *inside one file* and survives every cross-file check.

Observed 2026-10-03 in `long-context-models.md`:

- `:18` (carry-over, from `src_deepseek-v4-architecture`) — "DeepSeek V4 đạt 1M tokens, vượt xa Claude Opus (200K max)"
- `:49` (carry-over, same source) — `| Claude Opus | ~87 | N/A (200K max) |`
- `:30` (**added today**, from `src_unreasonable-effectiveness-of-html`) — "Thariq Shihipar dùng Opus 4.7 với context window 1 triệu token"

Both cannot be true. The raw article does say "the 1MM context window in Opus 4.7", so the new line faithfully reproduces its source — the defect is that the compile step never reconciled it against the existing lines.

## Detection

For each concept that gains a source today, extract numeric/capability claims and compare against the pre-existing text:

```bash
SLUG=long-context-models
echo "--- figures introduced today"
git diff -- wiki/concepts/$SLUG.md | grep -E '^\+' | grep -v '^+++' \
  | grep -oP '\d[\d.,]*\s*(K|M|%|token|GB|bytes)'
echo "--- figures already present"
git show HEAD:wiki/concepts/$SLUG.md \
  | grep -nP '\d[\d.,]*\s*(K|M|%|token|GB|bytes)'
# then compare overlapping entities: model names, percentages, limits
```

**Read the definition and any benchmark table outright — do not rely on the diff alone.** The stale figure usually hides in the definition line or a table cell (`:18` and `:49` here, both unchanged), so a diff-only check sees only the new side and reports nothing.

## Severity and handling

ERROR (Coherence + Factual) when both claims are affirmative and cannot both be true.

**Do not self-resolve which number is correct.** A content validator cannot verify a vendor's context-window spec from inside the vault. Report: both locations, which line is new (`git diff`) vs carry-over (`git show HEAD:`), and require out-of-KB verification before any fix. Contrasting this with Issue 1 of the 10-02 report — there, a claim about a missing target turned out to be *wrong* (the file did exist), so "verify the claim is still true" is not a formality; carry-forward claims decay.

## Root cause

Same family as Defect B (duplicate key idea, duplicate section-name drift): Compile Agent aggregates a new source without reconciling against what the concept already says. The remedy is a **prompt rule**, not a character-level fix:

> Before adding a quantitative claim to an existing concept, check whether it conflicts with a claim already in that file.

Suggested addition to `compile-agent/SKILL.md`. This is the second consecutive run (10-02, 10-03) where a previously-proposed compile-agent rule produced a real, measured improvement in output shape — the 3 defects that prompted the 10-02 request were all closed by 10-03.

## Same-batch template inconsistency — missing `## Notes`

4 of 10 concepts in one batch shipped without `## Notes` while 6 had it. An **empty** `## Notes` is intentional (Compile Agent template) and must never be flagged as an empty-content defect. The defect is the **missing section**, which is visible only when a batch is compared against itself:

```bash
for f in $NEW_CONCEPTS; do
  printf "%-38s " "$f"
  grep -q '^## Notes' "wiki/concepts/$f.md" && echo ok || echo "MISSING Notes"
done
```

WARNING (Completeness); Fix Agent adds the empty section. Format Validator lists `Notes` in concept `required_sections` (`reference.md:619`), so if it did not fire on these files that is a validator gap worth reporting to it rather than silently patching the files here.